from skill import Skill
from typing import List

class ISkillsRepository:
    def get_skills(self, user_id: int) -> List[Skill]:
        raise NotImplementedError

    def add_skill(self, user_id: int, skill: Skill) -> None:
        raise NotImplementedError

    def remove_skill(self, user_id: int, skill_id: int) -> None:
        raise NotImplementedError

    def update_skill(self, user_id: int, skill: Skill) -> None:
        raise NotImplementedError