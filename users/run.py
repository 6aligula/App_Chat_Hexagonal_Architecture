# project/run.py
import os
import uvicorn
from fastapi import FastAPI
from adapters.users_controller import router as users_router

app = FastAPI()

app.include_router(users_router)

if __name__ == "__main__":
    reload = os.getenv("DEBUG", "false").lower() == "true"
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=reload)

