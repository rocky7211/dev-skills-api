import os

# The FileService class contains functions to read, update, and create a file with a list of skills.
class FileService:
    # The readFile function reads the skills from a specified file and returns a list of skills.
    def readFile(file_path):
        skills = []
        with open(file_path, 'r') as file:
            for line in file.read().splitlines():
                parts = line.split(':')
                if len(parts) == 2:
                    skill, count = parts
                    try:
                        skills.append([skill, int(count)])
                    except ValueError:
                        # Handle or log the error, e.g., print a warning
                        print(f"Warning: Skipping invalid count for skill '{skill}': {count}")
                else:
                    # Handle lines that do not conform to the expected format
                    print(f"Warning: Skipping malformed line: {line}")
        return skills

    # The updateFile function takes a list of skills and writes it to a specified file, then updates the skills list.
    def updateFile(file_path, skills):
        # Write the updated list to the specified file
        with open(file_path, 'w') as file:
            for skill, count in skills:
                file.write(f"{skill}:{count}\n")
        return FileService.readFile(file_path)

    # The createSkillsFile function checks if the specified file exists and returns the skills list.
    def createSkillsFile(file_path):
        # Check if the specified file exists
        if os.path.exists(file_path):
            skills = FileService.readFile(file_path)
        else:
            # Create the file and initialize an empty list
            with open(file_path, 'w') as file:
                file.write('')
            skills = []
        return skills
