import json
from typing import Dict

import aiohttp


class PokeAPI:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/'

    async def get_pokemon(self, indice: int) -> Dict:
        """
        Método para retornar um dicionario de pokenon
        :param indice: incide do pokemon
        :return: json
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}pokemon/{indice}/') as response:
                if response.status != 200:
                    return None
                data = json.loads(await response.text())
                return data


