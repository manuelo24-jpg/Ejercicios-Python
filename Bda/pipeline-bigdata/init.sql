USE gimnasio;

-- Tabla de dimensiones
CREATE TABLE IF NOT EXISTS dim_maquinas (
    id_maquina INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    tipo VARCHAR(30),
    zona VARCHAR(30),
    fabricante VARCHAR(50)
);

-- Tabla de hechos
CREATE TABLE IF NOT EXISTS fact_uso (
    id_uso INT PRIMARY KEY AUTO_INCREMENT,
    id_maquina INT,
    duracion_min FLOAT,
    calorias FLOAT,
    frecuencia_cardiaca INT,
    timestamp DATETIME,
    FOREIGN KEY (id_maquina) REFERENCES dim_maquinas(id_maquina)
);

-- Datos iniciales de máquinas
INSERT INTO dim_maquinas (nombre, tipo, zona, fabricante) VALUES
('Cinta 1',        'Cardio',     'Planta Baja', 'Technogym'),
('Cinta 2',        'Cardio',     'Planta Baja', 'Life Fitness'),
('Bici 1',         'Cardio',     'Planta Baja', 'Technogym'),
('Bici 2',         'Cardio',     'Primera',     'Precor'),
('Elíptica 1',     'Cardio',     'Primera',     'Life Fitness'),
('Press Banca',    'Fuerza',     'Primera',     'Hammer Strength'),
('Sentadillas',    'Fuerza',     'Primera',     'Hammer Strength'),
('Remo',           'Fuerza',     'Segunda',     'Technogym'),
('TRX',            'Funcional',  'Segunda',     'TRX'),
('Battle Ropes',   'Funcional',  'Segunda',     'Escape Fitness');