import app.services.skills_service as skillsService
from app.infrastructure.db_repository import db_repository
from app.domain.skill import Skill

# A simple script to store and display a list of developer skills

def addSkill(skills):
    skills_dict = {skill[0]: skill[1] for skill in skills}  # Convert list to dictionary for efficient lookup
    try:
        while True:
            skill = input("Enter a skill: ").lower()
            if skill in skills_dict:
                skills_dict[skill] += 1
            else:
                skills_dict[skill] = 1

            repeat = input("Would you like to add another skill? (y/n): ")
            if repeat.lower() != "y":
                break

        # Convert dictionary back to list format and sort it
        updated_skills = sorted([[skill, count] for skill, count in skills_dict.items()], key=lambda x: x[0])

        # Write the updated list to `skills.txt` once
        with open('skills.txt', 'w') as file:
            for skill, count in updated_skills:
                file.write(f"{skill}:{count}\n")

        skillsService.menu(skillsService.sort(updated_skills))  # Update the menu with sorted skills
        return updated_skills  # Return the updated skills list for further use
    except Exception as e:
        print(f"An error occurred: {e}")
        return skills  # Return the original skills list in case of an error

# Assuming skillsMethods.createSkillsFile() returns a list of skills
skills = skillsService.createSkillsFile()

if skillsService.menu(skills):
    updated_skills = addSkill(skills)