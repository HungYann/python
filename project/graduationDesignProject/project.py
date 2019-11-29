# coding:UTF-8
from textwrap import dedent as d
from datetime import datetime as dt
import math
import datetime
import plotly.graph_objs as go
import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier

app = dash.Dash(__name__)
from numpy import arrayo
from numpy import argmax

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn import preprocessing
import timeit
import time
import datetime
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import roc_auc_score
import dash_core_components as dcc
# from sklearn import cross_validation,metrics

app = dash.Dash()
app.config['suppress_callback_exceptions'] = True
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
vact_epoch = datetime.datetime(year=2011, month=6, day=16, hour=5, minute=23, second=0)

mapbox_access_token = 'pk.eyJ1IjoiaG9ubGl1MTgiLCJhIjoiY2pzN3M4cTBkMDVvNjQ0cXhkcjc4OXM5eiJ9.7a4i9J2IgQ1wC4eh63fcVA'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# df369_1 = pd.read_csv('/Users/liuhongyang/Desktop/369_1.csv')







tab1_layout = [

    html.Div([
        dcc.Markdown(
            d("""



         --------------------------


      """))
    ]),

    html.Div([

        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=dt(1995, 8, 5),
            max_date_allowed=dt(2017, 9, 19),
            initial_visible_month=dt(2013, 9, 24),
            start_date=dt(2013, 9, 24),
            end_date=dt(2013, 9, 25)
        ),

        html.Div([
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {'label': 'Fuel Rate', 'value': 'Fuel Rate'},
                    {'label': 'Selected gear', 'value': 'Selected gear'},
                    {'label': 'Vehicle speed', 'value': 'Vehicle speed'},
                    {'label': 'Brake Pedal Position', 'value': 'Brake Pedal Position'},
                    {'label': 'Accelerate Pedal Position', 'value': 'Accelerate Pedal Position'},
                    {'label': 'Rel Speed Front Right', 'value': 'Rel Speed Front Right'},
                    {'label': 'Rel Speed Front Left', 'value': 'Rel Speed Front Left'},
                    {'label': 'Engine Fuel Temperature', 'value': 'Engine Fuel Temperature'},
                    {'label': 'Engine Speed', 'value': 'Engine Speed'}

                ],
                value='Fuel Rate'
            )

        ], style={'width': 318, 'height': 50}),

        dcc.RangeSlider(
            id='my-range-slider',
            min=0,
            max=240,
            step=1,
            value=[50, 60],
            marks={
                0: {'label': '0', 'style': {'color': '#000000'}},
                10: {'label': '1/24', 'style': {'color': '#000000'}},
                20: {'label': '2/24', 'style': {'color': '#000000'}},
                30: {'label': '3/24', 'style': {'color': '#000000'}},
                40: {'label': '4/24', 'style': {'color': '#000000'}},
                50: {'label': '5/24', 'style': {'color': '#000000'}},
                60: {'label': '6/24', 'style': {'color': '#000000'}},
                70: {'label': '7/24', 'style': {'color': '#000000'}},
                80: {'label': '8/24', 'style': {'color': '#000000'}},
                90: {'label': '9/24', 'style': {'color': '#000000'}},
                100: {'label': '10/24', 'style': {'color': '#000000'}},
                110: {'label': '11/24', 'style': {'color': '#000000'}},
                120: {'label': '12/24', 'style': {'color': '#000000'}},
                130: {'label': '13/24', 'style': {'color': '#000000'}},
                140: {'label': '14/24', 'style': {'color': '#000000'}},
                150: {'label': '15/24', 'style': {'color': '#000000'}},
                160: {'label': '16/24', 'style': {'color': '#000000'}},
                170: {'label': '17/24', 'style': {'color': '#000000'}},
                180: {'label': '18/24', 'style': {'color': '#000000'}},
                190: {'label': '19/24', 'style': {'color': '#000000'}},
                200: {'label': '20/24', 'style': {'color': '#000000'}},
                210: {'label': '21/24', 'style': {'color': '#000000'}},
                220: {'label': '22/24', 'style': {'color': '#000000'}},
                230: {'label': '23/24', 'style': {'color': '#000000'}},
                240: {'label': '1', 'style': {'color': '#000000'}}
            }
        ),

        html.Div([
            dcc.Markdown(
                d("""
               --------------------------


            """))
        ]),

        html.Button('Filter Button', id='submit-button', n_clicks=0),

        html.Div([
            dcc.Graph(
                id="diagram"
            )
        ]),

        html.Div(id='showSelectedNumberOfData'),

        html.Div([
            dcc.Markdown(
                d("""
          --------------------------


       """))
        ]),

        html.Div([

            html.Div([
                dcc.Graph(
                    id="map"
                )

            ])
        ]),

        dcc.RangeSlider(
            id='my-range-slider-map',
            min=0,
            max=100,
            step=1,
            value=[50, 60],
            marks={
                0: {'label': '0', 'style': {'color': '#000000'}},
                10: {'label': '10%', 'style': {'color': '#000000'}},
                20: {'label': '20%', 'style': {'color': '#000000'}},
                30: {'label': '30%', 'style': {'color': '#000000'}},
                40: {'label': '40%', 'style': {'color': '#000000'}},
                50: {'label': '50%', 'style': {'color': '#000000'}},
                60: {'label': '60%', 'style': {'color': '#000000'}},
                70: {'label': '70%', 'style': {'color': '#000000'}},
                80: {'label': '80%', 'style': {'color': '#000000'}},
                90: {'label': '90%', 'style': {'color': '#000000'}},
                100: {'label': '100%', 'style': {'color': '#000000'}},
            }
        ),

        html.Div([
            dcc.Markdown(
                d("""


            --------------------------


 """))
        ]),

    ])

]

