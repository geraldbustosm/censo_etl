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
estudia = rs.estudia()
respuesta_booleana = rs.respuesta_booleana()
nivel_curso_mas_alto_aprobado = rs.nivel_curso_mas_alto_aprobado()
trabajo_semana_pasada = rs.trabajo_semana_pasada()
rama_actividad_economica = rs.rama_actividad_economica()

# Estableciendo conexión a la base de datos
connection = pg.connect(host = 'localhost', user = 'postgres', database = 'censo', password = 'hola123a')
cursor = connection.cursor()

# Lectura del archivo en porciones, con una cantidad definida de filas (chunksize) por trozo
chunksize = 500000
tf = pd.read_csv('C://Users//Gerald//Documents//Proyecto Analítico//CENSO//Recursos//Microdato_Censo2017-Personas.csv', sep=';', chunksize=chunksize)

# Arreglos para almacenar en cada item un chunk sin duplicados (dataframe)
comunadistrito = []
zonalocalidad = []

# Recorrido del archivo con obtención de tuplas únicas (utilizando drop_duplicates) según lo que necesite cada tabla.
# Estas serán utilizadas posteriormente para insertarse.
# Al recorrer Microdato-Censo2017.csv, se insertará unicamente tuplas en la tabla Personas.

print("- Comienza el recorrido de Microdato-Censo2017.csv ⏳")

for chunk in tf:
    comunadistrito.append(chunk[['COMUNA', 'DC']].drop_duplicates())
    zonalocalidad.append(chunk[['ID_ZONA_LOC', 'ZC_LOC', 'AREA', 'DC']].drop_duplicates(subset=['ID_ZONA_LOC']))

    for index, row in chunk.iterrows():
        sql = 'INSERT INTO PERSONA VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (row['ID_ZONA_LOC'], row['NVIV'], row['NHOGAR'], row['PERSONAN'], parentesco[row['P07']], sexo[row['P08']], row['P09'], residencia_habitual[row['P10']], comunas[row['P10COMUNA']]['comuna'], paises[row['P10PAIS']], residencia_hace_5años[row['P11']], comunas[row['P11COMUNA']]['comuna'], paises[row['P11PAIS']], lugar_nacimiento[row['P12']], comunas[row['P12COMUNA']]['comuna'], paises[row['P12PAIS']], row['P12A_LLEGADA'], periodo_llegada[row['P12A_TRAMO']], estudia[row['P13']], row['P14'], nivel_curso_mas_alto_aprobado[row['P15']], respuesta_booleana[row['P15A']], respuesta_booleana[row['P16']], pueblo_listado[row['P16A']], pueblo_otro[row['P16A_OTRO']], trabajo_semana_pasada[row['P17']], rama_actividad_economica[row['P18']], row['P19'], row['P20'], row['P21M'], row['P21A'], paises[row['P10PAIS_GRUPO']], paises[row['P11PAIS_GRUPO']], paises[row['P12PAIS_GRUPO']], row['ESCOLARIDAD'], pueblo_listado[row['P16A_GRUPO']], comunas[row['P10COMUNA_15R']]['comuna'], comunas[row['P11COMUNA_15R']]['comuna'], comunas[row['P12COMUNA_15R']]['comuna'])
        cursor.execute(sql, values)
        connection.commit()

print('-- Se insertó persona 🕺')

# Se concatenan los dataframes almacenados en el arreglo y se vuelven a eliminar los duplicados
comunadistrito = pd.concat(comunadistrito).drop_duplicates()
zonalocalidad = pd.concat(zonalocalidad).drop_duplicates(subset=['ID_ZONA_LOC'])

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
    if(key== 98): break
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
print('Se van a insertar ', zonalocalidad)
for index, row in zonalocalidad.iterrows():
    sql = 'INSERT INTO ZONALOCALIDAD VALUES(%s, %s, %s, %s)'
    values = (row['ID_ZONA_LOC'].item(), row['ZC_LOC'].item(), row['DC'].item(), row['AREA'].item())
    cursor.execute(sql, values)
    connection.commit()
print('-- Se insertó en zonalocalidad 🌎')