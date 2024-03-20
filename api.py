import swapi


def get_film_data(film_id):
    film = swapi.get_film(film_id)

    if not film:
        return None

    characters = [(character.name, character.get_homeworld().name) for character in film.get_characters()]
    vehicles = [vehicle.name for vehicle in film.get_vehicles()]
    starships = [starship.name for starship in film.get_starships()]
    species = [specie.name for specie in film.get_species()]

    return {
        "title": film.title,
        "characters": characters,
        "vehicles": vehicles,
        "starships": starships,
        "species": species
    }
