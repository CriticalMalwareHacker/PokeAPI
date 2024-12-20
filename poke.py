import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    
    if response.status_code==200:
        poke_data=response.json()
        return poke_data
    else:
        print("Failed to retrieve data")

pokemon_name=input("Enter pokemon name: ")
info=get_pokemon_info(pokemon_name)
if info:
    print(f"Pokemon name: {info["name"].capitalize()}")
    print(f"Pokemon id: {info["id"]}")
    print(f"Pokemon height: {info["height"]}")
    print(f"Pokemon weight: {info["weight"]}")
