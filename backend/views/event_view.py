# views/event_view.py

from flask import jsonify
from controllers.event_controller import *

def get_event_created_view(gmail):
    events = get_event_created_controller(gmail)
    return jsonify(events)

def get_all_event_public_view():
    events = get_all_event_public_controller()
    return jsonify(events)

def get_event_public_view(event_id):
    events = get_event_public_controller(event_id)
    return events

def get_event_registered_view():
    events = get_event_registered_controller()
    return jsonify(events)

def get_event_past_view():
    events = get_event_past_controller()
    return jsonify(events)

def get_users_view():
    users = get_users_controller() 
    return jsonify(users)

def get_users_view_gmail(gmail):
    users = get_users_gmail_controller(gmail) 
    if users:  # Kiểm tra nếu có người dùng
        return users
    return None
def add_userinfo_view(name, email, phone, password, createat, updateat):
    user = add_userinfo_controller(name, email, phone, password, createat, updateat)
    return user
