import os
import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

from sklearn.svm import SVC

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score

from dash.dependencies import Input, Output, State
from datetime import datetime as dt
from textwrap import dedent as d
import plotly.graph_objs as go

def function(drive,car,mileage):
    #构建一个dataframe,columns值分别为car,mileage,drive

    queryX = pd.DataFrame({'car':car,'mileage':int(mileage),'drive':drive},index=[0]);

    #***


    print("------1")
    df= pd.read_csv('/Users/liuhongyang/Desktop/car_ad.csv',engine='python',usecols=['car','price','body','mileage','engV','engType','registration','year','model','drive'])  # doctest: +SKIP
    df.dropna(axis=0,how='any',inplace=True)

    X = df[['car','mileage','drive']]
    y = df['price']



    s = (X.dtypes == 'object')
    object_cols = list(s[s].index)
    label_X = X.copy()
    label_query_X = queryX.copy()

    print(label_X.head())
    print(queryX.head())

    label_encoder = LabelEncoder()
    print("-99")


    for col in object_cols:
        label_X[col] = label_encoder.fit_transform(label_X[col])
        label_query_X[col] = label_encoder.transform(queryX[col])

    print("-")

   # X_train, X_test, y_train, y_test = train_test_split(label_X, y, test_size=0.3)


    model = RandomForestRegressor(n_estimators=170, random_state=0)
   # model.fit(X_train, y_train)
    model.fit(label_X,y)
    price = model.predict(label_query_X)
    print(price)

    return price


##################

app =dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


tab1_layout = [

    html.Div([

        dcc.Dropdown(
            id='dropDown-price',
            options=[
                {'label': 'mileage', 'value': 'mileage'},
                {'label': 'car', 'value': 'car'},
                {'label': 'drive', 'value': 'drive'},

            ],
            value='mileage'
        ),
    ],style={'width': 318, 'height': 50}),


    html.Div([
        dcc.Graph(
            id="output-dropDown-price"
        )
    ]),

]





tab2_layout = [

    html.Div([

        dcc.Markdown(
            '''
 
                # The prediction system of second-hand car 
 
                ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g9e1e4lxl7j30g60budm8.jpg)
                ***
            '''
        ),

    ]),

    html.Div([

        dcc.Markdown(
d("""
     # Please choose car's band from the list
     |                 |       |          |             |
     |  ----           | ----  | ----     |    ----     |
     | Mercedes-Benz   |  BMW  | Toyota   |   Renault   |
     | VAZ             | Audi  |  Opel    |   Skoda     |
     |  Hyundai        |   Ford      |    Mitsubishi       |     Nissan        |
     |     Chevrolet            |   Daewoo    |     Kia     |     Honda              |
     |         Mazda         |    Peugeot     |   Lexus        |    Land Rover          |
              
    """))



    ]),

    html.Div([
        # car type
        dcc.Dropdown(
            id='dropDown-car',
            options=[
                {'label': 'Ford', 'value': 'Ford'},
                {'label': '2', 'value': '2'},
                {'label': '3', 'value': '3'},
                {'label': '4', 'value': '4'},
                {'label': '5', 'value': '5'},
                {'label': '6', 'value': '6'}
            ],
            value='Ford'
        )
    ], style={'width': 318, 'height': 50}),


    html.Div([
        dcc.Markdown(
            d("""
         
         
         
         
        
         
         # Please input mileage below:           
            
            
            
            """)
        )
    ]),


    html.Div([

        # mileage
        dcc.Input(id='textBox-mileage', type='text'),

    ], style={'width': 318, 'height': 50}),


    html.Div([
        dcc.Markdown(
            d("""





         # Please choose drive type:           
            |          |          |     |
            |    ---   | ---      |  --- |
            |  front   |  full    |  rear    |
        

            """)
        )

    ]),



    html.Div([
        # drive type

        dcc.Dropdown(
            id='dropDown-drive',
            options=[
                {'label': 'full', 'value': 'full'},
                {'label': '2', 'value': '2'},
                {'label': '3', 'value': '3'},
                {'label': '4', 'value': '4'},
                {'label': '5', 'value': '5'},
                {'label': '6', 'value': '6'}
            ],
            value='full'
        ),

        html.Button('Submit Button', id='submit-button', n_clicks=0),

    ],style={'width': 318, 'height': 50}),




    # visualization

    html.Div([
        dcc.Markdown(
            d("""
    -------------------------
    
    
    
    Output
    
    
    
    --------------------------


    """))
    ]),

    html.Div(id='output-dropDown-car'),

]






app.layout = html.Div([
    dcc.Tabs(id="tabs", value='1', children=[
        dcc.Tab(label='Data Visualization', value='1', children=tab1_layout),
        dcc.Tab(label='Manual prediction', value='2', children=tab2_layout),
    ])
])





def showScatter(title,x_value,y_value):
    data = []
    trace_close = go.Scatter(
        x = x_value,
        y = y_value,
        mode = 'markers',
        marker={'size':12}

    )

    data.append(trace_close)

    layout = {"title": title}

    return {
        'data': data,
        'layout': layout
    }






#使用dropdown list挑选值
@app.callback(
        Output('output-dropDown-price','figure'),
    [
        Input('dropDown-price','value')
    ]
)

def dropdown(value):
    df = pd.read_csv('/Users/liuhongyang/Desktop/car_ad.csv', engine='python',
                     usecols=['car', 'price', 'body', 'mileage', 'engV', 'engType', 'registration', 'year', 'model',
                              'drive'])  # doctest: +SKIP
    df.dropna(axis=0, how='any', inplace=True)
    title = 'the relation between '+value+' and price'

    return showScatter(title,df[value],df['price'])







@app.callback(
    Output('output-dropDown-car','children'),
    [
        Input('submit-button','n_clicks')
    ],
    [
    State('dropDown-drive','value'),
    State('dropDown-car','value'),
    State('textBox-mileage','value'),

    ])

def content_dropDowntCar(n_clicks,drive,car,mileage):
    price = ''
    if n_clicks>0:
        print(n_clicks,drive,car,mileage)
        price = function(drive, car, mileage)
        print(price)
    return u'''
        YOU HAVE SELECTED "{}" OF DATA
        '''.format(price)






if __name__ == '__main__':
    app.run_server(debug=True)