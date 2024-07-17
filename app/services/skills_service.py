from infrastructure.db_repository import SQLiteRepository
from domain.skill import Skill
from typing import List

# Class to handle the skills service
class SkillsService:

    # Constructor
    def __init__(self, repository: SQLiteRepository) -> None:
        self.repository = repository

    # Method to display the menu
    def add_skill(self, skill_name: str) -> bool:
        if skill_name == "":
            return False
        
        skill = self.repository.get_skill(skill_name)

        if skill:
            self.repository.increment_skill(skill)
        else:
            skill = Skill(skill_name)
            self.repository.add_skill(skill)
        return True

    # Method to find a skill
    def find_skill(self, skill_name: str) -> Skill:
        skill = self.repository.get_skill(skill_name)
        if skill:
            return skill
        return None
    
    # Method to decrement a skill
    def decrement_skill(self, skill_name: str) -> bool:
        skill = self.repository.get_skill(skill_name)
        if not skill:
            return False
        if skill and skill.get_count() > 1:
            self.repository.decrement_skill(skill)
        elif skill:
            self.repository.remove_skill(skill)
        return True

    # Method to remove a skill
    def remove_skill(self, skill_name: str) -> bool:
        skill = self.repository.get_skill(skill_name)
        if skill:
            self.repository.remove_skill(skill)
            return True
        return False

    # Method to get all skills
    def get_all_skills(self) -> List[Skill]:
        skills = self.repository.get_all_skills()
        return skills

    # Method to quit the application
    def quit(self) -> None:
        print("Closing connection...")
        self.repository.close_connection()
        print("Goodbye!")
        exit()