# chatbot-ml

Objectif : créer un interrogatoire médical permettant de fournir un premier diagnostic à distance.

## Run

```
docker run --name chatbot-ml -e POSTGRES_DB=chatbot-ml -e POSTGRES_USER=root -e POSTGRES_PASSWORD=toor -p 5432:5432 -d postgres:14-alpine
```

```
python -m flask run --debug
```
