from sqlalchemy.orm import Session
from models.dbmodels import User
from models.apimodels import UserCreate,UserUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username or Email already exists")

def get_user(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.userid == user_id).first()
        return user
    except:
        return None

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, updates: UserUpdate):
    db_user = db.query(User).filter(User.userid == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_by_name(db: Session, user_name: str, updates: UserUpdate):
    db_user = db.query(User).filter(User.username == user_name).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.userid == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user
