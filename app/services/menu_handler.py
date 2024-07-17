class MenuHandler:
    def __init__(self, skill_service):
        self.skill_service = skill_service

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
            self.add_skill_input()
        elif user_input == "2":
            self.find_skill_input()
        elif user_input == "3":
            self.decrement_skill_input()
        elif user_input == "4":
            self.remove_skill_input()
        elif user_input == "5":
            self.skill_service.get_all_skills()
        elif user_input == "6":
            self.quit()
        else:
            print("Invalid input. Please enter a number between 1 and 6.")
            return self.menu()

    def repeat_input(self, method: callable, action: str) -> None:
        repeat = input(f"Would you like to {action} another skill? (y/n): ").lower()
        if repeat == "y":
            method()
        else:
            self.menu()

    def user_skill_input(self) -> str:
        skill_name = input("Enter the skill name: ").lower()
        if skill_name == "":
            print("Skill name cannot be empty")
            return self.user_skill_input()
        return skill_name

    def add_skill_input(self) -> None:
        skill_name = self.user_skill_input()
        self.skill_service.add_skill(skill_name)
        self.repeat_input(self.add_skill_input, "add")

    def find_skill_input(self) -> None:
        skill_name = self.user_skill_input()
        skill = self.skill_service.find_skill(skill_name)
        if skill:
            print(skill)
        else:
            print("Skill not found")
        self.repeat_input(self.find_skill_input, "find")

    def decrement_skill_input(self) -> None:
        skill_name = self.user_skill_input()
        result = self.skill_service.decrement_skill(skill_name)
        print(result)
        self.repeat_input(self.decrement_skill_input, "decrement")

    def remove_skill_input(self) -> None:
        skill_name = self.user_skill_input()
        result = self.skill_service.remove_skill(skill_name)
        print(result)
        self.repeat_input(self.remove_skill_input, "remove")
