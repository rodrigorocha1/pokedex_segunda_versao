import os
import pickle
from entidades.pokemon import Pokemom
from typing import List


class APICache:

    def __init__(self):
        self.__caminho = os.getcwd() + '\\caches\\'

    def salvar_cache(self, nome_geracao: str, pokemons: List[Pokemom]):
        print('dentro do método de salvar_cache ')
        """
            Método para gravar o cache por geração
        :param nome_geracao: nome da geração lista do pokemo
        :param pokemons: Lista de pokemons
        :return:
        """
        with open(self.__caminho + nome_geracao, 'wb') as f:
            pickle.dump(pokemons, f)

    def abrir_cache(self, nome_geracao) -> List[Pokemom]:
        print('dentro do método de abrir_cache ')
        """
            Método para abrir o cache
        :param nome_geracao: nome da geração
        :return: lista de pokemons
        """
        with open(self.__caminho + nome_geracao, 'rb') as f:
            return pickle.load(f)

    def verificar_aquivo(self, id_geracao: str) -> bool:
        if id_geracao in os.listdir(self.__caminho):
            return True
        return False

    def __del__(self):
        for nome in os.listdir(self.__caminho):
            os.remove(self.__caminho + nome)


