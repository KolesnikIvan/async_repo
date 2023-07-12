from typing import List
import asyncpg
import asyncio
from asyncpg import Record

async def main():
    connection = await asyncpg.connect(host="127.0.0.1",
                            port=5432,
                            user="postgres",
                            database="products",
                            password="master")
    await connection.execute("INSERT INTO BRAND VALUES(DEFAULT, 'Levis2')")
    await connection.execute("INSERT INTO BRAND VALUES(DEFAULT, 'Seven2')")

    query = "SELECT brand_id, brand_name FROM BRAND"
    selection: List[Record] = await connection.fetch(query)
    for item in selection:
        print(item)

    await connection.close()

asyncio.run(main())
