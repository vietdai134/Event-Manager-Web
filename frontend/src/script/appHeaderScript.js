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
        const eventDates = document.querySelectorAll('.event_date');

        eventDates.forEach(h2 => {
          h2.style.color = this.isLightMode ? '#000' : 'white';
        });
    
        // document.body.style.backgroundColor = this.isLightMode ? 'white' : 'black';
      },
    },
  };