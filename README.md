# AtmosPro - Estación Meteorológica IoT

AtmosPro es una estación meteorológica basada en ESP32 con MicroPython que envía datos por Wi-Fi a un servidor Flask. Este servidor recibe, guarda y muestra los datos en una interfaz web simple, además de permitir su descarga en CSV.

## Funcionalidad

- Recibe datos ambientales desde el ESP32 por HTTP (temperatura, humedad, presión, luz, lluvia, CO₂, etc.).
- Guarda los datos en un archivo CSV si es un minuto múltiplo de 15.
- Muestra los datos más recientes en la interfaz web.
- Permite descargar el CSV de registros.
- Expone una API REST `/api/ultima` para obtener los últimos datos.

## Tecnologías

- ESP32 con MicroPython
- Flask + Gunicorn (Python 3)
- HTML5 + CSS (plantilla básica)

## Deploy automático

Este proyecto está preparado para ser desplegado automáticamente en [Render.com](https://render.com).

### Comandos Render

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn servidor_meteo:app`

## Estructura

AtmosPro/
├── servidor_meteo.py
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── ... (archivos CSS, JS, etc.)
├── datos/ # generado automáticamente
└── README.md

## Endpoints

- `/datos` → Recibe datos (POST)
- `/` → Página principal
- `/api/ultima` → Devuelve últimos datos en JSON
- `/descargar` → Descarga CSV

Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

