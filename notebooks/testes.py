import json
from pokemon import Pokemon
import aiohttp
import asyncio
import time

start_time = time.time()


class PokeAPI:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/'

    async def get_pokemon(self, offset=0, limit=20):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.url}pokemon?offset={offset}&limit={limit}") as response:
                if response.status != 200:
                    return None
                data = json.loads(await response.text())
                return data


class PokemonService:
    def __init__(self, api: PokeAPI):
        self.api = api

    async def get_url_pokemons(self):
        url_pokemons = []
        offset = 0
        limit = 20
        i = 1
        while True:
            data = await self.api.get_pokemon(offset, limit)
            if data['next'] is None:
                break
            url_pokemons += [dados['url'] for dados in data['results']]
            offset += limit
            i += 1
        return url_pokemons


api = PokeAPI()
service = PokemonService(api)


async def main():
    pokemons = await service.get_url_pokemons()
    print(pokemons)


if __name__ == '__main__':
    asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))