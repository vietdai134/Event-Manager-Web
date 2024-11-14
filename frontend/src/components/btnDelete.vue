<!-- RegisterButton.vue -->
<template>
  <button class="delete_btn" @click="deleteEventClick">xoá</button>
</template>
  
  <script>
import { deleteEvent } from "@/api/createdEventsAPI";
import Cookies from "js-cookie";
export default {
  data() {
    return {
      eventId: null,
      gmail: "",
    };
  },
  created() {
    this.gmail = Cookies.get("email");
    this.eventId = parseInt(this.$route.params.id);
  },
  methods: {
    async deleteEventClick() {
      try {
        const response = await deleteEvent(this.eventId, this.gmail);
        // alert(response.data.message);

        if (response.data.message === "event deleted successfully") {
          if (
            window.location.href.includes(`/Events-Created/${this.eventId}`)
          ) {
            this.$router.push({ name: "EventsCreated" });
          }
          localStorage.setItem("updateNotification", "Đã xoá thành công");
          // window.location.reload();
        }
      } catch (error) {
        console.error("Error deleting event:", error);
        alert("Có lỗi xảy ra khi xoá sự kiện.");
      }
    },
  },
};
</script>
  