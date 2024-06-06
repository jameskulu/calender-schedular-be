from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_pyfile("config.py")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./calender.sqlite3"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
scheduler = BackgroundScheduler()
scheduler.start()

from routes import *

api.add_resource(EventResource, "/events")
api.add_resource(EventDetailResource, "/events/<int:event_id>")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
