import os
import requests
from dotenv import load_dotenv

load_dotenv()


class OctopusEnergyClient:
    def __init__(self):
        self.user = os.getenv("OCTOPUS_KEY")
        self.mpan = os.getenv("MPAN")
        self.serial_number = os.getenv("METER_SERIAL_CODE")
        self.base_url = "https://api.octopus.energy/v1/"

    def get(self, url):
        # Append base URL if necessary
        if not url.startswith("https://"):
            url = self.base_url + url
        return requests.get(url, auth=(self.user, ""))

    def get_usage(self, limit=None, group_by=None, url=None):
        if url:
            return self.get(url)
        url = f"electricity-meter-points/{self.mpan}/meters/{self.serial_number}/consumption/?x"
        if group_by:
            url += f"&group_by={group_by}"
        if limit:
            url += f"&page_size={limit}"

        return self.get(url)
