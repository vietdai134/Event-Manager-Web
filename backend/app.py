# app.py

from flask import Flask
from flask_cors import CORS
from views.event_view import *

app = Flask(__name__)
CORS(app)


@app.route('/api/created-event', methods=['GET'])
def get_event_created():
    return get_event_created_view()
    

@app.route('/api/public-event', methods=['GET'])
def get_all_event_public():
    return get_all_event_public_view()

@app.route('/api/public-event/<int:event_id>', methods=['GET'])
def get_event_public(event_id):
    event = get_event_public_view(event_id)
    if event:
        return jsonify(event)  
    else:
        return jsonify({"error": "Event not found"}), 404


@app.route('/api/registered-event', methods=['GET'])
def get_event_registered():
    return get_event_registered_view()

@app.route('/api/past-event', methods=['GET'])
def get_event_past():
    return get_event_past_view()

if __name__ == '__main__':
    app.run(debug=True)


