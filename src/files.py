import json

"""
# Load the game catalog from the JSON file.
def load_catalog():

    try:
        with open ("data/games.json", "r") as file:

            catalog = json.load(file)

            return catalog
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
"""

def load_catalog():
    try:
        with open("data/games.json", "r") as file:
            catalog = json.load(file)
            print("Loaded:", catalog)
            return catalog

    except Exception as e:
        print(type(e).__name__, e)
        return {}

# Save the game catalog to the JSON file.
def save_catalog(catalog):

    with open ("data/games.json", "w") as file:
    
        json.dump(catalog, file, indent=4, ensure_ascii=False)


