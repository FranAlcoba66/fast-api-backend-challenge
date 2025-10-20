# service.py
from sqlalchemy.orm import Session
from typing import List, Optional
from .models import User
from .repository import UserRepository
from app.core.clients import PokemonAPIClient
import json, asyncio

class UserService:

    def __init__(self, repository: UserRepository):
        self._repository = repository
        self._pokemon_client = PokemonAPIClient()


    async def get_user_by_id(self, db: Session, user_id: int) -> dict:
        user = self._repository.get_by_id(db, user_id)
        if not user:
            raise ValueError(f"Usuario con ID {user_id} no encontrado.")

        pokemon_ids = user.pokemon_ids or []

        try:
            pokemons = await self._pokemon_client.get_multiple_pokemon_names(pokemon_ids)
        except Exception:
            pokemons = [{"id": pid, "name": None} for pid in pokemon_ids]

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "pokemon_ids": pokemon_ids,
            "pokemons": pokemons
        }

    async def get_all_users(self, db: Session) -> List[dict]:
        users = self._repository.get_all(db)
        users_list = []

        for user in users:
            pokemon_ids = user.pokemon_ids or []

            try:
                pokemons = await self._pokemon_client.get_multiple_pokemon_names(pokemon_ids)
            except Exception:
                pokemons = [{"id": pid, "name": None} for pid in pokemon_ids]

            users_list.append({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "pokemon_ids": pokemon_ids,
                "pokemons": pokemons
            })

        return users_list

    def create_user(self, db: Session, name: str, email: str, pokemon_ids: Optional[List[int]] = None) -> User:
        self._validate_email(email)
        return self._repository.create(db, name, email, pokemon_ids)

    def update_user(self, db: Session, user_id: int, name: Optional[str] = None, email: Optional[str] = None, pokemon_ids: Optional[List[int]] = None) -> User:
        if email is not None:
            self._validate_email(email)
        user = self._repository.update(db, user_id, name, email, pokemon_ids)
        if not user:
            raise ValueError(f"Usuario con ID {user_id} no encontrado.")
        return user

    def delete_user(self, db: Session, user_id: int):
        deleted = self._repository.delete(db, user_id)
        if not deleted:
            raise ValueError(f"Usuario con ID {user_id} no encontrado.")

    def _validate_email(self, email: str):
        if '@' not in email or '.' not in email:
            raise ValueError("El email proporcionado no es válido.")
