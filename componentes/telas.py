from asyncio import run

from entidades.cortipopokemon import Cor
from entidades.pokemon import Pokemom
from dash import html
import dash_bootstrap_components as dbc
from typing import List

from services.pokeservice import main


def layout_pokemon_id(pokemon: Pokemom):
    return dbc.Row(
        dbc.Col(
            [
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
            ]
        )
    )


def gerar_cartoes(pokemons: List[Pokemom], tipo=None):
    if tipo in [cor.name for cor in Cor]:
        return dbc.Row(
            dbc.Col(
                [
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
                    ) for pokemon in pokemons if tipo in pokemon.tipos
                ]
            )
        )
    else:
        return dbc.Row(
            dbc.Col(
                [
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
                    ) for pokemon in pokemons
                ]
            )
        )


def gera_tabs(tab, tipo=None, id_pokemon=None):
    if tab == 'id_primeira_geracao':
        inicio = 1
        fim = 151
        lista_pokemons = run(main(inicio, fim))
        opcoes_pokemon = [
            {'label': f'{pokemon.id} - {pokemon.name.title()}',
             'value': f'{pokemon.id}'}
            for pokemon in lista_pokemons
        ]
        if id_pokemon is None or id_pokemon == '0':

            return gerar_cartoes(pokemons=lista_pokemons, tipo=tipo), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon

        else:
            pokemon_unico = run(main(inicio, fim, id_pokemon))
            return layout_pokemon_id(pokemon=pokemon_unico), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon

    elif tab == 'id_segunda_geracao':
        inicio = 152
        fim = 251
        lista_pokemons = run(main(inicio, fim))
        opcoes_pokemon = [
            {'label': f'{pokemon.id} - {pokemon.name.title()}',
             'value': f'{pokemon.id}'}
            for pokemon in lista_pokemons
        ]
        if id_pokemon is None or id_pokemon == '0':

            return gerar_cartoes(pokemons=lista_pokemons, tipo=tipo), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon

        else:
            pokemon_unico = run(main(inicio, fim, id_pokemon))
            return layout_pokemon_id(pokemon=pokemon_unico), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon
    elif tab == 'id_terceira_geracao':
        return '3'
    elif tab == 'id_quarta_geracao':
        return '4'
    elif tab == 'id_quinta_geracao':
        return '5'
    elif tab == 'id_sexta_geracao':
        return '6'
    elif tab == 'id_setima_geracao':
        return '7'
    elif tab == 'id_oitava_geracao':
        return '8'
    elif tab == 'id_nona_geracao':
        inicio = 906
        fim = 1010
        lista_pokemons = run(main(inicio, fim))
        opcoes_pokemon = [
            {'label': f'{pokemon.id} - {pokemon.name.title()}',
             'value': f'{pokemon.id}'}
            for pokemon in lista_pokemons
        ]
        if id_pokemon is None or id_pokemon == '0':

            return gerar_cartoes(pokemons=lista_pokemons, tipo=tipo), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon

        else:
            pokemon_unico = run(main(inicio, fim, id_pokemon))
            return layout_pokemon_id(pokemon=pokemon_unico), \
                [
                    {
                        'label': 'Lista todos os pokemons',
                        'value': 0
                    },
                ] + opcoes_pokemon
    return html.P('Não selecionado')
