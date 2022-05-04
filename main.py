from fastapi import FastAPI
from endpoints.user import router as user_router
from endpoints.chat import router as chat_router

app = FastAPI()

app.include_router(user_router, tags=["user"])

app.include_router(chat_router, tags=["chat"])
