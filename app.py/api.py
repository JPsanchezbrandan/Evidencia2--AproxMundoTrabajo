from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuración de la base de datos
def crear_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vvv44444091',
        database='IoT_Sensores'
    )

# Endpoint para recibir datos del sensor
@app.route('/api/sensores', methods=['POST'])
def recibir_datos():
    data = request.get_json()
    movimiento = data.get('movimiento')
    
    # Mensaje de depuración
    print("Datos recibidos: ", data)

    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO datos_sensor (movimiento) VALUES (%s)"
        cursor.execute(sql, (movimiento,))
        conexion.commit()
        print("Datos insertados: ", movimiento)
        return jsonify({'message': 'Datos insertados con éxito!'}), 200
    except Error as e:
        print("Error al insertar datos: ", e)  # Mensaje de error
        return jsonify({'error': str(e)}), 500
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Iniciar el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

