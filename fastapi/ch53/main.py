from tables import create_tables, drop_tables
import asyncio
from services import *

async def main():
    # table create
    # await create_tables()

    # data create
    # await create_user("sonam", "sonam@gmail.com")
    # await create_user("ani", "anirban@gmail.com")
    # print(await get_user_by_id(2))
    # print(await get_all_users())
    # await update_user_email(2, "spani@gmail.com")
    await delte_user(1)


asyncio.run(main())