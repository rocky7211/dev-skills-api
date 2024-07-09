import skillsMethods

# A simple script to store and display a list of developer skills

# Check if `skills.txt` exists and returns the skills list
skills = skillsMethods.createSkillsFile()

def addSkill(skills):
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

        # Ask the user if they want to add another skill
        repeat = input("Would you like to add another skill? (y/n): ")
        if repeat.lower() == "y":
            addSkill(skills)
        else:
            skillsMethods.menu(skillsMethods.sort(skills))

# Checks to see if the user wants to add a skill
if skillsMethods.menu(skills):
    addSkill(skills)