git clone https://github.com/thodoxuan99/EnvironmentMonitor--ELK_RabbitMQ.git
cd EnvironmentMonitor--ELK_RabbitMQ
git checkout re_config
docker rm  -f RabbitMQ
docker-compose up --force-recreate  -d
docker restart ELK_RabbitMQ
docker exec -it RabbitMQ rabbitmq-plugins enable rabbitmq_mqtt