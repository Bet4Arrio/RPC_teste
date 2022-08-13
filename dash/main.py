# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from graphs import *

app = Dash(__name__)
TARGET_COLUMN = 'Capacidade de pagamento anual'

df = pd.read_csv("../toplot/abc_houses_alll.csv")

abc_curver_graph = abc_curve(df, TARGET_COLUMN+"_abc_class", [TARGET_COLUMN, "Dívida"], TARGET_COLUMN+"_porcentagem")

treemap_graph = treemap(df, TARGET_COLUMN+"_abc_class", TARGET_COLUMN)

pie = abc_pie(df, TARGET_COLUMN+"_abc_class", TARGET_COLUMN)


treemap_div = html.Div(children=[
    dcc.Graph(
        id='example-graph2',
        figure=treemap_graph
    ),
])
abc_curve_div = html.Div(children=[
    dcc.Graph(
        id='example-graph3',
        figure=pie,
        style={'width': '800', 'display': 'inline-block'}
    ),
    dcc.Graph(
            id='example-graph',
            figure=abc_curver_graph,
            style={'width': '800', 'display': 'inline-block'}
        ),
], style={'width': '100%', 'display': 'inline-block'})

app.layout = html.Div(children=[
    html.H1(children='Capacidade de pagamento das familias'),
    html.Div(children=[
        html.H3(children='''
            Representação de participação de Patrimonio das familias dividias em 3 grupos
        '''),
        html.H3(children='''
            Grupo A: 49,8% de todo o patrimonio no banco. 
        '''),
        html.H3(children='''
            Grupo B: 30,2% de todo o patrimonio no banco.
        '''),
        html.H3(children='''
            Grupo C: 20% de todo o patrimonio no banco.
        '''),
    ], style={"margin-left": "25%"}),

    abc_curve_div,
    treemap_div,

    
])

if __name__ == '__main__':
    app.run_server(debug=True)
