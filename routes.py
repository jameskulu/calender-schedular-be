import os
from datetime import datetime

import requests
from flask import jsonify, request
from flask_restful import Api, Resource

from app import app, db
from models import Event
from notifications import schedule_notification

api = Api(app)


class EventResource(Resource):
    def get(self):
        events = Event.query.all()
        return jsonify([event.json() for event in events])

    def post(self):
        data = request.get_json()
        print(data)

        # Field validation
        # if not data.get("title"):
        #     return jsonify({"error": "Title is required"}), 400
        # if not data.get("start_time"):
        #     return jsonify({"error": "Start time is required"}), 400
        # if not data.get("end_time"):
        #     return jsonify({"error": "End time is required"}), 400

        # try:
        #     start_time = datetime.fromisoformat(data["start_time"])
        #     end_time = datetime.fromisoformat(data["end_time"])
        # except ValueError:
        #     return jsonify({"error": "Invalid date format"}), 400

        # if start_time >= end_time:
        #     return jsonify({"error": "Start time must be before end time"}), 400

        # # Check for time conflicts
        # conflicting_events = Event.query.filter(
        #     db.or_(
        #         db.and_(Event.start_time <= start_time, Event.end_time > start_time),
        #         db.and_(Event.start_time < end_time, Event.end_time >= end_time),
        #         db.and_(Event.start_time >= start_time, Event.end_time <= end_time),
        #     )
        # ).all()

        # if conflicting_events:
        #     return (
        #         jsonify({"error": "Event time conflicts with an existing event"}),
        #         400,
        #     )

        new_event = Event(
            title=data["title"],
            description=data["description"],
            start_time=datetime.fromisoformat(data["start_time"]),
            end_time=datetime.fromisoformat(data["end_time"]),
            timezone=data["timezone"] if data.get("timezone") else None,
            participants=data["participants"] if data.get("participants") else None,
        )
        db.session.add(new_event)
        db.session.commit()
        # schedule_notification(new_event)
        return new_event.json(), 201


class EventDetailResource(Resource):

    def get(self, event_id):
        event = Event.query.get_or_404(event_id)
        return event.json(), 200

    def put(self, event_id):
        data = request.get_json()
        event = Event.query.get_or_404(event_id)

        event.title = data.get("title", event.title)
        event.description = data.get("description", event.description)
        event.start_time = (
            datetime.fromisoformat(data["start_time"])
            if "start_time" in data
            else event.start_time
        )
        event.end_time = (
            datetime.fromisoformat(data["end_time"])
            if "end_time" in data
            else event.end_time
        )
        event.timezone = data.get("timezone", event.timezone)
        event.participants = data.get("participants", event.participants)

        db.session.commit()
        return event.json(), 200

    def delete(self, event_id):
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return "", 204
