import {getEventRegisteredByGmail} from '@/api/registeredEventsAPI'
import Cookies from "js-cookie";
export default {
  data() {
    return {
      register_events: [],
      gmail:""
    };
  },
  created(){
    this.gmail=Cookies.get('email');
    // console.log(this.gmail);
  },
  mounted() {
    // Gọi API từ backend để lấy dữ liệu
    getEventRegisteredByGmail(this.gmail)
    .then(response => {
      this.register_events = response.data; // Assign data to register_events
      console.log(this.register_events)
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
  },
  computed: {
    filteredEvents() {
      if (!this.searchQuery) {
        return this.register_events; // Trả về register_events thay vì events
      }
      return this.register_events.filter((event) =>
        event.EventName.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    groupedEvents() {
      const grouped = {};
      const convertToDate = (dateString) => {
        const [day, month, year] = dateString.split("/");
        return new Date(`${year}-${month}-${day}`);
      };

      this.filteredEvents.forEach((event) => {
        const eventDate = event.StartTime;

        // Kiểm tra nếu sự kiện đã tồn tại trong nhóm hay chưa
        if (!grouped[eventDate]) {
          grouped[eventDate] = [];
        }

        // Kiểm tra sự kiện đã tồn tại trong nhóm đó chưa, nếu chưa thì thêm
        const isDuplicate = grouped[eventDate].some((e) => e.ID === event.ID);
        if (!isDuplicate) {
          grouped[eventDate].push(event);
        }
      });

      return Object.keys(grouped)
        .sort((a, b) => convertToDate(b) - convertToDate(a))
        .map((date) => ({
          date,
          events: grouped[date],
        }));
    },
  },

  methods: {
    getEventImage(image) {
      try {
        return require(`@/assets/img/${image}`);
      } catch (error) {
        console.error("Image not found:", error);
        return null; 
      }
    },

    registerEvent(eventId) {
      const event = this.register_events.find((e) => e.id === eventId); // Sử dụng register_events
      if (event) {
        if (event.registeredCount < event.maxParticipants) {
          event.registeredCount += 1;
          alert(`Bạn đã đăng ký tham gia sự kiện: ${event.name}`);
        } else {
          alert("Sự kiện này đã đạt giới hạn số lượng đăng ký.");
        }
      }
    },
    calculateRegisteredPercentage(event) {
      return (event.RegisteredCount / event.MaxAttendees) * 100;
    },
    getColorForPercentage(percentage) {
      if (percentage < 30) {
        return "#4caf50";
      } else if (percentage >= 30 && percentage < 60) {
        return "#FF9900";
      } else if (percentage >= 60 && percentage < 90) {
        return "#FF0000";
      } else {
        return "#EE0000";
      }
    },
  },
};
