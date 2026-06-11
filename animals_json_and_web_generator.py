import requests


API_KEY = "10QtOAXvqROOpvT7TeE8559W0TenbqBnfpzNFHW5"
API_URL = "https://api.api-ninjas.com/v1/animals"


def load_data():
    """Load animal data from API."""

    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"name": "fox"},
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("The API request timed out. Please try again later.")
        return []

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")
        return []

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")
        return []


def get_skin_types(data):
    """Return all available skin types."""

    skin_types = set()

    for animal_obj in data:
        characteristics = animal_obj.get("characteristics", {})

        if "skin_type" in characteristics:
            skin_types.add(characteristics["skin_type"])

    return sorted(skin_types)


def serialize_animal(animal_obj):
    """Serialize one animal into HTML."""

    output = ""

    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += (
            f'  <div class="card__title">'
            f'{animal_obj["name"]}</div>\n'
        )

    output += '  <div class="card__text">\n'
    output += "    <ul>\n"

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        output += (
            f'      <li><strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if "locations" in animal_obj:
        output += (
            f'      <li><strong>Location:</strong> '
            f'{", ".join(animal_obj["locations"])}</li>\n'
        )

    if "type" in characteristics:
        output += (
            f'      <li><strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


def generate_animals_html(data):
    """Generate HTML for all returned animals."""

    output = ""

    for animal_obj in data:
        output += serialize_animal(animal_obj)

    return output


def main():
    """Generate animals.html from template and API data."""

    data = load_data()

    if not data:
        print("No animal data received. Website was not created.")
        return

    animals_html = generate_animals_html(data)

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        html_template = handle.read()

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_html
    )

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(final_html)

    print("Website created successfully!")


if __name__ == "__main__":
    main()