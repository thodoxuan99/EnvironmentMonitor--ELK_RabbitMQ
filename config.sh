docker-compose up -d
#Config SSL for MQTT
docker cp rabbitmq.conf RabbitMQ:/etc/rabbitmq/
docker cp ssl RabbitMQ:/
docker exec RabbitMQ rabbitmq-plugins enable rabbitmq_mqtt
docker restart RabbitMQ