tab2_layout = [

    html.Div([
        dcc.Markdown(
            d("""
          --------------------------


       """))
    ]),

    html.Div([
        dcc.Graph(id='selected-data')
    ]),

    html.Div([
        dcc.Input(
            id='adding-rows-name',
            placeholder='Enter a column name...',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Column', id='adding-rows-button', n_clicks=0)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='adding-rows-table',
        columns=[{
            'name': 'Timestamp',
            'id': 'Timestamp',

        }] + [{'name': 'Data', 'id': 'Data'}],

        data=[{'input-data': i} for i in range(50)],

        editable=True,
        row_deletable=True
    ),

    html.Button('Add Row', id='editing-rows-button', n_clicks=0),

]

tab3_layout = [
    html.Div([
        dcc.Markdown(
            d("""
          --------------------------


       """))
    ]),

    dcc.Dropdown(
        id='algorithm-dropdown',
        options=[
            {'label': 'KNN', 'value': 'KNN'},
            {'label': 'DT', 'value': 'DT'},
            {'label': 'NW', 'value': 'NW'},
            {'label': 'SVM', 'value': 'SVM'}

        ],
        value=['KNN', 'DT'],
        multi=True

    ),

    html.Button(id='algorithm-button', n_clicks=0, children='Submit'),

    html.Div([
        dcc.Graph(
            id="end"
        )
    ])
]

tab4_layout = [
    html.Div([
        dcc.Markdown(
            d("""



         --------------------------


      """))
    ]),

    html.Div([

        dcc.DatePickerRange(
            id='application-my-date-picker-range',
            min_date_allowed=dt(1995, 8, 5),
            max_date_allowed=dt(2017, 9, 19),
            initial_visible_month=dt(2013, 9, 24),
            start_date=dt(2013, 9, 24),
            end_date=dt(2013, 9, 25)
        ),

        html.Div([
            dcc.Dropdown(
                id='application-my-dropdown',
                options=[
                    {'label': 'Fuel Rate', 'value': 'Fuel Rate'},
                    {'label': 'Selected gear', 'value': 'Selected gear'},
                    {'label': 'Vehicle speed', 'value': 'Vehicle speed'},
                    {'label': 'Brake Pedal Position', 'value': 'Brake Pedal Position'},
                    {'label': 'Accelerate Pedal Position', 'value': 'Accelerate Pedal Position'},
                    {'label': 'Rel Speed Front Right', 'value': 'Rel Speed Front Right'},
                    {'label': 'Rel Speed Front Left', 'value': 'Rel Speed Front Left'},
                    {'label': 'Engine Fuel Temperature', 'value': 'Engine Fuel Temperature'},
                    {'label': 'Engine Speed', 'value': 'Engine Speed'}

                ],
                value='Fuel Rate'
            )

        ], style={'width': 318, 'height': 50}),

        dcc.RangeSlider(
            id='application-my-range-slider',
            min=0,
            max=240,
            step=1,
            value=[50, 60],
            marks={
                0: {'label': '0', 'style': {'color': '#000000'}},
                10: {'label': '1/24', 'style': {'color': '#000000'}},
                20: {'label': '2/24', 'style': {'color': '#000000'}},
                30: {'label': '3/24', 'style': {'color': '#000000'}},
                40: {'label': '4/24', 'style': {'color': '#000000'}},
                50: {'label': '5/24', 'style': {'color': '#000000'}},
                60: {'label': '6/24', 'style': {'color': '#000000'}},
                70: {'label': '7/24', 'style': {'color': '#000000'}},
                80: {'label': '8/24', 'style': {'color': '#000000'}},
                90: {'label': '9/24', 'style': {'color': '#000000'}},
                100: {'label': '10/24', 'style': {'color': '#000000'}},
                110: {'label': '11/24', 'style': {'color': '#000000'}},
                120: {'label': '12/24', 'style': {'color': '#000000'}},
                130: {'label': '13/24', 'style': {'color': '#000000'}},
                140: {'label': '14/24', 'style': {'color': '#000000'}},
                150: {'label': '15/24', 'style': {'color': '#000000'}},
                160: {'label': '16/24', 'style': {'color': '#000000'}},
                170: {'label': '17/24', 'style': {'color': '#000000'}},
                180: {'label': '18/24', 'style': {'color': '#000000'}},
                190: {'label': '19/24', 'style': {'color': '#000000'}},
                200: {'label': '20/24', 'style': {'color': '#000000'}},
                210: {'label': '21/24', 'style': {'color': '#000000'}},
                220: {'label': '22/24', 'style': {'color': '#000000'}},
                230: {'label': '23/24', 'style': {'color': '#000000'}},
                240: {'label': '1', 'style': {'color': '#000000'}}
            }
        ),

        html.Div([
            dcc.Markdown(
                d("""
               --------------------------


            """))
        ]),

        html.Button('Filter Button', id='application-submit-button', n_clicks=0),

        html.Div([
            dcc.Graph(
                id="application-diagram"
            )
        ]),

        html.Div(id='application-showSelectedNumberOfData'),

        html.Div([
            dcc.Markdown(
                d("""
          --------------------------


       """))
        ]),

        dcc.Dropdown(
            id='application-algorithm-dropdown',
            options=[
                {'label': 'KNN', 'value': 'KNN'},
                {'label': 'DT', 'value': 'DT'},
                {'label': 'NW', 'value': 'NW'},
                {'label': 'SVM', 'value': 'SVM'}

            ],
            value='KNN'
        ),

        html.Button(id='button', n_clicks=0, children='Submit'),

        html.Div([
            dcc.Markdown(
                d("""
              --------------------------


           """))
        ]),

        html.Div([
            dcc.Graph(id='results')
        ]),

        html.Div([
            dcc.Markdown(
                d("""
     --------------------------


  """))
        ]),


        html.Div([
            dcc.Graph(
                id='labellingResults'
            )

        ]),

        # html.Div([
        #
        #     html.Div([
        #         dcc.Graph(
        #             id="application-map"
        #         )
        #
        #     ])
        # ]),

        # dcc.RangeSlider(
        #     id='application-my-range-slider-map',
        #     min=0,
        #     max=100,
        #     step=1,
        #     value=[50, 60],
        #     marks={
        #         0: {'label': '0', 'style': {'color': '#000000'}},
        #         10: {'label': '10%', 'style': {'color': '#000000'}},
        #         20: {'label': '20%', 'style': {'color': '#000000'}},
        #         30: {'label': '30%', 'style': {'color': '#000000'}},
        #         40: {'label': '40%', 'style': {'color': '#000000'}},
        #         50: {'label': '50%', 'style': {'color': '#000000'}},
        #         60: {'label': '60%', 'style': {'color': '#000000'}},
        #         70: {'label': '70%', 'style': {'color': '#000000'}},
        #         80: {'label': '80%', 'style': {'color': '#000000'}},
        #         90: {'label': '90%', 'style': {'color': '#000000'}},
        #         100: {'label': '100%', 'style': {'color': '#000000'}},
        #     }
        # ),

        html.Div([
            dcc.Markdown(
                d("""

       --------------------------


    """))
        ]),

    ])

]

app.layout = html.Div([
    dcc.Tabs(id="tabs", value=1, children=[
        dcc.Tab(label='Data Visualization', value=1, children=tab1_layout),
        dcc.Tab(label='Manual Labelling', value=2, children=tab2_layout),
        dcc.Tab(label='Modelling and Evaluation', value=3, children=tab3_layout),
        dcc.Tab(label='Automatic Labelling', value=4, children=tab4_layout)
    ])
])




@app.callback(
    dash.dependencies.Output('diagram', 'figure'),
    [
        dash.dependencies.Input('submit-button', 'n_clicks')
    ],
    [
        dash.dependencies.State('my-range-slider', 'value'),
        dash.dependencies.State('my-dropdown', 'value'),
        dash.dependencies.State('my-date-picker-range', 'start_date'),
        dash.dependencies.State('my-date-picker-range', 'end_date'),
    ]
)
def update_output(n_clicks, find, dropdown, start_date, end_date):
    title = "signal type is " + dropdown + " start date from " + start_date + " to " + end_date + "(not included)"
    xScatter = []
    yScatter = []

    if n_clicks > 0:

        total = []
        x_axis = []
        y_axis = []

        mydata = returnDate(start_date, end_date)
        directory = xuanze(dropdown)

        result = mydata.split(" ")

        print "the number of day:"
        print result[1]

        threshold = int(result[1])
        startTime = dt.strptime(result[0], '%Y-%m-%d')

        f = open(directory)

        start = timeit.default_timer()
        for line in f:
            total.append(line);

        for line in total:
            value = line.replace("\r\n", "").split("|")
            currentDatabaseTimeStamp = get_datetime(value[0])
            # print currentDatabaseTimeStampff
            DayValue = (currentDatabaseTimeStamp - startTime).days
            if DayValue < 0:
                continue;
            if DayValue >= threshold:
                break;
            x_axis.append(currentDatabaseTimeStamp)
            value_change = value[1].replace("\n", "")
            y_axis.append(value_change)

        elapsed = (timeit.default_timer() - start)

        numberOfData = len(x_axis)

        print "SelectedNumberOfData"
        print numberOfData

        s = numberOfData / 240 * int(find[0])
        e = numberOfData / 240 * int(find[1])

        for i in range(s, e):
            xScatter.append(x_axis[i])
            yScatter.append(y_axis[i])

        print elapsed
    return function(title, xScatter, yScatter)


@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [
        dash.dependencies.Input('submit-button', 'n_clicks'),
        dash.dependencies.Input('my-range-slider-map', 'value'),
        dash.dependencies.Input('my-date-picker-range', 'start_date'),
        dash.dependencies.Input('my-date-picker-range', 'end_date')
    ]
)
def mapTrack(n_clicks, find, start_date, end_date):
    longitudeMap = []
    latitudeMap = []
    timeMap = []
    maptitle = "bus track from " + start_date + "  to  " + end_date + "(not included)";

    if n_clicks > 0:

        longgitude = []
        latitude = []
        currentTimeStamp = []

        # print "map date information"
        mydata = returnDate(start_date, end_date)
        result = mydata.split(" ")
        # print "map------------>map"
        threshold = int(result[1])
        startTime = dt.strptime(result[0], '%Y-%m-%d')

        f = open('/Users/liuhongyang/Desktop/369_0.csv')
        f2 = open('/Users/liuhongyang/Desktop/369_1.csv')

        total1 = []
        total2 = []

        for line in f:
            total1.append(line);

        for line in f2:
            total2.append(line)

        for line in total1:
            value = line.replace("\r\n", "").split("|")
            currentDatabaseTimeStamp = get_datetime(value[0])
            DayValue = (currentDatabaseTimeStamp - startTime).days
            if DayValue < 0:
                continue;
            if DayValue >= threshold:
                break;
            currentTimeStamp.append(currentDatabaseTimeStamp)
            value_change = value[1].replace("\n", "")
            value_change_double = float(value_change) * 180 / math.pi
            longgitude.append(value_change_double)

        for line in total2:
            value = line.replace("\r\n", "").split("|")
            currentDatabaseTimeStamp = get_datetime(value[0])
            DayValue = (currentDatabaseTimeStamp - startTime).days
            if DayValue < 0:
                continue;
            if DayValue >= threshold:
                break;
            value_change = value[1].replace("\n", "")
            value_change2 = float(value_change) * 180 / math.pi
            latitude.append(value_change2)

        numberOfData = len(longgitude)
        s = numberOfData / 100 * int(find[0])
        e = numberOfData / 100 * int(find[1])

        for i in range(s, e):
            longitudeMap.append(longgitude[i])
            latitudeMap.append(latitude[i])
            timeMap.append(currentTimeStamp[i])

    return map(maptitle, longitudeMap, latitudeMap, timeMap)


@app.callback(
    Output('showSelectedNumberOfData', 'children'),
    [Input('diagram', 'selectedData')])
def numberOfData(selectedData):
    my = {'a': '1'}
    selectedDataNumber = 0
    if type(selectedData) == type(my):
        num = len(selectedData['points'])
        selectedDataNumber = num

    return u'''
        YOU HAVE SELECTED "{}" OF DATA
        '''.format(selectedDataNumber)


@app.callback(
    Output('selected-data', 'figure'),
    [Input('diagram', 'selectedData')])
def display_selected_data(selectedData):
    my = {'a': '1'}
    xaxis = []
    yaxis = []
    if type(selectedData) == type(my):
        num = len(selectedData['points'])
        for i in range(0, num):
            xaxis.append(selectedData['points'][i]['x'])
            yaxis.append(selectedData['points'][i]['y'])

    data = []
    trace_close = go.Scatter(
        x=xaxis,
        y=yaxis,
        mode='markers',
        marker=dict(
            color='rgb(255, 0, 0)',
            size=15
        )
    )

    data.append(trace_close)

    layout = {"title": 'selected scatter',
              "clickmode": 'event+select'
              }

    return {
        'data': data,
        'layout': layout
    }


@app.callback(
    Output('adding-rows-table', 'data'),
    [Input('editing-rows-button', 'n_clicks'),
     Input('diagram', 'selectedData'),
     ],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns')
     ])
