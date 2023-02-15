from dash import callback_context, dcc, html, Dash
from dash.dependencies import Input, Output, State

from entidades.cortipopokemon import Cor
import dash_bootstrap_components as dbc
from componentes.layouts import Layouts

context = html.Div(id='id_page_content')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server

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
                                className='inputs_dados',
                                value=None
                            ),
                            id='id_linha_input'
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
                                        dbc.Tab(label='Outras Formas',
                                                tab_id='id_outras_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Mega Formas',
                                                tab_id='id_mega_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Alola Formas',
                                                tab_id='id_alola_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Formas',
                                                tab_id='id_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Galar Formas',
                                                tab_id='id_galar_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='+ Formas',
                                                tab_id='id_mais_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='GMAX Formas',
                                                tab_id='id_gmax_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Hisui Formas',
                                                tab_id='id_hisui_formas',
                                                className='class_tab_name'),
                                        dbc.Tab(label='Origin Formas',
                                                tab_id='id_origin_formas',
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
               Input('id_select_input_pokemon', 'value'),
               [Input(f'{cor.name}', 'n_clicks') for cor in Cor], ])
def troca_tab(tab, pokemon, *_):
    ctx = callback_context
    l = Layouts()
    return l.gerar_tabs(tab, ctx.triggered_id, pokemon, tab)


if __name__ == "__main__":
    app.run_server(port=8052, debug=True)
