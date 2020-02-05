import resources as rs
import psycopg2 as pg
import pandas as pd

# Información base
paises = rs.paises()
regiones = rs.regiones()
provincias = rs.provincias()
comunas = rs.comunas()
distritos = rs.distritos()
pueblos = rs.pueblos()

# Estableciendo conexión a la base de datos
connection = pg.connect(host = 'localhost', user = 'postgres', database = 'censo', password = 'hola123a')
cursor = connection.cursor()

# Lectura del archivo en porciones, con una cantidad definida de filas (chunksize) por trozo
chunksize = 500000
tf = pd.read_csv('C://Users//Gerald//Documents//Proyecto Analítico//CENSO//Recursos//Microdato_Censo2017-Personas.csv', sep=';', chunksize=chunksize)

# Arreglos para almacenar en cada item un chunk sin duplicados (dataframe)
comunadistrito = []
zonalocalidad = []
viviendas = []
hogar = []

# Recorrido del archivo con obtención de tuplas únicas (utilizando drop_duplicates) según lo que necesite cada tabla.
# Estas serán utilizadas posteriormente para insertarse.
# Al recorrer Microdato-Censo2017.csv, se insertará unicamente tuplas en la tabla Personas.

print("Comienza el recorrido de Microdato-Censo2017.csv ⏳")

for chunk in tf:
    comunadistrito.append(chunk[['COMUNA', 'DC']].drop_duplicates())
    zonalocalidad.append(chunk[['ID_ZONA_LOC', 'ZC_LOC', 'AREA', 'DC']].drop_duplicates(subset=['ID_ZONA_LOC']))
    viviendas.append(chunk[['ID_ZONA_LOC', 'NVIV']].drop_duplicates())
    hogar.append(chunk[['ID_ZONA_LOC', 'NVIV', 'NHOGAR']].drop_duplicates())

    for index, row in chunk.iterrows():
        sql = 'INSERT INTO PERSONA VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (row['ID_ZONA_LOC'], row['NVIV'], row['NHOGAR'], row['PERSONAN'], row['P07'], row['P08'], row['P09'], row['P10'], row['P10COMUNA'], row['P10PAIS'], row['P11'], row['P11COMUNA'], row['P11PAIS'], row['P12'], row['P12COMUNA'], row['P12PAIS'], row['P12A_LLEGADA'], row['P12A_TRAMO'], row['P13'], row['P14'], row['P15'], row['P15A'], row['P16'], row['P16A'], row['P16A_OTRO'], row['P17'], row['P18'], row['P19'], row['P20'], row['P21M'], row['P21A'], row['P10PAIS_GRUPO'], row['P11PAIS_GRUPO'], row['P12PAIS_GRUPO'], row['ESCOLARIDAD'], row['P16A_GRUPO'], row['P10COMUNA_15R'], row['P11COMUNA_15R'], row['P12COMUNA_15R'])
        cursor.execute(sql, values)
        connection.commit()

print('Se insertaron todas las tuplas en la tabla Persona 🕺')

# Se concatenan los dataframes almacenados en el arreglo y se vuelven a eliminar los duplicados
comunadistrito = pd.concat(comunadistrito).drop_duplicates()
zonalocalidad = pd.concat(zonalocalidad).drop_duplicates(subset=['ID_ZONA_LOC'])
viviendas = pd.concat(viviendas).drop_duplicates()
hogar = pd.concat(hogar).drop_duplicates()

print('Comienza la inserción en el resto de tablas ⏳')

# Insertando información base: Regiones
for key in regiones:
    sql = 'INSERT INTO REGION VALUES(%s, %s, %s)'
    values = (regiones[key]['codigo_region'], regiones[key]['region'], regiones[key]['codigo_region15r'])
    cursor.execute(sql,values)
    connection.commit()
print('Se insertó en region 🗾')

# Insertando información base: Provincias
for key in provincias:
    sql = 'INSERT INTO PROVINCIA VALUES(%s, %s, %s, %s)'
    values = (provincias[key]['codigo_provincia'], provincias[key]['provincia'], provincias[key]['codigo_provincia'], provincias[key]['codigo_region'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en provincia 🌄')

# Insertando información base: Comunas
for key in comunas:
    sql = 'INSERT INTO COMUNA VALUES(%s, %s, %s, %s)'
    values = (comunas[key]['codigo_comuna'], comunas[key]['comuna'], comunas[key]['codigo_comuna'], comunas[key]['codigo_provincia'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en comuna 🗿')

# Insertando información base: Distritos
for i in range(len(distritos)):
    sql = 'INSERT INTO DISTRITO VALUES(%s)'
    values = (distritos[i],)
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en distrito 📃')

# Insertando información base: ComunaDistrito
for index, row in comunadistrito.iterrows():
    sql = 'INSERT INTO COMUNADISTRITO VALUES(%s, %s)'
    values = (row['COMUNA'], row['DC'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en comunadistritos 🌞')

# Insertando información base: ZonaLocalidad
for index, row in zonalocalidad.iterrows():
    sql = 'INSERT INTO ZONALOCALIDAD VALUES(%s, %s, %s, %s)'
    values = (zonalocalidad[key]['id_zonalocalidad'], zonalocalidad[key]['zona_localidad'], zonalocalidad[key]['codigo_distrito'], zonalocalidad[key]['area'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en zonalocalidad 🌎')

# Insertando información base: Viviendas
for index, row in viviendas.iterrows():
    sql = 'INSERT INTO VIVIENDA VALUES(%s, %s)'
    values = (row['ID_ZONA_LOC'].item(), row['NVIV'].item())
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en vivienda 🏠')

# Insertando información base: Hogar
for index, row in hogar.iterrows():
    sql = 'INSERT INTO HOGAR(%s, %s, %s)'
    values = (row['ID_ZONA_LOC'].item(), row['NVIV'].item(), row['NHOGAR'].item())
    cursor.execute(sql, values)
    connection.commit()
print('Se inserto en hogar 💗')