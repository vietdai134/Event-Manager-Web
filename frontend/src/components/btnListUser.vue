<!-- RegisterButton.vue -->
<template>
  <button class="list_user_btn" @click="listUserEvent">
    Xem danh sách đã đăng ký
  </button>
</template>
  
  <script>
export default {
  methods: {
    listUserEvent() {
      // Logic cho việc đăng ký
      console.log("danh sách sự kiện");
    },
  },
};
</script>
  