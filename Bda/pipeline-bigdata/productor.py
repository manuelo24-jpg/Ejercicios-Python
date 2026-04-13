import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

# Conexión al broker de Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# IDs de máquinas disponibles (del 1 al 10)
MAQUINAS = list(range(1, 11))

print("Productor iniciado. Enviando datos al tópico 'uso_gimnasio'...")

while True:
    # Generamos un evento aleatorio de uso de máquina
    evento = {
        "id_maquina": random.choice(MAQUINAS),
        "duracion_min": round(random.uniform(5, 60), 2),
        "calorias": round(random.uniform(30, 500), 2),
        "frecuencia_cardiaca": random.randint(60, 180),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Enviamos el evento al tópico
    producer.send('uso_gimnasio', evento)
    print(f"Enviado: {evento}")

    # Esperamos 2 segundos antes del siguiente evento
    time.sleep(2)