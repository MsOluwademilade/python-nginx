FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
RUN apt-get update && apt-get install -y iproute2
CMD ["python", "app.py"]
