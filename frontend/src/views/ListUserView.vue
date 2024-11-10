<template>
  <div id="app">
    <div class="container_list_view">
      <div class="list_view">
        <h1>Danh sách người đã đăng ký</h1>
        <div class="search-container">
          <div class="input-wrapper">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="Tìm kiếm"
              class="search-input"
            />
            <i
              class="fa-solid fa-magnifying-glass search-icon"
              style="color: #74c0fc"
            ></i>
          </div>
        </div>
        <ul>
          <li v-for="user in filteredListUser" :key="user.Gmail">
            {{ user.FullName }} - {{ user.Gmail }} - {{ user.PhoneNumber }}
          </li>
        </ul>
      </div>
      <div v-if="!filteredListUser.length && searchQuery">
        <p>Không có người dùng nào được tìm thấy</p>
      </div>
    </div>
  </div>
</template>
<script>
import { getListUserRegis } from "@/api/createdEventsAPI";

export default {
  data() {
    return {
      list_user: [],
      eventId: null,
      searchQuery: "", // Biến lưu trữ từ khóa tìm kiếm
    };
  },
  async created() {
    this.eventId = parseInt(this.$route.params.id);

    try {
      // Gọi API để lấy danh sách người dùng đã đăng ký
      const response = await getListUserRegis(this.eventId);
      this.list_user = response.data;

      // In ra danh sách người dùng
      console.log("List of registered users:", this.list_user);
    } catch (error) {
      console.error("Lỗi khi lấy dữ liệu sự kiện:", error);
    }
  },
  computed: {
    filteredListUser() {
      return this.list_user.filter(
        (user) =>
          user.FullName.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          user.Gmail.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          user.PhoneNumber.includes(this.searchQuery)
      );
    },
  },
};
</script>
<style scoped src="../css/ListView.css">

</style>