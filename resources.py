import pandas as pd

# Paises, regiones, provincias, comunas, y pueblos se entregarán
# como clave -> valor para poder hallar más facilmente el nombre

def paises():
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

def comunas():
    comunas = {}
    df = pd.read_csv('comunas.csv', sep=',')
    for i in range(len(df['comuna'])):
        comunas[df['codigo_comuna'][i]] = {
                        'codigo_comuna' : df['codigo_comuna'][i].item(),
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

def pueblos():
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