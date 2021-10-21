import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Engine_Capacity':1248, 'Fuel_Type':10, 'Fuel_Cost':807})

print(r.json())