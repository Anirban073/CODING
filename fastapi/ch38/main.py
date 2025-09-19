from tables import create_tables
from services import create_user
from services import *

# function call
create_tables()

# create data
create_user("sonam", "soanam@gmail.com")
# create_post(1, "anirban", "this is my first post")


# read data
print(get_user_by_id(1))
