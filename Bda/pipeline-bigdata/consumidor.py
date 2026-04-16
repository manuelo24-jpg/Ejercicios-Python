import json
import mysql.connector
from kafka import KafkaConsumer

# Conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="gimnasio_user",
    password="gimnasio1234",
    database="gimnasio"
)
cursor = db.cursor()

# Conexión a Kafka
# Conexión a Kafka (Añadimos los 3 brokers para Alta Disponibilidad)
consumer = KafkaConsumer(
    'uso_gimnasio', # Asegúrate de que este nombre coincida con el que creaste con docker exec
    bootstrap_servers=['localhost:9092', 'localhost:9094', 'localhost:9096'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumidor iniciado. Esperando mensajes de Kafka...")

for mensaje in consumer:
    dato = mensaje.value
    print(f"Recibido: {dato}")

    # Insertamos en la tabla de hechos
    sql = """
        INSERT INTO fact_uso (id_maquina, duracion_min, calorias, frecuencia_cardiaca, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        dato["id_maquina"],
        dato["duracion_min"],
        dato["calorias"],
        dato["frecuencia_cardiaca"],
        dato["timestamp"]
    )
    cursor.execute(sql, valores)
    db.commit()
    print(f"Insertado en MySQL ✅")