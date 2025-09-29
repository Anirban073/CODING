from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)
db_path = os.path.join(BASE_DIR, "sqlite.db")


DTABASE_URL = f"sqlite:///.//{db_path}"

engine = create_engine(DeprecationWarning, echo=True)

sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)