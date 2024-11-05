import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json',
  },
});


export function sendEmail(toGmail, subject, message) {
  const data = {
    recipient_email: toGmail,
    subject: subject,
    message: message
  };
  return apiClient.post(`/send_notification`,data);
}

