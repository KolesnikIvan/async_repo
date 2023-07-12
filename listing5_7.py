import asyncio
import asyncpg

from util.async_deco import async_timed

query = """
SELECT
p.product_id,
p.product_name,
p.brand_id,
s.sku_id,
pc.product_color_name,
ps.product_size_name
FROM product as p
JOIN sku as s on s.product_id = p.product_id
JOIN product_color as pc on pc.product_color_id = s.product_color_id
JOIN product_size as ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = 100
"""
async def query_prod(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(query)
    
@async_timed()
async def main():
    async with asyncpg.create_pool(
        min_size=6, max_size=6,
        host="127.0.0.1",
        port=5432,
        database="products",
        user="postgres",
        password="master") as pool:

        results = await asyncio.gather(query_prod(pool), 
                                       query_prod(pool),
                                       query_prod(pool))
        print(results)

asyncio.run(main())
            
