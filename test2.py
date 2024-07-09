"""
import os
from skillsMethods import createSkillsFile, readFile
# Function to simulate deletion of skills.txt for testing
def delete_skills_file():
    if os.path.exists('skills.txt'):
        os.remove('skills.txt')

# Function to create a predefined skills.txt for testing readFile
def create_predefined_skills_file():
    with open('skills.txt', 'w') as file:
        file.write('Python:5\n')
        file.write('JavaScript:3\n')
        file.write('InvalidLine\n')
        file.write('Java:Two\n')

# Test createSkillsFile
delete_skills_file()
skills = createSkillsFile()
assert os.path.exists('skills.txt'), "skills.txt was not created."
print("createSkillsFile test passed when file does not exist.")

skills = createSkillsFile()
assert isinstance(skills, list), "createSkillsFile did not return a list when file exists."
print("createSkillsFile test passed for existing file.")

# Test readFile
create_predefined_skills_file()
skills = readFile()
expected_skills = [['Python', 5], ['JavaScript', 3]]
assert skills == expected_skills, f"readFile did not return the expected list. Returned: {skills}"
print("readFile test passed.")
"""