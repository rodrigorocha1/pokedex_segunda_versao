from asyncio import run

from entidades.cortipopokemon import Cor
from entidades.pokemon import Pokemom
from dash import html
import dash_bootstrap_components as dbc
from typing import List

from services.pokeservice import main


def gerar_cartoes(pokemons: List[Pokemom]):
    return [
        dbc.Card(
            dbc.CardBody(
                [
                    dbc.CardImg(src=pokemon.img,
                                id=f'{pokemon.name}',
                                className='class_img_pokemon'),
                    html.P(f'{pokemon.id} - {pokemon.name.title()}',
                           id=f'id_card_{pokemon.id}',
                           className='class_nome_pokemon')
                ],
            ), className='class_cards_pokemons',
            color=f'{pokemon.cor}'
        ) for pokemon in pokemons
    ]


def gera_tabs(tab):
    if tab == 'id_primeira_geracao':

        inicio = 1
        fim = 9
        lista_pokemons = run(main(inicio, fim))
        return gerar_cartoes(pokemons=lista_pokemons), [
            {'label': f'{pokemon.id} - {pokemon.name.title()}',
             'value': f'{pokemon.id}'}
            for pokemon in lista_pokemons]
        # return tela_pokemon(lista_pokemons, ctx.triggered_id)
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
