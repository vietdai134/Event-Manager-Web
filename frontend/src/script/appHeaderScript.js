// appHeaderScript.js
import { setLightMode, getLightMode } from "@/script/theme"; // Nhập hàm từ theme.js

export default {
  name: "appHeader",
  data() {
    return {
      isLightMode: getLightMode(), // Lấy giá trị isLightMode từ theme.js
    };
  },
  methods: {
    toggleTheme() {
      this.isLightMode = !this.isLightMode; // Đảo giá trị
      setLightMode(this.isLightMode); // Gán giá trị mới vào theme.js
      // console.log("new islight: " + getLightMode());
      document.body.style.backgroundColor = this.isLightMode ? '#fff' : '#000';

      // Phát ra sự kiện để các component khác có thể nghe
      const event = new Event("lightModeChanged");
      window.dispatchEvent(event);
    },
  },
  mounted() {
    // Cập nhật màu nền khi trang được tải lại
    document.body.style.backgroundColor = this.isLightMode ? '#fff' : '#000';
  },
};
