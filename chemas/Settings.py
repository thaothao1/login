from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = '80cdef83fe2fe5f7d83c83696191736855597409b5692a3264a38252e169feb8'
