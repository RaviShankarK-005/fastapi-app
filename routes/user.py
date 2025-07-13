from fastapi import APIRouter, Depends, HTTPException
import dbutil.dbimpl as crud
from sqlalchemy.orm import Session
from dbutil.database import Base,engine
from models.dbmodels import User
from dbutil.database import get_db
from models.apimodels import UserCreate,UserUpdate,UserResp
import bcrypt
import authutil.auth as authimpl
from authutil.auth import authorize_roles

router = APIRouter(
    prefix="",
    dependencies=[Depends(authimpl.get_current_user)],  # 🔒 applies to all routes
    tags=["userutil"]
)
Base.metadata.create_all(bind=engine)

@router.post("/users/", response_model=UserResp)
def create(user: UserCreate, db: Session = Depends(get_db),current_user: User = Depends(authorize_roles(["ADMIN"]))):
    user.password= bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    return crud.create_user(db, user)

@router.get("/users/", response_model=list[UserResp])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@router.get("/users/{user_id}", response_model=UserResp)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id_name}", response_model=UserResp)
def update(user_id_name: str, updates: UserUpdate, db: Session = Depends(get_db),current_user: User = Depends(authorize_roles(["ADMIN"]))):
    if updates.password:
        updates.password= bcrypt.hashpw(updates.password.encode('utf-8'), bcrypt.gensalt())
    if user_id_name.isdigit():
        return crud.update_user(db, int(user_id_name), updates)
    return crud.update_user_by_name(db, user_id_name, updates)
    

@router.delete("/users/{user_id}", response_model=UserResp)
def delete(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)