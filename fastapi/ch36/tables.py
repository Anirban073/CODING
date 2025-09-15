from db import engine
from sqlalchemy import MetaData,Table,Column, Integer, String, DateTime

metadata = MetaData()

# user table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),

    Column("name", String(length=50), nullable=False),

    Column("email", String, nullable=False, unique=True),

    Column("phone", Integer, nullable=False, unique=True)
)

# address table
address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True),

    Column("street", String(length=50), nullable=False),

    Column("dist", String, nullable=False, unique=True),

    Column("country", String, nullable=False, unique=True)
)

# create table in database
def create_tables():
    metadata.create_all(engine)


# # drop table in database
# def drop_tables():
#     metadata.drop_all(engine)\

