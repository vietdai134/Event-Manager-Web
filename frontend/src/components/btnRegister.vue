<!-- RegisterButton.vue -->
<template>
  <button
    :class="isLightMode ? 'register_btn light_btn' : 'register_btn dark_btn'"
    @click="registerEventClick"
  >
    Đăng Ký
  </button>
</template>
  
  <script>
import getIsLightMode from "@/script/getIsLightMode";
import Cookies from "js-cookie";
import { registerEvent } from "@/api/publicEventsAPI";
import { notify } from "@/script/Notification";

export default {
  data() {
    return {
      eventId: null,
      gmail: "",
    };
  },

  mixins: [getIsLightMode],
  created() {
    this.gmail = Cookies.get("email");
    // console.log(this.gmail);
    this.eventId = parseInt(this.$route.params.id);
    // console.log(this.eventId)
  },
  methods: {
    async registerEventClick() {
      // console.log(this.eventId);
      if (
        !document.cookie
          .split("; ")
          .find((row) => row.startsWith("fullname="))
      ) {
        notify("Vui lòng đăng nhập trước khi đăng ký!", "warning");
        return; // Dừng hàm nếu không có cookie
      }
      try {
        const response = await registerEvent(this.eventId, this.gmail);
        // notify("Chào bạn!", "info");
        // console.log(response.data.message);
        if (response.data.message === "Event registered successfully") {
          notify("Đăng Ký Thành Công!", "success");
          setTimeout(() => {
            if (window.location.href.includes("Events-Public")) {
              this.$router.push({ name: "EventsPublic" });
            }
          }, 1000);
        }
      } catch (error) {
        console.error("Error registering event:", error);
        notify("Lỗi Khi Đăng Ký!", "error");
        // alert("Có lỗi xảy ra khi đăng ký sự kiện.");
      }
    },
    someMethod() {
      console.log(this.isLightMode);
      this.updateLightMode();
    },
  },
};
</script>
  