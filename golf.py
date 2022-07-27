from dash import Dash, dcc, html, Input, Output, State
from sklearn import datasets
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
import flask

df = pd.read_csv("t.csv")

df.Outlook[df.Outlook == 'overcast'] = 0
df.Outlook[df.Outlook == 'rainy'] = 1
df.Outlook[df.Outlook == 'sunny'] = 2
df[['Windy']] = df[['Windy']].astype(int)
model = LinearSVC()
model.fit(df[['Outlook', 'Temperature', 'Humidity', 'Windy']], df['Play'])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Play Golf Today?", id="header"),
    html.H2("Choose Outlook"),
    dcc.RadioItems(options=[
        {'label': 'overcast', 'value': 0},
        {'label': 'rainy', 'value': 1},
        {'label': 'sunny', 'value': 2},
    ],
        id="radioitems-input",
        value='overcast'
    ),

    html.Br(),
    html.H2("Enter Temperature : "), dcc.Input(id='input-on-submit2', type='text'),
    html.Br(),
    html.H2("Enter Humidity : "), dcc.Input(id='input-on-submit3', type='text'),
    html.Br(),
    html.H2("Windy?"),
    dcc.Dropdown(
        options=[
            {'label': 'Yes', 'value': 1},
            {'label': 'No', 'value': 0},
        ],
        id='dropdown',
        value='Yes'
    ),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Br(),
    html.Div(id='container-button-basic',
             children='')

])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('radioitems-input', 'value'),
    State('input-on-submit2', 'value'),
    State('input-on-submit3', 'value'),
    State('dropdown', 'value')
)
def update_output(n_clicks, value1, value2, value3, value4):
    # test1 = [value1, value2, value3, value4]
    test2 = [value1, value2, value3, value4]
    return 'ผลการทำนาย คือ :  {} '.format(
        list(model.predict([test2]))[0], )


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port='7080')