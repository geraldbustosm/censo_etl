import pandas as pd

def lista_paises():
    paises = {}
    df = pd.read_csv('paises.csv', sep=',')
    for i in range(len(df['codigo'])):
        paises[df['codigo'][i]] =   {
                                    'pais':df['pais'][i],
                                    'codigo_grupo': df['codigo_grupo'][i],
                                    'grupo': df['grupo'][i]
                                    }
    return paises

def lista_pueblos():
    pueblos = {}
    df = pd.read_csv('pueblos.csv')
    for i in range(len(df['pueblo'])):
        pueblos[df['id'][i]] = {
                                'codigo' : df['codigo'][i],
                                'pueblo' : df['pueblo'][i],
                                'listado': df['listado'][i]
        }
    return pueblos

def lista_comunas():
    comunas = {}
    df = pd.read_csv('comunas.csv', sep=',')
    for i in range(len(df['comuna'])):
        comunas[df['codigo_comuna'][i]] = {
                                        'comuna' : df['comuna'][i],
                                        'codigo_provincia' : df['codigo_provincia'][i]
                                        }
    return comunas

def lista_provincias():
    pass

def lista_regiones():
    pass