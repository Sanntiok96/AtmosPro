from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import csv

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

    def formatear(valor):
        if isinstance(valor, float):
            return f"{valor:.2f}".replace('.', ',')
        return valor

    fecha = datos.get("fecha", "0000-00-00")
    hora = datos.get("hora", "00:00")

    fila = [
        fecha,
        hora,
        formatear(datos["temp"]),
        formatear(datos["hum"]),
        formatear(datos["pres"]),
        formatear(datos["lux"]),
        formatear(datos["lluvia"]),
        formatear(datos["co2"]),
        formatear(datos["proba"])
    ]

    ultima_fila = fila

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(fila)

    return jsonify({"status": "ok"})

@app.route("/api/ultima")
def api_ultima():
    return jsonify(ultima_fila or [])

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
