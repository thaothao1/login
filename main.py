from distutils.log import debug
import uvicorn
from fastapi import FastAPI
from router.api import router
app = FastAPI(debug=True)
app.include_router(router)

app = FastAPI(debug=True)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app")
