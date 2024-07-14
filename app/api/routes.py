from flask import Flask, jsonify, request
from infrastructure.db_repository import SQLiteRepository
import services.skills_service as service

app = Flask(__name__)
repository = SQLiteRepository()
skills_service = service.SkillsService(repository)

@app.route('api/skills', methods=['GET'])
def get_all_skills():
    skills = skills_service.get_all_skills()
    return jsonify(skills)

@app.route('api/skills', methods=['POST'])
def add_skill():
    skill = request.json
    skills_service.add_skill(skill)
    return '', 201

@app.route('api/skills', methods=['DELETE'])
def remove_skill():
    skill = request.json
    skills_service.remove_skill(skill)
    return '', 204

@app.route('api/skills', methods=['PUT'])
def decrement_skill():
    skill = request.json
    skills_service.decrement_skill(skill)
    return '', 204

@app.route('api/skills', methods=['GET'])
def get_skill():
    skill = request.json
    skill = skills_service.find_skill(skill)
    return jsonify(skill)

if __name__ == '__main__':
    app.run(debug=True)

