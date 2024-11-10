<template>
    <div>
      <h1>Đổi mật khẩu</h1>
      <form @submit.prevent="checkPasswords">
        <div>
            <label for="oldPassword">Mật khẩu cũ:</label>
            <input
            type="password"
            id="oldPassword"
            v-model="oldPassword"
            placeholder="Nhập mật khẩu cũ"
            required
            />
        </div>
        <div>
          <label for="password">Mật khẩu:</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Nhập mật khẩu"
            required
          />
        </div>
        <div>
          <label for="confirmPassword">Xác nhận mật khẩu:</label>
          <input
            type="password"
            id="confirmPassword"
            v-model="confirmPassword"
            placeholder="Xác nhận mật khẩu"
            required
          />
        </div>
        <button type="submit">Kiểm tra</button>
      </form>

    </div>
  </template>
  
  <script>
  import Cookies from "js-cookie";
  import { userChangePassword,check_oldPassword } from "@/api/Login_Register";
  export default {
    data() {
      return {
        oldPassword: '',
        verifypass:'',
        password: '',
        confirmPassword: '',
        passwordsMatch: false,
        gmail:''
      };
    },
    methods: {
        async checkPasswords() {
            this.gmail = Cookies.get('email');

            if (!this.oldPassword) {
                console.error('Vui lòng nhập mật khẩu cũ!');
                return;
            }

            if (this.password !== this.confirmPassword) {
                console.error('Mật khẩu mới và xác nhận mật khẩu không khớp!');
                return;
            }

            try {
                const response = await check_oldPassword(this.gmail);
                this.verifypass = response.data.Password;

                if (this.oldPassword !== this.verifypass) {
                    console.error('Mật khẩu cũ không khớp!');
                    return;
                }

                console.log('Mật khẩu cũ khớp!');

                const updateResponse = await userChangePassword(this.password, this.gmail);

                if (updateResponse.data.message === "password updated successfully") {
                    console.log('Đổi mật khẩu thành công!');
                    localStorage.setItem("updateNotification", "Đổi mật khẩu thành công");

                    if (window.location.href.includes("ChangePassword")) {
                    this.$router.push({ name: "InfoUser" });
                    }
                } else {
                    console.error('Có lỗi xảy ra khi đổi mật khẩu.');
                }

            } catch (error) {
                console.error('Có lỗi xảy ra:', error);
                alert('Đã xảy ra lỗi. Vui lòng thử lại sau.');
            }
        },
    },
  };
  </script>
  
  <style scoped>
  form {
    max-width: 300px;
    margin: auto;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .success {
    color: green;
  }
  
  .error {
    color: red;
  }
  </style>
  