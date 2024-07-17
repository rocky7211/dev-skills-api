from flask import jsonify, current_app

# Function to configure the routes
def configure_routes(app):

    # New route to get all skills
    @app.route('/api/skills', methods=['GET'])
    def get_all_skills():
        skills_service = current_app.config['skills_service']
        skills = skills_service.get_all_skills()
        return jsonify(skills)

    # New route to add a skill
    @app.route('/api/skills/<string:skill_name>', methods=['POST'])
    def add_skill(skill_name):
        skills_service = current_app.config['skills_service']
        skills_service.add_skill(skill_name)
        return '', 201

    # New route to remove a skill
    @app.route('/api/skills/<string:skill_name>', methods=['DELETE'])
    def remove_skill(skill_name):
        skills_service = current_app.config['skills_service']
        skills_service.remove_skill(skill_name)
        return '', 204

    # New route to decrement a skill
    @app.route('/api/skills/<string:skill_name>', methods=['PUT'])
    def decrement_skill(skill_name):
        skills_service = current_app.config['skills_service']
        skills_service.decrement_skill(skill_name)
        return '', 204

    # New route to get a single skill
    @app.route('/api/skills/<string:skill_name>', methods=['GET'])
    def get_skill(skill_name):
        skills_service = current_app.config['skills_service']
        skill = skills_service.find_skill(skill_name)
        return jsonify(skill)