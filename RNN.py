import numpy as np
import psycopg2

# from keras.datasets import mnist
# from keras.utils import np_utils

from network import Network
from fc_layer import FCLayer
from act_layer import ActivationLayer
from activation_fun import tanh, tanh_prime
from loss_fun import mse, mse_prime
from inputOutput import crearInput,crearOutput

# obtención de los datos de entrenamiento
conn = psycopg2.connect(database="BBDD", user='postgres',
                        password='diego666', host='127.0.0.1', port='5432')
conn.autocommit = True
cursor = conn.cursor()
query_ultimo = '''SELECT "Orden" FROM public."Bonoloto" ORDER BY "Orden" DESC LIMIT 1'''
cursor.execute(query_ultimo)
orden_ultimo = cursor.fetchmany(1)[0][0]
# entrenamos con un 80% de las muestras totales
orden_ultimo_train = (orden_ultimo*8)/10
x_train=crearInput(1,7000)
y_train=crearOutput(1,7000)
print(x_train.shape)
print(y_train.shape)


#montar la red neuronal
net=Network()
net.add(FCLayer(5,5))#un input porque solo introducimos el array de las bolas
net.add(ActivationLayer(tanh,tanh_prime))
net.add(FCLayer(5,1))
net.add(ActivationLayer(tanh,tanh_prime))

#entrenamiento
net.use(mse,mse_prime)#funciones perdida
net.fit(x_train,y_train,epochs=3000, learning_rate=0.2)

#test
out=net.predict(x_train)
print(out)
