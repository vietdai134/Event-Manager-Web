# app.py

from flask import Flask
from flask_cors import CORS
from views.event_view import *
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/api/created-event/<string:gmail>', methods=['GET'])
def get_event_created(gmail):
    return get_event_created_view(gmail)
    

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

@app.route('/api/Login', methods=['GET'])  
def get_users():
    return get_users_view()

@app.route('/api/Login/<gmail>', methods=['GET'])
def get_userinfo_gmail_route(gmail):
    user_login_info = get_users_view_gmail(gmail)  # Gọi hàm controller
    if user_login_info: 
        return jsonify(user_login_info)  
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/api/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    print("Received data:", data)
    
    name = data.get('FullName')
    email = data.get('Gmail')
    phone = data.get('PhoneNumber')
    password = data.get('password')
    createat = data.get('CreatedAt')
    updateat = data.get('UpdatedAt')

    result = add_userinfo_view(name, email, phone, password, createat, updateat)
    
    return jsonify({'message': result}), 201

if __name__ == '__main__':
    app.run(debug=True)


