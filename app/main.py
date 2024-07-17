"""
Description: This file is the entry point of the application.
It creates an instance of the SkillsService class and calls the menu method to start the application.
"""
import threading
import services.skills_service as service
from api.routes import configure_routes
from services.menu_handler import MenuHandler
from infrastructure.db_repository import SQLiteRepository
from flask import Flask
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)

# Add the SkillsService instance to the app's configuration
configure_routes(app)
CORS(app)

# Method to run the menu
def run_menu():
    MenuHandler(app.config['skills_service']).menu()

# Entry point of the application
if __name__ == "__main__":
    # Create an instance of the SkillsService class
    skills_service = service.SkillsService(SQLiteRepository())
    app.config['skills_service'] = skills_service

    # Start the menu in a separate thread
    menu_thread = threading.Thread(target=run_menu)
    menu_thread.start()

    # Start the Flask app
    app.run(debug=True)