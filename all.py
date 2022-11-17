import time
from api import OctopusEnergyClient
from storage import Storage
from utils import debug

storage = Storage()
client = OctopusEnergyClient()


def fetch_batch(url=None):
    # recursively fetch all records
    record_count = 0
    insert_count = 0
    if url:
        records = client.get_usage(url=url, limit=100)
    else:
        records = client.get_usage(limit=100)
    for record in records.json()["results"]:
        record_count += 1
        if storage.insert_record(record):
            insert_count += 1
    debug(f"Inserted {insert_count} records from {record_count} results")
    if records.json()["next"]:
        time.sleep(0.3)  # Octopus Energy API limit is 5 requests per second
        fetch_batch(url=records.json()["next"])


debug("*** Fetch all electricity usage records ***")
fetch_batch()

storage.close()
