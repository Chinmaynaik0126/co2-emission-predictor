import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('emission.csv')

X = dataset.iloc[:,:3]
print(X)



y = dataset.iloc[:, -1]
print(y)
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.01,random_state=0 )
print("y_test")
print(y_test)

regressor = RandomForestRegressor(n_estimators=100)


regressor.fit(X_train, y_train,2)
y_predict= regressor.predict(X_test)
df=pd.DataFrame()
df["y_test"]=y_test
df['y_predict']=y_predict
print(df)



pickle.dump(regressor, open('model.pkl','wb'))


model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1248,2,21]]))
print(model.score(X,y))