from flask import Flask, jsonify, request
from flask_cors import CORS

from data import events, next_event_id, find_event_by_id

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Event Catalog!"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = find_event_by_id(event_id)
    if event is None:
        return jsonify({"error": f"Event {event_id} not found"}), 404
    return jsonify(event), 200


@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Title is required"}), 400

    new_event = {"id": next_event_id(), "title": title.strip()}
    events.append(new_event)
    return jsonify(new_event), 201


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
