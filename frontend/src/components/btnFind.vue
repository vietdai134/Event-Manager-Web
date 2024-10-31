<template>
  <div>
    <!-- Search Input -->
    <input
      type="text"
      v-model="searchQuery"
      placeholder="Tìm kiếm sự kiện theo tên"
    />

    <!-- Display Only the Filtered Event -->
    <div v-if="filteredEvents.length" class="list_container">
      <div class="event_row">
        <div 
          class="event_card" 
          :class="isLightMode ? 'light_card' : 'dark_card'"
        >
          <img 
            v-if="filteredEvents[0].Image" 
            :src="getEventImage(filteredEvents[0].Image)" 
            alt="Event Image" 
            class="event_image" 
          />
          <h3>{{ filteredEvents[0].EventName }}</h3>
          <p>{{ filteredEvents[0].Description }}</p>
          <p>Thời gian bắt đầu: {{ filteredEvents[0].StartTime }}</p>
          <p>Số người tham gia: {{ filteredEvents[0].registeredCount }} / {{ filteredEvents[0].maxParticipants }}</p>

          <!-- Register Button -->
          <button 
            @click="registerEvent(filteredEvents[0].id)" 
            :disabled="filteredEvents[0].registeredCount >= filteredEvents[0].maxParticipants"
          >
            Đăng ký
          </button>
        </div>
      </div>
    </div>

    <!-- Message if No Events Found -->
    <div v-else-if="searchQuery">
      <p>Không có sự kiện nào phù hợp với tìm kiếm của bạn.</p>
    </div>
  </div>
</template>

<script>
import eventPublicScript from '@/script/eventPublicScript';

export default {
  mixins: [eventPublicScript],
  data() {
    return {
      searchQuery: "", // Bind to the search input
    };
  },
  computed: {
    filteredEvents() {
      const matchedEvents = this.public_events.filter((event) =>
        event.EventName.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
      return matchedEvents.length ? [matchedEvents[0]] : []; // Trả về mảng chỉ chứa sự kiện đầu tiên hoặc mảng rỗng
    },
  },
  methods: {
    getEventImage(imageName) {
      try {
        return require(`@/assets/img/${imageName}`);
      } catch (error) {
        console.error("Image not found:", error);
        return ''; // Trả về chuỗi rỗng nếu hình ảnh không tìm thấy
      }
    },
  },
};
</script>

<style scoped>
.list_container {
  margin: 20px 0;
}

.event_row {
  display: flex;
  justify-content: center;
}

.event_card {
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  transition: box-shadow 0.3s;
}

.event_card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.event_image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin: 10px 0;
}

.light_card {
  background-color: #ffffff;
}

.dark_card {
  background-color: #333333;
  color: #ffffff;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
}
</style>
