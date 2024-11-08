<template>
  <div class="main_container">
    <div class="container_login_signin">
      <div class="login_content" v-if="!showRegister">
        <form @submit.prevent="handleLogin">
          <h2>Login</h2>
          <div class="form-group">
            <label for="gmail">Gmail</label>
            <input
              type="email"
              id="gmail"
              v-model="gmail"
              placeholder="Nhập Gmail"
              required
            />
          </div>
          <div class="form-group">
            <label for="password">Mật khẩu</label>
            <input
              type="password"
              id="password"
              v-model="password"
              placeholder="Nhập mật khẩu"
              required
            />
          </div>
          <button type="submit" class="login-button">Đăng nhập</button>
          <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
          <a href="#" @click.prevent="toggleForm">Đăng ký</a>
        </form>
      </div>

      <div class="element_hidden">
        <img src="../assets/img/events_login_1.jpg" alt="" />
      </div>

      <div class="register_content" v-if="showRegister">
        <form @submit.prevent="handleRegister">
          <h2>Register</h2>
          <div class="form-group">
            <label for="registerName">Họ và Tên</label>
            <input
              type="text"
              id="registerName"
              v-model="registerName"
              placeholder="Nhập Tên"
              required
            />
          </div>
          <div class="form-group">
            <label for="registerGmail">Gmail</label>
            <input
              type="email"
              id="registerGmail"
              v-model="registerGmail"
              placeholder="Nhập Gmail"
              required
            />
          </div>
          <div class="form-group">
            <label for="registerPhone">Số điện thoại</label>
            <input
              type="tel"
              id="registerPhone"
              v-model="registerPhone"
              placeholder="Nhập Số Điện Thoại"
              required
              pattern="0[0-9]{9}"
              title="Số điện thoại phải bắt đầu bằng 0 và có đúng 10 chữ số"
            />
          </div>
          <div class="form-group">
            <label for="registerPassword">Mật khẩu</label>
            <input
              type="password"
              id="registerPassword"
              v-model="registerPassword"
              placeholder="Nhập mật khẩu"
              @input="validatePasswords"
              required
            />
          </div>
          <div class="form-group">
            <label for="registerPasswordConfirm">Nhập lại mật khẩu</label>
            <input
              type="password"
              id="registerPasswordConfirm"
              v-model="registerPasswordConfirm"
              @input="validatePasswords"
              ref="passwordConfirmInput"
              placeholder="Nhập lại mật khẩu"
              required
            />
          </div>
          <input type="hidden" v-model="createdAt" />
          <input type="hidden" v-model="updatedAt" />
          <button type="submit" class="login-button">Đăng Ký</button>
          <a href="#" @click.prevent="toggleForm">Quay lại Đăng Nhập</a>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { get_users_gmail } from "@/api/Login_Register";
import { add_user } from "@/api/Login_Register";

import Cookies from "js-cookie";

export default {
  name: "LoginForm",
  data() {
    return {
      gmail: "",
      password: "",
      registerGmail: "",
      registerPassword: "",
      registerName: "",
      registerPhone: "",
      registerPasswordConfirm: "",
      showRegister: false,
      errorMessage: "",
      nameError: "",
      gmailError: "",
      phoneError: "",
      passwordError: "",
      confirmPasswordError: "",
      users: null,
      saveEmail: "",
      createdAt: new Date().toISOString().slice(0, 19).replace("T", " "),
      updatedAt: new Date().toISOString().slice(0, 19).replace("T", " "),
    };
  },
  methods: {
    validatePasswords() {
      const password = this.registerPassword;
      const passwordConfirm = this.registerPasswordConfirm;
      const passwordConfirmInput = this.$refs.passwordConfirmInput;

      if (password !== passwordConfirm) {
        passwordConfirmInput.setCustomValidity("Mật khẩu không khớp.");
      } else {
        passwordConfirmInput.setCustomValidity("");
      }
    },
    async fetchUserInfo() {
      try {
        const response = await get_users_gmail(this.gmail);
        this.users = response.data;
        this.errorMessage = "";
      } catch (error) {
        if (error.response && error.response.status === 404) {
          this.errorMessage = "Thông tin người dùng không chính xác.";
        } else {
          this.errorMessage = "Đã xảy ra lỗi. Vui lòng thử lại.";
        }
      }
    },
    async handleLogin() {
      await this.fetchUserInfo();
      if (!this.errorMessage) {
        const user = this.users.find((user) => user.Gmail === this.gmail);
        if (user) {
          if (user.Password === this.password) {
            this.errorMessage = "thành công";
            Cookies.set("email", user.Gmail, { expires: 1 / (24 * 60) });
            Cookies.set("fullname", user.FullName, { expires: 1 / (24 * 60) });
            this.saveEmail = user.Gmail;
            this.$emit("user-logged-in", user);
            this.$router.push({ name: "Home" });
          } else {
            this.errorMessage = "Mật khẩu không chính xác.";
          }
        } else {
          this.errorMessage = "Gmail không tồn tại.";
        }
      }
    },
    async handleRegister() {
      const registrationData = {
        FullName: this.registerName,
        Gmail: this.registerGmail,
        PhoneNumber: this.registerPhone,
        password: this.registerPassword,
        CreatedAt: this.createdAt,
        UpdatedAt: this.updatedAt,
      };

      // In ra dữ liệu để kiểm tra
      // console.log("Dữ liệu đăng ký:", registrationData);

      try {
        // console.log("Trước phản hồi từ server:");
        const response = await add_user(registrationData);
        // console.log("Phản hồi từ server:", response.data); // In ra phản hồi từ server
        alert(response.data.message); // Hiển thị thông báo từ server
        if (response.data.message === "User added successfully") {
            // Nếu đăng ký thành công, làm mới lại trang Login
            window.location.reload(); 
        }
      } catch (error) {
        console.error("Lỗi khi đăng ký:", error);
        alert("Đăng ký không thành công. Vui lòng thử lại."); // Thông báo lỗi
      }
    },

    toggleForm() {
      this.showRegister = !this.showRegister;
    },
  },
};
</script>

<style scoped src="../css/Login.css">

</style>


