# Ask the user for a valid game status. (✓)
def ask_status():

    while True:
        print("[P] Pending, [I] In Progress, [D] Dropped, [C] Completed")
        status = input("Game status: ")

        if status.lower() in ["p", "pending"]:
            return "Pending"

        elif status.lower() in ["i", "in progress", "playing"]:
            return "In Progress"

        elif status.lower() in ["d", "dropped"]:
            return "Dropped"

        elif status.lower() in ["c", "completed", "finished"]:
            return "Completed"

        else:
            print("Invalid command. Please choose one of the available options.")


# Ask for the game's playtime if it has already been started. (✓)
def ask_playtime(game_status):

    if game_status in ["Dropped", "Completed"]:
        while True:
            try:
                playtime = int(input("How many hours have you played? "))
                
                if playtime >= 0:
                    return playtime
                else: 
                    print("Playtime cannot be negative.")
            except ValueError:
                print("Invalid command. Please enter a number.")


# Ask for the game's rating if it has been completed. (✓)
def ask_rating(game_status):

    if game_status in ["Completed"]:
        while True:
            try:
                rating = int(input("Rate the game from 1 to 10: "))

                if 1 <= rating <= 10:
                    return rating

                else:
                    print("Please enter a number between 1 and 10.")

            except ValueError:
                print("Invalid command. Please enter a number.")


# Returns a specific piece of game data. (✓)
def show_data(game_data):

    while True:
        print("[S] Status, [P] Playtime, [R] Rating")
        data = input("Which game information would you like to see?")

        if data.lower() in ["s", "status"]:
            return game_data["Status"]

        elif data.lower() in ["p", "playtime"]:
            if "Playtime" in game_data:
                return game_data["Playtime"]
            print("This game doesn't have a registered playtime yet.")

        elif data.lower() in ["r", "rating"]:
            if "Rating" in game_data:
                return game_data["Rating"]
            print("This game doesn't have a registered rating yet.")

        else:
            print("Invalid command. Please choose a valid option.")


# Adds a game to the catalog. (✓)
def add_game():

    game_data = {}

    # Ask for the game's name.
    game = input("Which game would you like to add to your catalog? ")

    if game == "":
        print("Operation canceled.")
        return None, None

    game_status = ask_status()
    game_data["Status"] = game_status

    playtime = ask_playtime(game_status)

    if playtime is not None:
        game_data["Playtime"] = playtime

    rating = ask_rating(game_status)

    if rating is not None:
        game_data["Rating"] = rating

    return game_data, game


# Delete a game of the catalog.(✓)
def delete_game(catalog, game):
    del catalog[game]


# Change a game's status and update its data if necessary. (✓)
def change_status(catalog, game):
    details = catalog[game]
    old_status = details["Status"]
    while True:
            question = input("Changing the status could remove the playtime and rating. Continue? (Y/N) ")
            if question.lower() in ["yes", "y"]:
                new_status = ask_status()
                if old_status == new_status:
                    print("The game already has that status.")
                    return

                if old_status == "Completed":
                    if new_status in ["In Progress", "Pending"]:
                        if "Rating" in details:
                            del details["Rating"]
                        if "Playtime" in details:
                            del details["Playtime"]

                    elif new_status == "Dropped":
                        if "Rating" in details:
                            del details["Rating"]

                elif old_status == "Dropped":
                    if new_status in ["In Progress", "Pending"]:
                        if "Playtime" in details:
                            del details["Playtime"]
                        if "Rating" in details:
                            del details["Rating"]

                if new_status == "Completed":
                    if "Rating" not in details:
                        new_rating = ask_rating(new_status)
                        details["Rating"] = new_rating
                    if "Playtime" not in details:
                        new_playtime = ask_playtime(new_status)
                        details["Playtime"] = new_playtime
                elif new_status == "Dropped":
                    if "Playtime" not in details:
                        new_playtime = ask_playtime(new_status)
                        details["Playtime"] = new_playtime

                catalog[game]["Status"] = new_status
                break
            elif question.lower() in ["no", "n"]:
                print("Operation canceled")
                break
            else:
                print("Invalid command. Please choose a valid option.")


# Edit the information of an existing game. (✓)
def change_details(catalog, game):
   
    if game not in catalog:
        print("Game not in the catalog.")
    else:
        details = catalog[game]
        while True:
            print ("[S] Status, [P] Playtime, [R] Rating, [B] Back")
            choice = input("What do you want to change?")
            if choice.lower() in ("s", "status"):
                change_status(catalog, game)
                return catalog
            
            elif choice.lower() in ("p", "playtime", "play time"):

                 
                if "Playtime" in (details):
                    playtime = ask_playtime(details["Status"])
                    catalog[game]["Playtime"] = playtime
                    return catalog
                else:
                    print("There is no playtime recorded.")

            elif choice.lower() in ("r", "rating"):
                    
                #if "Rating" in (details):
                    rating = ask_rating(details["Status"])
                    catalog[game]["Rating"] = rating
                    return catalog
                #else:
                    #print("There is no rating yet. ")
            
            elif choice.lower() in ("b", "back", ""):
                return None
            
            else: 
                print("Invalid command. Please choose one of the available options.")


# Actions on data of the game. (✓)
def actions_menu(catalog, game):

    while True:

        print("[D] Delete game, [C] Change data, [S] Show data, [B] Back")
        choice = input("What do you want to do? ")
    
        if choice.lower() in ("d", "delete", "delete game"):
            delete_game(catalog, game)
            print("Game deleted.")
            break
        elif choice.lower() in ("c", "change", "change data"):
            catalog = change_details(catalog, game)
            if catalog is not None:
                return catalog
            else:
                print("Operation denied")
        elif choice.lower() in ("s", "show", "show data"):
            game_data = show_data(catalog[game])
            if game_data is not None:
                print(game_data)
            else:
                print("Operation denied")
        elif choice.lower() in ("b", "back", ""):
            return None
        else:
            print("Invalid command. Please choose one of the available options.")


# Returns a list of all games in the catalog. (✓)
def game_list(catalog):

    library= list(catalog.keys())
    return library
