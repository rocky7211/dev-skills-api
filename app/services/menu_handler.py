from services.skills_service import SkillsService

# Class to handle the menu options
class MenuHandler:

    # Constructor
    def __init__(self, skill_service: SkillsService) -> None:
        self.skill_service = skill_service

    # Method to display the menu
    def menu(self) -> None:
        print("\nWelcome! Type the number of the option you would like to choose:")
        print("1. Add a skill")
        print("2. Find a skill")
        print("3. Decrement a skill")
        print("4. Delete a skill")
        print("5. View skills")
        print("6. Exit")

        user_input = input("Enter a number: ")
        if user_input == "1":
            self.add_skill_handler()
            self.menu()
        elif user_input == "2":
            self.find_skill_handler()
            self.menu()
        elif user_input == "3":
            self.decrement_skill_handler()
            self.menu()
        elif user_input == "4":
            self.remove_skill_handler()
            self.menu()
        elif user_input == "5":
            self.get_skills_handler()
            self.menu()
        elif user_input == "6":
            self.skill_service.quit()
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
            self.menu()
        
    # Method to repeat the input
    def repeat_input_handler(self, method: callable, action: str) -> None:
        repeat = input(f"Would you like to {action} another skill? (y/n): ").lower()
        if repeat == "y":
            method()

    # Method to get the skill name from the user
    def user_input_handler(self) -> str:
        skill_name = input("Enter the skill name: ").lower()
        if skill_name == "":
            print("Skill name cannot be empty")
            return self.user_input_handler()
        return skill_name

    # Method to handle the add skill input
    def add_skill_handler(self) -> None:
        skill_name = self.user_input_handler()
        self.skill_service.add_skill(skill_name)
        self.repeat_input_handler(self.add_skill_handler, "add")

    # Method to handle the find skill input
    def find_skill_handler(self) -> None:
        skill_name = self.user_input_handler()
        skill = self.skill_service.find_skill(skill_name)
        if skill:
            print(skill)
        else:
            print("Skill not found")
        self.repeat_input_handler(self.find_skill_handler, "find")

    # Method to handle the decrement skill input
    def decrement_skill_handler(self) -> None:
        skill_name = self.user_input_handler()
        result = self.skill_service.decrement_skill(skill_name)
        print(result)
        self.repeat_input_handler(self.decrement_skill_handler, "decrement")

    # Method to handle the remove skill input
    def remove_skill_handler(self) -> None:
        skill_name = self.user_input_handler()
        result = self.skill_service.remove_skill(skill_name)
        print(result)
        self.repeat_input_handler(self.remove_skill_handler, "remove")

    def get_skills_handler(self) -> None:
        skills = self.skill_service.get_all_skills()
        for skill in skills:
            print(skill)