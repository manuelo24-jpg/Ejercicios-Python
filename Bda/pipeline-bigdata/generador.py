import argparse
import json
import time
import random
from kafka import KafkaProducer

# Configuración de argumentos
parser = argparse.ArgumentParser()
parser.add_argument('--broker', type=str, required=True, help="Host:Puerto del broker")
args = parser.parse_args()

# Inicialización del productor
producer = KafkaProducer(
    bootstrap_servers=[args.broker],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print(f"Enviando datos al broker: {args.broker}")

try:
    while True:
        # AQUÍ VA TU LÓGICA DE DATOS DEL GIMNASIO
        # Ejemplo:
        datos = {
            "usuario_id": random.randint(1, 500),
            "maquina": random.choice(["Cinta", "Prensa", "Mancuernas"]),
            "pulsaciones": random.randint(60, 160),
            "timestamp": int(time.time())
        }
        
        producer.send('datos_sensor', value=datos)
        print(f"Enviado: {datos}")
        time.sleep(1) 
except KeyboardInterrupt:
    print("Detenido.")
finally:
    producer.close()