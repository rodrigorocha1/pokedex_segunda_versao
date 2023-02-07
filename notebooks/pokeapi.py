import aiohttp
import dash
import dash_html_components as html
import dash_core_components as dcc
import requests

import asyncio


class PokemonData:
    def __init__(self, url):
        self.url = url

    async def get_pokemon_list(self):
        pokemons = []
        while self.url:
            data = await self.fetch(self.url)
            pokemons += data['results']
            self.url = data['next']
        return pokemons

    async def get_pokemon_info(self, name):
        data = await self.fetch(f'https://pokeapi.co/api/v2/pokemon/{name}')
        return data

    async def fetch(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()


class PokemonDashApp():
    def __init__(self, pokemon_data):
        self.app = dash.Dash()
        self.pokemon_data = pokemon_data

    async def create_layout(self):
        pokemons = await self.pokemon_data.get_pokemon_list()
        self.app.layout = html.Div([
            dcc.Dropdown(
                id='pokemon-dropdown',
                options=[{'label': pokemon['name'], 'value': pokemon['name']} for pokemon in pokemons],
                value=pokemons[0]['name']
            ),
            html.Div(id='pokemon-info')
        ])

        @self.app.callback(
            dash.dependencies.Output('pokemon-info', 'children'),
            [dash.dependencies.Input('pokemon-dropdown', 'value')])
        async def update_pokemon_info(value):
            pokemon_data = await self.pokemon_data.get_pokemon_info(value)
            return html.Div([
                html.H1(pokemon_data['name']),
                html.H2(f'Weight: {pokemon_data["weight"]}'),
                html.H2(f'Height: {pokemon_data["height"]}'),
                html.H2(f'Type: {pokemon_data["types"][0]["type"]["name"]}')
            ])

    def run_server(self):
        self.app.run_server(debug=True)


if __name__ == '__main__':
    pokemon_data = PokemonData('https://pokeapi.co/api/v2/pokemon')
    pokemon_app = PokemonDashApp(pokemon_data)
    asyncio.run(pokemon_app.create_layout())
    pokemon_app.run_server()