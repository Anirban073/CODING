from app.db.config import sessionLocal
from app.user.models import User
from sqlalchemy import select

# insert or create user
def create_user(name: str, email: str):
    with sessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()

# read all
def get_all_users():
    with sessionLocal() as session:
        htmt = select(User)
        users = session.scalars(htmt)
        return users.all()