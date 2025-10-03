from sqlmodel import Session, select
from app.db.config import engine
from app.user.models import User

def create_user(name: str, email: str):
    with Session(engine) as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    

def get_all_users():
    with Session(engine) as session:
        stmt = select(User)
        users = session.scalars(stmt)
        return users.all()