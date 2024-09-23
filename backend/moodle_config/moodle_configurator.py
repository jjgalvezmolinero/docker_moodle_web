import config.mongodb as MBD

def create_moodle_config(config):
    moodle_config = {
        'MOODLE_DOCKER_PHP_VERSION': config['MOODLE_DOCKER_PHP_VERSION'],
        'COMPOSE_PROJECT_NAME': config['COMPOSE_PROJECT_NAME'],
        'MOODLE_DOCKER_APP_PATH': config['MOODLE_DOCKER_APP_PATH'],
        'MOODLE_DOCKER_WEB_HOST': config['MOODLE_DOCKER_WEB_HOST'],
        'MOODLE_DOCKER_WWWROOT': config['MOODLE_DOCKER_WWWROOT'],
        'MOODLE_DOCKER_DB_PORT': config['MOODLE_DOCKER_DB_PORT'],
        'MOODLE_DOKCER_SERVER_PORT': config['MOODLE_DOKCER_SERVER_PORT'],
        'MOODLE_DOCKER_DB': config['MOODLE_DOCKER_DB'],
        'MOODLE_DOCKER_DBNAME': config['MOODLE_DOCKER_DBNAME'],
    }
    try:
        mongo_handler = MBD.MongoHandler()
        mongo_handler.conectar()
        mongo_handler.insertar_documento('ens', moodle_config)
        mongo_handler.cerrar_conexion()
        return {'status': 'success', 'message': 'Configuracion creada exitosamente'}
    except Exception as e:
        return {'status': 'error', 'message': f'Error al crear configuracion: {e}'}

def listar_configuraciones():
    try:
        mongo_handler = MBD.MongoHandler()
        mongo_handler.conectar()
        configuraciones = mongo_handler.buscar_documentos('ens')
        mongo_handler.cerrar_conexion()
        return {'status': 'success', 'configuraciones': configuraciones}
    except Exception as e:
        return {'status': 'error', 'message': f'Error al listar configuraciones: {e}'}

def get_moodle_config(name):
    try:
        mongo_handler = MBD.MongoHandler()
        mongo_handler.conectar()
        configuracion = mongo_handler.buscar_documentos('ens', {'COMPOSE_PROJECT_NAME': name})
        mongo_handler.cerrar_conexion()
        return {'status': 'success', 'configuracion': configuracion}
    except Exception as e:
        return {'status': 'error', 'message': f'Error al obtener configuracion: {e}'}