# Image de base
FROM python:3.12-slim

# Empêche Python de créer des fichiers .pyc et active le flush stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Exposer le port Flask
EXPOSE 5000

# Lancer le serveur Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
