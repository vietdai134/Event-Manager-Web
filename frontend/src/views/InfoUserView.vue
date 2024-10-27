<template>
    <div id="app">
      <h1>Trang Giao Diện</h1>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="name">Tên:</label>
          <input type="text" id="name" v-model="name" />
        </div>
        <div>
          <label for="email">Gmail:</label>
          <input type="email" id="email" v-model="email" readonly placeholder="example@gmail.com"  />

        </div>
        <div>
          <label for="message">Tin nhắn:</label>
          <input type="text" id="message" v-model="message" />
        </div>
        <button type="submit">Gửi</button>
      </form>
      <div v-if="submitted">
        <h2>Thông tin đã gửi:</h2>
        <p>Tên: {{ name }}</p>
        <p>Gmail: {{ email }}</p>
        <p>Tin nhắn: {{ message }}</p>
      </div>
    </div>
  </template>
  
  <script> 

  export default {
    
    data() {
      return {
        name: '',
        email: 'alice@example.com',
        message: '',
        submitted: false,
      };
    },
    methods: {
      handleSubmit() {
        this.submitted = true;
        
      },
    },
  };
  </script>
  
  <style>
 
  </style>
  