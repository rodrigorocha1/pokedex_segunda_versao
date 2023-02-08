import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph-output'),
    html.Br(),
    dcc.Dropdown(id='select-input')
])

@app.callback(
    Output('graph-output', 'figure'),
    [Input('select-input', 'value')]
)
def update_figure(select_value):
    # return a Plotly figure based on the selected value
    pass

@app.callback(
    Output('select-input', 'options'),
    [Input('graph-output', 'clickData'),
     Input('select-input', 'value')]
)
def update_options(clickData, select_value):
    options = [{'label': i, 'value': i} for i in range(10)]
    return options

if __name__ == '__main__':
    app.run_server(debug=True)