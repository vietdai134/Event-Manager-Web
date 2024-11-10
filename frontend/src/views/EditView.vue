<template>
    <div class="event-form">
      <h1>Sửa Thông Tin Sự Kiện</h1>
      <form @submit.prevent="submitEvent">
        
        <label for="EventType">Loại sự kiện</label>
        <input type="text" id="EventType" v-model="event.EventType" readonly  />
  
        <label for="EventName">Tên sự kiện</label>
        <input type="text" id="EventName" v-model="event.EventName" readonly />
  
        <label for="StartTime">Thời gian bắt đầu</label>
        <input type="datetime-local" id="StartTime" v-model="event.StartTime" />
  
        <label for="EndTime">Thời gian kết thúc</label>
        <input type="datetime-local" id="EndTime" v-model="event.EndTime" />
  
        <label for="Location">Địa điểm</label>
        <input type="text" id="Location" v-model="event.Location" />
  
        <label for="EventImages">Hình ảnh sự kiện</label>
        <textarea id="EventImages" v-model="event.EventImages" readonly ></textarea>
  
        <label for="Description">Mô tả</label>
        <textarea id="Description" v-model="event.Description"></textarea>
  
        <label for="RegisteredCount">Số người đã đăng ký</label>
        <input type="number" id="RegisteredCount" v-model="event.RegisteredCount" readonly />
  
        <label for="MaxAttendees">Số người tham gia tối đa</label>
        <input type="number" id="MaxAttendees" v-model="event.MaxAttendees" />
  
        <button type="submit">Lưu sự kiện</button>
      </form>
    </div>
  </template>
  
  <script>
  import { getEventById } from '@/api/publicEventsAPI';
  import { editEvent } from '@/api/createdEventsAPI';
  export default {
    data() {
      return {
        event: {
          EventType: '',
          EventName: '',
          StartTime: '',
          EndTime: '',
          Location: '',
          EventImages: '',  
          Description: '',
          RegisteredCount: 0,
          MaxAttendees: 0
        },
        list_event: [],
      };
    },
    
    async created() {
      this.eventId = parseInt(this.$route.params.id);
  
      try {
        // Gọi API để lấy danh sách người dùng đã đăng ký
        const response = await getEventById(this.eventId);
        this.list_event = response.data;
        const formatDateTime = (dateTime) => {
            if (!dateTime) return '';
            
            // Chuyển đổi chuỗi ngày giờ thành đối tượng Date
            const dateObj = new Date(dateTime);
            
            // Kiểm tra nếu dateObj là ngày hợp lệ
            if (isNaN(dateObj.getTime())) {
            console.error("Không thể chuyển đổi ngày giờ:", dateTime);
            return '';
            }
            
            // Chuyển đối tượng Date thành chuỗi đúng định dạng
            return dateObj.toISOString().slice(0, 16);
        };
        this.event = {
            EventType: this.list_event[0].EventType || '',
            EventName: this.list_event[0].EventName || '',
            StartTime: formatDateTime(this.list_event[0].StartTime) || '',
            EndTime: formatDateTime(this.list_event[0].EndTime) || '',
            Location: this.list_event[0].Location || '',
            EventImages: this.list_event[0].EventImages || '',
            Description: this.list_event[0].Description,
            RegisteredCount: this.list_event[0].RegisteredCount || 0,
            MaxAttendees: this.list_event[0].MaxAttendees || 0
        };
        // In ra danh sách người dùng
        console.log("List of registered users:", this.list_event[0]);
        
      } catch (error) {
        console.error("Lỗi khi lấy dữ liệu sự kiện:", error);
      }
    },
    methods: {
      async submitEvent() {
        try {
            const response = await editEvent(this.eventId,this.event.StartTime,this.event.EndTime,
                                    this.event.Location,this.event.Description,this.event.MaxAttendees);
            // alert(response.data.message); 

            if (response.data.message === "event updated successfully") {
              if (window.location.href.includes("editEvent")) {
                this.$router.push({ name: "DetailEventsCreated" });
              }
              localStorage.setItem("updateNotification", "Sửa thành công");
            }
        } catch (error) {
            console.error('Error update event:', error);
            alert('Có lỗi xảy ra khi sửa sự kiện.');
        }
      }
      
    }
  };
  </script>
  
  <style scoped>
  .event-form {
    max-width: 600px;
    margin: 0 auto;
  }
  .event-form label {
    display: block;
    margin-top: 15px;
    font-weight: bold;
  }
  .event-form input,
  .event-form textarea {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
  }
  .event-form button {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 16px;
  }
  </style>
  