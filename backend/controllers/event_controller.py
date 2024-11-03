# controllers/event_controller.py

from models.event_model import *

def get_event_created_controller(gmail):
    return get_all_event_created(gmail)

def get_all_event_public_controller():
    return get_all_event_Public()

def get_event_public_controller(event_id):
    return get_event_Public(event_id)

def get_event_registered_controller(gmail):
    return get_all_event_registered(gmail)

def get_event_past_controller(gmail):
    return get_all_event_past(gmail)

def get_users_controller():
    return get_users()

def get_users_gmail_controller(gmail):
    return get_users_gmail_model(gmail)

def add_userinfo_controller(name, email, phone, password, createat, updateat):
    return add_userinfo_model(name, email, phone, password, createat, updateat)

def register_event_controller(event_id,gmail):
    return register_event(event_id, gmail)
