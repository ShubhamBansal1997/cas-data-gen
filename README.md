Data Generator for CAS
----------------------

Creates a Kafka feed that simulates a subset of CAS data using fake data.

## Prerequisites
 
- Python 3.7+
- A valid [Kafka](https://kafka.apache.org) setup

## Installation

```
pip install -r requirements.txt
```

## Configuration

Assumes Kafka is available at `localhost:9092`. Edit `main.py` with the appropriate address if you
need to change it.

## Usage

```
python main.py [count]
```

Where `count` is the number of items *of each type* (forms/cases) to generate.

## Testing

To see the output you can use the following commands:

```python
kafka-console-consumer.sh --topic datagen-form --bootstrap-server http://localhost:9092 --from-beginning
kafka-console-consumer.sh --topic datagen-case --bootstrap-server http://localhost:9092 --from-beginning
```

## Source Data

The household case with ID `0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9` on the India server has been used as a basis 
for the case templates (including its child cases, etc.). 
You can [view the case here](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9/#related)
and use the [raw doc view](https://india.commcarehq.org/hq/admin/raw_doc/?id=0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9)
to see the raw JSON.
