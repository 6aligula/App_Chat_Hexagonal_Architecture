# users/Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Establece el PYTHONPATH para que el directorio actual esté en la ruta de búsqueda de Python
ENV PYTHONPATH=/app
# Expone el puerto que usará la aplicación
EXPOSE 8000

# Instala netcat-openbsd para que funcione el script de wait-for.sh
RUN apt-get update && apt-get install -y netcat-openbsd

RUN chmod +x /app/wait-for.sh

CMD ["/app/wait-for.sh", "db:5432", "uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]
