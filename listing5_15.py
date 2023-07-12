"""asynchronous cursor for db"""
import asyncio
import asyncpg

# async def main():
#     connection = await asyncpg.connect(
#         host="127.0.0.1",
#         port=5432,
#         database="products",
#         user="postgres",
#         password="master"
#     )
#     query = "SELECT product_id, product_name FROM product"
#     async with connection.transaction():
#         cursor = connection.cursor(query)
#         async for record in cursor:
#             print(record)

#     await connection.close()

# asyncio.run(main())

async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        database="products",
        user="postgres",
        password="master"
    )

    async with connection.transaction():
        query = "SELECT product_id, product_name FROM product"
        cursor = await connection.cursor(query)
        await cursor.forward(473)
        result = await cursor.fetch(100)
        for product in result:
            print(product)
    
    await connection.close()

asyncio.run(main())
