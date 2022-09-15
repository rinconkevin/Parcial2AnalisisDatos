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



main_window = tk.Tk()

url= "AirQualityUCI - copia.csv"
datos = pd.read_csv(url)

columnas = ['Fecha ', 'Hora', 'CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
datos.columns = columnas


#---------------------------- Modelo-------------------------------------------#
def hallarAtipicos(datos):
    c = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    valor = 999
    contador = 0;
    Atipicos1 = []
    k = 1.5
    for i in range(len(datos["CRPCO"])):
        Atipicos1.append(0);
    
    for i in c:
            p1 = np.quantile(datos[i], 0.25)
            u1 = np.quantile(datos[i], 0.75)
            
            RI1 = u1 - p1
            
            Lp11 = p1 - k * RI1
            Lp21 = u1 + k * RI1
    
            for j in datos[i]:
                if(j<Lp11 or j>Lp21):
                    Atipicos1[contador] = valor
                    contador = contador + 1
            contador = 0
            
    return Atipicos1

def EliminarDatosAtipicos(datos1, Atipicos):
    contador = 0
    for i in Atipicos:
        if(i == 999):
            datos1 = datos1.drop(index = [contador])
        contador = contador + 1
    return datos1
def show_selection():
    Opciones = ['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
    Eliminar = ComboSalida.get()
    Opciones.remove(Eliminar)
    k = ComboCantidad.get()
    ComboRE1["values"] = []
    ComboRE2["values"] = []
    ComboRE3["values"] = []
    ComboRE4["values"] = []
    ComboRE5["values"] = []
    ComboRE6["values"] = []
    ComboRE7["values"] = []
    ComboRE8["values"] = []
    ComboRE9["values"] = []
    ComboRE10["values"] = []
    ComboRE11["values"] = []
    ComboRE12["values"] = []
    ComboRE1.set("")
    ComboRE2.set("")
    ComboRE3.set("")
    ComboRE4.set("")
    ComboRE5.set("")
    ComboRE6.set("")
    ComboRE7.set("")
    ComboRE8.set("")
    ComboRE9.set("")
    ComboRE10.set("")
    ComboRE11.set("")
    ComboRE12.set("")
    
    if(k == "1"):
        ComboRE1["values"] = Opciones
    elif(k == "2"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
    elif(k == "3"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
    elif(k == "4"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
    elif(k == "5"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
    elif(k == "6"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
    elif(k == "7"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
        ComboRE7["values"] = Opciones
    elif(k == "8"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
        ComboRE7["values"] = Opciones
        ComboRE8["values"] = Opciones
    elif(k == "9"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
        ComboRE7["values"] = Opciones
        ComboRE8["values"] = Opciones
        ComboRE9["values"] = Opciones
    elif(k == "10"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
        ComboRE7["values"] = Opciones
        ComboRE8["values"] = Opciones
        ComboRE9["values"] = Opciones
        ComboRE10["values"] = Opciones
    elif(k == "11"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
        ComboRE7["values"] = Opciones
        ComboRE8["values"] = Opciones
        ComboRE9["values"] = Opciones
        ComboRE10["values"] = Opciones
        ComboRE11["values"] = Opciones
    elif(k == "12"):
        ComboRE1["values"] = Opciones
        ComboRE2["values"] = Opciones
        ComboRE3["values"] = Opciones
        ComboRE4["values"] = Opciones
        ComboRE5["values"] = Opciones
        ComboRE6["values"] = Opciones
        ComboRE7["values"] = Opciones
        ComboRE8["values"] = Opciones
        ComboRE9["values"] = Opciones
        ComboRE10["values"] = Opciones
        ComboRE11["values"] = Opciones
        ComboRE12["values"] = Opciones
        
def Tabla1(Entrada, Salida, datos, Forma):          
    X2=datos[Entrada]
        
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        X2=datos[Entrada]        
        Y=datos[Salida]
        
        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )
        
        modelo = LinearRegression()
        modelo.fit(X = np.array(X2_train).reshape(-1, 1), y = y2_train)
        print('entrada ' + Entrada + ', salida '+ Salida ,modelo.score(np.array(X2).reshape(-1, 1), Y))
        lista.append(modelo.score(np.array(X2).reshape(-1, 1), Y))  
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla2(Entrada1,Entrada2 , Salida, datos, Forma):
        
    X2=datos[[Entrada1, Entrada2]]    
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
                     
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla3(Entrada1,Entrada2,Entrada3, Salida, datos, Forma):
    X2=datos[[Entrada1, Entrada2,Entrada3]]


    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
     
def Tabla4(Entrada1,Entrada2,Entrada3,Entrada4, Salida, datos, Forma):
    X2=datos[[Entrada1, Entrada2,Entrada3,Entrada4]]

    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla5(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5]]

    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla6(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6]]

    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla7(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7]]

    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 +" - " + Entrada7 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla8(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8]]
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 +" - " + Entrada7 +" - " + Entrada8 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla9(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9]]
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 +" - " + Entrada7 +" - " + Entrada8 +" - " + Entrada9 + ', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla10(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9,Entrada10, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9,Entrada10]]
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 +" - " + Entrada7 +" - " + Entrada8 +" - " + Entrada9 + " - " + Entrada10 +', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla11(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9,Entrada10,Entrada11, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9,Entrada10,Entrada11]]
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 +" - " + Entrada7 +" - " + Entrada8 +" - " + Entrada9 + " - " + Entrada10 +" - " + Entrada11 +', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
def Tabla12(Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9,Entrada10,Entrada11,Entrada12, Salida, datos, Forma):
    X2=datos[[Entrada1,Entrada2,Entrada3,Entrada4,Entrada5,Entrada6,Entrada7,Entrada8,Entrada9,Entrada10,Entrada11,Entrada12]]
    lista = []
    for i in range(10):
        print("Prueba N°", (i+1) )
        modelo = LinearRegression()
        
        Y=datos[Salida]

        X2_train, X2_test, y2_train, y2_test = train_test_split(
                                                X2,
                                                Y,
                                                train_size   = 0.5,
                                            )

        modelo.fit(X= X2_train, y= y2_train )
        print('entrada ' + Entrada1 + " - " + Entrada2 + " - " + Entrada3 + " - " + Entrada4 + " - " + Entrada5 +" - " + Entrada6 +" - " + Entrada7 +" - " + Entrada8 +" - " + Entrada9 + " - " + Entrada10 +" - " + Entrada11 +" - " + Entrada12 +', salida '+ Salida ,modelo.score(np.array(X2_test), y2_test))
        lista.append(modelo.score(np.array(X2_test), y2_test))
    ComboResultado["values"] = lista
    mean = statistics.mean(lista)
    label.configure(text=mean)
    
    
def Regrasion():
    Atipicos = hallarAtipicos(datos)
    datos2 = EliminarDatosAtipicos(datos, Atipicos)
    k = ComboCantidad.get() 
    re1 = ComboRE1.get()
    re2 = ComboRE2.get()
    re3 = ComboRE3.get()
    re4 = ComboRE4.get()
    re5 = ComboRE5.get()
    re6 = ComboRE6.get()
    re7 = ComboRE7.get()
    re8 = ComboRE8.get()
    re9 = ComboRE9.get()
    re10 = ComboRE10.get()
    re11 = ComboRE11.get()
    re12 = ComboRE12.get()
    ATP = ComboAtipico.get() 
    Salida = ComboSalida.get()
    Forma = ComboForma.get()
    
    if(k == "1"):
        if(ATP == "Si"):
            Tabla1(re1, Salida, datos, Forma)
        else:
            Tabla1(re1, Salida, datos2, Forma)
    elif(k == "2"):
        if(ATP == "Si"):
            Tabla2(re1,re2, Salida, datos, Forma)
        else:
            Tabla2(re1,re2, Salida, datos2, Forma)
    elif(k == "3"):
        if(ATP == "Si"):
            Tabla3(re1,re2,re3, Salida, datos, Forma)
        else:
            Tabla3(re1,re2,re3, Salida, datos2, Forma)
    elif(k == "4"):
        if(ATP == "Si"):
            Tabla4(re1,re2,re3,re4, Salida, datos, Forma)
        else:
            Tabla4(re1,re2,re3,re4, Salida, datos2, Forma)
    elif(k == "5"):
        if(ATP == "Si"):
            Tabla5(re1,re2,re3,re4,re5, Salida, datos, Forma)
        else:
            Tabla5(re1,re2,re3,re4,re5, Salida, datos2, Forma)
    elif(k == "6"):
        if(ATP == "Si"):
            Tabla6(re1,re2,re3,re4,re5,re6, Salida, datos, Forma)
        else:
            Tabla6(re1,re2,re3,re4,re5,re6, Salida, datos2, Forma)
    elif(k == "7"):
        if(ATP == "Si"):
            Tabla7(re1,re2,re3,re4,re5,re6,re7, Salida, datos, Forma)
        else:
            Tabla7(re1,re2,re3,re4,re5,re6,re7, Salida, datos2, Forma)
    elif(k == "8"):
        if(ATP == "Si"):
            Tabla8(re1,re2,re3,re4,re5,re6,re7,re8, Salida, datos, Forma)
        else:
            Tabla8(re1,re2,re3,re4,re5,re6,re7,re8, Salida, datos2, Forma)
    elif(k == "9"):
        if(ATP == "Si"):
            Tabla9(re1,re2,re3,re4,re5,re6,re7,re8,re9, Salida, datos, Forma)
        else:
            Tabla9(re1,re2,re3,re4,re5,re6,re7,re8,re9, Salida, datos2, Forma)
    elif(k == "10"):
        if(ATP == "Si"):
            Tabla10(re1,re2,re3,re4,re5,re6,re7,re8,re9,re10, Salida, datos, Forma)
        else:
            Tabla10(re1,re2,re3,re4,re5,re6,re7,re8,re9,re10, Salida, datos2, Forma)
    elif(k == "11"):
        if(ATP == "Si"):
            Tabla11(re1,re2,re3,re4,re5,re6,re7,re8,re9,re10,re11, Salida, datos, Forma)
        else:
            Tabla11(re1,re2,re3,re4,re5,re6,re7,re8,re9,re10,re11, Salida, datos2, Forma)
    elif(k == "12"):
        if(ATP == "Si"):
            Tabla12(re1,re2,re3,re4,re5,re6,re7,re8,re9,re10,re11,re12, Salida, datos, Forma)
        else:
            Tabla12(re1,re2,re3,re4,re5,re6,re7,re8,re9,re10,re11,re12, Salida, datos2, Forma)
#----------------------------------------- Vista --------------------------#


main_window.config(width=1200, height=700)
main_window.title("Parcial N°2")
main_window.resizable(width = False, height = False)
fondo = tk.PhotoImage(file= "Fondo.PNG")
fondo1 = tk.Label(main_window, image=fondo).place(x=0, y=0, width=1200, height=700)

ComboSalida = ttk.Combobox(
    state="readonly",
    values=['CRPCO','PT08.S1','CRPH','CRPB', "PT08.S2s", "CRPNOx", "PT08.S3", "CRPNO2", "PT08.S4", "PT08.S5", "Temperatura", "Humedad", "Humedad Absoluta"]
)

ComboSalida.place(x=780, y=150)
ComboSalida.configure(width=20, height=10)

ComboCantidad = ttk.Combobox(
    state="readonly",
    values=["1","2","3","4","5","6","7","8","9","10","11","12"]
)

ComboCantidad.place(x=780, y=240)
ComboCantidad.configure(width=20, height=10)

ComboAtipico = ttk.Combobox(
    state="readonly",
    values=["Si", "No"]
)

ComboAtipico.place(x=780, y=330)
ComboAtipico.configure(width=20, height=10)

ComboResultado = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboResultado.place(x=680, y=550)
ComboResultado.configure(width=20, height=10)

label = ttk.Label(
    main_window,
    text='0',
    font=("Helvetica", 14))

label.pack(ipadx=10, ipady=10)
label.place(x=900, y=545)

ComboRE1 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE1.place(x=200, y=200)
ComboRE1.configure(width=20, height=10)

ComboRE2 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE2.place(x=200, y=228)
ComboRE2.configure(width=20, height=10)

ComboRE3 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE3.place(x=200, y=256)
ComboRE3.configure(width=20, height=10)

ComboRE4 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE4.place(x=200, y=284)
ComboRE4.configure(width=20, height=10)

ComboRE5 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE5.place(x=200, y=312)
ComboRE5.configure(width=20, height=10)

ComboRE6 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE6.place(x=200, y=340)
ComboRE6.configure(width=20, height=10)

ComboRE7 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE7.place(x=200, y=368)
ComboRE7.configure(width=20, height=10)

ComboRE8 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE8.place(x=200, y=396)
ComboRE8.configure(width=20, height=10)

ComboRE9 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE9.place(x=200, y=424)
ComboRE9.configure(width=20, height=10)

ComboRE10 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE10.place(x=200, y=452)
ComboRE10.configure(width=20, height=10)

ComboRE11 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE11.place(x=200, y=480)
ComboRE11.configure(width=20, height=10)

ComboRE12 = ttk.Combobox(
    state="readonly",
    values=[]
)

ComboRE12.place(x=200, y=508)
ComboRE12.configure(width=20, height=10)


#--------------------------------- Controlador -------------------------------#

button = tk.Button(text="Actualizar Entrada", command=show_selection, width= 34, height=3)
button.place(x=730, y=400)

button = tk.Button(text="Hallar Regresion", command=Regrasion, width= 28, height=2)
button.place(x=170, y=550)

main_window.mainloop()