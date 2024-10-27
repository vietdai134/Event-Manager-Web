// getIsLightMode.js
import { getLightMode } from "@/script/theme";

export default {
  data() {
    return {
      isLightMode: getLightMode(), // Lấy giá trị ban đầu từ theme.js
    };
  },
  methods: {
    updateLightMode() {
      this.isLightMode = getLightMode(); // Cập nhật giá trị isLightMode từ theme.js
    },
    formatDate(dateString) {
      const options = { year: "numeric", month: "2-digit", day: "2-digit" };
      const date = new Date(dateString);
      return date.toLocaleDateString("en-GB", options).replace(/\//g, "/"); // Định dạng ngày theo kiểu DD/MM/YYYY
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
