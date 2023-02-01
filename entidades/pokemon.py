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
        self._geracao = self.__verificar_geracao(self._id)
        self._peso = dados['weight']
        self._altura = dados['height']

    @property
    def peso(self):
        return self._peso

    @property
    def altura(self):
        return self._altura

    @property
    def geracao(self):
        return self._geracao

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

    def __verificar_geracao(self, id_pokemon: int) -> str:
        """
        Método para verificar a geração do pokemon
        :param id_pokemon: id do pokemon
        :return: Geração
        """
        if 1 <= id_pokemon <= 151:
            return 'Kanto - 1ª Geração'
        elif 152 <= id_pokemon <= 251:
            return 'Johto - 2ª Geração'
        elif 252 <= id_pokemon <= 386:
            return 'Hoenn - 3ª Geração'
        elif 387 <= id_pokemon <= 493:
            return 'Hoenn - 3ª Geração'
        elif 494 <= id_pokemon <= 649:
            return 'Unova - 5ª Geração'
        elif 650 <= id_pokemon <= 721:
            return 'Kalos - 6ª Geração'
        elif 722 <= id_pokemon <= 809:
            return 'Alola - 7ª Geração'
        elif 810 <= id_pokemon <= 905:
            return 'Galar - 8ª Geração'
        elif 906 <= id_pokemon <= 1010:
            return 'Paldea - 9ª Geração'
        elif 10001 <= id_pokemon <= 10032:
            return 'Outras Formas'
        elif 10033 <= id_pokemon <= 10090:
            return 'Mega Formas'
        elif 10091 <= id_pokemon <= 10115:
            return 'Formas Alola'
        elif 10116 <= id_pokemon <= 10160:
            return 'Formas'
        elif 10161 <= id_pokemon <= 10180:
            return 'Formas Galar'
        elif 10182 <= id_pokemon <= 10194:
            return '+ Formas'
        elif 10195 <= id_pokemon <= 10228:
            return 'Formas Gmax'
        elif 10229 <= id_pokemon <= 10244:
            return 'Formas Hisui'
        elif 10245 <= id_pokemon <= 10249:
            return 'Formas Origin'
