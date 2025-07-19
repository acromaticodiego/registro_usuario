from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal, engine, Base
from tasks import send_welcome_email, generate_profile_report

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register_user(email: str, full_name: str, db: Session = Depends(get_db)):
    user = User(email=email, full_name=full_name)
    db.add(user)
    db.commit()
    db.refresh(user)

    send_welcome_email.delay(user.email)
    generate_profile_report.delay(user.id)

    return {"message": "Usuario registrado exitosamente"}