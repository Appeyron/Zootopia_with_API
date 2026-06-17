"""
Animals Web Generator.

This module fetches animal data, serializes the information into HTML components,
and dynamically generates a webpage based on an HTML template.
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
TEMPLATE_PATH = SCRIPT_DIR / "animals_template.html"
OUTPUT_PATH = SCRIPT_DIR / "animals.html"


def serialize_animal(animal_obj):
    """Serialize one animal into HTML using a list and join."""
    parts = ['<li class="cards__item">\n']

    if "name" in animal_obj:
        parts.append(
            f'  <div class="card__title">{animal_obj["name"]}</div>\n'
        )

    parts.append('  <div class="card__text">\n    <ul>\n')

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        parts.append(
            f'      <li><strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if "locations" in animal_obj and animal_obj["locations"]:

        locations_str = ", ".join(animal_obj["locations"])
        parts.append(
            f'      <li><strong>Location:</strong> '
            f'{locations_str}</li>\n'
        )

    if "type" in characteristics:
        parts.append(
            f'      <li><strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    parts.append("    </ul>\n  </div>\n</li>\n")

    return "".join(parts)


def generate_animals_html(data, animal_name):
    """Generate HTML for all returned animals."""
    if not data:
        return (
            '<div class="card">\n'
            f'  <h2>The animal "{animal_name}" doesn\'t exist.</h2>\n'
            '  <p>Please try another animal name.</p>\n'
            '</div>\n'
        )

    return "".join(serialize_animal(animal_obj) for animal_obj in data)


def generate_website(data, animal_name):
    """Generate animals.html from template and animal data."""
    animals_html = generate_animals_html(data, animal_name)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as handle:
        html_template = handle.read()

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_html
    )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:

        handle.write(final_html)
