"""asyncio.start_server() coroutine example that is the whole functionality passed"""
import asyncio
from asyncio import StreamReader, StreamWriter

class ServerState:
    def __init__(self) -> None:
        self._writers = list()

    async def add_client(self, reader: StreamReader, writer: StreamWriter):
        self._writers.append(writer)
        await self._on_connect(writer)
        await asyncio.create_task(self._echo(reader, writer))
        self._notify_all(f"connected client {writer}")

    async def _on_connect(self, writer: StreamWriter):
        writer.write(f"Welcome! Number of connections {len(self._writers)}".encode())
        await writer.drain()
        await self._notify_all(f"New connection {writer}")

    async def _echo(self, reader, writer):
        try:
            while (data := await reader.readline()) != b'':
                writer.write(data)
                await writer.drain()
            self._writers.remove(writer)
            await self._notify_all(f"client disconnected. Number {len(self._writers)}")
        except Exception as e:
            self._writers.remove(writer)

    async def _notify_all(self, message: str):
        for writer in self._writers:
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as e:
                self._writers.remove(writer)


async def main():
    server_state = ServerState()

    async def client_connected(reader: StreamReader, writer: StreamWriter):
        await server_state.add_client(reader, writer)

    server = await asyncio.start_server(client_connected, "127.0.0.1", 8010)

    async with server:
        await server.serve_forever()

asyncio.run(main())
