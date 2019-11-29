import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
from textwrap import dedent as d

app =dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

    dcc.Markdown(
    '''
    
        # The prediction system of second-hand car 
        
        
        ![](https://tva1.sinaimg.cn/large/006y8mN6gy1g9e1e4lxl7j30g60budm8.jpg)
        ***
    '''

),

    #car type
    dcc.Dropdown(
        id='dropDown-car',
        options=[
            {'label':'1','value':'1'},
            {'label':'2','value':'2'},
            {'label':'3','value':'3'},
            {'label':'4','value':'4'},
            {'label':'5','value':'5'},
            {'label':'6','value':'6'}
        ],
        value= '1'
    ),





    #mileage
    dcc.Input(id='textBox-mileage',type='text'),



    #drive type

    dcc.Dropdown(
        id='dropDown-drive',
        options=[
            {'label': '1', 'value': '1'},
            {'label': '2', 'value': '2'},
            {'label': '3', 'value': '3'},
            {'label': '4', 'value': '4'},
            {'label': '5', 'value': '5'},
            {'label': '6', 'value': '6'}
        ],
        value='1'
    ),



    html.Button('Submit Button', id='submit-button', n_clicks=0),


    #visualization

    html.Div([
        dcc.Markdown(
            d("""

      --------------------------


   """))
    ]),


    html.Div(id='output-dropDown-car'),



])




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
    s = ''
    if n_clicks>0:
        s =drive+car+mileage

    return u'''
        YOU HAVE SELECTED "{}" OF DATA
        '''.format(s)





























# #car type
# @app.callback(
#     Output(component_id = 'output-dropDown-car',component_property='children'),
#     [
#      Input(component_id='submit-button',component_property='n_clicks'),
#      Input(component_id='dropDown-car',component_property='value')]
# )
# def content_dropDowntCar(value,n_clicks):
#     if n_clicks>0:
#         return 'dropdown {}'.format(value)
#
#
# #mileage
# @app.callback(
#     Output(component_id = 'textBox-div-mileage',component_property='children'),
#     [
#     Input(component_id='submit-button',component_property='n_clicks'),
#     Input(component_id='textBox-mileage',component_property='value')]
# )
# def content_textBox(value,n_clicks):
#     if n_clicks>0:
#         return 'this is {}'.format(value)
#
#
#
# #drive
# @app.callback(
#     Output('output-dropDown-drive','children'),
#     [
#     Input(component_id='submit-button',component_property='n_clicks'),
#     Input('dropDown-drive','value')])
# def content_dropdown(value,n_clicks):
#     if n_clicks>0:
#         return 'dropdown {}'.format(value)




if __name__ == '__main__':
    app.run_server(debug=True)