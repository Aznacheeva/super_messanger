from fastapi import APIRouter
from crud.chat import chat_database
from schemas.chat import Chat, ChatInDB

router = APIRouter(prefix="/chat")


@router.get("/{chat_id}")
async def get_chat(chat_id: int):
    """Получить чат по chat_id"""
    return chat_database[chat_id - 1]


@router.post("/", response_model=ChatInDB)
async def create_chat(chat: Chat):
    """Создать чат"""
    chat_db = ChatInDB(id=len(chat_database) + 1, **chat.dict)


@router.put("/{chat_id}", response_model=ChatInDB)
async def update_chat(chat_id: int, chat: Chat):
    """Обновить чат"""
    chat_db = chat_database[chat_id - 1]
    for param, value in chat.dict():
        chat_db[param] = value
    return chat_db


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int):
    db = list(chat_database)
    del db[chat_id - 1]
    return db
