# It is recommened to use same version as kafka broker is used.
# So no additional images are pulled.
FROM confluentinc/cp-kafka:latest


# Once it is executed, this container is not needed.
COPY create-topics.sh /tmp/create-topics.sh
ENTRYPOINT ["sh", "/tmp/create-topics.sh"]
