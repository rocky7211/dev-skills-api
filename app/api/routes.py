from flask import jsonify, current_app, request, render_template
import html
from services.skills_service import SkillsService

# Function to configure the routes
def configure_routes(app):

    @app.route('/')
    def root():
        return render_template("index.html")

    # New route to get all skills
    @app.route('/skills/get_all_skills', methods=['GET'])
    def get_all_skills():
        skills_service = current_app.config['skills_service']
        skills = skills_service.get_all_skills()
        skills_json = [skill.to_dict() for skill in skills]
        return jsonify(skills_json)

    # New route to add a skill
    @app.route('/skills/add_skill', methods=['POST'])
    def add_skill():
        skill_name = request.json.get('skill_name')
        skills_service = current_app.config['skills_service']
        added = skills_service.add_skill(skill_name)
        if added:
            return jsonify({'success': 'Skill added successfully'}), 201
        else:
            return jsonify({'error': 'Unable to add skill. Skill cannot be empty'}), 403

    # New route to remove a skill
    @app.route('/skills/remove_skill', methods=['DELETE'])
    def remove_skill():
        skill_name = request.json.get('skill_name')
        skills_service = current_app.config['skills_service']
        removed = skills_service.remove_skill(skill_name)
        if removed:
            return jsonify({'success': 'Skill removed successfully'}), 204
        else:
            return jsonify({'error': 'Unable to remove skill. Skill not found'}), 404
        
    # New route to decrement a skill
    @app.route('/skills/decrement_skill', methods=['PUT'])
    def decrement_skill():
        skill_name = request.json.get('skill_name')
        skills_service = current_app.config['skills_service']
        decremented = skills_service.decrement_skill(skill_name)
        if decremented:
            return jsonify({'success': 'Skill decremented successfully'}), 200
        else:
            return jsonify({'error': 'Unable to decrement skill. Skill not found'}), 404
        
    # New route to get a single skill
    @app.route('/skills/get_skill', methods=['GET'])
    def get_skill():
        skill_name = request.args.get('skill_name')
        skills_service = current_app.config['skills_service']
        skill = skills_service.find_skill(skill_name)
        return jsonify(skill.to_dict()) if skill else (f'{html.escape(skill_name)} not found.', 404)