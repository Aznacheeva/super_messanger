from fastapi import APIRouter, Depends, HTTPException,
from starlette import status

import crud.user
from schemas.user import User, UserInDB
from crud.user import get_user_by_id, delete_user
from deps import get_db

router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_user(user_id: int, db=Depends(get_db())):
    """Получить пользователя по заданному user_id"""
    user = get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found user with {user_id} id")

    return user


@router.post("/", response_model=UserInDB)
async def create_user(user: User, db=Depends(get_db())):
    """Создать пользователя"""
    # Здесь происходит добавление пользователя в базу
    result = crud.user.create_user(db=db, user=user)
    return result


@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user: User, db=Depends(get_db())):
    user_db = crud.user.update_user(db=db, user_id = user_id, user=user)
    # Здесь изменения сохраняются в базу
    return user_db


@router.delete("/{user_id}")
async def delete_user(user_id: int, db=Depends(get_db())):
    crud.user.delete_user(db=db, user_id=user_id)
