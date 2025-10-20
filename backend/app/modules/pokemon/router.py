# # app/modules/pokemon/router.py
# from fastapi import APIRouter, HTTPException, Query
# from typing import List
# from .service import get_pokemon, get_pokemon_list
# from .schemas import PokemonSchema

# router = APIRouter(
#     prefix="/pokemon",
#     tags=["pokemon"]
# )


# @router.get("/{name_or_id}", response_model=PokemonSchema)
# async def get_pokemon_by_name_or_id(name_or_id: str):
#     try:
#         return await get_pokemon(name_or_id)
#     except Exception:
#         raise HTTPException(status_code=404, detail=f"Pokémon '{name_or_id}' no encontrado")


# @router.post("/list", response_model=List[PokemonSchema])
# async def get_custom_pokemon_list(ids_or_names: List[str]):
#     """
#     Recibe una lista de nombres o IDs de Pokémon y devuelve los datos correspondientes.
#     """
#     if not ids_or_names:
#         raise HTTPException(status_code=400, detail="Debe enviar al menos un nombre o ID")
#     try:
#         return await get_pokemon_list(ids_or_names)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=f"Error obteniendo Pokémon: {str(e)}")
