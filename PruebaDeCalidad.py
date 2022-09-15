#Interfaz
from tkinter import ttk, Tk, Frame,Button 
import tkinter as tk

#Graficas
import pandas as pd
import matplotlib.pyplot as plot
from  scipy import stats
import numpy  as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
#from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math
from math import log
import statistics

url= "AirQualityUCI - copia.csv"
datos = pd.read_csv(url)

columnas = ['Fecha ', 'Hora', 'CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
datos.columns = columnas

from itertools import combinations
A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 2)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 3)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2, v3]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 4)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 5)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 6)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5,v6]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))
        
for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 7)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        v7 = i[6]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5,v6,v7]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))
        
for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 8)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        v7 = i[6]
        v8 = i[7]
        
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5,v6,v7,v8]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 9)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        v7 = i[6]
        v8 = i[7]
        v9 = i[8]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5,v6,v7,v8,v9]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 10)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        v7 = i[6]
        v8 = i[7]
        v9 = i[8]
        v10 = i[9]
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5,v6,v7,v8,v9,v10]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))

for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 11)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        v7 = i[6]
        v8 = i[7]
        v9 = i[8]
        v10 = i[9]
        v11 = i[10]
        
        #print(v1, " + ", v2)
        X2=datos[[v1, v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))
        
for j in A:
    #print(j)
    A = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    A.remove(j)
    temp = combinations(A, 12)
    for i in list(temp):
        v1 = i[0]
        v2 = i[1]
        v3 = i[2]
        v4 = i[3]
        v5 = i[4]
        v6 = i[5]
        v7 = i[6]
        v8 = i[7]
        v9 = i[8]
        v10 = i[9]
        v11 = i[10]
        v12 = i[11]
        
        #print(v1, " + ", v2)
        X2=datos[[v1, v2]]    
        lista = []
        modelo = LinearRegression()        
        Y=datos[j]
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                    X2,
                                                    Y,
                                                    train_size   = 0.5,
                                                )
        modelo.fit(X= X2_train, y= y2_train )
        print(modelo.score(np.array(X2_test), y2_test))
    
        
        