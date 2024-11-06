import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

// Tạo một instance của axios với URL gốc
const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json',
  },
});

export function getPublicEvents(gmail) {
  return apiClient.get(`/public-event/${gmail}`); 
}

// Hàm lấy thông tin sự kiện theo ID
export function getEventById(eventId) {
  return apiClient.get(`/public-event/${eventId}`);
}

export function registerEvent(eventId,gmail) {
  const data = {
    Gmail: gmail,
    event_id: eventId
  };
  return apiClient.post(`/register_event`,data);
}

