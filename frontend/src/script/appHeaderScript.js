export default {
    name: "appHeader",
    data() {
      return {
        isLightMode: true, // mặc định là chế độ sáng
      };
    },
    methods: {
      toggleTheme() {
        this.isLightMode = !this.isLightMode;
        document.body.style.backgroundColor = this.isLightMode ? '#fff' : '#000';
        document.body.style.color = this.isLightMode ? '#000' : '#e2e2e2';
      },
    },
  };