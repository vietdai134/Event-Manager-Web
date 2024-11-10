<template>
  <div class="container_wrapper">
    <div v-if="event" class="container_event_detail">
      <!-- Phần bên trái chiếm 70% -->
      <div class="left_content">
        <h2>{{ event.EventName }}</h2>
        <div class="img_event">
          <img
            :src="getEventImage(event.EventImages)"
            alt="Event image"
            class="event_image"
          />
        </div>
        <div class="info_detail">
          <p>{{ event.Description }}</p>
        </div>
      </div>
      <!-- Phần bên phải chiếm 30% -->
      <div class="right_content">
        <div class="event_details_box_light">
          <p><strong>Địa điểm:</strong> {{ event.Location }}</p>
          <p>
            <strong>Thời gian bắt đầu:</strong> {{ formatDate(event.StartTime) }} <br>
            <strong>Thời gian kết thúc:</strong> {{ formatDate(event.EndTime) }}
          </p>
          <p>
            <strong>Số lượng đã đăng ký:</strong> {{ event.RegisteredCount }} /
            {{ event.MaxAttendees }}
          </p>
          <!-- <button class="register_btn">Đăng Ký</button> -->
          <div>
            <component
              v-for="(button, index) in currentButtonComponents"
              :key="index"
              :is="button"
              @openDialog="openInviteDialog"
            />
          </div>
        </div>
      </div>

      <!-- Dialog thêm Gmail, chỉ hiện khi `showInviteDialog` là `true` -->
      <dialogAddGmail 
        :isVisible="showInviteDialog" 
        @close="closeInviteDialog" 
      />
    </div>
    <div v-else>
      <p>Không tìm thấy sự kiện.</p>
    </div>
  </div>
</template>
  
  <script>
import eventDetailScript from "@/script/eventDetailScript";
import { notify } from "@/script/Notification";
export default {
  mixins: [eventDetailScript],
  mounted(){
    const updateNotification = localStorage.getItem("updateNotification");
    if (updateNotification) {
        notify(updateNotification, "success");
        localStorage.removeItem("updateNotification"); // Xóa thông báo sau khi hiển thị
    }
  },
  methods:{
    formatDate(dateString) {
      if(dateString===""){
        return "dd/MM/yyyy hh:MM:ss";
      }
      const date = new Date(dateString);
      const day = String(date.getUTCDate()).padStart(2, "0");
      const month = String(date.getUTCMonth() + 1).padStart(2, "0"); // Tháng bắt đầu từ 0
      const year = date.getUTCFullYear();
      const hours = String(date.getUTCHours()).padStart(2, "0");
      const minutes = String(date.getUTCMinutes()).padStart(2, "0");
      const seconds = String(date.getUTCSeconds()).padStart(2, "0");

      return `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
    },
  }
};
</script>
  
  <style scoped src="../css/eventDetailStyle.css">
</style>
  