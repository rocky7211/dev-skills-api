from infrastructure.db_repository import SQLiteRepository
from domain.skill import Skill

class SkillsService:

    def __init__(self, repository: SQLiteRepository) -> None:
        self.repository = repository

    def add_skill(self) -> None:
        skillName = input("Enter the skill name: ").lower()
        if not skillName:
            print("Skill name cannot be empty")
            return self.add_skill()
        
        skill = self.repository.get_skill(skillName)

        if skill:
            self.repository.increment_skill(skill)
        else:
            skill = Skill(skillName)
            self.repository.add_skill(skill)
        
        repeat = input("Would you like to decrement another skill? (y/n): ")

        if repeat.lower() == "y":
            self.add_skill()
        else:
            self.menu()
    
    def remove_skill(self) -> None:
        skill_name = input("Enter a skill to delete: ").lower()
        if skill_name == "":    
            print("Skill name cannot be empty")
            return self.remove_skill()
        skill = self.repository.get_skill(skill_name)
        if skill:
            self.repository.remove_skill(skill)
            print(f"Skill removed: {skill}")
        else:
            print("Skill not found")

        repeat = input("Would you like to delete another skill? (y/n): ")
        if repeat.lower() == "y":
            self.remove_skill()
        else:
            self.menu()

    def decrement_skill(self) -> None:
        skill_name = input("Enter a skill to decrement: ").lower()
        if skill_name == "":
            print("Skill name cannot be empty")
            return self.decrement_skill()
        
        skill = self.repository.get_skill(skill_name)

        if skill:
            if skill.get_count() > 1:
                self.repository.decrement_skill(skill)
                print(f"Skill decremented: {skill}")
            else:
                print("Skill count is 0, deleting skill instead")
                self.repository.remove_skill(skill)
        else:
            print("Skill not found")

        repeat = input("Would you like to decrement another skill? (y/n): ")
        if repeat.lower() == "y":
            self.decrement_skill()
        else:
            self.menu()
    
    def view_skills(self, user_id: int) -> None:
        skills = self.repository.get_skills(user_id)
        for skill in skills:
            print(f"{skill.name}: {skill.count}")
    
    def find_skill(self) -> None:
        user_input = input("Enter a skill to find: ").lower()
        if user_input == "":
            print("Skill name cannot be empty")
            return self.find_skill()
        skill = self.repository.get_skill(user_input)
        if skill:
            print(skill)
        else:
            print("Skill not found")

        repeat = input("Would you like to find another skill? (y/n): ")
        if repeat.lower() == "y":
            self.find_skill()
        else:
            self.menu()

    def get_all_skills(self) -> None:
        skills = self.repository.get_all_skills()
        print("All skills:")
        for skill in skills:
            print(skill)
        self.menu()
    
    def quit(self) -> None:
        print("Closing connection...")
        self.repository.close_connection()
        print("Goodbye!")
        exit()

    # A menu to add, decrement, delete, find, and exit
    def menu(self):
        print("\nWelcome! Type the number of the option you would like to choose:")
        print("1. Add a skill")
        print("2. Find a skill")
        print("3. Decrement a skill")
        print("4. Delete a skill")
        print("5. View skills")
        print("6. Exit")
        user_input = input("Enter a number: ")

        if user_input == "1":
            self.add_skill()
        elif user_input == "2":
            self.find_skill()
        elif user_input == "3":
            self.decrement_skill()
        elif user_input == "4":
            self.remove_skill()
        elif user_input == "5":
            self.get_all_skills()
        elif user_input == "6":
            self.quit()
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
            return self.menu()

