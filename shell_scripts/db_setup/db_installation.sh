sudo docker pull ankane/pgvector
sudo docker run --name pgvector-db -e POSTGRES_PASSWORD=test@123 -p 5432:5432 --network network1 ankane/pgvector
sudo docker stop pgvector-db
sudo docker rm pgvector-db
