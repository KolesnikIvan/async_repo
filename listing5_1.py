import asyncpg
import asyncio

from util.db_create_statements import COLOR_INSERT, CREATE_BRAND_TABLE, CREATE_PRODUCT_COLOR_TABLE, CREATE_PRODUCT_SIZE_TABLE, CREATE_PRODUCT_TABLE, CREATE_SKU_TABLE, SIZE_INSERT

async def main():
    connection = await asyncpg.connect(host="127.0.0.1",
                                       port=5432,
                                       user="postgres",
                                       database="products",
                                       password="master")
    version = connection.get_server_version()
    print(f"got connection; version {version}")

    # "CREATE DATABASE products",
    statements = [
                  CREATE_BRAND_TABLE,
                  CREATE_PRODUCT_TABLE,
                  CREATE_PRODUCT_COLOR_TABLE,
                  CREATE_PRODUCT_SIZE_TABLE,
                  CREATE_SKU_TABLE,
                  SIZE_INSERT,
                  COLOR_INSERT]
    
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
        input()
    print("db is created")
    await connection.close()
    
asyncio.run(main())
