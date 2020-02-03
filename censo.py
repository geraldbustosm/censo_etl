import pandas as pd
import listas as ls
import psycopg2 as pg

# Estableciendo conexión a la base de datos
connection = pg.connect(host = 'localhost', user = 'postgres', database = 'censo', password = 'hola123a')
cursor = connection.cursor()

# Diccionarios a utilizar
paises = ls.paises()
regiones = ls.regiones()
provincias = ls.provincias()
comunas = ls.comunas()
distritos = ls.distritos()
comunadistrito = ls.comunadistrito()
pueblos = ls.pueblos()

# Insertando informaión base: Regiones
for key in regiones:
    sql = 'INSERT INTO REGION VALUES(%s, %s, %s)'
    values = (regiones[key]['codigo_region'], regiones[key]['region'], regiones[key]['codigo_region15r'])
    cursor.execute(sql,values)
    connection.commit()
print('Se insertaron las regiones')

# Insertando información base: Provincias
for key in provincias:
    sql = 'INSERT INTO PROVINCIA VALUES(%s, %s, %s, %s)'
    values = (provincias[key]['codigo_provincia'], provincias[key]['provincia'], provincias[key]['codigo_provincia'], provincias[key]['codigo_region'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertaron las provincias')

# Insertando información base: Comunas
for key in comunas:
    sql = 'INSERT INTO COMUNA VALUES(%s, %s, %s, %s)'
    values = (comunas[key]['codigo_comuna'], comunas[key]['comuna'], comunas[key]['codigo_comuna'], comunas[key]['codigo_provincia'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertaron las comunas')

# Insertando información base: Distritos
for i in range(len(distritos)):
    sql = 'INSERT INTO DISTRITO VALUES(%s)'
    values = (distritos[i],)
    cursor.execute(sql, values)
    connection.commit()
print('Se insertaron los distritos')

# Insertando información base: ComunaDistrito
for key in comunadistrito:
    sql = 'INSERT INTO COMUNADISTRITO VALUES(%s, %s)'
    values = (comunadistrito[key]['codigo_comuna'], comunadistrito[key]['codigo_distrito'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertaron comunadistritos')

# Leyendo csv
#tf = pd.read_csv('C://Users//Gerald//Documents//Proyecto Analítico//CENSO//Recursos//Microdato_Censo2017-Personas.csv', sep=';', chunksize=500000)

#Imprimiendo 500.000 filas por trozo

'''for chunk in tf:
    print(chunk)'''