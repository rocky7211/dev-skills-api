from infrastructure.db_repository import SQLiteRepository
from domain.skill import Skill

# Class to handle the skills service
class SkillsService:

    # Constructor
    def __init__(self, repository: SQLiteRepository) -> None:
        self.repository = repository

    # Method to display the menu
    def add_skill(self, skill_name: str) -> None:
        skill = self.repository.get_skill(skill_name)
        if skill:
            self.repository.increment_skill(skill)
        else:
            skill = Skill(skill_name)
            self.repository.add_skill(skill)

    # Method to find a skill
    def find_skill(self, skill_name: str) -> Skill:
        skill = self.repository.get_skill(skill_name)
        if skill:
            return skill
        return None
    
    # Method to decrement a skill
    def decrement_skill(self, skill_name: str) -> str:
        skill = self.repository.get_skill(skill_name)
        if skill:
            self.repository.decrement_skill(skill)
            return f"Skill decremented: {skill}"
        else:
            return "Skill not found"
        
    # Method to remove a skill
    def remove_skill(self, skill_name: str) -> str:
        skill = self.repository.get_skill(skill_name)
        if skill:
            self.repository.remove_skill(skill)
            print(f"Skill removed: {skill}")
        else:
            print("Skill not found")

    # Method to get all skills
    def get_all_skills(self) -> None:
        skills = self.repository.get_all_skills()
        print("All skills:")
        for skill in skills:
            print(skill)

    # Method to quit the application
    def quit(self) -> None:
        print("Closing connection...")
        self.repository.close_connection()
        print("Goodbye!")
        exit()