from api import get_film_data


def display_film_data(film_id):
    film_data = get_film_data(film_id)

    if film_data:
        print(f"Фільм: {film_data['title']}")

        print("Персонажі:")
        for i, character in enumerate(film_data['characters'], 1):
            print(f"  {i}. {character[0]} з планети {character[1]}")

        print("Транспортні засоби:")
        for i, vehicle in enumerate(film_data['vehicles'], 1):
            print(f"  {i}. {vehicle}")

        print("Космічні кораблі:")
        for i, starship in enumerate(film_data['starships'], 1):
            print(f"  {i}. {starship}")

        print("Види істот:")
        for i, specie in enumerate(film_data['species'], 1):
            print(f"  {i}. {specie}")
    else:
        print("Фільм не знайдено.")


if __name__ == "__main__":
    film_id = input("Введіть ідентифікатор фільму: ")
    display_film_data(film_id)
