from models import *
import asyncio
from services import *

async def main():
    # create tables
    # await create_table()
    # await create_user("sonam", "sonam@gmail.com")
    # await create_user("anirban", "anirban@gmail.com")
    # print(await get_user_by_id(2))
    # print(await get_all_users())
    # await update_user_email(2, "spani@gmail.com")
    await delete_user(1)

asyncio.run(main())