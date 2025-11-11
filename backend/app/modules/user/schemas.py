from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class PokemonInfo(BaseModel):
    id: int
    name: Optional[str]

class UserCreate(BaseModel):
    """Input DTO: Esquema para la creación de un usuario."""
    name: str
    email: str
    pokemon_ids: Optional[List[int]] = []

class UserUpdate(BaseModel):
    """Input DTO: Esquema para la actualización de un usuario."""
    name: Optional[str] = None
    email: Optional[str] = None
    pokemon_ids: Optional[List[int]] = None

class UserResponseDb(BaseModel):

    id: int
    name: str
    email: str
    pokemon_ids: List[int]
    pokemons: List[str] = None

    class ConfigDict:
        from_attributes = True

class UserResponse(BaseModel):
    """Output DTO: Esquema de respuesta para un usuario."""
    id: int
    name: str
    email: str
    pokemon_ids: List[int]
    pokemons: List[PokemonInfo] = []

    model_config = ConfigDict(from_attributes=True)