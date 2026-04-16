import argparse
import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

# Recibe el broker por parámetro (requerido para la Fase 4)
parser = argparse.ArgumentParser()
parser.add_argument('--broker', type=str, required=True, help="Host:Puerto del broker (ej: localhost:9092)")
args = parser.parse_args()

# Conexión al broker indicado
producer = KafkaProducer(
    bootstrap_servers=[args.broker],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

MAQUINAS = list(range(1, 11))

print(f"Generador iniciado → broker: {args.broker}")

try:
    while True:
        # Generamos evento aleatorio de uso de máquina del gimnasio
        evento = {
            "id_maquina": random.choice(MAQUINAS),
            "duracion_min": round(random.uniform(5, 60), 2),
            "calorias": round(random.uniform(30, 500), 2),
            "frecuencia_cardiaca": random.randint(60, 180),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        producer.send('uso_gimnasio', value=evento)
        print(f"Enviado: {evento}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Detenido.")
finally:
    producer.close()