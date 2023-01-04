import numpy as np
import psycopg2
from network import Network
from fc_layer import FCLayer
from act_layer import ActivationLayer
from activation_fun import tanh, tanh_prime
from loss_fun import mse, mse_prime

# obtención de los datos de entrenamiento
conn = psycopg2.connect(database="BBDD", user='postgres',password='diego666', host='127.0.0.1', port='5432')
conn.autocommit = True
cursor = conn.cursor()
query_ultimo = '''SELECT "Orden" FROM public."Primitiva" ORDER BY "Orden" DESC LIMIT 1'''
cursor.execute(query_ultimo)
orden_ultimo = cursor.fetchmany(1)[0][0]
#entrenamos con un 80% de las muestras totales
orden_ultimo_train=(orden_ultimo*8)/10
x_train =

#montar la red neuronal
net=Network()