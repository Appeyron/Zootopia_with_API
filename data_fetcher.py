"""
Data Fetcher Component.

This module loads environment variables and fetches animal data from the
API-Ninjas endpoint based on a provided animal name.
"""

import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """Fetches the animals data for the animal 'animal_name'.

    Returns:
        list: A list of dictionaries, where each dictionary represents
              an animal.
    """
    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"name": animal_name},
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")
        return []
