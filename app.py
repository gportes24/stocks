import os
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgp.css']

app= dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv(
    'sp500_1.csv')

app.layout = html.Div([
    dcc.Graph(
        id ='rolling average',
        figure={
            'data': [
                go.scatter(
                x=df[df['ticker']==i ]['High'],
                y=df[df['ticker'] == i]['Adj Close'],
                text=df[df['ticker']==i]['Date'],
                mode='markers',
                opacity =0.7,
                marker={
                'size': 15,
                'line':{'width':0.5, 'color':'black'}
                },
                name =i
                ) #for i in df.Date.unique()
                ],
                'layout': go.Layout(
                xaxis={'type': 'Log', 'title': 'Rolling Stock Average'},
                yaxis={'title': 'rolling averag'},
                margin ={'i': 40, 'b':40, 't': 10, 'r':10},
                legend={'x': 0, 'y': 1},
                hovermode = 'closest'

                )
            }
        )

])
if __name_=='__main__':
    app.run_server(debug=True)
