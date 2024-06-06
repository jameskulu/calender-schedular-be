from app import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    timezone = db.Column(db.String(50), nullable=True)
    participants = db.Column(db.String(255), nullable=True)

    def __init__(
        self, title, description, start_time, end_time, timezone, participants
    ):
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.timezone = timezone
        self.participants = participants

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time.isoformat() + "Z",
            "end_time": self.end_time.isoformat() + "Z",
            "timezone": self.timezone,
            "participants": self.participants,
        }
