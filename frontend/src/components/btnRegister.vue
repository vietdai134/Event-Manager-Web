<!-- RegisterButton.vue -->
<template>
  <button
    :class="isLightMode ? 'register_btn light_btn' : 'register_btn dark_btn'"
    @click="registerEvent"
  >
    Đăng Ký
  </button>
</template>
  
  <script>
import { getLightMode } from "@/script/theme";

export default {
  data() {
    return {
      // Khai báo biến isLightMode
      isLightMode: getLightMode(), // Lấy giá trị ban đầu từ theme.js
    };
  },
  methods: {
    registerEvent() {
      // Logic cho việc đăng ký
      console.log("Đăng ký sự kiện");
    },
    updateLightMode() {
      this.isLightMode = getLightMode(); // Cập nhật giá trị isLightMode từ theme.js
      // console.log("Giá trị isLightMode trong public.vue: ", this.isLightMode);
    },
  },
  mounted() {
    this.updateLightMode();
    window.addEventListener("lightModeChanged", this.updateLightMode);
  },
  beforeUnmount() {
    window.removeEventListener("lightModeChanged", this.updateLightMode);
  },
};
</script>
  