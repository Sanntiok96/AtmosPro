AtmosPro - Estación Meteorológica con ESP32 y Python

AtmosPro es un proyecto completo de estación meteorológica que utiliza un ESP32 con MicroPython para capturar datos ambientales y enviarlos a un servidor desarrollado en Python con Flask.


Funcionalidades

Lectura de temperatura, humedad, presión, luz, lluvia y calidad del aire (CO₂)

Cálculo de probabilidad de lluvia basado en condiciones ambientales

Envío de datos al servidor cada 10 segundos

Almacenamiento automático de datos en archivo CSV cada 15 minutos

Interfaz web responsive con diseño y animaciones modernas

Botón de descarga de registros históricos (CSV)

Cambios visuales de día y noche según la hora actual

Bluetooth BLE para comunicación con App Inventor (en desarrollo)


Componentes utilizados

ESP32 (con WiFi y BLE)

Sensor DHT22 (temperatura y humedad)

Sensor BMP280 (presión)

Sensor BH1750 (luz)

Sensor MQ135 (calidad del aire)

Sensor de lluvia analógico

Módulo RTC DS3231

Requisitos del servidor

Python 3.10+

Flask


Instalación rápida:

pip install -r requirements.txt

Archivos importantes

main.py: Código MicroPython para el ESP32

servidor_meteo.py: Servidor Flask que recibe datos y los guarda en CSV

/templates/index.html: Interfaz web para visualizar datos

/static/style.css: Estilos modernos inspirados en Windows 11

registro.csv: Archivo que almacena las lecturas (se genera automáticamente)


Cómo desplegar en Render

Subí tu repositorio a GitHub con los archivos necesarios.

Agregá los archivos requirements.txt y render.yaml.

Creá un nuevo Web Service en Render apuntando al repo.


¡Listoooooooo!


Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

