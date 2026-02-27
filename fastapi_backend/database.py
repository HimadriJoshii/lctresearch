from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
DATABASE_URL='sqlite:///../databases/tasks.sqlite3'
engine=create_engine(DATABASE_URL,connect_args={
    "check_same_thread":False
})

class Base(DeclarativeBase):
    pass
SessionLocal=sessionmaker(bind=engine)

def get_db():
    with SessionLocal() as db:
        yield db