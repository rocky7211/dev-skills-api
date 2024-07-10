from typing import Any, List
from domain.skill import Skill
from services.skills_service import SkillsService

class FileRepository:
    def get_all_skills(self, user_id: int) -> List[Skill]:
        pass

    def add_skill(self, user_id: int, skill: Skill) -> None:
        pass

    def remove_skill(self, user_id: int, skill: Skill) -> None:
        pass

    def decrement_skill(self, user_id: int, skill: Skill) -> None:
        pass

    def update_skill(self, user_id: int, skill: Skill) -> None:
        pass

    def get_skill(self, user_id: int, skill_name: str) -> Skill:
        pass

    @staticmethod
    def sort(skills: List[Skill]) -> List[Skill]:
        return sorted(skills, key=lambda x: x.count, reverse=True)

    @staticmethod
    def find_skill(skills: List[Skill]) -> None:
        skill = input("Enter a skill to find: ").lower()
        found = False

        for skill_obj in skills:
            if skill == skill_obj.name.lower():
                print(f"Skill found: {skill_obj.name}: {skill_obj.count}")
                found = True
                break

        if not found:
            print("Skill not found")

        repeat = input("Would you like to find another skill? (y/n): ")
        if repeat.lower() == "y":
            FileRepository.find_skill(skills)
        else:
            SkillsService.menu(skills)

    @staticmethod
    def decrement_skill(skills: List[Skill]) -> None:
        skill = input("Enter a skill to decrement: ").lower()
        found = False

        for skill_obj in skills:
            if skill == skill_obj.name.lower():
                skill_obj.count -= 1
                found = True

                if skill_obj.count == 0:
                    skills.remove(skill_obj)
                
                break

        if not found:
            print("Skill not found")
        else:
            FileRepository.update_file(skills)

        repeat = input("Would you like to decrement another skill? (y/n): ")
        if repeat.lower() == "y":
            FileRepository.decrement_skill(skills)
        else:
            SkillsService.menu(FileRepository.sort(skills))

    @staticmethod
    def delete_skill(skills: List[Skill]) -> None:
        skill = input("Enter a skill to delete: ").lower()
        found = False

        for skill_obj in skills:
            if skill == skill_obj.name.lower():
                skills.remove(skill_obj)
                found = True
                break

        if not found:
            print("Skill not found")
        else:
            FileRepository.update_file(skills)
        
        repeat = input("Would you like to delete another skill? (y/n): ")
        if repeat.lower() == "y":
            FileRepository.delete_skill(skills)
        else:
            SkillsService.menu(skills)

    @staticmethod
    def view_skills(skills: List[Skill]) -> None:
        print("Skills:")
        for skill_obj in skills:
            print(f"{skill_obj.name}: {skill_obj.count}")
        SkillsService.menu(skills)

    @staticmethod
    def exit_program() -> None:
        print("Exiting the program")
        quit()

    @staticmethod
    def add_skill(skills: List[Skill]) -> List[Skill]:
        skills_dict = {skill.name: skill.count for skill in skills}
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

            updated_skills = sorted([Skill(name, count) for name, count in skills_dict.items()], key=lambda x: x.name)

            with open('skills.txt', 'w') as file:
                for skill_obj in updated_skills:
                    file.write(f"{skill_obj.name}:{skill_obj.count}\n")

            SkillsService.menu(FileRepository.sort(updated_skills))
            return updated_skills
        except Exception as e:
            print(f"An error occurred: {e}")
            return skills
