import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Named export
export function getEventRegisteredByGmail(gmail) {
    return apiClient.get(`/registered-event/${gmail}`);
}

export function cancelRegisterEvent(eventId,gmail) {
  const data = {
    Gmail: gmail,
    event_id: eventId
  };
  return apiClient.delete(`/cancelRegistered`, { data: data });
}


export function getEventIDRegisteredByGmail(gmail) {
  return apiClient.get(`/eventid_regis/${gmail}`);
}