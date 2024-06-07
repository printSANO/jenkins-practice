from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import model
from database import SessionLocal, engine
from schema import UserCreate
from crud import create_user

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to Jenkins Test!"}

@app.get("/test/")
async def root():
    return {"message": "This is a test"}

@app.post("/users/", response_model=UserCreate)
def create_user_test(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)