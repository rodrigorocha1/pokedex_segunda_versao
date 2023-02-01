from typing import List, Dict
import requests
from entidades.cortipopokemon import Cor


class Pokemom:
    def __init__(self, dados: Dict):
        """
        atributos para desserializar o json de pokemons
        :param dados: dados dos pokemons em dicionários
        """
        self._id = dados['id']
        self._name = dados['name']
        self._peso = dados['weight']
        self._tipos = [tipos['type']['name'] for tipos in dados.get('types')]
        self._cor = ''.join([cor.value for cor in Cor if self._tipos[0] in cor.name])
        self._habilidade = [habilidades['ability']['name'] for habilidades in dados['abilities']]
        self._img = dados['sprites']['other']['home']['front_default'] \
            if dados['sprites']['other']['home']['front_default'] is not None else \
            dados['sprites']['other']['official-artwork']['front_default']
        self._estatisicas = {dados['stats'][i]['stat']['name']:
                                 dados['stats'][i]['base_stat'] for i in
                             range(len(dados['stats']))}

        self._moves = [dados['moves'][i]['move']['name'] for i in range(len(dados['moves']))]
        self._locations = self.__get_location(dados['location_area_encounters'])

    def __get_location(self, url: str) -> List[str]:
        req = requests.get(url)

        if req.status_code == 404:
            location = []
        else:
            location = req.json()
        return [location[i]['location_area']['name'] for i in range(len(location))]

    @property
    def locations(self):
        return self._locations

    @property
    def moves(self) -> List[str]:
        return self._moves

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id

    @property
    def tipos(self) -> List[str]:
        return self._tipos

    @property
    def img(self) -> str:
        return self._img

    @property
    def cor(self) -> str:
        return self._cor

    @property
    def habilidade(self) -> List[str]:
        return self._habilidade

    @property
    def estatisticas(self) -> Dict[str, int]:
        return self._estatisicas

    @property
    def peso(self) -> str:
        return self._peso
