import pandas as pd
import numpy as np 
import sklearn as sk 
from sklearn.linear_model import LinearRegression 
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('Japan_cities_rainfall.csv')
X=df.drop(['date_time','place','rainfall'],axis=1)
y=df['rainfall']

clf = DecisionTreeRegressor() 
clf.fit(X,y) 
data=pd.read_csv('rainfall_to_predict.csv')
input = data.drop(['date_time','place'],axis=1)

prediction=clf.predict(input)
result_rmse = verify_predictions(prediction.tolist())
print(result_rmse)
