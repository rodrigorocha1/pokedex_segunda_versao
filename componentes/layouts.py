from asyncio import run
from entidades.cortipopokemon import Cor
from entidades.pokemon import Pokemom
from dash import html
import dash_bootstrap_components as dbc
from typing import List
from services.pokeservice import main


class Layouts:
    """
        Classe para gerar o layout dos pokemons
    """

    def gerar_tabs(self, tab, tipo=None, id_pokemon=None, id_geracao=None):

        """
            Função para controlar as mudanças de seleção dos pokemons
        :param id_geracao: id da geracao do pokemon
        :param tab: recebe a tab selecionado
        :param tipo: Recebe o tipo do pokemon clicado no botão
        :param id_pokemon: recebe o id do pokemon
        :return: retorna os dados
        """

        if tab == 'id_primeira_geracao':
            inicio = 1
            fim = 151
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)

        elif tab == 'id_segunda_geracao':
            inicio = 152
            fim = 251
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_terceira_geracao':
            inicio = 252
            fim = 386
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_quarta_geracao':
            inicio = 387
            fim = 493
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_quinta_geracao':
            inicio = 494
            fim = 649
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_sexta_geracao':
            inicio = 650
            fim = 721
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_setima_geracao':
            inicio = 722
            fim = 809
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_oitava_geracao':
            inicio = 810
            fim = 905
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_nona_geracao':
            inicio = 906
            fim = 1008
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_outras_formas':
            inicio = 10001
            fim = 10032
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_mega_formas':
            inicio = 10033
            fim = 10090
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_alola_formas':
            inicio = 10091
            fim = 10115
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_formas':
            inicio = 10116
            fim = 10160
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_galar_formas':
            inicio = 10161
            fim = 10180
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_mais_formas':
            inicio = 10182
            fim = 10194
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_gmax_formas':
            inicio = 10195
            fim = 10228
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_hisui_formas':
            inicio = 10229
            fim = 10244
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)
        elif tab == 'id_origin_formas':
            inicio = 10245
            fim = 10249
            return self.__controle_tabs(inicio, fim, id_pokemon, tipo, id_geracao=id_geracao)

        return html.P('Não selecionado')

    def __controle_tabs(self, inicio: int, fim: int, id_pokemon: str, tipo: str, id_geracao: str):
        """
            Método para devolver um ou varios cartão
        :param inicio: ínicio das listagens do pokemon
        :param fim: fim das listagens do pokemon
        :param id_pokemon: id do pokemon
        :param tipo: tipo do pokemon selecionado
        :return: um ou vários cartões, depedendo do que for selecionado
        """

        lista_pokemons = run(main(inicio, fim, id_pokemon=None, id_geracao=id_geracao))

        opcoes_pokemon = [
            {'label': f'{pokemon.id} - {pokemon.name.title()}',
             'value': f'{pokemon.id}'}
            for pokemon in lista_pokemons
        ]

        if id_pokemon is None or id_pokemon == '0':
            return self.__gerar_cartoes(pokemons=lista_pokemons, tipo=tipo), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon

        else:
            pokemon_unico = run(main(inicio, fim, id_pokemon))
            return self.__gerar_cartao(pokemon=pokemon_unico), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon

    def __gerar_cartoes(self, pokemons: List[Pokemom], tipo=None):
        """
            Gera cartões de acordo com a seleção
        :param pokemons: Uma lista de objeto de pokemons
        :param tipo: O tipo de pokemons selecionado
        :return: um ou vários cartões, depedendo do que for selecionado
        """
        if tipo in [cor.name for cor in Cor]:
            return dbc.Row(
                dbc.Col(
                    [
                        self.__gerar_cartao(pokemon) for pokemon in pokemons if tipo in pokemon.tipos
                    ]

                )
            )
        else:
            return dbc.Row(
                dbc.Col(
                    [
                        self.__gerar_cartao(pokemon) for pokemon in pokemons
                    ]

                )
            )

    def __gerar_cartao(self, pokemon: Pokemom):
        '''
            Gera o Cartão propriamente dito
        :param pokemon: Uma lista de objeto
        :return: Gera um cartão
        '''
        return \
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.CardImg(src=pokemon.img,
                                    id=f'{pokemon.name}',
                                    className='class_img_pokemon'),
                        html.P(f'{pokemon.id} - {pokemon.name.title()}',
                               id=f'id_nome_pokemon_{pokemon.id}',
                               className='class_nome_pokemon'),
                        html.P(f' - '.join(pokemon.tipos).title(),
                               className='class_nome_pokemon'),
                        html.P(pokemon.geracao.title(),
                               className='class_nome_pokemon'),
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    html.Div(
                                                        f'{chave.upper()} - {valor}',
                                                        id=f'id_stats_name_{chave}',
                                                        className='class_nome_pokemon'
                                                    ),
                                                    md=8,
                                                    className='teste',
                                                    id=f'{chave}',

                                                ),
                                            ]
                                        ) for chave, valor in pokemon.estatisticas.items()
                                    ],
                                    label='Stats',
                                    label_style={
                                        'color': 'Black',
                                        'margin-left': '5px',
                                    },
                                    id='id_label_habilidade'
                                ),
                                dbc.Tab(
                                    [
                                        dbc.Row(
                                            [
                                                habilidade.capitalize()
                                            ],
                                            style={
                                                'margin-left': '5px',

                                            },
                                            id=f'id_habilidade{habilidade}'
                                        ) for habilidade in pokemon.habilidade
                                    ],
                                    label='Habilidades',
                                    label_style={
                                        'color': 'Black',
                                        'heigth': '30px'

                                    },
                                    id='id_label_habilidade',
                                    style={'heigth': '100px'},
                                    className='class_nome_pokemon'
                                ),
                                dbc.Tab(
                                    [
                                        dbc.Row(
                                            [
                                                move.capitalize()
                                            ],
                                            style={
                                                'margin-left': '5px'
                                            },
                                            className='class_nome_pokemon',
                                            id=f'id_moves_{move}'
                                        ) for move in pokemon.moves
                                    ],
                                    label='Moves',
                                    label_style={
                                        'color': 'black',
                                    },
                                    id='id_label_moves',
                                    className='class_habilidade',
                                ),
                                dbc.Tab(
                                    [
                                        dbc.Row(
                                            [
                                                loc.capitalize()
                                            ],
                                            style={
                                                'margin-left': '5px'
                                            },
                                            className='class_nome_pokemon',
                                            id=f'id_moves_{loc}'
                                        ) for loc in pokemon.locations
                                    ],
                                    label='Location',
                                    label_style={
                                        'color': 'black',
                                    },
                                    id='id_label_moves',
                                    className='class_habilidade',
                                )
                            ]
                        )
                    ],
                ), className='class_cards_pokemons',
                color=f'{pokemon.cor}'
            )
