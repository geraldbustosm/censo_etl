CREATE TABLE region(
    codigo_region INTEGER PRIMARY KEY,
    region VARCHAR(255),
    codigo_region15r INTEGER
);

CREATE TABLE provincia(
    codigo_provincia INTEGER PRIMARY KEY,
    provincia VARCHAR(255),
    codigo_provincia15r INTEGER,
    codigo_region INTEGER,
    FOREIGN KEY (codigo_region) REFERENCES region(codigo_region)
);

CREATE TABLE distrito(
    codigo_distrito INTEGER PRIMARY KEY
);

CREATE TABLE comuna(
    codigo_comuna INTEGER PRIMARY KEY,
    comuna VARCHAR(255),
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

CREATE TABLE persona(
    id_zonalocalidad INTEGER,
    nviv INTEGER,
    nhogar INTEGER,
    personan INTEGER,
    parentesco VARCHAR(255),
    sexo VARCHAR(255),
    edad INTEGER,
    residencia_habitual VARCHAR(255),
    comuna_residencia_habitual VARCHAR(255),
    pais_residencia_habitual VARCHAR(255),
    residencia_hace_5años VARCHAR(255),
    comuna_residencia_hace_5años VARCHAR(255),
    pais_residencia_hace_5años VARCHAR(255),
    lugar_nacimiento VARCHAR(255),
    comuna_nacimiento VARCHAR(255),
    pais_nacimiento VARCHAR(255),
    llegada_pais INTEGER,
    periodo_llegada_pais VARCHAR(255),
    estudia VARCHAR(255),
    curso_mas_alto_aprobado INTEGER,
    nivel_curso_mas_alto_aprobado VARCHAR(255),
    completo_nivel VARCHAR(255),
    pertenece_pueblo VARCHAR(255),
    pueblo_listado VARCHAR(255),
    pueblo_otro VARCHAR(255),
    trabajo_semana_pasada VARCHAR(255),
    rama_actividad_economica VARCHAR(255),
    total_hijos_nacidos_vivos INTEGER,
    total_hijos_actualmente_vivos INTEGER,
    mes_nacimiento_ultimo_hijo VARCHAR(255),
    año_nacimiento_ultimo_hijo INTEGER,
    pais_residencia_habitual_grupo VARCHAR(255),
    pais_residencia_hace_5años_grupo VARCHAR(255),
    pais_nacimiento_grupo VARCHAR(255),
    escolaridad INTEGER,
    pueblo_grupo VARCHAR(255),
    comuna_residencia_habitual_15r VARCHAR(255),
    comuna_residencia_hace_5años_15r VARCHAR(255),
    comuna_nacimiento_15r VARCHAR(255),
    PRIMARY KEY (id_zonalocalidad, nviv, nhogar, personan)
    --FOREIGN KEY (id_zonalocalidad) REFERENCES zonalocalidad(id_zonalocalidad)
);