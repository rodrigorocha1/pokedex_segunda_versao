from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from services.pokeservice import main
from entidades.cortipopokemon import Cor
from app import *
import dash_bootstrap_components as dbc
from asyncio import run
from componentes.telas import gera_tabs

context = html.Div(id='id_page_content')

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.ButtonGroup(
                        [
                            dbc.Button(
                                cor.name.capitalize(),
                                id=f'{cor.name}',
                                className='class_card',
                                style={'background-color': f'{cor.value}'}) for cor in Cor
                        ],
                        vertical=True,
                        id='id_botao_grupo_tipo'
                    ),
                    md=2,
                    id='id_coluna_1'),
                dbc.Col(
                    [
                        dbc.Row(

                            dbc.Select(
                                id='id_select_input_pokemon',
                                className='inputs_dados'
                            )

                        ),
                        dbc.Row(
                            [
                                dbc.Tabs(
                                    [
                                        dbc.Tab(label='Kanto - 1ª Geração',
                                                tab_id='id_primeira_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Johto - 2ª Geração',
                                                tab_id='id_segunda_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Hoenn - 3ª Geração',
                                                tab_id='id_terceira_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Sinnoh - 4ª Geração',
                                                tab_id='id_quarta_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Unova - 5ª Geração',
                                                tab_id='id_quinta_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Kalos - 6ª Geração',
                                                tab_id='id_sexta_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Alola - 7ª Geração',
                                                tab_id='id_setima_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Galar - 8ª Geração',
                                                tab_id='id_oitava_geracao',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Paldea - 9ª Geração',
                                                tab_id='id_nona_geracao',
                                                className='class_tab_name'),
                                    ],
                                    active_tab='id_primeira_geracao',
                                    id='id_tabs_geracao'
                                ),
                                html.Div(id='content'),
                            ],
                            id='id_segunda_linha'
                        )
                    ],
                    md=10
                )
            ]
        )
    ],
    id='id_tela_principal'
)


@app.callback(Output('content', 'children'),
              Output('id_select_input_pokemon', 'options'),
              [Input('id_tabs_geracao', 'active_tab'),
               [Input(f'{cor.name}', 'n_clicks') for cor in Cor],])
def troca_tab(tab, select_pokemon, *_):
    ctx = callback_context
    return gera_tabs(tab)


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
