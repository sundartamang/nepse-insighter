import requests
from constants.urls import ANSU_VALUATION_BACKEND_URL

def get_anu_valuation():
    try:
        response = requests.get(ANSU_VALUATION_BACKEND_URL, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        data_section = json_data.get("data")

        # Handle if "data" is a dict or a list
        if isinstance(data_section, dict):
            actual_data = data_section.get("data", [])
            total_count = data_section.get("count")
        elif isinstance(data_section, list):
            actual_data = data_section
            total_count = len(actual_data)
        else:
            actual_data = []
            total_count = 0
        return {
            "count" : total_count,
            "valuations": actual_data
        }
    except requests.RequestException as e:
        return None