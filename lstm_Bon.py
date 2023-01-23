import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from keras.layers import LSTM, Dense, Bidirectional, Dropout
from keras.models import model_from_json
from keras.optimizers import Adam

df_train = pd.read_csv('Bonoloto_db.csv',nrows=7999)
df_test=pd.read_csv('Bonoloto_db.csv',skiprows=8000,nrows=53)
#print(df_test)
'''print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())'''
#formato a train
df_train.drop(['Fecha','Reintegro','Orden'],axis=1,inplace=True)
scaler_train=StandardScaler().fit(df_train.values)
dataset_transformada_train=scaler_train.transform(df_train.values)
df_transformada_train=pd.DataFrame(data=dataset_transformada_train,index=df_train.index)
#formato a test
df_test.drop(['J-1-12-2022','0','7999'],axis=1,inplace=True)
scaler_test=StandardScaler().fit(df_test.values)
dataset_transformada_test=scaler_train.transform(df_test.values)
df_transformada_test=pd.DataFrame(data=dataset_transformada_test,index=df_test.index)
#print(df_transformada_test)

num_filas=df_train.values.shape[0]
tamaño_ventana=7#cantidad de sorteos a tener en cuenta en la predicción
num_features=df_train.values.shape[1]#número de bolas por sorteo
X=np.empty([num_filas - tamaño_ventana,tamaño_ventana,num_features], dtype=float)
y=np.empty([ num_filas - tamaño_ventana, num_features], dtype=float)
for i in range (0,num_filas - tamaño_ventana):
    #print(i)
    X[i]=df_transformada_train.iloc[i:i+tamaño_ventana,0: num_features]
    y[i]=df_transformada_train.iloc[i+tamaño_ventana:i+tamaño_ventana+1,0:num_features]

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
'''model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='mse', metrics=['accuracy'])
model.fit(x=X, y=y, batch_size=300, epochs=300, verbose=2)

# serialize model to JSON
model_json = model.to_json()
with open("model_Bon.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model_Bon.h5")
print("Saved model to disk")'''

# load json and create model
json_file = open('model_Bon.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_Bon.h5")
print("Loaded model from disk")

y_pred = model.predict(np.array([df_transformada_test]))
print("The predicted numbers in the last lottery game are:", scaler_test.inverse_transform(y_pred).astype(int)[0])
prediction = np.array(df_test.tail(1))
print("The actual numbers in the last lottery game were:", prediction[0])