Data Generator for CAS
----------------------

Creates a Kafka feed that simulates a subset of CAS data using fake data.

# Prerequisites
 
- Python 3.7+
- A valid [Kafka](https://kafka.apache.org) setup

# Installation

```
pip install -r requirements.txt
```

# Configuration

Assumes Kafka is available at `localhost:9092`. Edit `main.py` with the appropriate address if you
need to change it.

# Usage

```
python main.py
```


# Testing

To see the output you can use the following commands:

```python
kafka-console-consumer.sh --topic datagen-form --bootstrap-server http://localhost:9092 --from-beginning
kafka-console-consumer.sh --topic datagen-case --bootstrap-server http://localhost:9092 --from-beginning
```
