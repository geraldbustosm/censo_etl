# CENSO 2017 ETL
Realización de un ETL (Extract, Transform and Load) a un archivo csv del CENSO 2017 desarrollado en Chile.

Puedes descargar los archivos desde este enlace:

https://drive.google.com/file/d/1GCFewugVvQeJdoolM-vIzNNSzJvRxmWJ/view?usp=sharing

Encontrarás 3 ficheros:

1. Microdato_Censo2017-Personas.csv
2. Manual-Usuario.pdf
3. codigos_region_provincia_comuna.pdf

El entendimiento de los datos se puede conocer a través del manual de usuario. Para una búsqueda más rápida y simple se adjunta este diccionario solo con las 48 columnas que se trabajaran dispuestas en el csv.

# Diccionario CENSO 2017

| Columna       | Descripción                                                  | Atributo                         | Rango                                        |
| ------------- | ------------------------------------------------------------ | -------------------------------- | -------------------------------------------- |
| REGION        | Región                                                       | codigo_region                    | 1 - 16                                       |
| PROVINCIA     | Provincia                                                    | codigo_provincia                 | 11 - 163                                     |
| COMUNA        | Comuna                                                       | codigo_comuna                    | 1101 - 16305                                 |
| DC            | Distrito                                                     | distrito                         | 1 - 99                                       |
| AREA          | Área                                                         | area                             | 1 ó 2                                        |
| ZC_LOC        | Zona/Localidad                                               | zona_localidad                   | 1 - 999                                      |
| ID_ZONA_LOC   | Identificador único de zona/ localidad                       | id_zonalocalidad                 | 1 - 16053                                    |
| NVIV          | Número de la vivienda                                        | nviv                             | 0 - 9999                                     |
| NHOGAR        | Número de hogar                                              | nhogar                           | 1 - 36                                       |
| PERSONAN      | Número de persona                                            | personan                         | 1 - 9999                                     |
| P07           | Relación de parentesco                                       | parentesco                       | 1 - 19                                       |
| P08           | Sexo                                                         | sexo                             | 1 ó 2                                        |
| P09           | Edad                                                         | edad                             | 0 - 100                                      |
| P10           | Residencia habitual                                          | residencia_habitual              | 1 - 4 *(98 No aplica, 99 Missing)*           |
| P10COMUNA     | Comuna de residencia habitual                                | comuna_residencia_habitual       | 997 - 15202 *(98 No aplica, 99 Missing)*     |
| P10PAIS       | País de residencia habitual                                  | pais_residencia_habitual         | 0 - 997 *(998 No aplica, 999 Missing)*       |
| P11           | Residencia hace 5 años                                       | residencia_hace_5años            | 1 - 9 *(98 No aplica, 99 Missing)*           |
| P11COMUNA     | Comuna de residencia hace 5 años                             | comuna_residencia_hace_5años     | 997 - 15202 *(98 No aplica, 99 Missing)*     |
| P11PAIS       | País de residencia hace 5 años                               | pais_residencia_hace_5años       | 0 - 997 *(998 No aplica, 999 Missing)*       |
| P12           | Lugar de nacimiento                                          | lugar_nacimiento                 | 1 - 8 *(98 No aplica, 99 Missing)*           |
| P12COMUNA     | Comuna de nacimiento                                         | comuna_nacimiento                | 997 - 15202 *(98 No aplica, 99 Missing)*     |
| P12PAIS       | País de nacimiento                                           | pais_nacimiento                  | 0 - 997 *(998 No aplica, 999 Missing)*       |
| P12A_LLEGADA  | Año de llegada al país                                       | llegada_pais                     | 1950 - 2017 *(9998 No aplica, 9999 Missing)* |
| P12A_TRAMO    | Período de llegada al país                                   | periodo_llegada_pais             | 1 - 4 *(98 No aplica, 99 Missing)*           |
| P13           | Asiste actualmente a la educación formal                     | estudia                          | 1 - 3 *(98 No aplica, 99 Missing)*           |
| P14           | Curso o año más alto aprobado                                | curso_mas_alto_aprobado          | 0 - 8 *(98 No aplica, 99 Missing)*           |
| P15           | Nivel del curso más alto aprobado                            | nivel_curso_mas_alto_aprobado    | 1 - 4 *(98 No aplica, 99 Missing)*           |
| P15A          | Completó el nivel especificado                               | completo_nivel                   | 1 ó 2 *(98 No aplica, 99 Missing)*           |
| P16           | Se considera perteneciente a un pueblo indígena u originario | pertenece_pueblo                 | 1 ó 2 *(98 No aplica, 99 Missing)*           |
| P16A          | Pueblo indígena u originario listado                         | pueblo_listado                   | 1 - 10 *(98 No aplica, 99 Missing)*          |
| P16A_OTRO     | Pueblo indígena u originario Otro                            | pueblo_otro                      | 1 - 97 *(98 No aplica, 99 Missing)*          |
| P17           | Trabajó durante la semana pasada                             | trabajo_semana_pasada            | 1 - 8 *(98 No aplica, 99 Missing)*           |
| P18           | Rama de actividad económica                                  | rama_actividad_economica         | A - Z *(98 No aplica, 99 Missing)*           |
| P19           | Total hijos/as nacidos vivos                                 | total_hijos_nacidos_vivos        | 0 - 23 *(98 No aplica, 99 Missing)*          |
| P20           | Total hijos/as actualmente vivos                             | total_hijos_actualmente_vivos    | 0 - 23 *(98 No aplica, 99 Missing)*          |
| P21M          | Mes de nacimiento del último/a hijo/a                        | mes_nacimiento_ultimo_hijo       | 1 - 12 *(98 No aplica, 99 Missing)*          |
| P21A          | Año de nacimiento del último/a hijo/a                        | año_nacimiento_ultimo_hijo       | 1890 - 2017 *(98 No aplica, 99 Missing)*     |
| P10PAIS_GRUPO | País de residencia habitual grupo                            | pais_recidencia_habitual_grupo   | 0 - 997 *(998 No aplica, 999 Missing)*       |
| P11PAIS_GRUPO | País de residencia hace 5 años grupo                         | pais_residencia_hace_5años_grupo | 0 - 997 *(998 No aplica, 999 Missing)*       |
| P12PAIS_GRUPO | País de nacimiento grupo                                     | pais_nacimiento_grupo            | 0 - 997 *(998 No aplica, 999 Missing)*       |
| ESCOLARIDAD   | Años de escolaridad                                          | escolaridad                      | 0 - 21 *(98 No aplica, 99 Missing)*          |
| P16A_GRUPO    | Pueblo indígena u originario grupo                           | pueblo_grupo                     | 1 - 10 *(98 No aplica, 99 Missing)*          |
| REGION_15R    | Códigos de una región entre 01 y 15                          | codigo_region15r                 | 1 - 15                                       |
| PROVINCIA_15R | Concatenación entre REGION15R y el código de la provincia    | codigo_provincia15r              | 11 - 152                                     |
| COMUNA_15R    | Concatenación entre PRONVICIA_15R y código de la comuna      | codigo_comuna15r                 | 1101 - 15202                                 |
| P10COMUNA_15R | *Comuna de residencia habitual a 15 regiones*                | comuna_residencia_habitual_15r   | 1101 - 15202                                 |
| P11COMUNA_15R | *Comuna de residencia hace 5 años a 15 regiones*             | comuna_residencia_hace_5años_15r | 1101 - 15202                                 |
| P12COMUNA_15R | *Comuna de nacimiento a 15 regiones*                         | comuna_nacimiento_15r            | 1101 - 15202                                 |
# Diagrama entidad-relación
![CENSO DER](https://raw.githubusercontent.com/geraldbustosm/censo_etl/master/censo.png)

# Modelo relacional

Region					(**<u>codigo_region</u>**, region, codigo_region15r)

Provincia				(<u>**codigo_provincia**</u>, provincia, codigo_provincia15r, *codigo_region*)

Comuna				 (**<u>codigo_comuna</u>**, comuna, codigo_comuna15r, *codigo_provincia*)

Distrito				   (**<u>codigo_distrito</u>**)

ComunaDistrito	(**<u>codigo_comuna,codigo_distrito</u>**)

ZonaLocalidad	  (**<u>id_zonalocalidad</u>**, zona_localidad, area, *codigo_comuna*)

Persona				 (**<u>id_zonalocalidad,nviv,nhogar,personan</u>**, atributos)

---

Entidad					(<u>**primary_key**</u>, atributo, *foreign_key*)

# Anotaciones
* Region15R mantiene el mismo código de región, sin embargo, para la región 16 se cambia a 8.

* Las comunas que comiencen con `16xxx` no serán almacenadas en la base de datos, puesto que estas ya están pero con otro código `08xxx`. Sin embargo, la almacenaremos en un diccionario para saber directamente el nombre de dicha comuna.

* Se decidió generar diccionarios y listas dentro del modulo *resources.py* para acceder fácilmente a ellos mediante clave : valor en nuestro script principal *censo.py*.

  Se agregó una columna extra que tuviese el nombre relacionado al código.
  
  Por ejemplo, en parentesco solo existe el código 1 pero no su descripción, por tanto se agregó la descripción quedando el diccionario de la siguiente forma:
  
  `{1 : 'Jefe/a de hogar'}`
  
  Esto se hizo de manera un tanto "manual" puesto que esa información no estaba contemplada en *Microdato-Censo2017.csv*, sino que en *Manual_Usuario.pdf*.
  
* Se decidió acceder una sola vez a *Microdato-Censo2017.csv*, con esto se obtuvieron las tuplas necesarias y únicas para cada tabla (utilizando drop_duplicates(), consiguiendo así evitar múltiples consultas a la base de datos para saber si un registro ya existía o no). 

* Se decidió no declarar las llaves foráneas de la tabla Persona, puesto que al recorrer *Microdato-Censo2017.csv* aún faltaban que se insertasen las tuplas de las demás tablas, estas tuplas tendrían los campos que iban a ser llaves foráneas de Persona. Por ende, veríamos un error en la tabla Persona que indicaría que la llave foránea de la tupla a insertar no existe en la otra tabla.

* Se decidió no eliminar duplicados para Persona, puesto que cada tupla de *Microdato-Censo2017.csv* representa una persona en la población censada (y por ende, son todas distintas). Por otra parte, el costo en memoria de concatenar 17 millones de tuplas y luego eliminar sus posibles duplicados se hace muy costoso, arrojando *Memory Error*. Es por esto que al recorrer el archivo, se va insertando inmediatamente en la tabla Persona.