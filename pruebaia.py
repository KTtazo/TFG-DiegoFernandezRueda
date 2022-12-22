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

def extraerRecientesPri (bola, numSort,sortActual):
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #query_ultimo=SELECT 1 FROM public."Primitiva" WHERE "Orden" = 4492
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    #print(orden_ultimo)
    listabolas=[]
    listaindices=[]
    #print(bola1)
    for orden in range(numSort,0,-1):
        for b in range (7):
            bola1="Bola"+
               SELECT 1 FROM public."Primitiva" WHERE "Orden" = 4492
        print(orden)


extraerRecientes(0,50,1)