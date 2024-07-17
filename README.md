# Developer Skills Tracker

This Python application is designed to maintain and manage a list of developer skills along with their occurrence counts in a database. It supports adding, removing, displaying, and searching for skills through both a command-line interface and a Flask API. The application performs the following operations:

1. Checks if a database named `skills.db` exists. If it does, it connects to the database and loads the skills and their counts into a table. If the database does not exist, it creates the `skills.db` database and initializes a table for storing skills.

2. Introduces a `MenuHandler` class that manages the command-line menu options for the user to select such as adding a skill, removing a skill, decrementing a skill, displaying all skills, or searching for a specific skill. For each action, the application performs the corresponding operations:
    - **Add a Skill**: Searches the table for the entered skill. If found, increments the count; otherwise, adds the skill with a count of 1.
    - **Search for a Skill**: Searches for and displays the count of the specified skill.
    - **Decrement a Skill**: Decrements the skill's count by 1 and removes it if `count = 0`.
    - **Remove a Skill**: Removes the specified skill from the table if it exists.
    - **Display All Skills**: Shows all skills and their counts.
    - **Exit**: Displays an exit message, ensures all changes are committed to the database, closes the database connection, and quits the program.

3. Incorporates a Flask API that allows users or systems to perform operations such as adding, removing, decrementing, displaying, and searching for skills via HTTP requests. This extends the application's functionality to be accessible programmatically and through web services.

4. Updates the `skills.db` database with the current list of skills and their counts after any modification.

The skills and their counts are stored in the `skills.db` database in a table with columns `skill` and `count`.

#### Requirements:
- Python 3.x
- SQLite3 (comes bundled with Python 3.x)
- Flask (for the API)

#### Recent Updates:
- **Database Integration**: Transitioned from using a text file (`skills.txt`) to a SQLite database (`skills.db`) for storing skills and their counts. This enhances data integrity and allows for more complex queries.
- **Test Cases Added**: Introduced test cases in `test_skillsMethods.py` to ensure the accuracy and reliability of the application's functionalities. These tests cover all the main operations such as adding, removing, decrementing, and searching for skills, now with database integration.
- **Error Handling**: Improved error handling across the application to provide clearer messages and prevent the application from exiting unexpectedly during runtime.
- **Flask API Integration**: Added a Flask API to allow for programmatic access to the application's functionalities, enabling operations like adding, removing, decrementing, and searching for skills through HTTP requests.
- **MenuHandler Class**: Introduced a new `MenuHandler` class to manage command-line interactions, streamlining the process of performing operations through the command-line interface.

#### Usage:
1. Ensure Python 3.x and Flask are installed on your system.
2. Place the application files in a directory of your choice.
3. Run the application using the command `python main.py` for command-line interactions or `flask run` to start the Flask API server.
4. Currently, upon running `python main.py` this will initiate both the Flask API and CLI program. This will change later.
4. Follow the on-screen prompts to manage skills through the command-line interface. The application allows adding, removing, displaying, and searching for skills. It will update the counts, save them to `skills.db`.
5. To interact with the application through the Flask API, send HTTP requests to the appropriate endpoints for adding, removing, decrementing, displaying, and searching for skills.
6. To run test cases, type `python3 -m unittest`.