def update_columns(n_clicks, selectedData, rows, columns):
    my = {'a': '1'}
    xaxis = []
    yaxis = []
    if type(selectedData) == type(my):
        num = len(selectedData['points'])
        print num
        for i in range(0, num):
            xaxis.append(selectedData['points'][i]['x'])
            yaxis.append(selectedData['points'][i]['y'])
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    for row, i, j in zip(rows, xaxis, yaxis):
        try:
            row['Timestamp'] = i
            row['Data'] = j
        except:
            row['Timestamp'] = 'NA'
            row['Data'] = 'NA'

    return rows


@app.callback(
    Output('adding-rows-table', 'columns'),
    [Input('adding-rows-button', 'n_clicks')],
    [State('adding-rows-name', 'value'),
     State('adding-rows-table', 'columns')])
def update_columns(n_clicks, value, existing_columns):
    if n_clicks > 0:
        existing_columns.append({
            'id': value, 'name': value,
            'editable_name': True, 'deletable': True
        })
    return existing_columns


@app.callback(
    Output('end', 'figure'),
    [Input('algorithm-button', 'n_clicks')],
    [State('adding-rows-table', 'data'),
     State('adding-rows-table', 'columns'),
     State('algorithm-dropdown', 'value')])
def display_output(n_clicks, rows, columns, dropdown):
    Algorithm_name = []
    # ['KNN', 'DT', 'NW', 'SVM']

    accuracy = []

    for i in dropdown:
        if i == 'KNN':
            Algorithm_name.append(i)
        if i == 'DT':
            Algorithm_name.append(i)
        if i == 'NW':
            Algorithm_name.append(i)
        if i == 'SVM':
            Algorithm_name.append(i)

    if n_clicks > 0:

        total = []

        x = [(c['id']) for c in columns]
        num = len(x)
        for i in range(num):
            column = x[i]
            data = []
            for row in rows:
                if row.get(column) is not None:
                    data.append(row.get(column))
            total.append(data)

        num2 = len(total)
        if num2 <= 2:
            print "number of columns must more than two"
        else:
            time = total[0]
            numeric_vlaue = total[1:num2 - 1]
            label = total[-1]

            numberOfTimeColumn = len(time)
            numberOfLabelColumn = len(label)

            if numberOfTimeColumn != numberOfLabelColumn:
                print "Warning numberOfTimeColumn is not equal numberOfLabelColumn"
                return;

            if numberOfTimeColumn < 6:
                print "Warning the numberOfTimeColumn is too few, please add other data"
                return;

            value1 = array(time)
            value2 = array(label)
            label_encoder = LabelEncoder()
            integer_encoded_time = label_encoder.fit_transform(value1)
            integer_encoded_label = label_encoder.fit_transform(value2)
            X = []

            for i, j in zip(integer_encoded_time, numeric_vlaue[0]):
                X.append([i, j])

            for i in dropdown:
                if i == 'KNN':
                    algorithm1 = KNNAlgorithm(X, integer_encoded_label)
                    accuracy.append(algorithm1)
                if i == 'DT':
                    algorithm2 = DTAlgorithm(X, integer_encoded_label)
                    accuracy.append(algorithm2)
                if i == 'NW':
                    algorithm3 = NWAlgorithm(X, integer_encoded_label)
                    accuracy.append(algorithm3)
                if i == 'SVM':
                    algorithm4 = SVMAlgorithm(X, integer_encoded_label)
                    accuracy.append(algorithm4)

    numberOfAlgorithm2=len(Algorithm_name);

    # for i in range(0, numberOfAlgorithm2):
    #     print i;


    data=[]
    algorithm_accuarcy=[]
    algorithm_f1_score=[]
    algorithm_averave_precision=[]
    len_accuracy_is_null= len(accuracy);


    if len_accuracy_is_null!=0:

        for i in range(len(accuracy)):
            variable = []
            variable = accuracy[i]
            algorithm_accuarcy.append(variable[0])

        for i in range(len(accuracy)):
            variable = []
            variable = accuracy[i]
            algorithm_f1_score.append(variable[1])

        for i in range(len(accuracy)):
            variable = []
            variable = accuracy[i]
            algorithm_averave_precision.append(variable[2])

        # print algorithm_accuarcy
        # print algorithm_f1_score
        # print algorithm_averave_precision

        trace1 = go.Bar(
            x=Algorithm_name,
            y=algorithm_accuarcy,
            text=algorithm_accuarcy,
            name="accuarcy",
            marker=dict(

                line=dict(
                    color='rgb(49,130,189)',
                    width=1.5),
            )
        )


        trace2 = go.Bar(
            x=Algorithm_name,
            y=algorithm_f1_score,
            text=algorithm_f1_score,
            name="f1-score",
            marker=dict(

                line=dict(
                    color='rgb(49,130,189)',
                    width=1.5),
            )
        )


        trace3 = go.Bar(
            x=Algorithm_name,
            y=algorithm_averave_precision,
            text=algorithm_averave_precision,
            name="average-precision",
            marker=dict(

                line=dict(
                    color='rgb(49,130,189)',
                    width=1.5),
            )
        )

        data=[trace1,trace2,trace3]


    layout = go.Layout(
        title="Modelling Evaluation",
        barmode='group'
    )


    return {
        'data': data,
        'layout': layout
    }

    #return showBar(Algorithm_name, accuracy)




