# adapters/users_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.user_model import User
from application.users_service import (
    get_user,
    get_users,
    create_user,
    update_user,
    delete_user
)
from infrastructure.database import SessionLocal, engine, Base
from infrastructure import models

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.post("/users/", response_model=User)
def create_new_user(user: User, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.put("/users/{user_id}", response_model=User)
def update_existing_user(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.delete("/users/{user_id}", response_model=User)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user
