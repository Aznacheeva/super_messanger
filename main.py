import uvicorn
from fastapi import FastAPI
from endpoints.user import router as user_router
from endpoints.chat import router as chat_router
from core.db.models import Base
from core.db.session import engine, db_url

app = FastAPI()

app.include_router(user_router, tags=["user"])

app.include_router(chat_router, tags=["chat"])

if __name__=="__main__":
    print(db_url)
    Base.metadata.create_all(engine)
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8080,
        reload=True,
        debug=True,
    )
