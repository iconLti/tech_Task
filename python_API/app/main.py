from fastapi import FastAPI
from app.routers import router

import uvicorn



app = FastAPI(title="1.0.0")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)