@app.callback(
    dash.dependencies.Output('application-diagram', 'figure'),
    [
        dash.dependencies.Input('application-submit-button', 'n_clicks')
    ],
    [
        dash.dependencies.State('application-my-range-slider', 'value'),
        dash.dependencies.State('application-my-dropdown', 'value'),
        dash.dependencies.State('application-my-date-picker-range', 'start_date'),
        dash.dependencies.State('application-my-date-picker-range', 'end_date'),
    ]
)
def update_output(n_clicks, find, dropdown, start_date, end_date):
    title = "signal type is " + dropdown + " start date from " + start_date + " to " + end_date + "(not included)"
    xScatter = []
    yScatter = []

    if n_clicks > 0:

        total = []
        x_axis = []
        y_axis = []

        mydata = returnDate(start_date, end_date)
        directory = xuanze(dropdown)

        result = mydata.split(" ")

        print "Application-the number of day:"
        print result[1]

        threshold = int(result[1])
        startTime = dt.strptime(result[0], '%Y-%m-%d')

        f = open(directory)

        start = timeit.default_timer()
        for line in f:
            total.append(line);

        for line in total:
            value = line.replace("\r\n", "").split("|")
            currentDatabaseTimeStamp = get_datetime(value[0])
            # print currentDatabaseTimeStampff
            DayValue = (currentDatabaseTimeStamp - startTime).days
            if DayValue < 0:
                continue;
            if DayValue >= threshold:
                break;
            x_axis.append(currentDatabaseTimeStamp)
            value_change = value[1].replace("\n", "")
            y_axis.append(value_change)

        elapsed = (timeit.default_timer() - start)

        numberOfData = len(x_axis)

        print "Application-SelectedNumberOfData"
        print numberOfData

        s = numberOfData / 240 * int(find[0])
        e = numberOfData / 240 * int(find[1])

        for i in range(s, e):
            xScatter.append(x_axis[i])
            yScatter.append(y_axis[i])

        print "Application-elapsed"
        print elapsed
    return function(title, xScatter, yScatter)


