from flask import Flask
from config import Config
from models import db
from routes import api

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
