# views/event_view.py

from flask import jsonify
from controllers.event_controller import *

def get_event_created_view(gmail):
    events = get_event_created_controller(gmail)
    return jsonify(events)

def get_all_event_public_view(gmail):
    events = get_all_event_public_controller(gmail)
    return jsonify(events)

def get_event_public_view(event_id):
    events = get_event_public_controller(event_id)
    return events

def get_event_registered_view(gmail):
    events = get_event_registered_controller(gmail)
    return jsonify(events)

def get_event_past_view(gmail):
    events = get_event_past_controller(gmail)
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

def register_event_view(event_id,gmail):
    return register_event_controller(event_id,gmail)

def cancel_register_view(gmail,event_id):
    return cancel_register_controller(gmail,event_id)

def delete_event_view(gmail,event_id):
    return delete_event_controller(gmail,event_id)

def add_event_view(EventType, EventName,StartTime,EndTime,
                         Location,EventImages,Description,RegisteredCount
                         ,MaxAttendees,Gmail):
    return add_event_controller(EventType, EventName,StartTime,EndTime,
                         Location,EventImages,Description,RegisteredCount
                         ,MaxAttendees,Gmail)
    
def edit_user_view(FullName,Gmail,PhoneNumber):
    return edit_user_controller(FullName,Gmail,PhoneNumber)

def user_list_view(event_id):
    return user_list_controller(event_id)

def edit_event_view(ID,StartTime,EndTime,Location,Description,MaxAttendees):
    return edit_event_controller(ID,StartTime,EndTime,Location,Description,MaxAttendees)

def send_email_view(recipient_email, subject, message):
    return send_email_controller(recipient_email, subject, message)

def get_eventID_regis_view(gmail):
    return get_eventID_regis_controller(gmail)

def update_password_view(password,gmail):
    return update_password_controller(password,gmail)

def check_oldPassword_view(gmail):
    return check_oldPassword_controller(gmail)