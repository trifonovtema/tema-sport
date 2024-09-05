from backend.constants import KafkaTopic
from core.config import get_settings

BOOTSTRAP_SERVER = "kafka:9092"


def generate_create_topics_script(filename="./kafka/create-topics.sh"):
    settings = get_settings()
    with open(filename, "w") as f:
        f.write("#!/bin/sh\n\n")
        command = "echo -e 'Creating missing Kafka topics:'\n"
        f.write(command)
        for topic in KafkaTopic:
            print(f"{topic=}")
            command = f"kafka-topics --bootstrap-server {BOOTSTRAP_SERVER} --create --if-not-exists --topic {topic.value} --replication-factor 1 --partitions 3\n"
            f.write(command)

        command = "echo -e 'Kafka topics:'\n"
        f.write(command)
        command = f"kafka-topics --bootstrap-server {BOOTSTRAP_SERVER} -list\n"
        f.write(command)
    print(f"Script '{filename}' generated successfully.")


if __name__ == "__main__":
    generate_create_topics_script()
