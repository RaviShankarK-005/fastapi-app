from fastapi import APIRouter, Depends, HTTPException
from models.apimodels import UserLogin,Token,UserResp
from sqlalchemy.orm import Session
from models.dbmodels import User
from dbutil.database import get_db
import authutil.auth as authimpl


router = APIRouter(
    prefix="",
    tags=["jwtutil"]
)

@router.post("/login", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_login.username).first()
    if not user or not authimpl.verify_password(user_login.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = authimpl.create_access_token(data={"sub": user.username,"role":user.role})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=UserResp)
def read_users_me(current_user: User = Depends(authimpl.get_current_user)):
    return current_user