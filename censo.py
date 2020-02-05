import resources as rs
import psycopg2 as pg
import pandas as pd

# Información base
paises = rs.paises()
regiones = rs.regiones()
provincias = rs.provincias()
comunas = rs.comunas()
distritos = rs.distritos()
pueblo_listado = rs.pueblo_listado()
pueblo_otro = rs.pueblo_otro()
parentesco = rs.parentesco()
sexo = rs.sexo()
residencia_habitual = rs.residencia_habitual()
residencia_hace_5años = rs.residencia_hace_5años()
lugar_nacimiento = rs.lugar_nacimiento()
periodo_llegada = rs.periodo_llegada()
respuesta_booleana = rs.respuesta_booleana()
nivel_curso_mas_alto_aprobado = rs.nivel_curso_mas_alto_aprobado()
trabajo_semana_pasada = rs.trabajo_semana_pasada()

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

print("- Comienza el recorrido de Microdato-Censo2017.csv ⏳")

for chunk in tf:
    comunadistrito.append(chunk[['COMUNA', 'DC']].drop_duplicates())
    zonalocalidad.append(chunk[['ID_ZONA_LOC', 'ZC_LOC', 'AREA', 'DC']].drop_duplicates(subset=['ID_ZONA_LOC']))
    viviendas.append(chunk[['ID_ZONA_LOC', 'NVIV']].drop_duplicates())
    hogar.append(chunk[['ID_ZONA_LOC', 'NVIV', 'NHOGAR']].drop_duplicates())

    print('trozo')
    for index, row in chunk.iterrows():
        sql = 'INSERT INTO PERSONA VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (row['ID_ZONA_LOC'].item(), row['NVIV'].item(), row['NHOGAR'].item(), row['PERSONAN'].item(), parentesco[row['P07'].item()], sexo[row['P08'].item()], row['P09'].item(), residencia_habitual[row['P10'].item()], comunas[row['P10COMUNA'].item()], paises[row['P10PAIS'].item()], residencia_hace_5años[row['P11'].item()], comunas[row['P11COMUNA'].item()], paises[row['P11PAIS'].item()], lugar_nacimiento[row['P12'].item()], comunas[row['P12COMUNA'].item()], paises[row['P12PAIS'].item()], row['P12A_LLEGADA'], periodo_llegada[row['P12A_TRAMO'].item()], estudia[row['P13'].item()], row['P14'], nivel_curso_mas_alto_aprobado[row['P15'].item()], respuesta_booleana[row['P15A'].item()], respuesta_booleana[row['P16'].item()], pueblo_listado[row['P16A'].item()], pueblo_otro[row['P16A_OTRO'].item()], trabajo_semana_pasada[row['P17'].item()], row['P18'], row['P19'], row['P20'], row['P21M'], row['P21A'], paises[row['P10PAIS_GRUPO'].item()], paises[row['P11PAIS_GRUPO'].item()], paises[row['P12PAIS_GRUPO'].item()], row['ESCOLARIDAD'], pueblo_listado[row['P16A_GRUPO'].item()], comunas[row['P10COMUNA_15R'].item()], comunas[row['P11COMUNA_15R'].item()], comunas[row['P12COMUNA_15R'].item()])
        cursor.execute(sql, values)
        connection.commit()

print('-- Se insertaron todas las tuplas en la tabla Persona 🕺')

# Se concatenan los dataframes almacenados en el arreglo y se vuelven a eliminar los duplicados
comunadistrito = pd.concat(comunadistrito).drop_duplicates()
zonalocalidad = pd.concat(zonalocalidad).drop_duplicates(subset=['ID_ZONA_LOC'])
viviendas = pd.concat(viviendas).drop_duplicates()
hogar = pd.concat(hogar).drop_duplicates()

print('-Comienza la inserción en el resto de tablas ⏳')

# Insertando información base: Regiones
for key in regiones:
    sql = 'INSERT INTO REGION VALUES(%s, %s, %s)'
    values = (key, regiones[key]['region'], regiones[key]['codigo_region15r'])
    cursor.execute(sql,values)
    connection.commit()
print('-- Se insertó en region 🗾')

# Insertando información base: Provincias
for key in provincias:
    sql = 'INSERT INTO PROVINCIA VALUES(%s, %s, %s, %s)'
    values = (key, provincias[key]['provincia'], key, provincias[key]['codigo_region'])
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en provincia 🌄')

# Insertando información base: Comunas
for key in comunas:
    if(comunas[key]['codigo_provincia'] == 99): break
    sql = 'INSERT INTO COMUNA VALUES(%s, %s, %s, %s)'
    values = (key, comunas[key]['comuna'], key, comunas[key]['codigo_provincia'])
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en comuna 🗿')

# Insertando información base: Distritos
for i in range(len(distritos)):
    sql = 'INSERT INTO DISTRITO VALUES(%s)'
    values = (distritos[i],)
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en distrito 📃')

# Insertando información base: ComunaDistrito
for index, row in comunadistrito.iterrows():
    sql = 'INSERT INTO COMUNADISTRITO VALUES(%s, %s)'
    values = (row['COMUNA'].item(), row['DC'].item())
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en comunadistritos 🌞')

# Insertando información base: ZonaLocalidad
for index, row in zonalocalidad.iterrows():
    sql = 'INSERT INTO ZONALOCALIDAD VALUES(%s, %s, %s, %s)'
    values = (row['ID_ZONA_LOC'].item(), row['ZC_LOC'].item(), row['DC'].item(), row['AREA'].item())
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en zonalocalidad 🌎')

# Insertando información base: Viviendas
for index, row in viviendas.iterrows():
    sql = 'INSERT INTO VIVIENDA VALUES(%s, %s)'
    values = (row['ID_ZONA_LOC'].item(), row['NVIV'].item())
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en vivienda 🏠')

# Insertando información base: Hogar
for index, row in hogar.iterrows():
    sql = 'INSERT INTO HOGAR(%s, %s, %s)'
    values = (row['ID_ZONA_LOC'].item(), row['NVIV'].item(), row['NHOGAR'].item())
    cursor.execute(sql, values)
    connection.commit()
print('-- Se inserto en hogar 💗')