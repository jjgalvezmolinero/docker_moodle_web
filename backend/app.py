from flask import Flask
from flask_cors import CORS
import moodle_config.routes as MC

app = Flask(__name__)
CORS(app)

app.register_blueprint(MC.moodle_config, url_prefix='/config')

if __name__ == '__main__':
    app.run()