import asyncio
import atexit
from typing import List
from services.pokeapi import PokeAPI
from entidades.pokemon import Pokemom
from services.api_cache import APICache


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


async def main(inicio, fim, id_pokemon=None, id_geracao=None) -> List[Pokemom]:
    apicache = APICache()
    if id_pokemon is None or id_pokemon == 0:
        if apicache.verificar_aquivo(id_geracao) is False:
            pokemons = await service.get_lista_pokemons(inicio, fim)
            apicache.salvar_cache(id_geracao, pokemons)
        else:
            pokemons = apicache.abrir_cache(id_geracao)
    else:
        pokemons = await service.obter_dados_pokemon_id(id_pokemon)

    atexit.register(lambda: apicache.__del__() if apicache else None)
    return pokemons


if __name__ == '__main__':
    asyncio.run(main(906, 1008))
