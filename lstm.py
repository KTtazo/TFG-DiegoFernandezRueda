import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from keras.layers import LSTM, Dense, Bidirectional, Dropout
from keras.optimizers import Adam

df = pd.read_csv('Bonoloto_db.csv')
'''print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())'''
df.drop(['Fecha','Reintegro','Orden'],axis=1,inplace=True)
#print(df.head())
scaler=StandardScaler().fit(df.values)
dataset_transformada=scaler.transform(df.values)
df_transformada=pd.DataFrame(data=dataset_transformada,index=df.index)

#print(df_transformada.head())

num_filas=df.values.shape[0]
tamaño_ventana=7#cantidad de sorteos a tener en cuenta en la predicción
num_features=df.values.shape[1]#número de bolas por sorteo
print(num_filas)
print(tamaño_ventana)
print(num_features)
print("----")
X=np.empty([num_filas - tamaño_ventana,tamaño_ventana,num_features], dtype=float)
y=np.empty([ num_filas - tamaño_ventana, num_features], dtype=float)
for i in range (0,num_filas - tamaño_ventana):
    #print(i)
    X[i]=df_transformada.iloc[i:i+tamaño_ventana,0: num_features]
    y[i]=df_transformada.iloc[i+tamaño_ventana:i+tamaño_ventana+1,0:num_features]

'''print(X.shape)
print(y.shape)
print(X[1])
print("y:----")
print(y[1])'''

model=keras.Sequential()
model.add(Bidirectional(LSTM(240, input_shape = (tamaño_ventana, num_features), return_sequences = True)))
model.add(Dropout(0.2))
model.add(Bidirectional(LSTM(240, input_shape=(
    tamaño_ventana, num_features), return_sequences=True)))
model.add(Dropout(0.2))
model.add(Bidirectional(LSTM(240, input_shape=(
    tamaño_ventana, num_features), return_sequences=True)))
model.add(Bidirectional(LSTM(240, input_shape=(
    tamaño_ventana, num_features), return_sequences=False)))
model.add(Dense(59))
model.add(Dense(num_features))
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='mse', metrics=['accuracy'])
model.fit(x=X, y=y, batch_size=300, epochs=10, verbose=2)
