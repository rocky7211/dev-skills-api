
# The sort function takes a list of skills and sorts it by count in descending order.
def sort(skills):
    skills.sort(key=lambda x: (x[1], x[0]), reverse=True)
    with open('skills.txt', 'w') as file:
        for skill, count in skills:
            file.write(f"{skill}:{count}\n")
    with open('skills.txt', 'r') as file:
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
            print("Skills:")
            print(file.read())

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
            print("Skills:")
            print(file.read())

    