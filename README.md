# 🎮 Game Library

Game Library is a command-line application written in Python that allows users to manage a personal video game catalog.

The application lets users add games, search for them, update their information, track their progress, record playtime, rate completed games, and automatically save their data.

## ✨ Features

* Add games to a personal catalog.
* Search games by name.
* Display stored game information.
* Update a game's status, playtime, and rating.
* Delete games from the catalog.
* Track game progress through different statuses:

  * Pending
  * In Progress
  * Dropped
  * Completed
* Record playtime for played games.
* Rate completed games.
* Validate user input to prevent invalid data.
* Automatically save and load the catalog using JSON files.

## 🚀 Version 2 Improvements

Compared to the first version, this update introduces:

* Persistent data storage using JSON.
* Automatic loading and saving of the game catalog.
* File handling with Python's built-in tools.
* Separation of responsibilities through multiple modules.
* Improved input validation.
* Better organization and maintainability of the code.

## 🛠️ Technologies

* Python 3
* JSON
* File handling
* Exception handling
* Git and GitHub

## 📂 Project Structure

```
game-library/
│
├── src/
│   ├── main.py
│   ├── catalog.py
│   └── files.py
│
├── data/
│   └── juegos.json
│
├── README.md
└── .gitignore
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/FacundoVeraO/game-library.git
```

Navigate to the project folder:

```bash
cd game-library
```

Run the application:

```bash
python src/main.py
```

## 🎯 Purpose

This project was created as part of my learning process while studying Computer Science at UBA.

Its main goal is to practice and improve fundamental programming concepts, including:

* Functions.
* Dictionaries.
* Loops.
* Conditional logic.
* Input validation.
* Error handling.
* File handling.
* JSON data storage.
* Code organization.
* Git and GitHub workflow.

## 🔮 Future Improvements

Possible improvements for future versions:

* Add a graphical user interface (GUI).
* Add advanced search filters.
* Add statistics and progress tracking.
* Improve the user experience.
* Add additional game information.
* Implement more advanced data management features.
