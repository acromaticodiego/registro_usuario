# Sistema de Registro con Tareas en Segundo Plano

Este proyecto usa **FastAPI**, **MySQL**, **Celery** y **Redis** para registrar usuarios y procesar tareas en segundo plano como enviar correos o generar informes, sin bloquear la respuesta al usuario.

## ¿Cómo funciona?

1. El usuario se registra mediante un `POST /register`.
2. Los datos se guardan en una base de datos MySQL.
3. Se ejecutan dos tareas en segundo plano:
   - Enviar un correo de bienvenida.
   - Generar un informe del perfil del usuario.

Todo esto usando **Celery**, para que el backend responda rápido y las tareas pesadas se hagan en segundo plano sin afectar la experiencia.

## Tecnologías utilizadas

- `FastAPI` – para la API web.
- `MySQL` – base de datos relacional.
- `Celery` – para ejecutar tareas asincrónicas.
- `Redis` – actúa como broker de mensajes para Celery.
