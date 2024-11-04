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
          <label for="PhoneNumber">Số điện thoại:</label>
          <input type="text" id="PhoneNumber" v-model="PhoneNumber" />
        </div>
        <button type="submit">Sửa</button>
      </form>
      <div v-if="submitted">
        <h2>Thông tin đã gửi:</h2>
        <p>Tên: {{ name }}</p>
        <p>Gmail: {{ email }}</p>
        <p>Tin nhắn: {{ PhoneNumber }}</p>
      </div>
    </div>
  </template>
  
  <script> 
  import Cookies from 'js-cookie'; 
  import { get_users_gmail,editInfoUser } from '@/api/Login_Register';
  export default {
    created(){
      this.gmail=Cookies.get('email');
    },
    data() {
      return {
        name: '',
        email: '',
        PhoneNumber: '',
        submitted: false,
        user_info: [],
      };
    },
    mounted() {
      get_users_gmail(this.gmail)
      .then(response => {
        this.user_info = response.data; 
        this.name=this.user_info[0].FullName
        this.email=this.gmail
        this.PhoneNumber=this.user_info[0].PhoneNumber
        // console.log(this.user_info[0])
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    },
    methods: {
      async handleSubmit(){
        // console.log(this.gmail+""+this.name+""+this.PhoneNumber )
        try {
          const response = await editInfoUser(this.gmail,this.name,this.PhoneNumber );
          alert(response.data.message); 

          if (response.data.message === "user updated successfully") {
            window.location.reload(); 
          }
        } catch (error) {
          console.error('Error update user:', error);
          alert('Có lỗi xảy ra khi sửa thông tin.');
        }
      }
      
    },
  };
  </script>
  
  <style>
 
  </style>
  