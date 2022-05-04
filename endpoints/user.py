from fastapi import APIRouter
from schemas.user import User, UserInDB
from crud.user import user_database

router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_user(user_id: int):
    """Получить пользователя по заданному user_id"""
    return user_database[user_id - 1]


@router.post("/", response_model=UserInDB)
async def create_user(user: User):
    """Создать пользователя"""
    # Здесь происходит добавление пользователя в базу
    user_db = UserInDB(id=len(user_database) + 1, **user.dict())
    return user_db


@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user: User):
    user_db = user_database[user_id - 1]
    for param, value in user.dict():
        user_db[param] = value
    # Здесь изменения сохраняются в базу
    return user_db


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    db = list(user_database)
    del db[user_id - 1]
    return db
