import asyncio
import asyncpg
from faker import Faker

async def insert_brands(connection):
    fake = Faker()
    brands = set()
    while len(brands) <= 100:
        brands.add((fake.word(),))
    insert = "INSERT INTO brand VALUES(DEFAULT, $1)"
    await connection.executemany(insert, list(brands))
    # for _ in range(100):
    #     brand = fake.word()
    #     await connection.execute(f"INSERT INTO brand VALUES(DEFAULT, '{brand}')")

async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="master",
        database="products"
    )
    await insert_brands(connection)
    await connection.close()

asyncio.run(main())
