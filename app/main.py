"""
Description: This file is the entry point of the application.
It creates an instance of the SkillsService class and calls the menu method to start the application.
"""
import services.skills_service as service
from infrastructure.db_repository import SQLiteRepository

if __name__ == "__main__":
    repository = SQLiteRepository()
    skills_service = service.SkillsService(repository)
    skills_service.menu()