@app.callback(
    Output('application-showSelectedNumberOfData', 'children'),
    [Input('application-diagram', 'selectedData')])
def numberOfData(selectedData):
    my = {'a': '1'}
    selectedDataNumber = 0
    if type(selectedData) == type(my):
        num = len(selectedData['points'])
        selectedDataNumber = num

    return u'''
        YOU HAVE SELECTED "{}" OF DATA
        '''.format(selectedDataNumber)


@app.callback(
    dash.dependencies.Output('results', 'figure'),
    [
        dash.dependencies.Input('button', 'n_clicks')
    ],
    [
        dash.dependencies.State('application-diagram', 'selectedData'),
        dash.dependencies.State('application-algorithm-dropdown', 'value'),
        dash.dependencies.State('adding-rows-table', 'data'),
        dash.dependencies.State('adding-rows-table', 'columns')
    ]
)

def display_selected_data(n_clicks, selectedData, dropdown, rows, columns):
    prediciton = []
    data = []
    layout = {"title": 'prediction'}
    inputData=[]

    if n_clicks > 0:

        xaxis = []
        yaxis = []
        # generate predictive data

        my = {'a': '1'}
        if type(selectedData) == type(my):
            num = len(selectedData['points'])
            for i in range(0, num):
                xaxis.append(selectedData['points'][i]['x'])
                yaxis.append(selectedData['points'][i]['y'])
        value_timestamp = array(xaxis)
        label_encoder = LabelEncoder()
        integer_encoded_time = label_encoder.fit_transform(value_timestamp)
        for i, j in zip(integer_encoded_time, yaxis):
            prediciton.append([i, j])
            inputData=yaxis

        # selected data which the same with evaluation

        total = []

        x = [(c['id']) for c in columns]
        num = len(x)
        for i in range(num):
            column = x[i]
            data = []
            for row in rows:
                if row.get(column) is not None:
                    data.append(row.get(column))
            total.append(data)

        num2 = len(total)
        if num2 <= 2:
            print "number of columns must more than two"
        else:

            time = total[0]
            numeric_vlaue = total[1:num2 - 1]
            label = total[-1]

            numberOfTimeColumn = len(time)
            numberOfLabelColumn = len(label)

            if numberOfTimeColumn != numberOfLabelColumn:
                print "Warning numberOfTimeColumn is not equal numberOfLabelColumn"
                return;

            if numberOfTimeColumn < 6:
                print "Warning the numberOfTimeColumn is too few, please add other data"
                return;
            X = []

            value1 = array(time)
            value2 = array(label)
            
            
            label_encoder = LabelEncoder()
            integer_encoded_time = label_encoder.fit_transform(value1)
            integer_encoded_label = label_encoder.fit_transform(value2)

            for i, j in zip(integer_encoded_time, numeric_vlaue[0]):
                X.append([i, j])

            if dropdown == 'KNN':
                prediciton = applyKNNAlgorithm(prediciton, X, integer_encoded_label)
            if dropdown == 'DT':
                prediciton = applyDTAlgorithm(prediciton, X, integer_encoded_label)
            if dropdown == 'NW':
                prediciton = applyNWAlgorithm(prediciton, X, integer_encoded_label)
            if dropdown == 'SVM':
                prediciton = applySVMAlgorithm(prediciton, X, integer_encoded_label)




            count = 0
            prediciton_y = []

            for i in prediciton:
                prediciton_y.append(i)
                if i == prediciton_y[0]:
                    count = count + 1


            # numOfPrediction=len(prediciton_y)


            # ratio=float(count/numOfPrediction)*100
            # name=prediciton_y[0]+"occupied"+ratio+"%"
            # print "type:"
            # print type(prediciton_y[0])
            #add prediction value so that people could compare
            #label
            trace = go.Table(
                header=dict(values=list(['Timestamp','Data', 'label_results']),
                            fill=dict(color='#C2D4FF'),
                            align=['left'] * 5),
                cells=dict(values=[xaxis,inputData,prediciton_y],
                           fill=dict(color='#F5F8FF'),
                           align=['left'] * 5))

            data = [trace]

    return {
        'data': data,
        'layout': layout
    }




