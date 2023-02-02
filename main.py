import datetime
from dash import callback_context, dcc, html
from dash.dependencies import Input, Output, State
from app import *
import dash_bootstrap_components as dbc

context = html.Div(id='id_page_content')

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col('Coluna 1', md=2, id='id_coluna_1'),
                dbc.Col(
                    [
                        dbc.Row(
                            dbc.InputGroup(
                                [
                                    dbc.Input(id='id_numero_pokemon', placeholder='digite o numero do pokemon', type='integer'),
                                    dbc.Button(id='id_text_pokemon', n_clicks=0),
                                ]
                            )
                        ),
                        dbc.Row(
                            'linha 2'
                        )
                    ],
                    md=10)
            ]
        )
    ]
    ,
    id='id_tela_principal'

)

if __name__ == "__main__":
    app.run_server(port=8051, debug=True)
