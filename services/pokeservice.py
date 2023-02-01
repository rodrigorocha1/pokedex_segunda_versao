import asyncio
from typing import List
import requests
from services.pokeapi import PokeAPI
from entidades.pokemon import Pokemom


class PokemonService:
    def __init__(self, api: PokeAPI):
        """
        Atributo para receber a conexão
        :param api:
        """
        self.api = api

    async def get_lista_pokemons(self, inicio, fim) -> List[Pokemom]:
        """

        :param inicio: inicio do número pokemon
        :param fim: fim numero
        :return: Uma Lista de pokemons
        """
        pokemons = []

        for indice in range(inicio, fim + 1):
            pokemons_data = await self.api.get_pokemon(indice)
            obj_pokemon = Pokemom(pokemons_data)
            pokemons.append(obj_pokemon)
        return pokemons

    async def obter_dados_pokemon_id(self, id_pokemon: int) -> Pokemom:
        """
        Faz a chamada da api e retorna em um objeto
        :param id_pokemon: id do pokemon int
        :return: objeto do tipo pokemon
            """
        pokemons_data = await self.api.get_pokemon(id_pokemon)
        pokemon = Pokemom(pokemons_data)
        return pokemon


api = PokeAPI()
service = PokemonService(api)


async def main():
    pokemons = await service.get_lista_pokemons(906, 950)
    for pokemon in pokemons:
        print(pokemon.id)
        print(pokemon.name)
        print(pokemon.tipos)
        print(pokemon.geracao)
        print()


if __name__ == '__main__':
    asyncio.run(main())
