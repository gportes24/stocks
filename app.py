import os
import dash
imoport dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgp.css']

app.dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv()



app.layout = html.Div([
    html.H2("Stocks Data"),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label':i, 'value':i} for i in ['GOOG', 'MMM', 'ZTS']],
        value= 'ZTS'
    ),
    html.Div('display-value')
])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

@app.callback(dash.dependencie.Output('display-values', 'children'),[dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'you have selected "{}"'.format(value)'


    if __name_-='__main__':
        app.run_server(debug=True)
