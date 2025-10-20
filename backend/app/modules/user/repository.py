# repository.py
from sqlalchemy.orm import Session
from .models import User
from typing import List, Optional

class UserRepository:

    def get_all(self, db: Session) -> List[User]:
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def create(self, db: Session, name: str, email: str, pokemon_ids: Optional[List[int]] = None) -> User:
        user = User(name=name, email=email, pokemon_ids=pokemon_ids or [])
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, user_id: int, name: Optional[str] = None, email: Optional[str] = None, pokemon_ids: Optional[List[int]] = None) -> Optional[User]:
        user = self.get_by_id(db, user_id)
        if not user:
            return None
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if pokemon_ids is not None:
            user.pokemon_ids = pokemon_ids
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user_id: int) -> bool:
        user = self.get_by_id(db, user_id)
        if not user:
            return False
        db.delete(user)
        db.commit()
        return True
