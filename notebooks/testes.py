import json
import aiohttp
import asyncio
import time

start_time = time.time()


class PokeAPI:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/'

    async def get_pokemon(self, indice: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}pokemon/{indice}/') as response:
                if response.status != 200:
                    return None
                data = json.loads(await response.text())
                return data


class PokemonService:
    def __init__(self, api: PokeAPI):
        self.api = api

    async def get_url_pokemons(self, inicio, fim):
        pokemons = []
        i = 1
        for indice in range(inicio, fim + 1):
            print(i)
            data = await self.api.get_pokemon(indice)
            pokemons.append(data)
            i += 1

        return pokemons


api = PokeAPI()
service = PokemonService(api)


async def main():
    pokemons = await service.get_url_pokemons(1, 100)
    print(pokemons)


if __name__ == '__main__':
    asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))