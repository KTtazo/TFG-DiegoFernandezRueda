from fileinput import close
from queue import Empty
from telnetlib import SE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
#para lista deplegable



path='/Users/Diego/Downloads/chromedriver'
web='https://lawebdelaprimitiva.com/Primitiva/Historico%20de%20sorteos.html'
driver=webdriver.Chrome(path)
driver.get(web)
#lista desplegable
#nueva API, antes había opción de usar Select pero ahora no, más dificil
lispes=driver.find_element("id","anio")
lispes = driver.find_elements(By.CSS_SELECTOR, 'select[name="anio"] option')
opciones = lispes.find_elements(By.TAG_NAME, "option")#lista de las opciones del desplegable
"""for option in opciones:
    print("Value is: %s" % option.get_attribute("value"))"""

opciones[-2].click()
linea2=driver.find_element(By.XPATH, '//*[@title="Jueves 30 de Octubre de 1986"]').text
linea=driver.find_element(By.ID, 'id_sorteo7').text
"""todos=driver.find_elements(By.CLASS_NAME, "bolas")
for bolita in todos:
    print(bolita.text)#también devuelve únicamente los 6 primeros como abajo"""
print(linea2)
print(linea)
print('----------'+linea2)
for bola in range(20):
    try:
        print("--------")
        name='id_sorteo' + str(bola)
        print(name)
        linea=driver.find_element(By.ID, name).text
        print(linea)
    except:
        print("An exception occurred")
    

#coincidencias=driver.find_elements(By.TAG_NAME, 'li')
#coincidencias2=coincidencias
"""for coincidencia in coincidencias:
    print(coincidencia.text)"""

driver.close()


#print(lispes)
