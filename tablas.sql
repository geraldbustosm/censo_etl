CREATE TABLE region(
    codigo_region INTEGER PRIMARY KEY,
    region VARCHAR(50),
    codigo_region15r INTEGER
);

CREATE TABLE provincia(
    codigo_provincia INTEGER PRIMARY KEY,
    provincia VARCHAR(50),
    codigo_provincia15r INTEGER,
    codigo_region INTEGER,
    FOREIGN KEY (codigo_region) REFERENCES region(codigo_region)
);

CREATE TABLE distrito(
    codigo_distrito INTEGER PRIMARY KEY
);

CREATE TABLE comuna(
    codigo_comuna INTEGER PRIMARY KEY,
    comuna VARCHAR(50),
    codigo_comuna15r INTEGER,
    codigo_provincia INTEGER,
    FOREIGN KEY (codigo_provincia) REFERENCES provincia(codigo_provincia)
);

CREATE TABLE comunadistrito(
    codigo_comuna INTEGER,
    codigo_distrito INTEGER,
    PRIMARY KEY (codigo_comuna, codigo_distrito)
);

CREATE TABLE zonalocalidad(
    id_zonalocalidad INTEGER PRIMARY KEY,
    zona_localidad INTEGER,
    codigo_distrito INTEGER,
    area INTEGER,
    FOREIGN KEY (codigo_distrito) REFERENCES distrito(codigo_distrito)
);

CREATE TABLE vivienda(
    id_zonalocalidad INTEGER,
    nviv INTEGER,
    PRIMARY KEY (id_zonalocalidad, nviv),
    FOREIGN KEY (id_zonalocalidad) REFERENCES zonalocalidad(id_zonalocalidad)
);

CREATE TABLE hogar(
    id_zonalocalidad INTEGER,
    nviv INTEGER,
    nhogar INTEGER,
    PRIMARY KEY (id_zonalocalidad, nviv, nhogar),
    FOREIGN KEY (id_zonalocalidad, nviv) REFERENCES vivienda(id_zonalocalidad, nviv)
);

CREATE TABLE persona(
    id_zonalocalidad INTEGER,
    nviv INTEGER,
    nhogar INTEGER,
    personan INTEGER,
    parentesco VARCHAR(50),
    sexo VARCHAR(50),
    edad INTEGER,
    residencia_habitual VARCHAR(50),
    comuna_residencia_habitual VARCHAR(50),
    pais_residencia_habitual VARCHAR(50),
    residencia_hace_5años VARCHAR(50),
    comuna_residencia_hace_5años VARCHAR(50),
    pais_residencia_hace_5años VARCHAR(50),
    lugar_nacimiento VARCHAR(50),
    comuna_nacimiento VARCHAR(50),
    pais_nacimiento VARCHAR(50),
    llegada_pais INTEGER,
    periodo_llegada_pais VARCHAR(50),
    estudia VARCHAR(50),
    curso_mas_alto_aprobado INTEGER,
    nivel_curso_mas_alto_aprobado VARCHAR(50),
    completo_nivel VARCHAR(50),
    pertenece_pueblo VARCHAR(50),
    pueblo_listado VARCHAR(50),
    pueblo_otro VARCHAR(50),
    trabajo_semana_pasada VARCHAR(50),
    rama_actividad_economica VARCHAR(50),
    total_hijos_nacidos_vivos INTEGER,
    mes_nacimiento_ultimo_hijo VARCHAR(50),
    año_nacimiento_ultimo_hijo INTEGER,
    pais_residencia_habitual_grupo VARCHAR(50),
    pais_residencia_hace_5años_grupo VARCHAR(50),
    pais_nacimiento_grupo VARCHAR(50),
    escolaridad INTEGER,
    pueblo_grupo VARCHAR(50),
    comuna_residencia_habitual_15r VARCHAR(50),
    comuna_residencia_hace_5años_15r VARCHAR(50),
    comuna_nacimiento_15r VARCHAR(50),
    PRIMARY KEY (id_zonalocalidad, nviv, nhogar, personan),
    FOREIGN KEY (id_zonalocalidad, nviv, nhogar) REFERENCES hogar(id_zonalocalidad,nviv,nhogar)
);