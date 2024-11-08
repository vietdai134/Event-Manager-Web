<template>
    <div id="app">
      <h1>Thông tin người dùng</h1>
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

  h1 {
    margin-top: 20px;
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }

  form div {
    margin-right: 50px;
    margin-left: 50px;
    margin-bottom: 15px;
  }

  label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
    color: #555;
  }

  input[type="text"],
  input[type="email"] {
    width: 100%;
    padding: 10px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    transition: border-color 0.3s, box-shadow 0.3s;
  }

  input[type="text"]:focus,
  input[type="email"]:focus {
    border-color: #007BFF;
    box-shadow: 0 0 8px rgba(0, 123, 255, 0.2);
    outline: none;
  }

  input[readonly] {
    background-color: #e9ecef;
    cursor: not-allowed;
  }

  button[type="submit"] {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
    color: #fff;
    background-color: #007BFF;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
  }

  button[type="submit"]:hover {
    background-color: #0056b3;
    transform: translateY(-2px);
  }

  button[type="submit"]:active {
    background-color: #004085;
  }

  /* Style for submitted data */
  h2 {
    color: #333;
  }

  p {
    margin: 5px 0;
  }
</style>


  