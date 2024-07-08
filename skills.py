import os
import skillsMethods

# A simple script to store and display a list of developer skills

# Check if `skills.txt` exists
if os.path.exists('skills.txt'):
    # Read the file and store the skills in a list
    with open('skills.txt', 'r') as file:
        skills = [line.split(':') for line in file.read().splitlines()]
        skills = [[skill, int(count)] for skill, count in skills]
else:
    # Create the file and initialize an empty list
    open('skills.txt', 'w').close()
    skills = []

while True:
    # Ask the user for a skill
    skill = input("Enter a skill: ").lower() 
    found = False

    # Check if the skill is in the list and update the count
    for i in range(len(skills)):
        if skill == skills[i][0]:
            skills[i][1] += 1
            found = True
            break

    if not found:
        # Add the skill to the list with a count of 1
        skills.append([skill, 1])

    # Write the updated list to `skills.txt`
    with open('skills.txt', 'w') as file:
        for skill, count in skills:
            file.write(f"{skill}:{count}\n")

    # Read the file and print the skills
    with open('skills.txt', 'r') as file:
        print("Skills:")
        print(file.read())

    # Ask the user if they want to add another skill
    choice = input("Do you want to add another skill? (y/n): ")
    if choice.lower() != "y":
        break
    
# Sort the skills by count in descending order once the user is done    
# skillsMethods.decrementSkill(skills)
# skillsMethods.sort(skills)
# skillsMethods.deleteSkill(skills)