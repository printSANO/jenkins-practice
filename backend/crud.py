from sqlalchemy.orm import Session
from model import User
from schema import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
