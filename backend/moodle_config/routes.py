from flask import Blueprint, request, jsonify
import moodle_config.moodle_configurator as MC

moodle_config = Blueprint('moodle_config', __name__)

@moodle_config.route('/create', methods=['POST'])
def create():
    config = request.json
    response = MC.create_moodle_config(config)
    return jsonify(response)

@moodle_config.route('/list', methods=['GET'])
def list():
    response = MC.listar_configuraciones()
    return jsonify(response)

