git clone https://github.com/thodoxuan99/EnvironmentMonitor--ELK_RabbitMQ.git
cd EnvironmentMonitor--ELK_RabbitMQ
git checkout re_config
docker-compose up --force-recreate  -d
#Wait for starting service
docker exec -it RabbitMQ rabbitmq-plugins enable rabbitmq_mqtt