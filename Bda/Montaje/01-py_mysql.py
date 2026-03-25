#!/usr/bin/env python3

# Instalar las librerías necesarias
"""
python -m venv pruebasBDs
source pruebasBDs/bin/activate 
pip install mysql-connector-python tqdm
"""
import random
import time
import mysql.connector
from tqdm import tqdm  

# Lista de 50 nombres españoles
nombres = [
    "Antonio", "Manuel", "José", "Francisco", "David", "Juan", "Javier", "Miguel", "Luis", "Carlos",
    "Pedro", "Rafael", "Jesús", "Miguel Ángel", "Sergio", "Daniel", "Alejandro", "Fernando", "Diego", "Pablo",
    "Adrián", "Jorge", "Iván", "Alberto", "Rubén", "Mario", "Víctor", "Raúl", "Guillermo", "Álvaro",
    "Óscar", "Hugo", "Marco", "Iker", "Samuel", "Emilio", "Esteban", "Andrés", "Joel", "Lucas",
    "Axel", "Marcos", "Leandro", "Kevin", "Bruno", "Ernesto", "Felipe", "Julián", "César", "Simón"
]

# Lista de 50 apellidos españoles
apellidos = [
    "García", "Martínez", "López", "Sánchez", "Pérez", "González", "Rodríguez", "Fernández", "Gómez", "Díaz",
    "Hernández", "Ruiz", "Jiménez", "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro",
    "Torres", "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Suárez", "Molina",
    "Morales", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Iglesias", "Núñez",
    "Medina", "Garrido", "Cortés", "Vidal", "Castillo", "Guerrero", "Esteban", "Vega", "Campos", "Méndez"
]


# Conexión a MySQL (asegúrate de que la BD de Docker esté levantada)
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root"
    ,autocommit=True  # Si forzamos commit en cada operación individual el tiempo se dispara 
)
cursor = conn.cursor()

# Crear la base de datos si no existe y usarla
cursor.execute("DROP DATABASE IF EXISTS personas_db")  # Limpiar la base de datos antes de empezar
cursor.execute("CREATE DATABASE IF NOT EXISTS personas_db")
cursor.execute("USE personas_db")

# Crear la tabla "personas" si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        apellido1 VARCHAR(100),
        apellido2 VARCHAR(100)
    )
""")

# Crear índices en cada uno de los campos
cursor.execute("CREATE INDEX idx_nombre ON personas (nombre)")
cursor.execute("CREATE INDEX idx_apellido1 ON personas (apellido1)")
cursor.execute("CREATE INDEX idx_apellido2 ON personas (apellido2)")

# Insertar las personas de una en una (sin optimización, para medir el tiempo individual)
# Número de personas a generar (para pruebas, puedes reducir este número)
n = 1*1000 # 1 millón de inserciones 
# Tomar el tiempo de inicio
start_time = time.time()
for _ in tqdm(range(n), 
              desc="Insertando personas", 
              bar_format="{desc} {bar} Tiempo estimado: {remaining}"):
    nombre = random.choice(nombres)
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)
    cursor.execute(
        "INSERT INTO personas (nombre, apellido1, apellido2) VALUES (%s, %s, %s)",
        (nombre, apellido1, apellido2)
    )
    # si usaramos autocommit=True, cada INSERT se confirma inmediatamente (y es mucho mas lento)

# Tomar el tiempo de finalización

end_time = time.time()
print(f"Tiempo transcurrido: {end_time - start_time:.2f} segundos")

# Cerrar cursor y conexión
cursor.close()
conn.close()
