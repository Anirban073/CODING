from models import Users, Posts
from db import sessionLocal

# insert or create user
def create_user(name: str, email:str):
    with sessionLocal() as session:
        user = Users(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    

# insert or create post
def create_post(user_id: int, title:str, content:str):
    with sessionLocal() as session:
        post = Posts (user_id=user_id, title=title, content=content)
        session.add(post)
        session.commit()


# read user by id
def get_user_by_id(user_id: int):
    with sessionLocal() as session:
        user = session.get(Users, user_id)
        return user