<template>
    <div id="app">
      <h1>danh sách người đã đăng ký</h1>
      <ul>
        <li v-for="user in list_user" :key="user.Gmail">{{ user.FullName }} - {{ user.Gmail }} - {{ user.PhoneNumber }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { getListUserRegis } from '@/api/createdEventsAPI';
  
  export default {
    data() {
      return {
        list_user: [],
        eventId: null
      };
    },
    async created() {
      this.eventId = parseInt(this.$route.params.id);
  
      try {
        // Gọi API để lấy danh sách người dùng đã đăng ký
        const response = await getListUserRegis(this.eventId);
        this.list_user = response.data;
  
        // In ra danh sách người dùng
        console.log("List of registered users:", this.list_user);
      } catch (error) {
        console.error("Lỗi khi lấy dữ liệu sự kiện:", error);
      }
    },
  }
  </script>
  