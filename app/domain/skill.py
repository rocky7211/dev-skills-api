
# This file contains the Skill class which is used to represent a skill in the system.
class Skill():

    def __init__(self, name: str, count = 1) -> None:
        self.name = name
        self.count = count

    def get_count (self) -> int:
        return self.count
    
    def get_name (self) -> str:
        return self.name
    
    def set_count (self, count: int) -> None:
        if count < 0:
            raise ValueError("Count cannot be negative")
        self.count = count

    def set_name (self, name: str) -> None:
        self.name = name

    def increment_count (self) -> None:
        self.count += 1
    
    def decrement_count (self) -> None:
        self.count -= 1

    def to_dict(self) -> dict:
        return {"name": self.name, "count": self.count}
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Skill):
            return False
        return self.name == other.name and self.count == other.count
    
    def __str__(self) -> str:
        return f"{self.name}: {self.count}"