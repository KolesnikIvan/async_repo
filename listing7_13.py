"""tkinter.mainloop + asyncio.event_loop"""
# import asyncio
# from concurrent.futures import Future
# from typing import Callable, Optional

# class StressTest:

#     def __init__(self,
#                 loop: asyncio.AbstractEventLoop,
#                 url: str,
#                 total_requests: int,
#                 callback: Callable[[int, int], None]) -> None:
#         self._completed_requests: int = 0
#         self._load_test_future: Optional[Future] = None
#         self._loop = loop
#         self._url = url
#         self._total_requests = total_requests
#         self._callback = callback
#         self._refresh_rate = total_requests // 100

#     def start(self):
#         future = asyncio.run_coroutine_threadsafe(self._make_requests(),
#                                                   self.loop)
#         self._load_test_future = future

#     def cancel(self):
#         if self._load_test_future:
#             self._loop.call_soon_threadsafe(self._load_test_future.cancel)

#     async def _get_url(self, sessin: ClientSession, url: str):
#         try:
#             await session.get(url)
#         except Exception as e:
#             print(e)

#         self._completed_requests = self._completed_requests + 1
#         if self._completed_requests == self._total_requests \ 
#             or self._completed_Requests % self._refresh_rate ==0:
#         self._callback(self._completed_requests, self._total_requests)

#     async def _make_requests(self):
#         async with ClientSession() as session:
#             reqs = [self._get_url(session, self._url) for _ in 
#                     reange(self._total_requests)]
#         await asyncio.gqther(*reqs)

import asyncio
from typing import Optional
from concurrent.futures import Future

from aiohttp import ClientSession

class StressTest:
    def __init__(self, 
                 loop: asyncio.AbstractEventLoop,
                 total_requests: int,
                 url: str,
                 callback: callable):
        self._total_requests = total_requests
        self.completed_requests: int = 0
        self._loop = loop
        self._url
        self._callback = callback
        self._refresh_rate = total_requests // 100
        self._load_test_future: Optional[Future] = None

    def start(self):
        future = asyncio.run_coroutine_threadsafe(self._make_request, 
                                                  self.loop)
        self._load_test_future = future

    def cancel(self):
        if self._load_test_fitire:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [self._get_url(session, self.url) for _ in range(self._total_request)]
            await asyncio.gether(*reqs)
        
    async def _get_url(self, url, session: ClientSession):
        try:
            await session.get(url)
        except Exception as e:
            print(str(e))
        self._completed_requests = self._completed_requests + 1
        if self._completed_requests % self._refresh_rate == 0 \
                or self._competed_requests == self._total_requests:
            self._callback(self._completed_requests, self._total_requests)
