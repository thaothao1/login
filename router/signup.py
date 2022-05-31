from http.client import HTTPException
from os import access
from fastapi import APIRouter, Depends, status
from chemas.userbase import UserBase
from typing import List
from database import session
from chemas.userlogin import UserLogin
from models.user import User
from fastapi_jwt_auth import AuthJWT
from chemas.Settings import Settings

app = APIRouter()

users = []


@AuthJWT.load_config
def get_config():
    return Settings()


@app.post("/signup", status_code=201)
def create_user(request: UserBase):
    new_user = User(username=request.username, password=request.password)
    session.add(new_user)
    session.commit()
    return new_user


@app.get("/users", status_code=201)
def get_user():
    data = session.query(User).all()
    return {"data": data}


@app.post('/login')
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    data = session.query(User).all()
    for i in data:
        if i.username == user.username and i.password == user.password:
            access_token = Authorize.create_access_token(subject=user.username)
            refresh_token = Authorize.create_refresh_token(
                subject=user.username)
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            return {"error": "Invalid username or password"}


@app.get('/protected')
def get_logged_in_user(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        return {"error": "Invalid username or password"}

    current_user = Authorize.get_jwt_subject()

    return {"current_user": current_user}
