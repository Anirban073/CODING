from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer
from db import engine


class Base(DeclarativeBase):
    pass


# user model
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone:Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"<Users(id={self.id}, name={self.name}, email={self.email})>"



