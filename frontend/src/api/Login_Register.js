import axios from 'axios';
import { API_BASE_URL } from './BaseUrl';

// Tạo một instance của axios với URL gốc
const apiClient = axios.create({
  baseURL: `${API_BASE_URL}`,
  headers: {
    'Content-Type': 'application/json', // Đảm bảo Content-Type là application/json
  },
});

// Hàm gửi yêu cầu POST để đăng nhập
// export function get_users() {
//   return apiClient.get('/Login');  
// }
export function get_users_gmail(gmail) {
  return apiClient.get(`/Login/${gmail}`);  
}
export function add_user(userData) {
  return apiClient.post('/add_user', userData, {
    headers: {
      'Content-Type': 'application/json',
    },
  });
}

export function editInfoUser(gmail, fullName, phoneNumber) {
  const data = {
    Gmail: gmail,
    FullName: fullName,
    PhoneNumber: phoneNumber
  };
  return apiClient.put(`/edit_user`, data);
}

export function userChangePassword(password,gmail) {
  const data = {
    Password:password,
    Gmail: gmail
  };
  return apiClient.put(`/change_password`, data);
}

export function check_oldPassword(gmail) {
  return apiClient.get(`/check_oldPassword/${gmail}`);  
}