@app.callback(
    dash.dependencies.Output('labellingResults','figure'),
    [
        dash.dependencies.Input('button','n_clicks')
    ],
    [
        dash.dependencies.State('application-diagram', 'selectedData'),
        dash.dependencies.State('application-algorithm-dropdown', 'value'),
        dash.dependencies.State('adding-rows-table', 'data'),
        dash.dependencies.State('adding-rows-table', 'columns')
    ]
)

def display_selected_data(n_clicks, selectedData, dropdown, rows, columns):
    prediciton = []
    data = []
    layout = {"title": 'prediction'}
    if n_clicks>0:
        xaxis = []
        yaxis = []
        # generate predictive data

        my = {'a': '1'}
        if type(selectedData) == type(my):
            num = len(selectedData['points'])
            for i in range(0, num):
                xaxis.append(selectedData['points'][i]['x'])
                yaxis.append(selectedData['points'][i]['y'])
        value_timestamp = array(xaxis)
        label_encoder = LabelEncoder()
        integer_encoded_time = label_encoder.fit_transform(value_timestamp)
        for i, j in zip(integer_encoded_time, yaxis):
            prediciton.append([i, j])

        # selected data which the same with evaluation

        total = []
        x = [(c['id']) for c in columns]
        num = len(x)
        for i in range(num):
            column = x[i]
            data = []
            for row in rows:
                if row.get(column) is not None:
                    data.append(row.get(column))
            total.append(data)

        num2 = len(total)
        if num2 <= 2:
            print "number of columns must more than two"
        else:
            time = total[0]
            numeric_vlaue = total[1:num2 - 1]
            label = total[-1]

            numberOfTimeColumn = len(time)
            numberOfLabelColumn = len(label)

            if numberOfTimeColumn != numberOfLabelColumn:
                print "Warning numberOfTimeColumn is not equal numberOfLabelColumn"
                return;

            if numberOfTimeColumn < 6:
                print "Warning the numberOfTimeColumn is too few, please add other data"
                return;
            X = []

            value1 = array(time)
            value2 = array(label)
            label_encoder = LabelEncoder()
            integer_encoded_time = label_encoder.fit_transform(value1)
            integer_encoded_label = label_encoder.fit_transform(value2)

            for i, j in zip(integer_encoded_time, numeric_vlaue[0]):
                X.append([i, j])

            if dropdown == 'KNN':
                prediciton = applyKNNAlgorithm(prediciton, X, integer_encoded_label)
            if dropdown == 'DT':
                prediciton = applyDTAlgorithm(prediciton, X, integer_encoded_label)
            if dropdown == 'NW':
                prediciton = applyNWAlgorithm(prediciton, X, integer_encoded_label)
            if dropdown == 'SVM':
                prediciton = applySVMAlgorithm(prediciton, X, integer_encoded_label)

            count = 0
            prediciton_y = []

            for i in prediciton:
                prediciton_y.append(i)
                if i == prediciton_y[0]:
                    count = count + 1

            trace=go.Scatter(
                x=xaxis,
                y=prediciton_y,
                mode='markers'
            )

            numOfPrediction = len(prediciton_y)
            ratio=float(count)/float(numOfPrediction)*100
            name = "The result:'"+str(prediciton_y[0]) + "' occupys " + str(round(ratio,2)) + "% of total data"
            data=[trace]

            layout = {"title": name}




    return {
        'data': data,
        'layout': layout
    }









