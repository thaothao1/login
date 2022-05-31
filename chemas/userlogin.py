from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "thaone",
                "password": "Thaothao123"
            }
        }
