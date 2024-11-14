<template>
  <div class="container_edit">
    <div class="event-form">
      <h1>Sửa Thông Tin Sự Kiện</h1>
      <form @submit.prevent="submitEvent">
        <div class="form_group_img">
          <!-- <label for="EventImages">Hình ảnh sự kiện</label> -->
          <img :src="imgSrc" alt="Uploaded Image" />
        </div>
        <div class="form_group_checkbox">
          <label for="EventType">Loại sự kiện</label>
          <input
            type="checkbox"
            id="EventType"
            :checked="event.EventType"
            disabled
          />
        </div>

        <div class="form_group">
          <label for="EventName">Tên sự kiện</label>
          <input
            type="text"
            id="EventName"
            v-model="event.EventName"
            disabled
          />
        </div>

        <div class="form_group">
          <label for="StartTime">Thời gian bắt đầu</label>
          <input
            type="datetime-local"
            id="StartTime"
            v-model="event.StartTime"
            required
            title="Không được để trống"
          />
        </div>

        <div class="form_group">
          <label for="EndTime">Thời Lượng</label>
          <input
            v-model="eventDuration"
            min="1"
            max="10"
            type="number"
            required
            title="Thời lượng từ 1 đến 10 giờ"
          />
        </div>

        <div class="form_group">
          <label for="Location">Địa điểm</label>
          <input type="text" id="Location" v-model="event.Location" />
        </div>

        <div class="form_group">
          <label for="Description">Mô tả</label>
          <textarea id="Description" v-model="event.Description"></textarea>
        </div>

        <div class="form_group">
          <label for="RegisteredCount">Số người đã đăng ký</label>
          <input
            type="number"
            id="RegisteredCount"
            v-model="event.RegisteredCount"
            disabled
          />
        </div>

        <div class="form_group">
          <label for="MaxAttendees">Số người tham gia tối đa</label>
          <input
            type="number"
            id="MaxAttendees"
            min="50"
            max="2000"
            v-model="event.MaxAttendees"
          />
        </div>

        <button id="edit_btn" type="submit">Lưu sự kiện</button>
      </form>
    </div>
  </div>
</template>
  
  <script>
import { getEventById } from "@/api/publicEventsAPI";
import { editEvent } from "@/api/createdEventsAPI";
import { notify, confirmNotify } from "@/script/Notification";

export default {
  data() {
    return {
      imgSrc: "",
      eventDuration: 1,
      event: {
        EventType: null,
        EventName: "",
        StartTime: "",
        EndTime: "",
        Location: "",
        EventImages: "",
        Description: "",
        RegisteredCount: 0,
        MaxAttendees: 0,
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
        if (!dateTime) return "";

        // Chuyển đổi chuỗi ngày giờ thành đối tượng Date
        const dateObj = new Date(dateTime);

        // Kiểm tra nếu dateObj là ngày hợp lệ
        if (isNaN(dateObj.getTime())) {
          console.error("Không thể chuyển đổi ngày giờ:", dateTime);
          return "";
        }

        // Chuyển đối tượng Date thành chuỗi đúng định dạng
        return dateObj.toISOString().slice(0, 16);
      };

      this.event = {
        EventType: this.list_event[0].EventType === "PL" ? true : false,
        EventName: this.list_event[0].EventName || "",
        StartTime: formatDateTime(this.list_event[0].StartTime) || "",
        EndTime: formatDateTime(this.list_event[0].EndTime) || "",
        Location: this.list_event[0].Location || "",
        EventImages: this.list_event[0].EventImages || "",
        Description: this.list_event[0].Description,
        RegisteredCount: this.list_event[0].RegisteredCount || 0,
        MaxAttendees: this.list_event[0].MaxAttendees || 0,
      };
      this.imgSrc = require(`../assets/img/${this.event.EventImages}`);
      this.event.EventImages;
      // In ra danh sách người dùng
      console.log("List of registered users:", this.list_event[0]);
    } catch (error) {
      console.error("Lỗi khi lấy dữ liệu sự kiện:", error);
    }
  },
  methods: {
    async submitEvent() {
      confirmNotify(
        "Bạn có chắc muốn thay đổi thông tin sự kiện không?",
        async () => {
          try {
            const enddate = new Date(this.event.StartTime);
            enddate.setHours(
              enddate.getHours() + parseInt(this.eventDuration, 10)
            );
            const formatDateTime = (date) => {
              const yyyy = date.getFullYear();
              const mm = String(date.getMonth() + 1).padStart(2, "0"); // Month is 0-indexed
              const dd = String(date.getDate()).padStart(2, "0");
              const hh = String(date.getHours()).padStart(2, "0");
              const min = String(date.getMinutes()).padStart(2, "0");
              return `${yyyy}-${mm}-${dd} ${hh}:${min}:00`;
            };

            this.event.EndTime = formatDateTime(enddate);
            const response = await editEvent(
              this.eventId,
              this.event.StartTime,
              this.event.EndTime,
              this.event.Location,
              this.event.Description,
              this.event.MaxAttendees
            );
            // console.log(response.data.message);

            if (response.data.message === "event updated successfully") {
              if (window.location.href.includes("editEvent")) {
                this.$router.push({ name: "DetailEventsCreated" });
              }
              localStorage.setItem("updateNotification", "Sửa thành công");
            }
          } catch (error) {
            console.error("Error update event:", error);
            notify("Có lỗi xảy ra khi sửa sự kiện.", "error");
          }
        },
        () => {
          console.log("Người dùng đã hủy thao tác.");
        }
      );
    },
  },
};
</script>
  
  <style scoped src ="../css/editView.css">
</style>
  