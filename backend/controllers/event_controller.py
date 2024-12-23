# controllers/event_controller.py

from models.event_model import *

def get_event_created_controller(gmail):
    return get_all_event_created(gmail)

def get_all_event_public_controller(gmail):
    return get_all_event_Public(gmail)

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

def cancel_register_controller(gmail,event_id):
    return cancel_register_event(gmail,event_id)

def delete_event_controller(gmail,event_id):
    return delete_event(gmail,event_id)

def add_event_controller(EventType, EventName,StartTime,EndTime,
                         Location,EventImages,Description,RegisteredCount
                         ,MaxAttendees,Gmail):
    return add_event(EventType, EventName,StartTime,EndTime,Location,
                     EventImages,Description,RegisteredCount,MaxAttendees,Gmail)
    
def edit_user_controller(FullName,Gmail,PhoneNumber):
    return edit_info_user(FullName,Gmail,PhoneNumber)

def user_list_controller(event_id):
    return get_list_regis(event_id)

def edit_event_controller(ID,StartTime,EndTime,Location,Description,MaxAttendees):
    return edit_info_event(ID,StartTime,EndTime,Location,Description,MaxAttendees)

def send_email_controller(recipient_email, subject, message):
    return send_email(recipient_email, subject, message)

def get_eventID_regis_controller(gmail):
    return get_eventID_regis(gmail)

def update_password_controller(password,gmail):
    return update_password(password,gmail)

def check_oldPassword_controller(gmail):
    return check_oldPassword(gmail)