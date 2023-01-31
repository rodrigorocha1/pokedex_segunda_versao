from typing import List, Dict
import requests
from cortipopokemon import Cor


class Pokemon:
    class Pokemom:
        def __init__(self, resultado: Dict):
            self._id = resultado['id']
            self._name = resultado['name']
            self._peso = resultado['weight']
            self._tipos = [tipos['type']['name'] for tipos in resultado.get('types')]
            self._cor = ''.join([cor.value for cor in Cor if self._tipos[0] in cor.name])
            self._habilidade = [habilidades['ability']['name'] for habilidades in resultado['abilities']]
            self._img = resultado['sprites']['other']['home']['front_default'] \
                if resultado['sprites']['other']['home']['front_default'] is not None else \
                resultado['sprites']['other']['official-artwork']['front_default']
            self._estatisicas = {resultado['stats'][i]['stat']['name']:
                                     resultado['stats'][i]['base_stat'] for i in
                                 range(len(resultado['stats']))}

            self._moves = [resultado['moves'][i]['move']['name'] for i in range(len(resultado['moves']))]
            # self._locations = self.__get_location(kwargs['location_area_encounters'])
            self._locations = self.__get_location(resultado['location_area_encounters'])

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
