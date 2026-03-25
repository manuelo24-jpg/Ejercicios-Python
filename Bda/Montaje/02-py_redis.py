#!/usr/bin/env python3

# Instalar las librerías necesarias
"""
source pruebasBDs/bin/activate   ## (si no existe el entorno: pyhton -m venv pruebasBDs)
pip install redis
"""

import redis
import random
import time
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

# Conexión a Redis
client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Insertar las personas de una en una (sin optimización, para medir el tiempo individual)
# Número de personas a generar (para pruebas, puedes reducir este número)
n = 1000*1000 # 1 millón de inserciones (cada una en una transacción)
# Tomar el tiempo de inicio
start_time = time.time()
for i in tqdm(range(n), 
              desc="Insertando personas", 
              bar_format="{desc} {bar} Tiempo estimado: {remaining}"):
    nombre = random.choice(nombres)
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)

    row_key = f"persona_{i}"

    client.set(str(row_key), str({
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2
    }).encode('utf-8'))

# Tomar el tiempo de finalización
end_time = time.time()
print(f"Tiempo transcurrido: {end_time - start_time:.2f} segundos")

