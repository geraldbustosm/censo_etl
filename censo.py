from resources import Resources
import psycopg2 as pg
import pandas as pd


# Información base
rs = Resources()
paises = rs.paises()
regiones = rs.regiones()
provincias = rs.provincias()
comunas = rs.comunas()
distritos = rs.distritos()
comunadistrito = rs.comunadistrito()
zonalocalidad = rs.zonalocalidad()
viviendas = rs.viviendas()
hogar = rs.hogar()
personas = rs.personas()
pueblos = rs.pueblos()

# Estableciendo conexión a la base de datos
connection = pg.connect(host = 'localhost', user = 'postgres', database = 'censo', password = 'hola123a')
cursor = connection.cursor()

'''

# Insertando informaión base: Regiones
for key in regiones:
    sql = 'INSERT INTO REGION VALUES(%s, %s, %s)'
    values = (regiones[key]['codigo_region'], regiones[key]['region'], regiones[key]['codigo_region15r'])
    cursor.execute(sql,values)
    connection.commit()
print('Se insertó en regiones 🗾')

# Insertando información base: Provincias
for key in provincias:
    sql = 'INSERT INTO PROVINCIA VALUES(%s, %s, %s, %s)'
    values = (provincias[key]['codigo_provincia'], provincias[key]['provincia'], provincias[key]['codigo_provincia'], provincias[key]['codigo_region'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en provincias 🌄')

# Insertando información base: Comunas
for key in comunas:
    sql = 'INSERT INTO COMUNA VALUES(%s, %s, %s, %s)'
    values = (comunas[key]['codigo_comuna'], comunas[key]['comuna'], comunas[key]['codigo_comuna'], comunas[key]['codigo_provincia'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en comunas 🗿')

# Insertando información base: Distritos
for i in range(len(distritos)):
    sql = 'INSERT INTO DISTRITO VALUES(%s)'
    values = (distritos[i],)
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en distritos 📃')

# Insertando información base: ComunaDistrito
for key in comunadistrito:
    sql = 'INSERT INTO COMUNADISTRITO VALUES(%s, %s)'
    values = (comunadistrito[key]['codigo_comuna'], comunadistrito[key]['codigo_distrito'])
    cursor.execute(sql, values)
    connection.commit()
print('Se insertó en comunadistritos 🌞')

# Insertando información base: ZonaLocalidad
for key in zonalocalidad:
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
print('Se insertó en viviendas 🏠')

# Leyendo csv
tf = pd.read_csv('C://Users//Gerald//Documents//Proyecto Analítico//CENSO//Recursos//Microdato_Censo2017-Personas.csv', sep=';', chunksize=500000)

#Imprimiendo 500.000 filas por trozo
for chunk in tf:
    for index, row in chunk.iterrows():
        # Variables a utilizar
        id_zonalocalidad = row['ID_ZONA_LOC']
        zona_localidad = row['ZC_LOC']
        area = row['AREA']
        codigo_distrito = row['DC']
        nviv = row['NVIV']
        nhogar = row['NHOGAR']
        personan = row['PERSONAN']
        parentesco = row['P07']
        sexo = row['P08']
        edad = row['P09']
        residencia_habitual = row['P10']
        comuna_residencia_habitual = row['P10COMUNA']
        pais_residencia_habitual = row['P10PAIS']
        residencia_hace_5años = row['P11']
        comuna_residencia_hace_5años = row['P11COMUNA']
        pais_residencia_hace_5años = row['P11PAIS']
        lugar_nacimiento = row['P12']
        comuna_nacimiento = row['P12COMUNA']
        pais_nacimiento = row['P12PAIS']
        llegada_pais = row['P12A_LLEGADA']
        periodo_llegada_pais = row['P12A_TRAMO']
        estudia = row['P13']
        curso_mas_alto_aprobado = row['P14']
        nivel_curso_mas_alto_aprobado = row['P15']
        completo_nivel = row['P15A']
        pertenece_pueblo = row['P16']
        pueblo_listado = row['P16A']
        pueblo_otro = row['P16A_OTRO']
        trabajo_semana_pasada = row['P17']
        rama_actividad_economica = row['P18']
        total_hijos_nacidos_vivos = row['P19']
        total_hjos_actualmente_vivos = row['P20']
        mes_nacimiento_ultimo_hijo = row['P21M']
        año_nacimiento_ultimo_hijo = row['P21A']
        pais_residencia_habitual_grupo = row['P10PAIS_GRUPO']
        pais_residencia_habitual_grupo = row['P11PAIS_GRUPO']
        pais_nacimiento_grupo = row['P12PAIS_GRUPO']
        escolaridad = row['ESCOLARIDAD']
        pueblo_grupo = row['P16A_GRUPO']
        comuna_residencia_habitual_15r = row['P10COMUNA_15R']
        comuna_residencia_hace_5años_15r = row['P11COMUNA_15R']
        comuna_nacimiento_15r = row['P12COMUNA_15R']

        # Inserción ZonaLocalidad
        sql = 'SELECT COUNT(*) FROM ZONALOCALIDAD WHERE id_zonalocalidad = %s'
        values = (id_zonalocalidad,)
        cursor.execute(sql, values)
        result = cursor.fetchone()

        if(result[0] == 0):
            sql = 'INSERT INTO ZONALOCALIDAD VALUES(%s, %s, %s, %s)'
            values = (id_zonalocalidad, zona_localidad, area, codigo_distrito)
            cursor.execute(sql, values)
            connection.commit()
        print('Se insertaron zonalocalidad 🛶')

        # Inserción Vivienda
        #sql = 'INSERT INTO VIVIENDA VALUES(%s, %s)'
        #values = (id_zonalocalidad, nviv)
        # Inserción Hogar
        
        # Inserción Persona'''