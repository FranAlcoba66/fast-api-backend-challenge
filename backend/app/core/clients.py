# app/core/clients.py
import httpx, asyncio
from app.core.config import get_settings
from typing import List

settings = get_settings()

class PokemonAPIClient:

    def __init__(self):
        self.client = httpx.AsyncClient(base_url=settings.POKEMON_API_URL)

    async def get_pokemon(self, pokemon_id: int) -> dict:
        response = await self.client.get(f"pokemon/{pokemon_id}")
        response.raise_for_status()
        return response.json()

    async def get_pokemon_name(self, pokemon_id: int) -> str:
        data = await self.get_pokemon(pokemon_id)
        return data["name"]

    async def get_multiple_pokemon_names(self, ids: List[int]) -> List[dict]:
        # Llamadas paralelas
        tasks = [self.get_pokemon(pid) for pid in ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        pokemons_data = []
        for r, pid in zip(results, ids):
            if isinstance(r, Exception):
                pokemons_data.append({"id": pid, "name": None})
            else:
                pokemons_data.append({"id": pid, "name": r.get("name", None)})
        return pokemons_data

    async def close(self):
        await self.client.aclose()
