# Developer Skills Tracker

This Python application is designed to maintain and manage a list of developer skills along with their occurrence counts in a database. It supports adding, removing, displaying, and searching for skills. The application performs the following operations:

1. Checks if a database named `skills.db` exists. If it does, it connects to the database and loads the skills and their counts into a table. If the database does not exist, it creates the `skills.db` database and initializes a table for storing skills.

2. Enters a menu that has options for the user to select such as adding a skill, removing a skill, decrementing a skill, displaying all skills, or searching for a specific skill. For each action, the application performs the corresponding operations:
    - **Add a Skill**: Searches the table for the entered skill. If found, increments the count; otherwise, adds the skill with a count of 1.
    - **Search for a Skill**: Searches for and displays the count of the specified skill.
    - **Decrement a Skill**: Decrements the skill's count by 1 and removes it if `count = 0`.
    - **Remove a Skill**: Removes the specified skill from the table if it exists.
    - **Display All Skills**: Shows all skills and their counts.
    - **Exit**: Displays an exit message, ensures all changes are committed to the database, closes the database connection, and quits the program.

3. Updates the `skills.db` database with the current list of skills and their counts after any modification.

4. Calls the `skillsSort` module to sort the skills. The sorting can be done either in descending order by count and then alphabetically for skills with the same count, or in ascending order based on a new method. The sorting now occurs within the database query for efficiency.

The skills and their counts are stored in the `skills.db` database in a table with columns `skill` and `count`. The `skillsSort` module ensures that the list is sorted appropriately after each update.

#### Requirements:
- Python 3.x
- SQLite3 (comes bundled with Python 3.x)

#### Recent Updates:
- **Database Integration**: Transitioned from using a text file (`skills.txt`) to a SQLite database (`skills.db`) for storing skills and their counts. This enhances data integrity and allows for more complex queries.
- **Test Cases Added**: Introduced test cases in `test_skillsMethods.py` to ensure the accuracy and reliability of the application's functionalities. These tests cover all the main operations such as adding, removing, decrementing, and searching for skills, now with database integration.
- **Enhanced Sorting Feature**: Improved the `skillsSort` module to offer more flexible sorting options, allowing users to sort skills not only by count but also alphabetically in ascending or descending order, directly using SQL queries for improved performance.
- **Error Handling**: Improved error handling across the application to provide clearer messages and prevent the application from exiting unexpectedly during runtime.

#### Usage:
1. Ensure Python 3.x is installed on your system.
2. Place the application files and the `skillsSort` module in a directory of your choice.
3. Run the application using the command `python skillsList.py`.
4. Follow the on-screen prompts to manage skills. The application allows adding, removing, displaying, and searching for skills. It will update the counts, save them to `skills.db`, and sort the list using the `skillsSort` module.
5. To run test cases, type `python3 -m unittest`.