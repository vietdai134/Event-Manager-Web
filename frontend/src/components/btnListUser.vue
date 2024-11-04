<!-- RegisterButton.vue -->
<template>
    <button class="list_user_btn" @click="listUserEvent">Xem danh sách đã đăng ký</button>
  </template>
  
  <script>
  // import { getListUserRegis } from '@/api/createdEventsAPI';
  export default {
    data() {
    return {
        list_user: [],
        eventId:null
      };
    },
    created() {
      this.eventId = parseInt(this.$route.params.id);
    },
    methods: {
      
      listUserEvent() {
        // console.log(this.eventId)
        // try {
        //   const response = await getListUserRegis(this.eventId);
        //   this.list_user = response.data;
          
        //   // In ra danh sách người dùng
        //   console.log("List of registered users:", this.list_user);
          
        // } catch (error) {
        //   console.error("Lỗi khi lấy dữ liệu sự kiện:", error);
        //   this.event = null;
        // }
        this.$router.push({ path: '1/listUser' });
      }
    }
  }
  </script>
  