<!-- RegisterButton.vue -->
<template>
  <button class="list_user_btn" @click="listUserEvent">
    Xem danh sách đã đăng ký
  </button>
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
        this.$router.push({ path: `${this.eventId}`+'/listUser' });
      }
    }
  }
  </script>
  