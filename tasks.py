from celery import Celery
import time

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task
def send_welcome_email(email):
    time.sleep(3)
    print(f"✅ Correo enviado a {email}")

@celery.task
def generate_profile_report(user_id):
    time.sleep(5)
    print(f"📄 Informe generado para el usuario {user_id}")