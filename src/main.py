"""
Game Library - Version 2

A simple command-line application written in Python.

Features:
- Add games to a personal catalog.
- Search for games by name.
- Update a game's status, playtime, and rating.
- Delete games from the catalog.
- Track playtime for played games.
- Rate completed games.
- Display stored game information.
- Automatically save and load the catalog using JSON.

This project was built as a learning exercise while studying Python.
Its main goal is to practice core programming concepts, including
dictionaries, functions, loops, input validation, file handling,
exception handling, JSON data storage, and code organization.

The project is organized into separate modules for the application
logic, file management, and the main program.
"""
import files
import catalog

game_catalog = files.load_catalog()

# Main menu.
def menu(game_catalog):

    while True:
        print("[S] Search, [A] Add, [B] Back")
        action = input("What would you like to do? Search for a game or add a new one? ")

        if action.lower() in ["s", "search"]:
            
            if not game_catalog:
                print("Your catalog is empty.")
                continue

            game_list = catalog.game_list(game_catalog)
            print(game_list)
            game = input("Which game would you like to search for? ")

            if game in game_list:
                catalog.actions_menu(game_catalog, game)

            else:
                print("Game not in catalog")

        elif action.lower() in ["a", "add"]:
            game_data, game = catalog.add_game()

            if game is not None:
                game_catalog[game] = game_data

        elif action.lower() in ["b", "back"]:
            break

        else:
            print("Invalid command. Please choose one of the available options.")

menu(game_catalog)
files.save_catalog(game_catalog)
