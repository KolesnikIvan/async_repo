import asyncio
import random
import asyncpg
from faker import Faker

fake = Faker()


def gen_products(quantity:int):
    products = list()
    for _ in range(quantity):
        desc = fake.words(10)
        brand_id = random.randint(1,112)
        products.append((" ".join(desc), brand_id))
    return products

def gen_skus(quantity):
    skus = list()
    for _ in range(quantity):
        prod_id = random.randint(1,1000)
        size_id = random.randint(1,3)
        color_id = random.randint(1, 2)
        skus.append((prod_id, size_id, color_id))
    return skus

async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        database="products",
        user="postgres",
        password="master"
    )

    products = gen_products(1000)
    command_insert_prods = "INSERT INTO product VALUES(DEFAULT, $1, $2)"
    await connection.executemany(command_insert_prods, products)
    
    skus = gen_skus(100000)
    command_insert_sku = "INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)"
    await connection.executemany(command_insert_sku, skus)

asyncio.run(main())
