import os

# A menu to add, decrement, delete, find, and exit
def menu(skills):
    print("\nWelcome! Type the number of the option you would like to choose:")
    print("1. Add a skill")
    print("2. Decrement a skill")
    print("3. Delete a skill")
    print("4. Find a skill")
    print("5. View skills")
    print("6. Exit")
    user_input = input("Enter a number: ")

    if user_input == "1":
        return 1
    elif user_input == "2":
        decrementSkill(skills)
    elif user_input == "3":
        deleteSkill(skills)
    elif user_input == "4":
        findSkill(skills)
    elif user_input == "5":
        viewSkills(skills)
    elif user_input == "6":
        exit()
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
        return menu(skills)

# The sort function takes a list of skills and sorts it by count in descending order.
def sort(skills):
    skills.sort(key=lambda x: (x[1], x[0]), reverse=True)
    with open('skills.txt', 'w') as file:
        for skill, count in skills:
            file.write(f"{skill}:{count}\n")
    with open('skills.txt', 'r') as file:
        skills = [line.split(':') for line in file.read().splitlines()]
        skills = [[skill, int(count)] for skill, count in skills]
        print("Skills:")
        print(file.read())

# The findSkill function takes a list of skills and asks the user for a skill to find.
def findSkill(skills):
    # Ask the user for a skill to find
    skill = input("Enter a skill to find: ").lower()
    found = False

    # Check if the skill is in the list
    for i in range(len(skills)):
        if skill == skills[i][0]:
            print(f"Skill found: {skills[i][0]}: {skills[i][1]}")
            found = True
            break

    if not found:
        print("Skill not found")

    repeat = input("Would you like to find another skill? (y/n): ")
    if repeat.lower() == "y":
        findSkill(skills)
    else:
        menu(skills)

# The decrementSkill function takes a list of skills and asks the user for a skill to decrement.
def decrementSkill(skills):
    # Ask the user for a skill to decrement
    skill = input("Enter a skill to delete: ").lower()
    found = False

    # Check if the skill is in the list and update the count
    for i in range(len(skills)):
        if skill == skills[i][0]:
            skills[i][1] -= 1
            found = True

            # Remove the skill if the count is 0
            if skills[i][1] == 0:
                skills.pop(i)
            
            break

    if not found:
        print("Skill not found")
    else:
        # Write the updated list to `skills.txt`
        with open('skills.txt', 'w') as file:
            for skill, count in skills:
                file.write(f"{skill}:{count}\n")
        with open('skills.txt', 'r') as file:
            skills = [line.split(':') for line in file.read().splitlines()]
            skills = [[skill, int(count)] for skill, count in skills]
            print("Skills:")
            print(file.read())

    repeat = input("Would you like to decrement another skill? (y/n): ")
    if repeat.lower() == "y":
        decrementSkill(skills)
    else:
        menu(skills)

# The deleteSkill function takes a list of skills and asks the user for a skill to delete.
def deleteSkill(skills):
    # Ask the user for a skill to delete
    skill = input("Enter a skill to delete: ").lower()
    found = False

    # Check if the skill is in the list and update the count
    for i in range(len(skills)):
        if skill == skills[i][0]:
            skills.pop(i)
            found = True
            break

    if not found:
        print("Skill not found")
    else:
        # Write the updated list to `skills.txt`
        with open('skills.txt', 'w') as file:
            for skill, count in skills:
                file.write(f"{skill}:{count}\n")
        with open('skills.txt', 'r') as file:
            skills = [line.split(':') for line in file.read().splitlines()]
            skills = [[skill, int(count)] for skill, count in skills]
            print("Skills:")
            print(file.read())
    
    repeat = input("Would you like to delete another skill? (y/n): ")
    if repeat.lower() == "y":
        deleteSkill(skills)
    else:
        menu(skills)

def createSkillsFile():
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
    return skills

def viewSkills(skills):
    # Read the file and print the skills
    print("Skills:")
    for i in range(len(skills)):
        print(f"{skills[i][0]}: {skills[i][1]}")
    menu(skills)

# The exit function prints a message and exits the program.
def exit():
    print("Exiting the program")
    quit()