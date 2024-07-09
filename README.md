# Developer Skills Tracker

This Python script is designed to maintain and manage a list of developer skills along with their occurrence counts. It supports adding, removing, displaying, and searching for skills. The script performs the following operations:

1. Checks if a file named `skills.txt` exists in the current directory. If it does, it reads the file and loads the skills and their counts into a list. If the file does not exist, it creates an empty `skills.txt` file and initializes an empty list for storing skills.

2. Enters a menu that has options for the user to select such as adding a skill, removing a skill, decrementing a skill, displaying all skills, or searching for a specific skill. For each action, the script performs the corresponding operations:
    - **Add a Skill**: Searches the list for the entered skill. If found, increments the count; otherwise, adds the skill with a count of 1.
    - **Search for a Skill**: Searches for and displays the count of the specified skill.
    - **Decrement a Skill**: decrements the skils count by 1 and removes it if `count = 0`.
    - **Remove a Skill**: Removes the specified skill from the list if it exists.
    - **Display All Skills**: Shows all skills and their counts.
    - **Exit**: Displays a exit message and quits the program.

3. Updates the `skills.txt` file with the current list of skills and their counts after any modification.

4. Calls the `skillsSort` module to sort the skills. The sorting can be done either in descending order by count and then alphabetically for skills with the same count, or in ascending order based on a new method.

The skills and their counts are stored in the `skills.txt` file in the format `skill:count`, one skill per line. The `skillsSort` module ensures that the list is sorted appropriately after each update.

#### Requirements:
- Python 3.x
- No external libraries are required.

#### Recent Updates:
- **Test Cases Added**: Introduced test cases in `test_skillsMethods.py` to ensure the accuracy and reliability of the script's functionalities. These tests cover all the main operations such as adding, removing, decrementing, and searching for skills.
- **Enhanced Sorting Feature**: Improved the `skillsSort` module to offer more flexible sorting options, allowing users to sort skills not only by count but also alphabetically in ascending or descending order.
- **Error Handling**: Improved error handling across the script to provide clearer messages and prevent the script from exiting unexpectedly during runtime.

#### Usage:
1. Ensure Python 3.x is installed on your system.
2. Place the script and the `skillsSort` module in a directory of your choice.
3. Run the script using the command `python skillsList.py`.
4. Follow the on-screen prompts to manage skills. The script allows adding, removing, displaying, and searching for skills. It will update the counts, save them to `skills.txt`, and sort the list using the `skillsSort` module.
5. To run test cases type `python3 -m unittest`.
6. To exit the script, follow the prompts or use a keyboard interrupt (e.g., Ctrl+C in most terminals).

#### Note:
- This script handles duplicate skill entries in a case-insensitive manner by converting all entered skills to lowercase before processing.
- The `skillsSort` module is used to sort the skills list each time it is updated, ensuring the list is always in the correct order.
- The script uses a simple text file for storage, making it easy to view or edit the list of skills outside the script.
- Enhanced error handling has been implemented for file operations to ensure robustness.
- `test_skills.py` has one test case commented out, due to an error with the test case. This will be fixed in future versions.
- `test_skillsMethods.py` is a spare test script, that tests individual functions within `skillsMethods.py`.