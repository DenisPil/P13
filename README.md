## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

### Docker Hub

Permet de lancer l'application dans un conteneur en local, à partir de la dernière version qui se trouve sur : https://hub.docker.com/repository/docker/denispil/oc_lettings

- La première étape est de cloner le repo sur github : `git clone git@github.com:DenisPil/P13.git`
- Ensuite activer l'environement virtuel `source venv/bin/activate`.
- Pour terminer se mettre dans le répertoire racine de l'application
- Puis activer le conteneur `docker-compose up`
- Et se rendre à l'adresse `localhost:8000`

### CircleCI & Heroku

Utilisation d'un Pipeline CI/CD et déploiement sur Heroku

Prérequis:
- Un compte GitHub.
- Un compte Circleci.
- Un compte Heroku.
- Un compte DockerHub.
- Un compte Sentry.

Se rendre dans les settings de CircleCI puis dans l'onglet "Variable d'environnement"

| NAME | VALUE | 
| ------|-----|
| DOCKER_LOGIN | Username de votre compte DockerHub|
| DOCKER_PASSWORD | Token de votre compte DockerHub|
| HEROKU_API_KEY | API-KEY de votre compte Heroku|
| HEROKU_APP_NAME | Le nom de votre application sur Heroku|
| SECRET_KEY | La clé qui ce trouve dans le settings.py de l'application Django|
| SENTRY_DSN | le DSN de votre projet Sentry|

Le pipeline est executé automatiquement lors d'un push sur Github.
CircleCI automatise le déploiement sur Heroku et la dernière image est sauvegardée sur Dockerhub.