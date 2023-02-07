from entidades.cortipopokemon import Cor
from entidades.pokemon import Pokemom
from dash import html
import dash_bootstrap_components as dbc


def gerar_cartoes(pokemon: Pokemom):
    return [
        dbc.CardImg(src=pokemon.img,
                    id=f'{pokemon.name}',
                    style={'width': '200px',
                           'height': '150px',
                           'margin-left': '50px',
                           'top': '0px'}),
        dbc.CardBody(
            [
                html.H5(f"{pokemon.id}-{pokemon.name.capitalize()}",
                        className="card-title",
                        title=pokemon.name,
                        id=f'nome_pokemon_{pokemon.id}', style={'font-size': '17px', 'text-align': 'justify'}),
                html.P(f"{' - '.join(pokemon.tipos).title()}"),
                dbc.Tabs(
                    [
                        dbc.Tab([
                            dbc.Row(
                                [
                                    dbc.Col(html.Div(f"{chave.upper()} - {valor}", id=f'id_stats_name_{chave}'),
                                            md=8,
                                            style={'font-size': '12px', 'margin-top': '1px'}),
                                    dbc.Col(
                                        dbc.Progress(value=valor, style={"height": "10px"},
                                                     id=f'id_progress_{chave}'),
                                        md=4,
                                        style={'margin-top': '5px'})
                                ]
                            ) for chave, valor in pokemon.estatisticas.items()

                        ],
                            label="Stats", label_style={'color': 'black'}, id='id_label_stats'),
                        # dbc.Tab(pokemon.habilidade, label="Habilites", label_style={'color': 'black'}),
                        dbc.Tab([
                            dbc.Row(
                                [
                                    habilidade.capitalize()
                                ], style={'margin-left': '5px'}, id=f'id_habilidade_{habilidade}'
                            ) for habilidade in pokemon.habilidade
                        ]
                            , label="Habilites", label_style={'color': 'black'}, id='label_habilidade'),
                        dbc.Tab([
                            dbc.Row(
                                [
                                    moves.capitalize()
                                ], style={'margin-left': '5px'
                                          }, id=f'id_moves_{moves}'
                            ) for moves in pokemon.moves
                        ]
                            , label="Moves", label_style={'color': 'black'}, id='label_moves',
                            style={"height": "120px", "overflow-y": "auto", 'overflow-x': 'hidden'}),
                        dbc.Tab([
                            dbc.Row(
                                [
                                    locations.title()
                                ], style={'margin-left': '5px'}
                            ) for locations in pokemon.locations
                        ]
                            , label="Location", label_style={'color': 'black'}, id='label_locations',
                            style={"height": "120px", "overflow-y": "auto", 'overflow-x': 'hidden'}),
                    ], style={'font-size': '10px'}
                ),
            ],
        )
    ]


def tela_pokemon(lista_pokemons, tipo=None):
    estilo = {'width': '305px',
              'left': '150px',
              'right': '85px',
              'height': '400px',
              }
    if tipo in [cor.name for cor in Cor]:
        return dbc.Row([  # Com tipo Selecionado
            dbc.Col(
                dbc.Card(gerar_cartoes(pokemon),
                         style=estilo,
                         color=f'{pokemon.cor}'

                         ), id=f'id_card_{pokemon.id}',
                style={'padding': '10px'},
                width="auto")
            for pokemon in lista_pokemons if tipo in pokemon.tipos]
        )
    return dbc.Row([  # Sem tipo selecionado
        dbc.Col(
            dbc.Card(gerar_cartoes(pokemon),
                     style=estilo,
                     color=f'{pokemon.cor}'

                     ), id=f'id_card_{pokemon.id}',
            style={'padding': '10px'},
            width="auto")
        for pokemon in lista_pokemons]
    )
