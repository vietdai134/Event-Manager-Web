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
      this.$emit("close");
    },
    async checkPasswords() {
      this.gmail = Cookies.get("email");

      if (!this.oldPassword) {
        notify("Vui lòng nhập mật khẩu cũ!", "warning");
        console.error("Vui lòng nhập mật khẩu cũ!");
        return;
      }

      if (this.password !== this.confirmPassword) {
        notify("Mật khẩu mới và xác nhận mật khẩu không khớp!", "warning");
        console.error("Mật khẩu mới và xác nhận mật khẩu không khớp!");
        return;
      }
      confirmNotify(
        "Bạn có chắc muốn đổi mật khẩu không?",
        async () => {
          try {
            const response = await check_oldPassword(this.gmail);
            this.verifypass = response.data.Password;

            if (this.oldPassword !== this.verifypass) {
              notify("Mật khẩu cũ không khớp!", "warning");
              console.error("Mật khẩu cũ không khớp!");
              return;
            }

            console.log("Mật khẩu cũ khớp!");

            const updateResponse = await userChangePassword(
              this.password,
              this.gmail
            );

            if (
              updateResponse.data.message === "password updated successfully"
            ) {
              console.log("Đổi mật khẩu thành công!");
              localStorage.setItem(
                "updateNotification",
                "Đổi mật khẩu thành công"
              );

              if (window.location.href.includes("ChangePassword")) {
                this.$router.push({ name: "InfoUser" });
              }
            } else {
              notify("Có lỗi xảy ra khi đổi mật khẩu.", "error");
              console.error("Có lỗi xảy ra khi đổi mật khẩu.");
            }
          } catch (error) {
            console.error("Có lỗi xảy ra:", error);
            notify("Có lỗi xảy ra catch.", "error");
          }
        },
        () => {
          // Hủy thao tác khi người dùng nhấn nút "Hủy"
          console.log("Người dùng đã hủy thao tác.");
        }
      );
    },
  },
};
</script>
  
<style scoped src="../css/dialog.css">
</style>
  