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


def primitiva():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    service = Service(executable_path='/Users/Diego/Downloads/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    weblink= 'https://lawebdelaprimitiva.com/Primitiva/Historico%20de%20sorteos.html'
    driver.get(weblink)
    # accept cookies
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Consentir"]'))).click()
    # get all dates
    lispes=driver.find_element("id","anio")
    dates = driver.find_elements(By.CSS_SELECTOR, 'select[name="anio"] option')
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # Preparing SQL queries to INSERT a record into the database.
    j=0
    for idx in reversed(range(len(dates))):#empieza en 1985
        Select(driver.find_element(By.ID, 'anio')).select_by_index(idx)# select date
        print(f"{driver.current_url.split('/')[-1].split('.')[0]} year")#imprimir el año que usamos
        # get all raffles in the current date
        sorteos = driver.find_elements(By.CSS_SELECTOR, 'div[class="title"] ul')
        sorteos=reversed(sorteos)
        i=0
        for sorteo in sorteos:
            #print(sorteo.text)
            driver.execute_script("arguments[0].scrollIntoView(true);", sorteo)# bajar la vista hasta el sorteo que usamos
            #time.sleep(2)
            words_list = sorteo.text.split()
            #print(fechas[i].get_attribute("title"))
            #print(i)
            #print(sorteo)
            fecha=words_list[0]+"-"+str(driver.current_url.split('/')[-1].split('.')[0])
            query='''INSERT INTO public."Primitiva" VALUES ('''"'" + fecha + "',"+ words_list[1] +","+ words_list[2] +","+ words_list[3] +","+ words_list[4] +","+ words_list[5] +","+ words_list[6] +","+ words_list[7] +","+ words_list[8] +"," + str(j) +")"
            i+=1
            j+=1
            #print(j)
            #print(query)
            
            cursor.execute(query)
            # Commit your changes in the database
            conn.commit()
            #print(raffle.text)

    driver.quit()
    conn.close()
    tiempo_fin=datetime.now()
    print("Tiempo transcurrido (Primitiva): " +str(tiempo_fin - tiempo_ini))

def bonoloto():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    service = Service(executable_path='/Users/Diego/Downloads/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    weblink= 'https://lawebdelaprimitiva.com/Bonoloto/Historico%20de%20sorteos.html'
    driver.get(weblink)
    # accept cookies
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Consentir"]'))).click()
    # get all dates
    lispes=driver.find_element("id","anio")
    dates = driver.find_elements(By.CSS_SELECTOR, 'select[name="anio"] option')
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # Preparing SQL queries to INSERT a record into the database.
    j=0
    for idx in reversed(range(len(dates))):#empieza en 1985
        Select(driver.find_element(By.ID, 'anio')).select_by_index(idx)# select date
        print(f"{driver.current_url.split('/')[-1].split('.')[0]} year")#imprimir el año que usamos
        # get all raffles in the current date
        sorteos = driver.find_elements(By.CSS_SELECTOR, 'div[class="title"] ul')
        sorteos=reversed(sorteos)
        i=0
        for sorteo in sorteos:
            #print(sorteo.text)
            driver.execute_script("arguments[0].scrollIntoView(true);", sorteo)# bajar la vista hasta el sorteo que usamos
            #time.sleep(2)
            words_list = sorteo.text.split()
            #print(fechas[i].get_attribute("title"))
            #print(i)
            #print(sorteo)
            fecha=words_list[0]+"-"+str(driver.current_url.split('/')[-1].split('.')[0])
            query='''INSERT INTO public."Bonoloto" VALUES ('''"'" + fecha + "',"+ words_list[1] +","+ words_list[2] +","+ words_list[3] +","+ words_list[4] +","+ words_list[5] +","+ words_list[6] +","+ words_list[7] +","+ words_list[8] +"," + str(j) +")"
            i+=1
            j+=1
            #print(j)
            #print(query)
            
            cursor.execute(query)
            # Commit your changes in the database
            conn.commit()
            #print(raffle.text)

    driver.quit()
    conn.close()
    tiempo_fin=datetime.now()
    print("Tiempo transcurrido (Primitiva): " +str(tiempo_fin - tiempo_ini))

def actualizar_bonoloto():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    service = Service(executable_path='/Users/Diego/Downloads/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    weblink= 'https://lawebdelaprimitiva.com/Bonoloto/Historico%20de%20sorteos.html'
    driver.get(weblink)
    # accept cookies
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Consentir"]'))).click()
    # get all dates
    dates = driver.find_elements(By.CSS_SELECTOR, 'select[name="anio"] option')
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    
    conn.autocommit = True#Setting auto commit false
    
    cursor = conn.cursor()#Creating a cursor object using the cursor() method
    # Preparing SQL queries to INSERT a record into the database.
    j=0
    for idx in reversed(range((len(dates[:2])))):#empezamos en el año necesario para actualizar
        print(idx)        
        Select(driver.find_element(By.ID, 'anio')).select_by_index(idx)# select date
        # select date
        año=driver.current_url.split('/')[-1].split('.')[0]
        print(año)
        print(f"{driver.current_url.split('/')[-1].split('.')[0]} year")#imprimir el año que usamos
        # get all raffles in the current date
        sorteos = driver.find_elements(By.CSS_SELECTOR, 'div[class="title"] ul')
        sorteos=reversed(sorteos)
        i=0
        query_ultimo='''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
        #print(query_ultimo)
        cursor.execute(query_ultimo)
        orden_ultimo=cursor.fetchmany(1)[0][0]
        print(orden_ultimo)
        for sorteo in sorteos:
            driver.execute_script("arguments[0].scrollIntoView(true);", sorteo)# subir la vista hasta el sorteo que usamos
            words_list = sorteo.text.split()
            fecha=words_list[0]+"-"+año
            #print(fecha)
            query='''SELECT exists (SELECT 1 FROM public."Bonoloto" WHERE "Fecha" = '''+"'" +fecha + "'" +" LIMIT 1)"
            #print(query)
            cursor.execute(query)
            respuesta = cursor.fetchmany(1)#buscar si existe la fecha en la BBDD
            if(respuesta[0][0]!=True):
                orden_ultimo+=1 
                query2='''INSERT INTO public."Bonoloto" VALUES ('''"'" + fecha + "',"+ words_list[1] +","+ words_list[2] +","+ words_list[3] +","+ words_list[4] +","+ words_list[5] +","+ words_list[6] +","+ words_list[7] +","+ words_list[8] +"," + str(orden_ultimo) +")"
                cursor.execute(query2)
                print("Actualizado dato:\n"+ query2)
            else:
                print("Dato presente en BBDD \n" + query)
                
            i+=1
                    
            conn.commit()# Commit your changes in the database
            #print(raffle.text)
    driver.quit()
    conn.close()

def actualizar_primitiva():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])

    service = Service(executable_path='/Users/Diego/Downloads/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    weblink= 'https://lawebdelaprimitiva.com/Primitiva/Historico%20de%20sorteos.html'
    driver.get(weblink)
    # accept cookies
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Consentir"]'))).click()
    # get all dates
    dates = driver.find_elements(By.CSS_SELECTOR, 'select[name="anio"] option')
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    
    conn.autocommit = True#Setting auto commit false
    
    cursor = conn.cursor()#Creating a cursor object using the cursor() method
    # Preparing SQL queries to INSERT a record into the database.
    j=0
    for idx in reversed(range((len(dates[:2])))):#empezamos en el año necesario para actualizar
        print(idx)        
        Select(driver.find_element(By.ID, 'anio')).select_by_index(idx)# select date
        # select date
        año=driver.current_url.split('/')[-1].split('.')[0]
        print(año)
        print(f"{driver.current_url.split('/')[-1].split('.')[0]} year")#imprimir el año que usamos
        # get all raffles in the current date
        sorteos = driver.find_elements(By.CSS_SELECTOR, 'div[class="title"] ul')
        sorteos=reversed(sorteos)
        i=0
        query_ultimo='''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
        #print(query_ultimo)
        cursor.execute(query_ultimo)
        orden_ultimo=cursor.fetchmany(1)[0][0]
        print(orden_ultimo)
        for sorteo in sorteos:
            driver.execute_script("arguments[0].scrollIntoView(true);", sorteo)# subir la vista hasta el sorteo que usamos
            words_list = sorteo.text.split()
            fecha=words_list[0]+"-"+año
            #print(fecha)
            query='''SELECT exists (SELECT 1 FROM public."Primitiva" WHERE "Fecha" = '''+"'" +fecha + "'" +" LIMIT 1)"
            #print(query)
            cursor.execute(query)
            respuesta = cursor.fetchmany(1)#buscar si existe la fecha en la BBDD
            if(respuesta[0][0]!=True):
                orden_ultimo+=1 
                query2='''INSERT INTO public."Primitiva" VALUES ('''"'" + fecha + "',"+ words_list[1] +","+ words_list[2] +","+ words_list[3] +","+ words_list[4] +","+ words_list[5] +","+ words_list[6] +","+ words_list[7] +","+ words_list[8] +"," + str(orden_ultimo) +")"
                cursor.execute(query2)
                print("Actualizado dato:\n"+ query2)
            else:
                print("Dato presente en BBDD \n" + query)
                
            i+=1
                    
            conn.commit()# Commit your changes in the database
            #print(raffle.text)
    driver.quit()
    conn.close()
    
    
    driver.quit()
    conn.close()

def CompPrimitiva():
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
            last=UltimaAparicionPri(orden,valorBola)
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

def CompBonoloto(start,finish):
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    #print(orden_ultimo)
    for orden in range(start,finish):
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
            print(valorBola)
            last=UltimaAparicionBon(orden,valorBola) 
            print(last)
            lastList.append(last)
            #print(lastList)
        #print(lastList)
        queryInsert='''INSERT INTO public."BonolotoComp" VALUES ('''"'" + str(fecha) + "',"+ str(lastList[0]) +","+ str(lastList[1]) +","+ str(lastList[2]) +","+ str(lastList[3]) +","+ str(lastList[4]) +","+ str(lastList[5]) +","+ str(lastList[6]) +"," + str(orden) +")"
        cursor.execute(queryInsert)
        #print(queryInsert)
    conn.commit()
    conn.close()  
    tiempo_fin=datetime.now()
    print("Tiempo transcurrido (Bonoloto): " +str(tiempo_fin - tiempo_ini))  

def UltimaAparicionPri(ordenEntrada, bola):
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

def UltimaAparicionBon(ordenEntrada, bola):
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    conn.autocommit = True#Setting auto commit false
    cursor = conn.cursor()
    for ordenEvaluado in range(ordenEntrada-1,0,-1):
        for b in range(7):
            bola1="Bola"+str(b+1) 
            queryCheck='''SELECT exists ( SELECT 1 FROM public."Bonoloto" WHERE "Orden" = '''+ str(ordenEvaluado) +''' AND "'''+ bola1 +'''"='''+ str(bola) +''' LIMIT 1);'''
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

def estadisticasPri():
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    conn.autocommit = True#Setting auto commit false
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    #print(orden_ultimo)
    listaMedia=[]
    listaMediana=[]
    listaModa=[]
    listaDesv=[]
    listaVarianza=[]
    for b in range(7):
        bola=b+1
        bola="Bola"+str(bola) 
        lista=[]
        for orden in range(0,orden_ultimo):
            query='''SELECT "'''+bola+'''" FROM public."Primitiva" WHERE "Orden" ='''+ str(orden) +''';'''
            cursor.execute(query)
            valorBola=cursor.fetchmany(1)[0][0]
            if(valorBola<1000):
                lista.append(valorBola)
        #print(lista)
        listaMedia.append(statistics.mean(lista))
        listaMediana.append(statistics.median(lista))
        listaModa.append(statistics.mode(lista))
        listaDesv.append(statistics.pstdev(lista))
        listaVarianza.append(statistics.variance(lista))
    
    queryDeleteMean='''DELETE FROM public."EstadisticasPri" WHERE "Categoria" = 'Media';'''
    queryInsertMean='''INSERT INTO public."EstadisticasPri" VALUES ('''"'Media',"+ str(listaMedia[0]) +","+ str(listaMedia[1]) +","+ str(listaMedia[2]) +","+ str(listaMedia[3]) +","+ str(listaMedia[4]) +","+ str(listaMedia[5]) +","+ str(listaMedia[6]) +")"
    cursor.execute(queryDeleteMean)
    cursor.execute(queryInsertMean)
    queryDeleteMedian='''DELETE FROM public."EstadisticasPri" WHERE "Categoria" = 'Mediana';'''
    queryInsertMedian='''INSERT INTO public."EstadisticasPri" VALUES ('''"'Mediana',"+ str(listaMediana[0]) +","+ str(listaMediana[1]) +","+ str(listaMediana[2]) +","+ str(listaMediana[3]) +","+ str(listaMediana[4]) +","+ str(listaMediana[5]) +","+ str(listaMediana[6]) +")"
    cursor.execute(queryDeleteMedian)
    cursor.execute(queryInsertMedian)
    queryDeleteModa='''DELETE FROM public."EstadisticasPri" WHERE "Categoria" = 'Moda';'''
    queryInsertModa='''INSERT INTO public."EstadisticasPri" VALUES ('''"'Moda',"+ str(listaModa[0]) +","+ str(listaModa[1]) +","+ str(listaModa[2]) +","+ str(listaModa[3]) +","+ str(listaModa[4]) +","+ str(listaModa[5]) +","+ str(listaModa[6]) +")"
    cursor.execute(queryDeleteModa)
    cursor.execute(queryInsertModa)
    queryDeleteDes='''DELETE FROM public."EstadisticasPri" WHERE "Categoria" = 'DesviacionEstandar';'''
    queryInsertDes='''INSERT INTO public."EstadisticasPri" VALUES ('''"'DesviacionEstandar',"+ str(listaDesv[0]) +","+ str(listaDesv[1]) +","+ str(listaDesv[2]) +","+ str(listaDesv[3]) +","+ str(listaDesv[4]) +","+ str(listaDesv[5]) +","+ str(listaDesv[6]) +")"
    cursor.execute(queryDeleteDes)
    cursor.execute(queryInsertDes)
    queryDeleteVar='''DELETE FROM public."EstadisticasPri" WHERE "Categoria" = 'Varianza';'''
    queryInsertVar='''INSERT INTO public."EstadisticasPri" VALUES ('''"'Varianza',"+ str(listaVarianza[0]) +","+ str(listaVarianza[1]) +","+ str(listaVarianza[2]) +","+ str(listaVarianza[3]) +","+ str(listaVarianza[4]) +","+ str(listaVarianza[5]) +","+ str(listaVarianza[6]) +")"
    cursor.execute(queryDeleteVar)
    cursor.execute(queryInsertVar)
    conn.commit()
    conn.close() 
    tiempo_fin=datetime.now()
    print("Tiempo transcurrido (Primitiva) stats: " +str(tiempo_fin - tiempo_ini)) 

def estadisticasBon():
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    conn.autocommit = True#Setting auto commit false
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    #print(orden_ultimo)
    listaMedia=[]
    listaMediana=[]
    listaModa=[]
    listaDesv=[]
    listaVarianza=[]
    for b in range(7):
        bola=b+1
        bola="Bola"+str(bola) 
        lista=[]
        print(orden_ultimo)
        for orden in range(0,orden_ultimo):
            query='''SELECT "'''+bola+'''" FROM public."Bonoloto" WHERE "Orden" ='''+ str(orden) +''';'''
            #print(query)
            cursor.execute(query)
            #print(orden)
            valorBola=cursor.fetchmany(1)[0][0]
            if(valorBola<1000):
                lista.append(valorBola)
        #print(lista)
        listaMedia.append(statistics.mean(lista))
        listaMediana.append(statistics.median(lista))
        listaModa.append(statistics.mode(lista))
        listaDesv.append(statistics.pstdev(lista))
        listaVarianza.append(statistics.variance(lista))
    
    queryDeleteMean='''DELETE FROM public."EstadisticasBon" WHERE "Categoria" = 'Media';'''
    queryInsertMean='''INSERT INTO public."EstadisticasBon" VALUES ('''"'Media',"+ str(listaMedia[0]) +","+ str(listaMedia[1]) +","+ str(listaMedia[2]) +","+ str(listaMedia[3]) +","+ str(listaMedia[4]) +","+ str(listaMedia[5]) +","+ str(listaMedia[6]) +")"
    cursor.execute(queryDeleteMean)
    cursor.execute(queryInsertMean)
    queryDeleteMedian='''DELETE FROM public."EstadisticasBon" WHERE "Categoria" = 'Mediana';'''
    queryInsertMedian='''INSERT INTO public."EstadisticasBon" VALUES ('''"'Mediana',"+ str(listaMediana[0]) +","+ str(listaMediana[1]) +","+ str(listaMediana[2]) +","+ str(listaMediana[3]) +","+ str(listaMediana[4]) +","+ str(listaMediana[5]) +","+ str(listaMediana[6]) +")"
    cursor.execute(queryDeleteMedian)
    cursor.execute(queryInsertMedian)
    queryDeleteModa='''DELETE FROM public."EstadisticasBon" WHERE "Categoria" = 'Moda';'''
    queryInsertModa='''INSERT INTO public."EstadisticasBon" VALUES ('''"'Moda',"+ str(listaModa[0]) +","+ str(listaModa[1]) +","+ str(listaModa[2]) +","+ str(listaModa[3]) +","+ str(listaModa[4]) +","+ str(listaModa[5]) +","+ str(listaModa[6]) +")"
    cursor.execute(queryDeleteModa)
    cursor.execute(queryInsertModa)
    queryDeleteDes='''DELETE FROM public."EstadisticasBon" WHERE "Categoria" = 'DesviacionEstandar';'''
    queryInsertDes='''INSERT INTO public."EstadisticasBon" VALUES ('''"'DesviacionEstandar',"+ str(listaDesv[0]) +","+ str(listaDesv[1]) +","+ str(listaDesv[2]) +","+ str(listaDesv[3]) +","+ str(listaDesv[4]) +","+ str(listaDesv[5]) +","+ str(listaDesv[6]) +")"
    cursor.execute(queryDeleteDes)
    cursor.execute(queryInsertDes)
    queryDeleteVar='''DELETE FROM public."EstadisticasBon" WHERE "Categoria" = 'Varianza';'''
    queryInsertVar='''INSERT INTO public."EstadisticasBon" VALUES ('''"'Varianza',"+ str(listaVarianza[0]) +","+ str(listaVarianza[1]) +","+ str(listaVarianza[2]) +","+ str(listaVarianza[3]) +","+ str(listaVarianza[4]) +","+ str(listaVarianza[5]) +","+ str(listaVarianza[6]) +")"
    cursor.execute(queryDeleteVar)
    cursor.execute(queryInsertVar)
    conn.commit()
    conn.close() 
    tiempo_fin=datetime.now()
    print("Tiempo transcurrido (Bonoloto) stats: " +str(tiempo_fin - tiempo_ini))

def desvEstBon():
    conn = psycopg2.connect(database="BBDD", user='postgres',
                            password='diego666', host='127.0.0.1', port='5432')
    conn.autocommit = True  # Setting auto commit false
    cursor = conn.cursor()
    query_ultimo = '''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo = cursor.fetchmany(1)[0][0]
    listaBolas=[[],[],[],[],[],[],[]]
    for orden in range(0, orden_ultimo):
        listaDesv = []
        for b in range(7):
            #print(listaBolas[b])
            bola = b+1
            bola = "Bola"+str(bola)
            query = '''SELECT "'''+bola + \
                '''" FROM public."Bonoloto" WHERE "Orden" =''' + \
                str(orden) + ''';'''
            cursor.execute(query)
            valorBola = cursor.fetchmany(1)[0][0]
            listaBolas[b].append(valorBola)
            # print(listaBolas)
            if (len(listaBolas[b]) < 2):
                listaDesv.append(0)

            else:
                listaDesv.append(statistics.variance(listaBolas[b])) 
        
        queryInsertDes = '''INSERT INTO public."BonolotoDesvEst" VALUES ('''+str(listaDesv[0]) + "," + str(listaDesv[1]) + "," + str(listaDesv[2]) + "," + str(listaDesv[3]) + "," + str(listaDesv[4]) + "," + str(listaDesv[5]) + "," + str(listaDesv[6]) + ","+str(orden)+")"
        #print(queryInsertDes)
        cursor.execute(queryInsertDes)
        
def desvEstPri():
    conn = psycopg2.connect(database="BBDD", user='postgres',
                            password='diego666', host='127.0.0.1', port='5432')
    conn.autocommit = True  # Setting auto commit false
    cursor = conn.cursor()
    query_ultimo = '''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo = cursor.fetchmany(1)[0][0]
    listaBolas = [[], [], [], [], [], [], []]
    for orden in range(0, orden_ultimo):
        listaDesv = []
        for b in range(7):
            # print(listaBolas[b])
            bola = b+1
            bola = "Bola"+str(bola)
            query = '''SELECT "'''+bola + \
                '''" FROM public."Primitiva" WHERE "Orden" =''' + \
                str(orden) + ''';'''
            cursor.execute(query)
            valorBola = cursor.fetchmany(1)[0][0]
            listaBolas[b].append(valorBola)
            # print(listaBolas)
            if (len(listaBolas[b]) < 2):
                listaDesv.append(0)

            else:
                listaDesv.append(statistics.variance(listaBolas[b]))

        queryInsertDes = '''INSERT INTO public."PrimitivaDesvEst" VALUES ('''+str(listaDesv[0]) + "," + str(listaDesv[1]) + "," + str(
            listaDesv[2]) + "," + str(listaDesv[3]) + "," + str(listaDesv[4]) + "," + str(listaDesv[5]) + "," + str(listaDesv[6]) + ","+str(orden)+")"
        # print(queryInsertDes)
        cursor.execute(queryInsertDes)


def mediaBon():
    conn = psycopg2.connect(database="BBDD", user='postgres',
                            password='diego666', host='127.0.0.1', port='5432')
    conn.autocommit = True  # Setting auto commit false
    cursor = conn.cursor()
    query_ultimo = '''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo = cursor.fetchmany(1)[0][0]
    listaBolas = [[], [], [], [], [], [], []]
    for orden in range(0, orden_ultimo):
        listaMed = []
        for b in range(7):
            # print(listaBolas[b])
            bola = b+1
            bola = "Bola"+str(bola)
            query = '''SELECT "'''+bola + \
                '''" FROM public."Bonoloto" WHERE "Orden" =''' + \
                str(orden) + ''';'''
            cursor.execute(query)
            valorBola = cursor.fetchmany(1)[0][0]
            listaBolas[b].append(valorBola)
            # print(listaBolas)
            listaMed.append(statistics.mean(listaBolas[b]))

        queryInsertMedia = '''INSERT INTO public."BonolotoMedia" VALUES ('''+str(listaMed[0]) + "," + str(listaMed[1]) + "," + str(
            listaMed[2]) + "," + str(listaMed[3]) + "," + str(listaMed[4]) + "," + str(listaMed[5]) + "," + str(listaMed[6]) + ","+str(orden)+")"
        # print(queryInsertDes)
        cursor.execute(queryInsertMedia)


def mediaPri():
    conn = psycopg2.connect(database="BBDD", user='postgres',
                            password='diego666', host='127.0.0.1', port='5432')
    conn.autocommit = True  # Setting auto commit false
    cursor = conn.cursor()
    query_ultimo = '''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo = cursor.fetchmany(1)[0][0]
    listaBolas = [[], [], [], [], [], [], []]
    for orden in range(0, orden_ultimo):
        listaMed = []
        for b in range(7):
            # print(listaBolas[b])
            bola = b+1
            bola = "Bola"+str(bola)
            query = '''SELECT "'''+bola + \
                '''" FROM public."Primitiva" WHERE "Orden" =''' + \
                str(orden) + ''';'''
            cursor.execute(query)
            valorBola = cursor.fetchmany(1)[0][0]
            listaBolas[b].append(valorBola)
            # print(listaBolas)
            listaMed.append(statistics.mean(listaBolas[b]))

        queryInsertMedia = '''INSERT INTO public."PrimitivaMedia" VALUES ('''+str(listaMed[0]) + "," + str(listaMed[1]) + "," + str(
            listaMed[2]) + "," + str(listaMed[3]) + "," + str(listaMed[4]) + "," + str(listaMed[5]) + "," + str(listaMed[6]) + ","+str(orden)+")"
        # print(queryInsertDes)
        cursor.execute(queryInsertMedia)

def aparicionesPri(num,veces):
    cuenta=0
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    conn.autocommit = True#Setting auto commit false
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    for ordenEvaluado in range (orden_ultimo-veces,orden_ultimo):
        #print(ordenEvaluado)
        queryCheck='''SELECT exists ( SELECT 1 FROM public."Primitiva" WHERE "Orden" =''' +str(ordenEvaluado)+''' AND ("Bola1"='''+str(num)+''' OR "Bola2"='''+str(num)+''' OR "Bola3"='''+str(num)+''' OR "Bola4"='''+str(num)+''' OR "Bola5"='''+str(num)+''' OR "Bola6"='''+str(num)+''' OR "Bola7"='''+str(num)+''') LIMIT 1);'''
        cursor.execute(queryCheck)
        respuesta=cursor.fetchmany(1)[0][0]
        if(respuesta==True):
            cuenta+=1
    print(cuenta)

def aparicionesBon(num,veces):
    cuenta=0
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    conn.autocommit = True#Setting auto commit false
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    for ordenEvaluado in range (orden_ultimo-veces,orden_ultimo):
        #print(ordenEvaluado)
        queryCheck='''SELECT exists ( SELECT 1 FROM public."Bonoloto" WHERE "Orden" =''' +str(ordenEvaluado)+''' AND ("Bola1"='''+str(num)+''' OR "Bola2"='''+str(num)+''' OR "Bola3"='''+str(num)+''' OR "Bola4"='''+str(num)+''' OR "Bola5"='''+str(num)+''' OR "Bola6"='''+str(num)+''' OR "Bola7"='''+str(num)+''') LIMIT 1);'''
        cursor.execute(queryCheck)
        respuesta=cursor.fetchmany(1)[0][0]
        if(respuesta==True):
            cuenta+=1
    print(cuenta)

def regLinPri():
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
            #print(lastList)
    #print(listabolas)
    slope, intercept, r_value, p_value, std_err = stats.linregress(listaindices,listabolas)
    print("Error: "+str(r_value**2))#se eleva para que dé un valor positivo
    fitLine=[]
    for x in range(len(listabolas)):
        fitLine.append(slope * x + intercept)
    #figure, axis = plt.subplots(3, 2)
    plt.scatter(listaindices,listabolas,s = 4, color = 'b', label = 'Bolas')  
    plt.plot(listaindices, fitLine, c='r',alpha = 0.5, label = 'Linear fit')
    plt.show()
     
def regLinBon():
    bola=7
    #Establishing the connection
    conn = psycopg2.connect(database="BBDD", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
    #Setting auto commit false
    conn.autocommit = True
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    query_ultimo='''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
    cursor.execute(query_ultimo)
    orden_ultimo=cursor.fetchmany(1)[0][0]
    #print(orden_ultimo)
    listabolas=[]
    listaindices=[]
    for orden in range(0,orden_ultimo):
        listaindices.append(orden)
        bola1="Bola"+str(bola)   
        query='''SELECT "'''+bola1+'''" FROM public."Bonoloto" WHERE "Orden" ='''+ str(orden) +''';'''
        #print(query)
        cursor.execute(query)
        valorBola=cursor.fetchmany(1)[0][0]
        listabolas.append(valorBola)
        #print(lastList)
    slope, intercept, r_value, p_value, std_err = stats.linregress(listaindices,listabolas)
    fitLine=[]
    for x in range(len(listabolas)):
        fitLine.append(slope * x + intercept)
    print("Error: "+str(r_value**2))#se eleva para que dé un valor positivo
    #print(fitLine)
    plt.scatter(listaindices,listabolas,s = 4, color = 'b', label = 'Bolas')  
    plt.plot(listaindices, fitLine, c='r',alpha = 0.5, label = 'Linear fit')
    plt.show()  

def regPolPri():
    bola1=7
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
    fit = np.polyfit(x, y, 4)
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

#tiempo_ini=datetime.now()
thread1=threading.Thread(name="hilo1",target=primitiva)
#thread1.start()
thread2=threading.Thread(name="hilo2",target=bonoloto)
#thread2.start()
thread3=threading.Thread(name="hilo3",target=actualizar_bonoloto)
#thread3.start()
thread4=threading.Thread(name="hilo4",target=actualizar_primitiva)
#thread4.start()
thread5=threading.Thread(name="hilo5",target=CompPrimitiva)
#thread5.start()
thread6=threading.Thread(name="hilo6",target=CompBonoloto,args=(0,1500))
thread7=threading.Thread(name="hilo7",target=CompBonoloto,args=(1500,3000))
thread8=threading.Thread(name="hilo8",target=CompBonoloto,args=(3000,4500))
thread9=threading.Thread(name="hilo9",target=CompBonoloto,args=(4500,6000))
thread10=threading.Thread(name="hilo10",target=CompBonoloto,args=(6000,8000))
'''thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()'''
thread11=threading.Thread(name="hilo11",target=estadisticasPri)
#thread11.start()
thread12=threading.Thread(name="hilo12",target=estadisticasBon)
#thread12.start()
thread18 = threading.Thread(name="hilo18", target=desvEstBon)
#thread18.start()
thread19 = threading.Thread(name="hilo19", target=desvEstPri)
#thread19.start()
thread20 = threading.Thread(name="hilo20", target=mediaBon)
#thread20.start()
thread21 = threading.Thread(name="hilo21", target=mediaPri)
thread21.start()
thread13=threading.Thread(name="hilo13",target=aparicionesPri,args=(2,50))
#thread13.start()
thread14=threading.Thread(name="hilo14",target=aparicionesBon,args=(2,50))
#thread14.start()
thread15=threading.Thread(name="hilo15",target=regLinPri)
#thread15.start()
thread16=threading.Thread(name="hilo16",target=regLinBon)
#thread16.start()
thread17=threading.Thread(name="hilo17",target=regPolPri)
#thread17.start()