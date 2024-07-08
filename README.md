# Developer Skills Tracker

This Python script is designed to maintain a list of developer skills along with their occurrence counts. It performs the following operations:

1. Checks if a file named `skills.txt` exists in the current directory. If it does, it reads the file and loads the skills and their counts into a list. If the file does not exist, it creates an empty `skills.txt` file and initializes an empty list for storing skills.

2. Enters a loop that continuously prompts the user to enter a skill. For each entered skill, the script performs the following actions:
    a. Searches the list of skills for the entered skill. If the skill is found, it increments the count associated with that skill.
    b. If the skill is not found in the list, it adds the skill with a count of 1.
    c. Updates the `skills.txt` file with the current list of skills and their counts.
    d. Calls the `skillsSort` module to sort the skills based on their counts and, for skills with the same count, alphabetically.

The skills and their counts are stored in the `skills.txt` file in the format `skill:count`, one skill per line. After each update, the `skillsSort` module ensures that the list is sorted first by count (in descending order) and then alphabetically for skills with the same count.

#### Requirements:
- Python 3.x
- No external libraries are required.

#### Usage:
1. Ensure Python 3.x is installed on your system.
2. Place the script and the `skillsSort` module in a directory of your choice.
3. Run the script using the command `python skillsList.py`.
4. Follow the on-screen prompts to enter skills. The script will update the counts, save them to `skills.txt`, and then sort the list using the `skillsSort` module.
5. To exit the script, use a keyboard interrupt (e.g., Ctrl+C in most terminals).

#### Note:
- This script handles duplicate skill entries in a case-insensitive manner by converting all entered skills to lowercase before processing.
- The `skillsSort` module is used to sort the skills list each time it is updated, ensuring the list is always in the correct order.
- The script uses a simple text file for storage, making it easy to view or edit the list of skills outside the script.