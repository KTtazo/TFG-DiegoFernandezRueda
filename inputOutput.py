import numpy as np
import psycopg2
#iniciar los input y output
x_train = np.array([[[1.0000, 1.0000, 1.0000, 1.0000, 1.0000]]])


def crearInput(bola, orden):
    x_train = np.array([[[1.0000, 1.0000, 1.0000, 1.0000, 1.0000]]])
    conn = psycopg2.connect(database="BBDD", user='postgres',
                            password='diego666', host='127.0.0.1', port='5432')
    conn.autocommit = True  # Setting auto commit false
    cursor = conn.cursor()
    for orden in range(0, orden):
        arrayInputs = []
        bola1 = "B"+str(bola)
        queryAp5 = '''SELECT "'''+bola1 + \
            '''" FROM public."BonolotoAp5" WHERE "Orden" =''' + \
            str(orden) + ''';'''
        cursor.execute(queryAp5)
        arrayInputs.append(cursor.fetchmany(1)[0][0])
        queryAp10 = '''SELECT "'''+bola1 + \
            '''" FROM public."BonolotoAp10" WHERE "Orden" =''' + \
            str(orden) + ''';'''
        cursor.execute(queryAp10)
        arrayInputs.append(cursor.fetchmany(1)[0][0])
        queryDesvEst = '''SELECT "'''+bola1 + \
            '''" FROM public."BonolotoDesvEst" WHERE "Orden" =''' + \
            str(orden) + ''';'''
        cursor.execute(queryDesvEst)
        arrayInputs.append(cursor.fetchmany(1)[0][0])
        queryDistMed = '''SELECT "'''+bola1 + \
            '''" FROM public."BonolotoDistMedia" WHERE "Orden" =''' + \
            str(orden) + ''';'''
        cursor.execute(queryDistMed)
        arrayInputs.append(cursor.fetchmany(1)[0][0])
        queryMedia = '''SELECT "'''+bola1 + \
            '''" FROM public."BonolotoMedia" WHERE "Orden" =''' + \
            str(orden) + ''';'''
        cursor.execute(queryMedia)
        arrayInputs.append(cursor.fetchmany(1)[0][0])
        #print(arrayInputs)
        x_train = np.insert(
            x_train, x_train.shape[0], arrayInputs, axis=0)
    return x_train


def crearOutput(bola, orden):
    y_train = np.array([[[0.0000]]])
    conn = psycopg2.connect(database="BBDD", user='postgres',
                            password='diego666', host='127.0.0.1', port='5432')
    conn.autocommit = True  # Setting auto commit false
    cursor = conn.cursor()
    for orden in range(0, orden):
        query = '''SELECT "Bola'''+str(bola) + \
                '''" FROM public."Bonoloto" WHERE "Orden" =''' + \
                str(orden) + ''';'''
        cursor.execute(query)
        y_train = np.insert(
            y_train, y_train.shape[0], cursor.fetchmany(1)[0][0], axis=0)
    return y_train

