from flask import Flask
from flask_cors import CORS
from pytz import timezone
from api.routes import nepse_insighter_api

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(nepse_insighter_api, url_prefix='/api')
    return app

ist = timezone('Asia/Kathmandu')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
