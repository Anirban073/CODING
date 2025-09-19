from models import create_tables,drop_tables
from services import *

create_tables()
# drop_tables()

# create data
# result = create_user("soanam", "sonam@g.c")
# print(result)

create_post(1,"hello world", "this is my first post")


# read data
print(get_user_by_id(1))