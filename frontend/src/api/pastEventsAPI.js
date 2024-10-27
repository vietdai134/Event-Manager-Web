import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Named export
export function getEventPastByGmail() {
    return apiClient.get(`/past-event`);
}
