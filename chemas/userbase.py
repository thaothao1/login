from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Nga Hoang",
                "password": "password"
            }
        }
