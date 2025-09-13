
#fichiers utilisé

Dockerfile            : construction image
docker-compose.yml    : lance les conteneurs
app.py                : code de l’appli
requirements.txt      : dépendances Python


#Commandes utilisées

docker build -t tpdocker:1.0 .     # créer image
docker run -d -p 5000:5000 --name flask-container tpdocker:1.0   # lancer conteneur
docker compose up --build           # lancer plusieurs conteneurs


#pour git

git init                              # initialiser dépôt
git branch -m main                    # renommer branche
git add .                             # ajouter fichiers
git commit -m "Initial commit"        # valider modifications
git remote add origin https://github.com/ikramboukcem/tpDocker.git      # lier dépôt distant
git push -u origin main               # envoyer sur GitHub

