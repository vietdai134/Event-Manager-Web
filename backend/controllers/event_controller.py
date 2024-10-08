# controllers/event_controller.py

from models.event_model import *

def get_event_created_controller():
    return get_all_event_created()

def get_all_event_public_controller():
    return get_all_event_Public()

def get_event_public_controller(event_id):
    return get_event_Public(event_id)

def get_event_registered_controller():
    return get_all_event_registered()


def get_event_past_controller():
    return get_all_event_past()