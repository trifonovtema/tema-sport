#!/bin/sh

echo -e 'Creating missing Kafka topics:'
kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic users --replication-factor 1 --partitions 3
kafka-topics --bootstrap-server kafka:9092 --create --if-not-exists --topic websocket --replication-factor 1 --partitions 3
echo -e 'Kafka topics:'
kafka-topics --bootstrap-server kafka:9092 -list
