import datetime
import requests
import os

# Webhook de Slack desde variable de entorno
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

# Fecha de hoy
hoy = datetime.date.today()

# Último día del mes
ultimo_dia_mes = (hoy.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
dias_restantes = (ultimo_dia_mes - hoy).days

# Solo se envía si faltan 7 días o menos para terminar el mes
if dias_restantes <= 7:
    mensaje = {
        "text": ":calendar: *¡Recordatorio mensual!* No olvidemos preguntar por los *eventos* y los *vuelos directos* :airplane:"
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=mensaje)

    if response.status_code == 200:
        print("✅ Mensaje enviado a Slack correctamente.")
    else:
        print(f"❌ Error al enviar mensaje: {response.status_code} - {response.text}")
else:
    print("ℹ️ No estamos en la última semana del mes. No se envía mensaje.")
