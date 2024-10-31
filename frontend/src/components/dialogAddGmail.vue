<template>
  <div v-if="isVisible" class="dialog_overlay">
    <div class="dialog_content">
      <h3>Mời người tham gia</h3>

      <!-- Phần thêm Gmail -->
      <div class="email_input_section">
        <input
          type="email"
          v-model="newEmail"
          placeholder="Nhập Gmail"
          @keyup.enter="addEmail"
        />
        <button id="add_email" @click="addEmail">
          Thêm<i class="fa-regular fa-at" style="color: white"></i>
        </button>
      </div>
      <div v-if="loading" class="loading">Đang kiểm tra email...</div>
      <div v-if="validate === true" class="valid">Email hợp lệ</div>
      <div v-if="validate === false" class="invalid">Email không hợp lệ</div>
      <div class="email_list">
        <h4>Danh sách Gmail đã thêm:</h4>
        <ul class="list_added_email">
          <li v-for="(email, index) in emailList" :key="index">
            {{ email }}
            <button @click="removeEmail(index)">Xóa</button>
          </li>
        </ul>
      </div>

      <!-- Phần thông báo -->
      <div class="message_section">
        <div ref="editorContainer" class="editor"></div>
        <!-- <textarea
          v-model="message"
          placeholder="Nhập thông điệp gửi cho người tham gia"
        ></textarea> -->
      </div>

      <div class="dialog_actions">
        <button @click="closeDialog">Hủy</button>
        <button @click="invite">Mời</button>
      </div>
    </div>
  </div>
</template>

<script>
import Quill from "quill";
import "quill/dist/quill.snow.css";
import { nextTick } from "vue";

export default {
  name: "DialogAddGmail",
  props: {
    isVisible: Boolean,
  },
  data() {
    return {
      newEmail: "",
      emailList: [],
      message: "",
      validate: false,
      loading: false,
    };
  },
  methods: {
    initQuill() {
      if (this.$refs.editorContainer) {
        // Check if the ref exists
        this.quill = new Quill(this.$refs.editorContainer, {
          theme: "snow",
        });
      } else {
        console.error("Editor container not found.");
      }
    },
    addEmail() {
      const emailPattern = /^[^\s@]+@gmail\.com$/;

      if (!this.newEmail) {
        alert("Vui lòng nhập một địa chỉ email!");
      } else if (!emailPattern.test(this.newEmail)) {
        alert("Địa chỉ email không hợp lệ!");
      } else if (this.emailList.includes(this.newEmail)) {
        alert("Email này đã có trong danh sách!");
      } else {
        this.checkEmailValidity(this.newEmail)
          .then((isValid) => {
            if (isValid) {
              this.emailList.push(this.newEmail);
              this.newEmail = "";
            } else {
              alert("Email này không tồn tại hoặc không hợp lệ!");
            }
          })
          .catch((error) => {
            console.error("Lỗi khi kiểm tra email:", error);
            alert("Có lỗi xảy ra trong quá trình kiểm tra email.");
          });
      }
    },
    async checkEmailValidity(email) {
      this.loading = true; // Bắt đầu trạng thái loading
      try {
        const apiKey = "f6464b9945c045a0b041e24eba4fb157";
        const response = await fetch(
          `/api/v2/validate?api_key=${apiKey}&email=${email}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        console.log("Response status:", response.status);

        if (response.ok) {
          const data = await response.json();
          console.log("Data:", data); // Log dữ liệu nhận được để kiểm tra

          this.loading = false; // Kết thúc trạng thái loading

          if (data && data.status === "invalid") {
            this.validate = false; // Email hợp lệ
            return false;
          } else {
            this.validate = true; // Email không hợp lệ
            return true;
          }
        } else {
          console.log("Error response:", response);
          throw new Error("Không thể kết nối tới ZeroBounce.");
        }
      } catch (error) {
        this.loading = false;
        console.error("Lỗi khi kiểm tra email:", error);
        alert("Có lỗi xảy ra trong quá trình kiểm tra email.");
        return false;
      }
    },
    invite() {
      // Logic để gửi lời mời cho các email
      console.log("Gmail:", this.emailList);
      console.log("Thông điệp:", this.message);
      this.closeDialog();
    },
    closeDialog() {
      this.$emit("close");
    },
  },
  watch: {
    isVisible(newVal) {
      if (newVal) {
        nextTick(() => {
          this.initQuill();
        });
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.initQuill();
    });
  },
};
</script>

<style scoped src="../css/dialog.css">
</style>
