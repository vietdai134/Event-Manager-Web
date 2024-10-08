<!-- RegisterButton.vue -->
<template>
    <button class="cancel_register_btn" @click="cancelregisterEvent">Huỷ đăng Ký</button>
  </template>
  
  <script>
  export default {
    methods: {
        cancelregisterEvent() {
        // Logic cho việc đăng ký
        console.log('Đăng ký sự kiện');
      }
    }
  }
  </script>
  