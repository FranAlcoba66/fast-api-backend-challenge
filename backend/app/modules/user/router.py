# router.py
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from .schemas import UserCreate, UserResponse, UserUpdate
from .service import UserService
from .repository import UserRepository
from app.core.databse import get_db
import asyncio
router = APIRouter()

def get_user_service() -> UserService:
    return UserService(repository=UserRepository())


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(
    user_in: UserCreate,
    service: UserService = Depends(get_user_service),
    db: Session = Depends(get_db)
):
    try:
        return service.create_user(
            db,
            name=user_in.name,
            email=user_in.email,
            pokemon_ids=user_in.pokemon_ids
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[UserResponse])
async def read_users_endpoint(
    service: UserService = Depends(get_user_service),
    db: Session = Depends(get_db)
):
    return await service.get_all_users(db)


# 🔹 Endpoint ASÍNCRONO para obtener usuario por ID con pokemons
@router.get("/{user_id}", response_model=UserResponse)
async def read_user_endpoint(
    user_id: int,
    service: UserService = Depends(get_user_service),
    db: Session = Depends(get_db)
):
    try:
        return await service.get_user_by_id(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(
    user_id: int,
    user_in: UserUpdate,
    service: UserService = Depends(get_user_service),
    db: Session = Depends(get_db)
):
    try:
        return service.update_user(
            db,
            user_id,
            user_in.name,
            user_in.email,
            pokemon_ids=user_in.pokemon_ids
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(
    user_id: int,
    service: UserService = Depends(get_user_service),
    db: Session = Depends(get_db)
):
    try:
        service.delete_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
