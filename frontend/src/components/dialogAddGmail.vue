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
      validate: null, // Trạng thái kiểm tra email
      loading: false, // Trạng thái đang tải
    };
  },
  methods: {
    initQuill() {
      if (this.$refs.editorContainer) {
        this.quill = new Quill(this.$refs.editorContainer, {
          theme: "snow",
        });
      } else {
        console.error("Editor container not found.");
      }
    },
    async addEmail() {
      const emailPattern = /^[^\s@]+@gmail\.com$/;

      if (!this.newEmail) {
        alert("Vui lòng nhập một địa chỉ email!");
      } else if (!emailPattern.test(this.newEmail)) {
        alert("Địa chỉ email không hợp lệ!");
      } else if (this.emailList.includes(this.newEmail)) {
        alert("Email này đã có trong danh sách!");
      } else {
        this.loading = true;
        this.validate = null;

        const isValid = await this.checkEmailValidity(this.newEmail);
        this.loading = false;

        if (isValid) {
          this.emailList.push(this.newEmail);
          this.newEmail = "";
          this.validate = true;
        } else {
          this.validate = false;
          alert("Email này không tồn tại hoặc không hợp lệ!");
        }
      }
    },
    async checkEmailValidity(email) {
      const url = `https://cors-anywhere.herokuapp.com/https://apps.emaillistverify.com/api/verifyEmail?secret=wILF2TjO1dAHFSldZQ1RA&email=${email}`;

      try {
        const response = await fetch(url, {
          method: "GET",
          headers: {
            Origin: "http://localhost:8080",
            "X-Requested-With": "XMLHttpRequest",
          },
        });
        const text = await response.text();
        if (text === "ok") {
          return true; // Email hợp lệ
        } else if (text === "email_disabled") {
          return false; // Email không hợp lệ
        } else {
          // Nếu không nhận được "ok" hoặc "invalid", hãy in ra để kiểm tra
          console.log("Phản hồi không xác định:", text);
          return false;
        }
      } catch (error) {
        console.error("Lỗi khi kiểm tra email:", error);
        return false;
      }
    },
    removeEmail(index) {
      this.emailList.splice(index, 1);
    },
    closeDialog() {
      this.$emit("close");
    },
    invite() {
      alert("Gửi lời mời thành công!");
      this.closeDialog();
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
