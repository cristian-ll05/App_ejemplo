from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def mostrar_info():
    nombre = "Cristian llangari" 
    universidad = "Universidad de Guayaquil" 

    # Usamos la zona horaria de Guayaquil
    zona_horaria = pytz.timezone('America/Guayaquil')
    fecha_hora_actual = datetime.now(zona_horaria).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Información Personal</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            h1 {{ color: #333; }}
            p {{ color: #666; font-size: 1.1em; }}
        </style>
    </head>
    <body>
        <h1>{nombre}</h1>
        <p><strong>Universidad:</strong> {universidad}</p>
        <p><strong>Fecha y Hora (Guayaquil):</strong> {fecha_hora_actual}</p>
        <p>¡Esta es una app sencilla desplegada con AWS App Runner!</p>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    # App Runner espera que la aplicación escuche en el puerto 8080
    app.run(host='0.0.0.0', port=8080)
