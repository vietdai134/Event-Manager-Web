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
      <div v-if="validate === true" class="valid" style="color: green">
        Email hợp lệ
      </div>
      <div v-if="validate === false" class="invalid" style="color: red">
        Email không hợp lệ
      </div>
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
import { sendEmail } from "@/api/sendNoti";
// import { getEvenCreateByGmail } from "@/api/createdEventsAPI";
import { notify, confirmNotify } from "@/script/Notification";

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
      created_events: [],
      gmail: [],
    };
  },
  methods: {
    Fun_getEvenCreateByGmail(gmail, message) {
      sendEmail(gmail, "Lời mời tham gia sự kiện", message);
    },
    invite() {
      if (this.emailList.length === 0) {
        notify("Danh sách email không được để trống!", "warning");
        return;
      }

      const message = this.quill.getText().trim();
      if (message === "") {
        notify("Thông điệp không được để trống!", "warning");
        return;
      }
      confirmNotify(
        "Bạn có chắc muốn mời?",
        () => {
          const message = this.quill.getText();
          this.emailList.forEach((email) => {
            this.Fun_getEvenCreateByGmail(email, message);
          });
          notify("Gửi lời mời thành công!", "success");
          // alert("Gửi lời mời thành công!");
          this.emailList = [];
          this.quill.setText("");
          (this.validate = null), this.closeDialog();
        },
        () => {
          console.log("Đã hủy mời!");
        }
      );
    },
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
        notify("Vui lòng nhập một địa chỉ email!", "warning");
      } else if (!emailPattern.test(this.newEmail)) {
        notify("Địa chỉ email không hợp lệ!", "warning");
      } else if (this.emailList.includes(this.newEmail)) {
        notify("Email này đã có trong danh sách!", "warning");
      } else {
        this.loading = true;
        this.validate = null;
        const isValid = await this.checkEmailValidity(this.newEmail);
        this.loading = false;
        if (isValid) {
          this.emailList.push(this.newEmail);
          this.newEmail = "";
          this.validate = true;
          notify("Thêm Email thành công!", "success");
        } else {
          this.validate = false;
          notify("Email này không tồn tại hoặc không hợp lệ!", "warning");
        }
      }
    },
    async checkEmailValidity(email) {
      const url = `https://emailvalidation.abstractapi.com/v1/?api_key=98c148c7a3cd4091a489f0dc1b08cb18&email=${email}`;

      try {
        const response = await fetch(url, { method: "GET" });
        const data = await response.json();
        // console.log(data);

        // Kiểm tra trạng thái "deliverability"
        if (data.deliverability === "DELIVERABLE") {
          return true; // Email hợp lệ
        } else {
          return false; // Email không hợp lệ
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
