import data_fetcher
import animals_web_generator


def main():
    """Ask user for an animal and generate website."""

    animal_name = input("Enter a name of an animal: ").strip()

    data = data_fetcher.fetch_data(animal_name)

    animals_web_generator.generate_website(data, animal_name)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()