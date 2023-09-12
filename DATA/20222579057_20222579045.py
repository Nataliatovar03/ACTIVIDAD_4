# -*- coding: utf-8 -*-
"""20222579057 - 20222579045.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eVrUVFRHL6ZLrKqQD-Za4h0xtgftjOdj
"""

!pip install dnspython
!pip install pymongo==3.10

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos_teoricos = pd.read_csv("/content/drive/MyDrive/PROGRAMACIÓN II/TAREA 4/Data ingeniero 1.csv")
datos_teoricos

plt.plot(	datos_teoricos['Esfuerzo[kN]'] , datos_teoricos['Deformacion[mm]'])#PLOTEAR DATOS DE ESFUERZO VS DEFORMACION
plt.xlabel('Esfuerzo [kN]')
plt.ylabel('Deformación [mm]')
plt.title('Asentamiento inmediato')
plt.grid()
plt.gca().invert_yaxis()

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://nataliatovarc0303:1234@cluster0.vsdestk.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.Tarea4.DatosReales#DEFINIR EN LA BASE DE DATOS DE MONGO LOS DATOS ANTERIORES

data = {
    "Esfuerzo[kN]": 2980,#INTRODUCIR VALORES DE ESFUERZO Y DEFORMACIÓN
    "Deformacion[mm]": 9
}
db.insert_one(data)
for x in db.find():
  print(x)

data_list = []
for data_real_bd in db.find():
    data_list.append(data_real_bd)#AGREGAR LOS VALORES DE DATA REAL A LA LISTA DE DATOS

data_real = pd.DataFrame(data_list)
data_real_fit = data_real
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1)#PREPARAR VALORES PARA LA REGRESION LINEAL
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)
x_lim = data_real['Esfuerzo[kN]'].iloc[-1]
y_lim = data_real['Deformacion[mm]'].iloc[-1]
model = LinearRegression()
model.fit(X, y)#ENTRENAR REGRESION
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)
print('la predicción a 1000 kN es de: ', prediction ,'mm')
gr_sin_prediccion()
gr_con_prediccion(x_lim,y_lim)
gr_con_prediccion_3000(prediction)

def gr_con_prediccion(x_lim,y_lim):
  plt.figure(figsize=(15, 6))
  plt.plot(	datos_teoricos['Esfuerzo[kN]'] , datos_teoricos['Deformacion[mm]'])
  plt.scatter(	data_real['Esfuerzo[kN]'] , data_real['Deformacion[mm]'], color='red')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 2: teórico versus real [ZOOM]')
  plt.xlim(0, x_lim)
  plt.ylim(0, y_lim)
  plt.grid()
  plt.gca().invert_yaxis()

def gr_con_prediccion_3000(prediction):
  plt.figure(figsize=(15, 6))
  plt.plot(	datos_teoricos['Esfuerzo[kN]'] , datos_teoricos['Deformacion[mm]'])
  plt.scatter(	data_real['Esfuerzo[kN]'] , data_real['Deformacion[mm]'], color='red')
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')
  plt.scatter(	3000 , prediction, color='green')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN')
  plt.xlim(0, 3000)
  plt.ylim(0, 45)
  plt.grid()
  plt.gca().invert_yaxis()

def gr_sin_prediccion():
  plt.figure(figsize=(15, 6))
  plt.plot(	datos_teoricos['Esfuerzo[kN]'] , datos_teoricos['Deformacion[mm]'])
  plt.scatter(	data_real['Esfuerzo[kN]'] , data_real['Deformacion[mm]'], color='red')
  plt.xlabel('Esfuerzo [kN]')
  plt.ylabel('Deformación [mm]')
  plt.title('Gráfica 1: teórico versus real')
  plt.grid()
  plt.gca().invert_yaxis()