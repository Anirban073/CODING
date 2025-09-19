from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from db import engine


class Base(DeclarativeBase):
    pass

# user model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email:Mapped[str] = mapped_column(String, nullable=False, unique=True)


def __repr__(self):
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"
    

# post model one to many
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete="CASCADE"), nullable=False)

    title: Mapped[str] = mapped_column(String, nullable=False)
    content:Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"<Post id={self.id} title={self.title}>"
    

# create table
def create_tables():
    Base.metadata.create_all(engine)


# drop table
def  drop_tables():
    Base.metadata.drop_all(engine)