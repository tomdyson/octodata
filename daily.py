from api import OctopusEnergyClient
from storage import Storage
from utils import debug

storage = Storage()
client = OctopusEnergyClient()

# Fetch and store usage for the last 100 half hours
records = client.get_usage(limit=100)
record_count = 0
insert_count = 0
for record in records.json()["results"]:
    record_count += 1
    if storage.insert_record(record):
        insert_count += 1

storage.close()

debug(f"Inserted {insert_count} records from {record_count} results")
