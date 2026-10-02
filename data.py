# In-memory event storage. Data resets each time the server restarts.
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]


def next_event_id():
    """Return the next unique ID for a new event."""
    return max((e["id"] for e in events), default=0) + 1


def find_event_by_id(event_id):
    """Return the event with the given ID, or None if it doesn't exist."""
    return next((e for e in events if e["id"] == event_id), None)
