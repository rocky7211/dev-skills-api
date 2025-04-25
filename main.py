"""
Description: This file is the entry point of the application.
It creates an instance of the SkillsService class and adds it to the Flask app's configuration.
"""
import sys
import os

# Add the 'app' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

import app.services.skills_service as service
from app.api.routes import configure_routes
from app.infrastructure.db_repository import PostgreSQLRepository
from flask import Flask
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)

# Add the SkillsService instance to the app's configuration
configure_routes(app)
CORS(app)

# Entry point of the application
if __name__ == "__main__":
    # Connect to the PostgreSQL database
    db_url = os.environ.get("DATABASE_URL")
    if db_url is None:
        raise ValueError("DATABASE_URL environment variable not set")
    skills_service = service.SkillsService(PostgreSQLRepository(db_url))
    app.config['skills_service'] = skills_service

    # Start the Flask app
    app.run(debug=False, host='0.0.0.0')
