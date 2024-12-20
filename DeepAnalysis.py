import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_list = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
            planet_list.append(planet)
    return planet_list

def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if 'mass' in planet and planet['mass'] is not None:
            mass_value = planet['mass']['massValue'] * (10 ** planet['mass']['massExponent'])
            if mass_value > max_mass:
                max_mass = mass_value
                heaviest_planet = planet
    if heaviest_planet:
        name = heaviest_planet['englishName']
        mass = max_mass
        return name, mass
    else:
        return None, 0
    
planets = fetch_planet_data()
if planets:
    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")