# @app.callback(
#     dash.dependencies.Output('application-map', 'figure'),
#     [
#         dash.dependencies.Input('application-submit-button', 'n_clicks'),
#         dash.dependencies.Input('application-my-range-slider-map', 'value'),
#         dash.dependencies.Input('application-my-date-picker-range', 'start_date'),
#         dash.dependencies.Input('application-my-date-picker-range', 'end_date')
#     ]
# )
# def mapTrack(n_clicks, find, start_date, end_date):
#     longitudeMap = []
#     latitudeMap = []
#     timeMap = []
#     maptitle = "bus track from " + start_date + "  to  " + end_date + "(not included)";
#
#     if n_clicks > 0:
#
#         longgitude = []
#         latitude = []
#         currentTimeStamp = []
#
#         # print "map date information"
#         mydata = returnDate(start_date, end_date)
#         result = mydata.split(" ")
#         # print "map------------>map"
#         threshold = int(result[1])
#         startTime = dt.strptime(result[0], '%Y-%m-%d')
#
#         f = open('/Users/liuhongyang/Desktop/369_0.csv')
#         f2 = open('/Users/liuhongyang/Desktop/369_1.csv')
#
#         total1 = []
#         total2 = []
#
#         for line in f:
#             total1.append(line);
#
#         for line in f2:
#             total2.append(line)
#
#         for line in total1:
#             value = line.replace("\r\n", "").split("|")
#             currentDatabaseTimeStamp = get_datetime(value[0])
#             DayValue = (currentDatabaseTimeStamp - startTime).days
#             if DayValue < 0:
#                 continue;
#             if DayValue >= threshold:
#                 break;
#             currentTimeStamp.append(currentDatabaseTimeStamp)
#             value_change = value[1].replace("\n", "")
#             value_change_double = float(value_change) * 180 / math.pi
#             longgitude.append(value_change_double)
#
#         for line in total2:
#             value = line.replace("\r\n", "").split("|")
#             currentDatabaseTimeStamp = get_datetime(value[0])
#             DayValue = (currentDatabaseTimeStamp - startTime).days
#             if DayValue < 0:
#                 continue;
#             if DayValue >= threshold:
#                 break;
#             value_change = value[1].replace("\n", "")
#             value_change2 = float(value_change) * 180 / math.pi
#             latitude.append(value_change2)
#
#         numberOfData = len(longgitude)
#         s = numberOfData / 100 * int(find[0])
#         e = numberOfData / 100 * int(find[1])
#
#         for i in range(s, e):
#             longitudeMap.append(longgitude[i])
#             latitudeMap.append(latitude[i])
#             timeMap.append(currentTimeStamp[i])
#
#     return map(maptitle, longitudeMap, latitudeMap, timeMap)


# def showBar(name, accuracy):
#     trace1 = go.Bar(
#         x=name[0],
#         y=accuracy[0],
#         text=accuracy[0],
#         name='accuracy',
#         marker=dict(
#
#             line=dict(
#                 color='rgb(49,130,189)',
#                 width=1.5),
#         )
#
#     )
#     trace2=go.Bar(
#         x=name[1],
#         y=accuracy[1],
#         text=accuracy[1],
#         name='F1_score',
#         marker=dict(
#
#             line=dict(
#                 color='rgb(49,130,189)',
#                 width=1.5),
#         )
#
#     )
#
#
#
#     data = [trace1,trace2]
#     layout = go.Layout(
#         title="Modelling Evaluation",
#         barmode='group'
#     )
#
#     return {
#         'data': data,
#         'layout': layout
#     }







def xuanze(dropdown):
    if dropdown == 'Fuel Rate':
        return "/Users/liuhongyang/Desktop/369_16617.csv"
    elif dropdown == 'Selected gear':
        return "/Users/liuhongyang/Desktop/369_16772.csv"
    elif dropdown == 'Vehicle speed':
        return "/Users/liuhongyang/Desktop/369_23644.csv"
    elif dropdown == 'Brake Pedal Position':
        return "/Users/liuhongyang/Desktop/369_23676.csv"
    elif dropdown == 'Accelerate Pedal Position':
        return "/Users/liuhongyang/Desktop/369_23913.csv"
    elif dropdown == 'Rel Speed Front Right':
        return "/Users/liuhongyang/Desktop/369_24030.csv"
    elif dropdown == 'Rel Speed Front Left':
        return "/Users/liuhongyang/Desktop/369_24031.csv"
    elif dropdown == 'Engine Fuel Temperature':
        return "/Users/liuhongyang/Desktop/369_25274.csv"
    elif dropdown == 'Engine Speed':
        return "/Users/liuhongyang/Desktop/369_26115.csv"
    else:
        return "/Users/liuhongyang/Desktop/369_16617.csv"


