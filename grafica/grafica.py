from data.data import *
from BD.baseDatos import *
from sklearn.linear_model import LinearRegression
from grafica.grafica import *
import pandas as pd

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos()#DEFINIR UNA LISTA DE DATOS
data_real = pd.DataFrame(data_list)#UNA BASE DE DATOS CON LA LISTA ANTERIOR
data_real_fit = data_real#BASE PARA ENTRENAR EL MODELO SIGUIENTE
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1)#X, VALIABLE ENTRENADA DE LOS ESFUERZOS
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)#Y, VALIABLE ENTRENADA DE LA DEFORMACION
x_lim = data_real['Esfuerzo[kN]'].iloc[-1]#EL LIMITE DEL ESFUERZO ES UN VALOR -1
y_lim = data_real['Deformacion[mm]'].iloc[-1]#EL LIMITE DE LA DEFORMACION ES EL VALOR -1
model = LinearRegression()#MODELO DE REGRESION LINEAL
model.fit(X, y)#ENTRENAR EL MODELO CON VALORES X Y Y
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)#PREDECIR LOS VALORES CON UN ARREGLO DE VALORES
print('la predicción a 1000 kN es de: ', prediction ,'mm')#IMPRIMIR LOS VALORES ENCONTRADOSS


dataRealEsfuerzo = data_real['Esfuerzo[kN]']
dataRealDeformacion = data_real['Deformacion[mm]']

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)

