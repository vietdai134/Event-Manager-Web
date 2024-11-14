<template>
  <div class="container_change">
    <div class="dialog_chandePass">
      <button class="close_button" @click="closeDialog">✖</button>
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
  </div>
</template>
  
  <script>
import Cookies from "js-cookie";
import { userChangePassword, check_oldPassword } from "@/api/Login_Register";
import { notify, confirmNotify } from "@/script/Notification";
export default {
  data() {
    return {
      oldPassword: "",
      verifypass: "",
      password: "",
      confirmPassword: "",
      passwordsMatch: false,
      gmail: "",
    };
  },

  methods: {
    closeDialog() {
      this.$router.push({ path: "/Info-User" });
      this.$emit("close");
    },
    async checkPasswords() {
      this.gmail = Cookies.get("email");

      // Loại bỏ khoảng trắng thừa ở đầu và cuối mật khẩu
      const trimmedOldPassword = this.oldPassword.trim();
      const trimmedNewPassword = this.password.trim();
      const trimmedConfirmPassword = this.confirmPassword.trim();

      if (!trimmedOldPassword) {
        notify("Vui lòng nhập mật khẩu cũ!", "warning");
        return;
      }

      if (trimmedNewPassword !== trimmedConfirmPassword) {
        notify("Mật khẩu mới và xác nhận mật khẩu không khớp!", "warning");
        return;
      }

      if (trimmedOldPassword === trimmedNewPassword) {
        notify("Mật khẩu cũ và mật khẩu mới không được giống nhau!", "warning");
        return;
      }

      confirmNotify("Bạn có chắc muốn đổi mật khẩu không?", async () => {
        try {
          const response = await check_oldPassword(this.gmail);
          this.verifypass = response.data.Password;
          // console.log(trimmedOldPassword)
          if (trimmedOldPassword !== this.verifypass.trim()) {
            notify("Mật khẩu cũ không khớp!", "warning");
            return;
          }

          const updateResponse = await userChangePassword(
            trimmedNewPassword,
            this.gmail
          );

          if (updateResponse.data.message === "password updated successfully") {
            localStorage.setItem(
              "updateNotification",
              "Đổi mật khẩu thành công"
            );

            if (window.location.href.includes("ChangePassword")) {
              this.$router.push({ name: "InfoUser" });
              this.closeDialog();
              window.location.reload();
            }
          } else {
            notify("Có lỗi xảy ra khi đổi mật khẩu.", "error");
          }
        } catch (error) {
          console.error("Có lỗi xảy ra:", error);
          notify("Có lỗi xảy ra catch.", "error");
        }
      });
    },
  },
};
</script>
  
<style scoped src="../css/dialog.css">
</style>
  