def returnDate(start_date, end_date):
    start_date2 = dt(2013, 9, 24)
    end_date2 = dt(2013, 9, 25)

    if start_date is not None:
        start_date2 = dt.strptime(start_date, '%Y-%m-%d')
        print start_date

    if end_date is not None:
        end_date2 = dt.strptime(end_date, '%Y-%m-%d')
        print end_date

    val = end_date2 - start_date2

    if start_date is not None:
        mydata = str(start_date) + " " + str(val)
    else:
        mydata = str(start_date2.strftime('%Y-%m-%d')) + " " + str(val)
    return mydata


def function(title, x_value, y_value):
    data = []
    trace_close = go.Scatter(
        x=x_value,
        y=y_value,
        mode='markers',
        marker={'size': 12}
    )

    data.append(trace_close)

    layout = {"title": title,
              "clickmode": 'event+select'}

    return {
        'data': data,
        'layout': layout
    }


def map(title, longgitude, latitude, currentTimeStamp):
    data = [
        go.Scattermapbox(
            lat=longgitude,
            lon=latitude,
            mode='markers',
            text=currentTimeStamp,
            marker=dict(
                color='rgb(255, 0, 0)',
                size=9
            ),
        )
    ]

    layout = go.Layout(
        title=title,
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            accesstoken=mapbox_access_token,
            center=dict(
                lat=38.92,
                lon=-77.07
            ),
            pitch=0,
            zoom=0

        ),
    )

    return {
        'data': data,
        'layout': layout
    }


def get_datetime(_value):
    return vact_epoch + datetime.timedelta(milliseconds=int(_value))


def applyKNNAlgorithm(prediction, X, integer_encoded_label):
    KNN = KNeighborsClassifier(n_neighbors=2)
    KNN.fit(X, integer_encoded_label)
    return KNN.predict(prediction)


def applyDTAlgorithm(prediction, X, integer_encoded_label):
    DT = tree.DecisionTreeClassifier()
    DT.fit(X, integer_encoded_label)
    return DT.predict(prediction)


def applySVMAlgorithm(prediction, X, integer_encoded_label):
    SVM = SVC()
    SVM.fit(X, integer_encoded_label)
    return SVM.predict(prediction)


def applyNWAlgorithm(prediction, X, integer_encoded_label):
    NW = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    NW.fit(X, integer_encoded_label)
    return NW.predict(prediction)








def KNNAlgorithm(X, integer_encoded_label):
    metrics=[]
    KNN = KNeighborsClassifier(n_neighbors=2)
    KNN.fit(X, integer_encoded_label)
    accuracy = cross_val_score(KNN, X, integer_encoded_label, cv=3, scoring="accuracy")
    F_score=cross_val_score(KNN, X, integer_encoded_label, cv=3, scoring="f1")
    Average_precision = cross_val_score(KNN, X, integer_encoded_label, cv=3, scoring="average_precision")

    accuracyMean = accuracy.mean()
    F_score_mean = F_score.mean()
    Average_precision_mean=Average_precision.mean()

    metrics.append(accuracyMean)
    metrics.append(F_score_mean)
    metrics.append(Average_precision_mean)
    return metrics


def DTAlgorithm(X, integer_encoded_label):
    metrics=[]
    DT = tree.DecisionTreeClassifier()
    DT.fit(X, integer_encoded_label)
    #print(DT.predict(X))
    accuracy = cross_val_score(DT, X, integer_encoded_label, cv=1, scoring="accuracy")
    F_score=cross_val_score(DT, X, integer_encoded_label, cv=1, scoring="f1")
    Average_precision=cross_val_score(DT, X, integer_encoded_label, cv=1, scoring="average_precision")

    accuracyMean = accuracy.mean()
    F_score_mean = F_score.mean()
    Average_precision_mean=Average_precision.mean()

    metrics.append(accuracyMean)
    metrics.append(F_score_mean)
    metrics.append(Average_precision_mean)
    return metrics


def NWAlgorithm(X, integer_encoded_label):
    metrics = []
    NW = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    NW.fit(X, integer_encoded_label)
    #print(NW.predict(X))
    accuracy = cross_val_score(NW, X, integer_encoded_label, cv=3, scoring="accuracy")
    F_score=cross_val_score(NW, X, integer_encoded_label, cv=3, scoring="f1")
    Average_precision= cross_val_score(NW, X, integer_encoded_label, cv=3, scoring="average_precision")

    accuracyMean = accuracy.mean()
    F_score_mean = F_score.mean()
    Average_precision_mean = Average_precision.mean()

    metrics.append(accuracyMean)
    metrics.append(F_score_mean)
    metrics.append(Average_precision_mean)

    return metrics


def SVMAlgorithm(X, integer_encoded_label):
    metrics = []
    SVM = SVC()
    SVM.fit(X, integer_encoded_label)
    #print(SVM.predict(X))
    accuracy = cross_val_score(SVM, X, integer_encoded_label, cv=3, scoring="accuracy")
    F_score= cross_val_score(SVM, X, integer_encoded_label, cv=3, scoring="f1")
    Average_precision= cross_val_score(SVM, X, integer_encoded_label, cv=3, scoring="average_precision")

    accuracyMean = accuracy.mean()
    F_score_mean = F_score.mean()
    Average_precision_mean = Average_precision.mean()

    metrics.append(accuracyMean)
    metrics.append(F_score_mean)
    metrics.append(Average_precision_mean)
    return metrics


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=7001)



