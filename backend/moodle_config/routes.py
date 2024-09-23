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

@moodle_config.route('/get/<name>', methods=['GET'])
def get(name):
    response = MC.get_moodle_config(name)
    return jsonify(response)

@moodle_config.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    response = MC.delete_moodle_config(name)
    return jsonify(response)