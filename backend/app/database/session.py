from sqlalchemy.orm import sessionmaker, Session
from app.database.engine import engine
from collections.abc import Generator

# SessionLocal creates a factory. Instance of SQLALchemy Session
SessionLocal = sessionmaker(bind=engine)

def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        # yield delivers Session to the code requesting get_session()
        # after the use it suspends this function
        yield db
    finally:
        db.close()
