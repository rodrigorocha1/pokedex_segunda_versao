from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from services.pokeservice import main
from entidades.cortipopokemon import Cor
from app import *
import dash_bootstrap_components as dbc
from asyncio import run
from componentes.telas import tela_pokemon

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
                            dbc.InputGroup(
                                [
                                    dbc.Input(id='id_text_pokemon',
                                              placeholder='digite o numero do pokemon'),
                                    dbc.Button('Pesquisar',
                                               id='id_btn_pokemon',
                                               n_clicks=0),
                                ],
                                id='id_group_pokemon'
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
                                html.Div(id='content')
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
              [Input('id_tabs_geracao', 'active_tab'),
               Input('id_btn_pokemon', 'n_clicks'),
               [Input(f'{cor.name}', 'n_clicks') for cor in Cor],
               [State('id_text_pokemon', 'value')]
               ])
def troca_tab(tab, *_):
    ctx = callback_context
    print('tab', tab)
    value = ctx.states_list[0].get('value')
    # print(ctx.inputs_list[1]['value'])
    # print(ctx.states_list)
    print('ctx.triggered_id', ctx.triggered_id)
    # if ctx.inputs_list[1]['value'] == 0:
    #     raise PreventUpdate

    if tab == 'id_primeira_geracao':

        inicio = 1
        fim = 5
        lista_pokemons = run(main(inicio, fim))
        print(lista_pokemons[0])

        # return tela_pokemon(lista_pokemons, ctx.triggered_id)
        return '1'
    elif tab == 'id_segunda_geracao':
        return '2'
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
        return '9'
    return html.P('Não selecionado')


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
