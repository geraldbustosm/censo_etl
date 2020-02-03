import pandas as pd

# Paises, regiones, provincias, comunas, y pueblos se entregarán
# como clave -> valor para poder hallar más facilmente el nombre

class Resources:

    def __init__(self):
        tf = pd.read_csv('C://Users//Gerald//Documents//Proyecto Analítico//CENSO//Recursos//Microdato_Censo2017-Personas.csv', sep=';', chunksize=500000)
        # Dataframes a utilizar
        self.__comunadistrito = []
        self.__zonalocalidad = []
        self.__viviendas = []
        self.__hogar = []
        self.__personas = [] # Pbb no sea necesario eliminar duplicados xke no deberia

        # Se utiliza drop_duplicates() para eliminar tuplas que en ciertas 
        # columnas tengan todos sus datos repetidos, evitandonos asi
        # Realizar consultas una y otra vez a la bd para saber si ya existe un registro
        for chunk in tf:
            self.__comunadistrito.append(chunk[['COMUNA', 'DC']].drop_duplicates())
            self.__zonalocalidad.append(chunk[['ID_ZONA_LOC', 'ZC_LOC', 'AREA', 'DC']].drop_duplicates(subset=['ID_ZONA_LOC']))
            self.__viviendas.append(chunk[['ID_ZONA_LOC', 'NVIV']].drop_duplicates())
            self.__hogar.append(chunk[['ID_ZONA_LOC', 'NVIV', 'NHOGAR']].drop_duplicates())
            #self.personas.append(chunk[['']]).drop_duplicates()

        self.__comunadistrito = pd.concat(self.__comunadistrito).drop_duplicates()
        self.__zonalocalidad = pd.concat(self.__zonalocalidad).drop_duplicates(subset=['ID_ZONA_LOC'])
        self.__viviendas = pd.concat(self.__viviendas).drop_duplicates()
        self.__hogar = pd.concat(self.__hogar).drop_duplicates()
        #self.personas = pd.concat(self.personas).drop_duplicates()


    # Generando diccionarios a utilizar
    def paises(self):
        paises = {}
        df = pd.read_csv('paises.csv', sep=',')
        for i in range(len(df['codigo'])):
            paises[df['codigo'][i]] = {
                                    'codigo' : df['codigo'][i],
                                    'pais' : df['pais'][i],
                                    'codigo_grupo': df['codigo_grupo'][i],
                                    'grupo': df['grupo'][i]
                                        }
        return paises

    def regiones(self):
        regiones = {}
        df = pd.read_csv('regiones.csv', sep=',')
        for i in range(len(df['region'])):
            regiones[i] = {
                            'codigo_region' : df['codigo_region'][i].item(),
                            'region' : df['region'][i],
                            'codigo_region15r' : df['codigo_region15r'][i].item()
                        }
        return regiones

    def provincias(self):
        provincias = {}
        df = pd.read_csv('provincias.csv', sep=',')
        for i in range(len(df['provincia'])):
            provincias[i] = {
                                'codigo_provincia' : df['codigo_provincia'][i].item(),
                                'provincia' : df['provincia'][i],
                                'codigo_region' : df['codigo_region'][i].item()
                            }
        return provincias

    def comunas(self):
        comunas = {}
        df = pd.read_csv('comunas.csv', sep=',')
        for i in range(len(df['comuna'])):
            comunas[df['codigo_comuna'][i]] = {
                            'codigo_comuna' : df['codigo_comuna'][i].item(),
                            'comuna' : df['comuna'][i],
                            'codigo_provincia' : df['codigo_provincia'][i].item()
                        }
        return comunas

    def distritos(self):
        distritos = []
        for i in range(33):
            distritos.append(i+1)
        distritos.append(99)
        return distritos

    def pueblos(self):
        pueblos = {}
        df = pd.read_csv('pueblos.csv')
        for i in range(len(df['pueblo'])):
            pueblos[df['id'][i]] = {
                                    'id'     : df['id'][i].item(),
                                    'codigo' : df['codigo'][i].item(),
                                    'pueblo' : df['pueblo'][i],
                                    'listado': df['listado'][i]
            }
        return pueblos

    # Generando dataframes a utilizar

    def comunadistrito(self):
        return self.__comunadistrito
    def zonalocalidad(self):
        return self.__zonalocalidad
    def viviendas(self):
        return self.__viviendas
    def hogar(self):
        return self.__hogar
    def personas(self):
        return self.__personas

