#app.py
from flask import Flask
from config import Config
from models import db
from flasgger import Swagger
from routes import api

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

swagger = Swagger(app)
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

