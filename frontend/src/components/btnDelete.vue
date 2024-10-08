<!-- RegisterButton.vue -->
<template>
    <button class="delete_btn" @click="deleteEvent">xoá</button>
  </template>
  
  <script>
  export default {
    methods: {
        deleteEvent() {
        // Logic cho việc đăng ký
        console.log('Xoá event');
      }
    }
  }
  </script>
  