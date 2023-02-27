from datetime import datetime
import logging
import threading
import time
import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import seed
from random import random
import statistics
import pandas as pd
from pylab import *
from scipy import stats
seed(3)

def regPolPri():
    bola1=1
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    #print(orden_ultimo)
    listabolas=[]
    listaindices=[]
    #print(bola1)
    for orden in range(0,orden_ultimo):
        listaindices.append(orden)
        bola="Bola"+str(bola1)   
        query='''SELECT "'''+bola+'''" FROM public."Primitiva" WHERE "Orden" ='''+ str(orden) +''';'''
            #print(query)
        cursor.execute(query)
        valorBola=cursor.fetchmany(1)[0][0]
        listabolas.append(valorBola)
    x=np.array(listaindices)
    y=np.array(listabolas)
    '''p4=np.poly1d(np.polyfit(y, x, 2))
    # calculamos la curva polinomica de 4 grado que se ajusta a los datos 
    # pintamos la muestra y la funcion polinomica en rojo para ver como se ajusta  

    xp = np.linspace(0, 7, 100)
    plt.scatter(y,x)  
    plt.plot(xp, p4(xp), c='r')
    plt.show()'''
    fit = np.polyfit(x, y, 2)
    a = fit[0]
    b = fit[1]
    c = fit[2]
    fit_equation = a * np.square(x) + b * x + c
    #Plotting
    fig1 = plt.figure()
    ax1 = fig1.subplots()
    ax1.plot(x, fit_equation,color = 'r',alpha = 0.5, label = 'Polynomial fit')
    ax1.scatter(x, y, s = 5, color = 'b', label = 'Data points')
    ax1.set_title('Polynomial fit example')
    ax1.legend()
    plt.show()

thread17=threading.Thread(name="hilo17",target=regPolPri)
thread17.start()