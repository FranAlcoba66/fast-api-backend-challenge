# # app/modules/pokemon/service.py
# from typing import List
# import asyncio
# from app.core.clients import fetch_pokemon
# from .schemas import PokemonSchema, PokemonType


# async def get_pokemon(name_or_id: str) -> PokemonSchema:
#     data = await fetch_pokemon(name_or_id)
#     types = [PokemonType(name=t["type"]["name"]) for t in data.get("types", [])]
#     return PokemonSchema(id=data["id"], name=data["name"], types=types)


# async def get_pokemon_list(ids_or_names: List[str]) -> List[PokemonSchema]:
#     """
#     Obtiene un listado de Pokémon según una lista de nombres o IDs.
#     """
#     tasks = [get_pokemon(str(item)) for item in ids_or_names]
#     return await asyncio.gather(*tasks)
