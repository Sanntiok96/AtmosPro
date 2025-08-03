# servidor_meteo.py
from flask import Flask, request, render_template, send_from_directory, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

if not os.path.exists("datos"):
    os.makedirs("datos")

CSV_FILE = os.path.join("datos", "registro.csv")

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            "Fecha", "Hora", "Temperatura (°C)", "Humedad (%)",
            "Presión (hPa)", "Luz (Lux)", "Lluvia (0-1023)",
            "CO2 (ppm)", "Probabilidad lluvia (%)"
        ])

ultima_fila = None

@app.route("/datos", methods=["POST"])
def recibir_datos():
    global ultima_fila
    datos = request.get_json()
    ahora = datetime.now()

    def formatear(valor):
        if isinstance(valor, float):
            return f"{valor:.2f}".replace('.', ',')
        return valor

    fila = [
        ahora.strftime("%Y-%m-%d"),
        ahora.strftime("%H:%M"),  # Solo hora y minutos
        formatear(datos["temp"]),
        formatear(datos["hum"]),
        formatear(datos["pres"]),
        formatear(datos["lux"]),
        formatear(datos["lluvia"]),
        formatear(datos["co2"]),
        formatear(datos["proba"])
    ]

    ultima_fila = fila

    if ahora.minute in [0, 15, 30, 45] and ahora.second == 0:
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(fila)

    return {"status": "ok"}

@app.route("/api/ultima")
def api_ultima():
    if ultima_fila:
        return jsonify(ultima_fila)
    return jsonify([])

@app.route("/")
def index():
    columnas = [
        "Fecha", "Hora", "Temperatura (°C)", "Humedad (%)",
        "Presión (hPa)", "Luz (Lux)", "Lluvia (0-1023)",
        "CO2 (ppm)", "Probabilidad lluvia (%)"
    ]
    return render_template("index.html", columnas=columnas)

@app.route("/descargar")
def descargar_csv():
    return send_from_directory("datos", "registro.csv", as_attachment=True)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
