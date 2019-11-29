import os
print(os.getcwd())
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



#X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#forest_model = RandomForestRegressor(random_state=1)


df= pd.read_csv('/Users/liuhongyang/Desktop/car_ad.csv',engine='python',usecols=['car','price','body','mileage','engV','engType','registration','year','model','drive'])  # doctest: +SKIP


df.dropna(axis=0,how='any',inplace=True)


X = df[['car','mileage','drive']]
y = df['price']
pd.set_option('display.max_rows', 80)
print(df['drive'].value_counts())




X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

label_X_train = X_train.copy()

label_X_test = X_test.copy()

label_encoder = LabelEncoder()


#input string------




#--------------

for col in object_cols:
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_test[col] = label_encoder.fit_transform(X_test[col])


model = RandomForestRegressor(n_estimators=170, random_state=0)
model.fit(label_X_train,y_train)



#print (label_X_test.head())

#preds = model.predict(label_X_test)


# validate the score of value
#score = mean_absolute_error(y_test, preds)
#print('MAE:', score)








# print (X_train.head())
# print (X_test.head())
# print (y_train.head())
# print (y_test.head())

#




#print(score_dataset(X_train, X_test, y_train, y_test))

#one-hot encoding


## delete vacancy rows

#df.dropna(axis=0,how='any',inplace=True)
#print (df.columns)
#print (df.isnull().sum())
#print (df.head())
#
# app.layout = html.Div([
#     dcc.Graph(
#         id = 'car_id_information',
#         figure={
#             'data':[
#
#                 dict(
#                     x = df['year'],
#                     y = df['price'],
#                     mode = 'markers',
#                     opacity = 0.7,
#
#                 )
#             ],
#
#             'layout':dict(
#
#                 hovermdoe='closest'
#
#             )
#         }
#     )
# ])
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
