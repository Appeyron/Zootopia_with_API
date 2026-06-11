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


def generate_animals_html(data, animal_name):
    """Generate HTML for all returned animals."""

    if not data:
        return (
            '<div class="card">\n'
            f'  <h2>The animal "{animal_name}" doesn\'t exist.</h2>\n'
            '  <p>Please try another animal name.</p>\n'
            '</div>\n'
        )

    output = ""

    for animal_obj in data:
        output += serialize_animal(animal_obj)

    return output


def generate_website(data, animal_name):
    """Generate animals.html from template and animal data."""

    animals_html = generate_animals_html(data, animal_name)

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        html_template = handle.read()

    final_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_html
    )

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(final_html)