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
seed(3)

def CompPrimitivaOrd():
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
    for orden in range(0,orden_ultimo):
        #print("......."+str(orden))
        queryFecha='''SELECT "Fecha" FROM public."Primitiva" WHERE "Orden" ='''+ str(orden) +''';'''
        cursor.execute(queryFecha)
        fecha=cursor.fetchmany(1)[0][0]
        lastList=[]
        for b in range(7):
            bola=b+1
            bola="Bola"+str(bola)   
            query='''SELECT "'''+bola+'''" FROM public."Primitiva" WHERE "Orden" ='''+ str(orden) +''';'''
            #print(query)
            cursor.execute(query)
            valorBola=cursor.fetchmany(1)[0][0]
            last=UltimaAparicionPriOrd(orden,valorBola)
            lastList.append(last)
            #print(lastList)
        #print(lastList)
        queryInsert='''INSERT INTO public."PrimitivaComp" VALUES ('''"'" + str(fecha) + "',"+ str(lastList[0]) +","+ str(lastList[1]) +","+ str(lastList[2]) +","+ str(lastList[3]) +","+ str(lastList[4]) +","+ str(lastList[5]) +","+ str(lastList[6]) +"," + str(orden) +")"
        cursor.execute(queryInsert)
        #print(queryInsert)
    conn.commit()
    conn.close() 
    tiempo_fin=datetime.now()
    print("Tiempo transcurrido (Primitiva): " +str(tiempo_fin - tiempo_ini)) 

def CompBonolotoOrdenado():
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    print(orden_ultimo)
    for orden in range(0,orden_ultimo):
        print("......."+str(orden))
        queryFecha='''SELECT "Fecha" FROM public."Bonoloto" WHERE "Orden" ='''+ str(orden) +''';'''
        cursor.execute(queryFecha)
        fecha=cursor.fetchmany(1)[0][0]
        lastList=[]
        for b in range(7):
            bola=b+1
            bola="Bola"+str(bola)   
            query='''SELECT "'''+bola+'''" FROM public."Bonoloto" WHERE "Orden" ='''+ str(orden) +''';'''
            #print(query)
            cursor.execute(query)
            valorBola=cursor.fetchmany(1)[0][0]
            last=UltimaAparicion(orden,valorBola)
            lastList.append(last)
            #print(lastList)
        #print(lastList)
        queryInsert='''INSERT INTO public."BonolotoComp" VALUES ('''"'" + str(fecha) + "',"+ str(lastList[0]) +","+ str(lastList[1]) +","+ str(lastList[2]) +","+ str(lastList[3]) +","+ str(lastList[4]) +","+ str(lastList[5]) +","+ str(lastList[6]) +"," + str(orden) +")"
        #cursor.execute(queryInsert)
        print(queryInsert)
    conn.commit()
    conn.close()    
def UltimaAparicionPriOrd(ordenEntrada, bola):
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    conn.autocommit = True#Setting auto commit false
    cursor = conn.cursor()
    for ordenEvaluado in range(ordenEntrada-1,0,-1):
        for b in range(7):
            bola1="Bola"+str(b+1) 
            queryCheck='''SELECT exists ( SELECT 1 FROM public."Primitiva" WHERE "Orden" = '''+ str(ordenEvaluado) +''' AND "'''+ bola1 +'''"='''+ str(bola) +''' LIMIT 1);'''
            print(queryCheck)
            cursor.execute(queryCheck)
            respuesta=cursor.fetchmany(1)[0][0]
            if(respuesta==True):
                #print(respuesta)
                #print(ordenEntrada-ordenEvaluado)
                return ordenEntrada-ordenEvaluado
            
            #print(ordenEvaluado)
    #print(30000)
    return int(random()*10000000)#random es para que no se repita el numero de sorteos

    

    
    #tiempo_fin=datetime.now()
    #print("Tiempo transcurrido (Primitiva): " +str(tiempo_fin - tiempo_ini))

#CompPrimitiva()
#UltimaAparicion(9,60)
CompPrimitivaOrd()
tiempo_ini=datetime.now()