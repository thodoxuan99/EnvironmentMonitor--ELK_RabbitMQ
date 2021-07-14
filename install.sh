git clone https://github.com/thodoxuan99/EnvironmentMonitor--ELK_RabbitMQ.git
cd EnvironmentMonitor--ELK_RabbitMQ
git checkout re_config
docker-compose up --force-recreate  -d
#Config SSL for MQTT
docker cp rabbitmq.conf RabbitMQ:/etc/rabbitmq/
docker cp ssl RabbitMQ:/
docker exec RabbitMQ rabbitmq-plugins enable rabbitmq_mqtt
docker restart RabbitMQ