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

tiempo_ini=datetime.now()
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
conn = psycopg2.connect(database="Prueba", user='postgres', password='diego666', host='127.0.0.1', port= '5432')
#Setting auto commit false
conn.autocommit = True
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Preparing SQL queries to INSERT a record into the database.
for idx in reversed(range(len(dates))):
    # select date
    Select(driver.find_element(By.ID, 'anio')).select_by_index(idx)
    print(f"{driver.current_url.split('/')[-1].split('.')[0]} year")
    # get all raffles in the current date
    raffles = driver.find_elements(By.CSS_SELECTOR, 'div[class="title"] ul')
    for raffle in raffles:
        # scroll to current raffle
        driver.execute_script("arguments[0].scrollIntoView(true);", raffle)
        words_list = raffle.text.split()
        #print(words_list)
        texto='''INSERT INTO public."Bonoloto" VALUES ('''"'" + words_list[0] + "',"+ words_list[1] +","+ words_list[2] +","+ words_list[3] +","+ words_list[4] +","+ words_list[5] +","+ words_list[6] +","+ words_list[7] +","+ words_list[8] +")"
        #print(texto)
        cursor.execute(texto)
        # Commit your changes in the database
        conn.commit()
        #print(raffle.text)

driver.quit()

tiempo_fin=datetime.now()
print("Tiempo transcurrido: " +str(tiempo_fin - tiempo_ini))