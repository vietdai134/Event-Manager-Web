<template>
  <div id="app">
    <div class="container">
      <div class="profile-container">
        <div class="icon_content">
          <div class="icon">
            <i class="fa-solid fa-user"></i>
          </div>
        </div>
        <div class="profile">
          <h1>Profile</h1>
          <p class="profile_info name" :title="displayname">
            Tên: {{ displayname }}
          </p>
          <p class="profile_info email" :title="email">Email: {{ email }}</p>
          <p class="profile_info">Ngày tạo: {{ formatDate(createdAt) }}</p>
          <p class="profile_info">Ngày sửa: {{ formatDate(updatedAt) }}</p>
        </div>
      </div>
      <h1>Thay đổi Thông Tin</h1>
      <form @submit.prevent="handleSubmit">
        <div class="form_group_info">
          <label for="name">Tên:</label>
          <input type="text" id="name" v-model="name" required />
        </div>
        <div class="form_group_info">
          <label for="email">Gmail:</label>
          <input
            type="email"
            id="email"
            v-model="email"
            readonly
            placeholder="example@gmail.com"
          />
        </div>
        <div class="form_group_info">
          <label for="PhoneNumber">Số điện thoại:</label>
          <input
            type="text"
            id="PhoneNumber"
            pattern="^0\d{9}$"
            title="Số điện thoại phải chứa 10 chữ số và bắt đầu bằng 0"
            v-model="PhoneNumber"
          />
        </div>
        <div class="btn_content">
          <button type="submit" class="submit-btn">Sửa</button>
        </div>
      </form>
      <!-- <div v-if="submitted" class="submitted-info">
        <h2>Thông tin đã gửi:</h2>
        <p>Tên: {{ name }}</p>
        <p>Gmail: {{ email }}</p>
        <p>Tin nhắn: {{ PhoneNumber }}</p>
      </div> -->
    </div>
  </div>
</template>

  
  <script>
import Cookies from "js-cookie";
import { get_users_gmail, editInfoUser } from "@/api/Login_Register";
import { notify, confirmNotify } from "@/script/Notification";

export default {
  created() {
    this.gmail = Cookies.get("email");
  },
  data() {
    return {
      displayname: "",
      name: "",
      email: "",
      PhoneNumber: "",
      createdAt: "",
      updatedAt: "",
      submitted: false,
      user_info: [],
    };
  },
  mounted() {
    const updateNotification = localStorage.getItem("updateNotification");
    if (updateNotification) {
      notify(updateNotification, "success");
      localStorage.removeItem("updateNotification"); // Xóa thông báo sau khi hiển thị
    }

    get_users_gmail(this.gmail)
      .then((response) => {
        this.user_info = response.data;
        this.name = this.user_info[0].FullName;
        this.displayname = this.user_info[0].FullName;
        this.email = this.gmail;
        this.PhoneNumber = this.user_info[0].PhoneNumber;
        this.createdAt = this.user_info[0].CreatedAt;
        this.updatedAt = this.user_info[0].UpdatedAt;
        // console.log(this.user_info[0])
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  },
  methods: {
    formatDate(dateString) {
      if(dateString===""){
        return "dd/MM/yyyy hh:MM:ss";
      }
      const date = new Date(dateString);
      const day = String(date.getUTCDate()).padStart(2, "0");
      const month = String(date.getUTCMonth() + 1).padStart(2, "0"); // Tháng bắt đầu từ 0
      const year = date.getUTCFullYear();
      const hours = String(date.getUTCHours()).padStart(2, "0");
      const minutes = String(date.getUTCMinutes()).padStart(2, "0");
      const seconds = String(date.getUTCSeconds()).padStart(2, "0");

      return `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
    },
    async handleSubmit() {
      if (!Cookies.get("fullname")) {
        notify("Vui lòng đăng nhập trước khi sửa.", "warning");
        return;
      }
      if (
        this.name === this.user_info[0].FullName &&
        this.PhoneNumber === this.user_info[0].PhoneNumber
      ) {
        notify("Vui lòng thay đổi thông tin trước khi lưu.", "warning");
        return;
      }

      // Sử dụng confirmNotify để xác nhận hành động từ người dùng
      confirmNotify(
        "Bạn có chắc muốn thay đổi thông tin không?",
        async () => {
          try {
            const response = await editInfoUser(
              this.gmail,
              this.name,
              this.PhoneNumber
            );
            // notify(response.data.message);

            if (response.data.message === "user updated successfully") {
              // notify("Thay đổi thành công", "success"); // Gọi thông báo sau khi reload
              // setTimeout(() => {
              //   window.location.reload(); // Sau khi thông báo, reload lại trang
              // }, 500);
              Cookies.set("fullname", this.name);
              if (window.location.href.includes("editEvent")) {
                this.$router.push({ name: "DetailEventsCreated" });
              }
              localStorage.setItem("updateNotification", "Sửa thành công");
              window.location.reload();
            }
          } catch (error) {
            console.error("Error updating user:", error);
            notify("Có lỗi xảy ra khi sửa thông tin.", "error");
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
  
<style scoped src="../css/infoUser.css">
</style>


  