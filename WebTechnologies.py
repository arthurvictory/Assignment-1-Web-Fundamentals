# Task 1 Setup virtual environment and install requests package
import requests
import json

# Task 2 Fetch data from the Pokemon API
api_url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(api_url)
json_data = response.text

pokemon_data = json.loads(json_data)

# Extract name and abilities
name = pokemon_data["name"] 
abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
print(f"Pokemon Name: {name.capitalize()}") 
print("Abilities:") 
for ability in abilities: 
    print(f"- {ability}")
    print()
    
# Task 3: Analyzing and Displaying Data
def fetch_pokemon_data(pokemon_name):
    try: 
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}" 
        response = requests.get(api_url) 
        return response.json() 
    except Exception as e: 
        print(f"Error fetching data for {pokemon_name}: {e}") 
        return None

def calculate_average_weight(pokemon_list):
    if not pokemon_list: 
        return 0 
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list) 
    average_weight = total_weight / len(pokemon_list) 
    return average_weight

pokemon_names = ["bulbasaur", "squirtle", "charmander"] 
pokemon_data_list = []

for name in pokemon_names: 
    data = fetch_pokemon_data(name) 
    if data: 
        pokemon_data_list.append(data)

average_weight = calculate_average_weight(pokemon_data_list)

for pokemon in pokemon_data_list: 
    name = pokemon["name"].capitalize() 
    abilities = [ability["ability"]["name"] for ability in pokemon["abilities"]] 
    print(f"Pokemon Name: {name}") 
    print("Abilities:") 
    for ability in abilities: 
        print(f"- {ability}") 
        print()
    print(f"Average Weight: {average_weight}") 
    
    if __name__ == "__main__": 
        pass