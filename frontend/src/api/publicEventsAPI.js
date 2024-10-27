import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

// Tạo một instance của axios với URL gốc
const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json',
  },
});

export function getPublicEvents() {
  return apiClient.get('/public-event'); 
}

// Hàm lấy thông tin sự kiện theo ID
export function getEventById(eventId) {
  return apiClient.get(`/public-event/${eventId}`);
}



