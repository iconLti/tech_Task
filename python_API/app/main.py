from fastapi import FastAPI
from routers import router

import uvicorn



app = FastAPI(title="0.0.1")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

