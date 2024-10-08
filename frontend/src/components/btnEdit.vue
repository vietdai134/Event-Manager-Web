<!-- RegisterButton.vue -->
<template>
    <button class="edit_btn" @click="editEvent">Sửa</button>
  </template>
  
  <script>
  export default {
    methods: {
        editEvent() {
        // Logic cho việc đăng ký
        console.log('Sửa event');
      }
    }
  }
  </script>
  