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

## Running tests

To run tests just run the following in the root of the repository:

```
pytest
```

## Source Data

The household case with ID `0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9` on the India server has been used as a basis 
for the case templates (including its child cases, etc.). 
You can [view the case here](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9/#related)
and use the [raw doc view](https://india.commcarehq.org/hq/admin/raw_doc/?id=0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9)
to see the raw JSON.

The following table is the list of Case IDs used:

Description         | Case Type  | Case ID
------------------- | ---------- | -------
Household           | household  | [0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/0d3ebba1-cf52-4d89-aea4-2fe5ec9c9ed9/#related)
Pregnant Person     | person     | [7802432e-548d-499c-90cc-5b0b41f203f0](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/7802432e-548d-499c-90cc-5b0b41f203f0/)
Pregnant CCS Record | ccs_record | [d02668b4-0175-4fe7-920d-c0ea3568d6b3](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/d02668b4-0175-4fe7-920d-c0ea3568d6b3/)
Mother's Person     | person     | [23eb689a-8997-471f-946e-db06355296a6](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/23eb689a-8997-471f-946e-db06355296a6/)
Child's Person      | person     | [51407edd-6c91-421f-9558-2f517fc359ae](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/51407edd-6c91-421f-9558-2f517fc359ae/)
Mother's CCS Record | ccs_record | [d8962f84-6327-41bd-8572-076c621f7eae](https://india.commcarehq.org/a/icds-dashboard-qa/reports/case_data/d8962f84-6327-41bd-8572-076c621f7eae/)


And for Forms:

Description         | Form Type  | Form ID
------------------- | ---------- | -------
Birth Preparedness  | BP         | [4623a1a0-8182-4764-8be1-5f7a7ebb31b1](https://india.commcarehq.org/a/icds-dashboard-qa/reports/form_data/4623a1a0-8182-4764-8be1-5f7a7ebb31b1/#form-xml)
Post Natal Care     | PNC 			 | [c28f99cb-e706-4e28-a245-60147a1f692d](https://india.commcarehq.org/a/icds-cas/reports/form_data/c28f99cb-e706-4e28-a245-60147a1f692d/#form-xml)
Take Home Ration		| THR				 | [5cbb6dcb-89de-4da2-a3b1-5237f4dd3182]https://india.commcarehq.org/a/icds-cas/reports/form_data/5cbb6dcb-89de-4da2-a3b1-5237f4dd3182/#form-data
Delivery Form 			| Delivery	 | [a684eab2-db48-4ffa-9cdb-8ade3e36ff8b]https://india.commcarehq.org/a/icds-cas/reports/form_data/a684eab2-db48-4ffa-9cdb-8ade3e36ff8b/
