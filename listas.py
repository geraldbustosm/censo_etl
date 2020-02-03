import pandas as pd

# Lista de paises, comunas y pueblos se entregarán como clave -> valor
# para poder hallar más facilmente el nombre del pais, comuna o pueblo
# antes de insertarlo a la base de datos, evitando asi realizar multiples querys

# Para las demas listas no es necesario clave -> valor, 
# pues se recorreran normalmente mediante su iteración ya que estas
# si deben estar en la base de datos con su código.

def paises():
    paises = {}
    df = pd.read_csv('paises.csv', sep=',')
    for i in range(len(df['codigo'])):
        paises[df['codigo'][i]] =   {
                                    'pais':df['pais'][i],
                                    'codigo_grupo': df['codigo_grupo'][i],
                                    'grupo': df['grupo'][i]
                                    }
    return paises

def pueblos():
    pueblos = {}
    df = pd.read_csv('pueblos.csv')
    for i in range(len(df['pueblo'])):
        pueblos[df['id'][i]] = {
                                'codigo' : df['codigo'][i],
                                'pueblo' : df['pueblo'][i],
                                'listado': df['listado'][i]
        }
    return pueblos

def comunas():
    comunas = {}
    df = pd.read_csv('comunas.csv', sep=',')
    for i in range(len(df['comuna'])):
        comunas[df['codigo_comuna'][i]] = {
                        'comuna' : df['comuna'][i],
                        'codigo_provincia' : df['codigo_provincia'][i].item()
                    }
    return comunas

def distritos():
    distritos = []
    for i in range(33):
        distritos.append(i+1)
    distritos.append(99)
    return distritos

def comunadistrito():
    comunadistrito = {}
    df = pd.read_csv('comunadistrito.csv')
    for i in range(len(df['codigo_comuna'])):
        comunadistrito[i] = {
                            'codigo_comuna' : df['codigo_comuna'][i],
                            'codigo_distrito' : df['codigo_distrito'][i]
        }
    return comunadistrito

def provincias():
    provincias = {}
    df = pd.read_csv('provincias.csv', sep=',')
    for i in range(len(df['provincia'])):
        provincias[i] = {
                            'codigo_provincia' : df['codigo_provincia'][i].item(),
                            'provincia' : df['provincia'][i],
                            'codigo_region' : df['codigo_region'][i].item()
                        }
    return provincias

def regiones():
    regiones = {}
    df = pd.read_csv('regiones.csv', sep=',')
    for i in range(len(df['region'])):
        regiones[i] = {
                        'codigo_region' : df['codigo_region'][i].item(),
                        'region' : df['region'][i],
                        'codigo_region15r' : df['codigo_region15r'][i].item()
                    }
    return regiones