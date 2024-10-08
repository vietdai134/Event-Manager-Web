<!-- RegisterButton.vue -->
<template>
    <button class="register_btn" @click="registerEvent">Đăng Ký</button>
  </template>
  
  <script>
  export default {
    methods: {
      registerEvent() {
        // Logic cho việc đăng ký
        console.log('Đăng ký sự kiện');
      }
    }
  }
  </script>
  