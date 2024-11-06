import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Named export
export function getEvenCreateByGmail(gmail) {
    return apiClient.get(`/created-event/${gmail}`);
}

export function deleteEvent(eventId,gmail) {
  const data = {
    Gmail: gmail,
    event_id: eventId
  };
  return apiClient.delete(`/delete_Event`, { data: data });
}

export function addEvent(EventType, EventName,StartTime,EndTime,
                              Location,EventImages,Description
                              ,MaxAttendees,Gmail) {
  const data = {
    EventType: EventType,
    EventName: EventName,
    StartTime: StartTime,
    EndTime: EndTime,
    Location: Location,
    EventImages: EventImages,
    Description: Description,
    RegisteredCount: 0,
    MaxAttendees: MaxAttendees,
    Gmail:Gmail
  };
  return apiClient.post(`/add_event`,data);
}

export function editEvent(ID,StartTime,EndTime,Location,Description,MaxAttendees) {
  const data = {
    ID:ID,
    // EventType: EventType,
    // EventName: EventName,
    StartTime: StartTime,
    EndTime: EndTime,
    Location: Location,
    // EventImages: EventImages,
    Description: Description,
    // RegisteredCount: 0,
    MaxAttendees: MaxAttendees,
    
  };
  return apiClient.put(`/edit_event`,data);
}

export function getListUserRegis(eventId) {
  return apiClient.get(`/user_list/${eventId}`);
}