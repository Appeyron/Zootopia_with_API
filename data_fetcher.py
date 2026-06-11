import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.

    Returns: a list of animals, each animal is a dictionary.
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