# Dockerfile for Chat Service
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY ./requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . /app

# Exponer el puerto (si es necesario, por ejemplo, si usas Flask)
EXPOSE 5001

# Comando para ejecutar el servicio
CMD ["python", "application/chat_main.py"]
