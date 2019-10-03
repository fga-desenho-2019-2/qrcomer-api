echo "Subindo serviços"
docker-compose up -d db
sleep 10
docker-compose up -d api

echo "Fazendo migrações"
docker exec -it user-service python manage.py makemigrations
docker exec -it user-service python manage.py migrate

echo "Fazendo dump dos dados do banco de dados"
docker exec -it user-service python manage.py dumpdata > db/db.json

echo "Sucesso, backup salvo na pasta db"
sudo docker-compose stop