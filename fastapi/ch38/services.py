from db import engine
from tables import users,posts
from sqlalchemy import insert, select, update, delete


# insert or create user
def create_user(name: str, email: str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email)
        conn.execute(stmt)
        conn.commit()


# insert or create post
def create_post(user_id: int, title: str, content: str):
    with engine.connect() as conn:
        stmt = insert(posts).values(user_id=user_id, title=title, content = content)
        conn.execute(stmt)
        conn.commit()



# get single user by id
def get_user_by_id(user_id: int):
    with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id)
        result = conn.execute(stmt).first()
        return result
