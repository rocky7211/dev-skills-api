from flask import jsonify, current_app
from services.skills_service import SkillsService

# Function to configure the routes
def configure_routes(app):

    # New route to get all skills
    @app.route('/api/skills/get_all_skills', methods=['GET'])
    def get_all_skills():
        skills_service = current_app.config['skills_service']
        skills = skills_service.get_all_skills()
        skills_json = [skill.to_dict() for skill in skills]
        return jsonify(skills_json)

    # New route to add a skill
    @app.route('/api/skills/add_skill/<string:skill_name>', methods=['POST'])
    def add_skill(skill_name):
        skills_service = current_app.config['skills_service']
        added = skills_service.add_skill(skill_name)
        return 201 if added else (f'Unable to add skill. Skill cannot be empty', 403)

    # New route to remove a skill
    @app.route('/api/skills/remove_skill/<string:skill_name>', methods=['DELETE'])
    def remove_skill(skill_name):
        skills_service = current_app.config['skills_service']
        removed = skills_service.remove_skill(skill_name)
        return 204 if removed else (f'Unable to remove skill. {skill_name} not found.', 404)

    # New route to decrement a skill
    @app.route('/api/skills/decrement_skill/<string:skill_name>', methods=['PUT'])
    def decrement_skill(skill_name):
        skills_service = current_app.config['skills_service']
        decremented = skills_service.decrement_skill(skill_name)
        return 204 if decremented else (f'Unable to decrement skill. {skill_name} not found.', 404)

    # New route to get a single skill
    @app.route('/api/skills/get_skill/<string:skill_name>', methods=['GET'])
    def get_skill(skill_name):
        skills_service = current_app.config['skills_service']
        skill = skills_service.find_skill(skill_name)
        return jsonify(skill.to_dict()) if skill else (f'{skill_name} not found.', 404)