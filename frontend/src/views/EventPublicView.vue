<template>
  <div class="container_public_event">
    <h1 style="text-align: center; font-size: 2.5em; margin: 20px 0;" :class="isLightMode ? 'light-text' : 'dark-text'">
      Sự Kiện Công Khai
    </h1>
    <div class="list_container" v-for="group in groupedEvents" :key="group.date">
      <h2 :class="isLightMode ? 'event_date_light light-mode-text' : 'event_date_dark dark-mode-text'" >
       {{ formatDate(group.date) }}
      </h2>
      <div class="row_container">
        <div class="event_row">
          <router-link
            v-for="event in group.events"
            :key="event.id"
            :to="{ name: 'DetailEventPublic', params: { id: event.ID } }"
            class="event_card_link"
            exact
          >
            <div :class="isLightMode ? 'event_card light_card' : 'event_card dark_card'">
              <img
                :src="getEventImage(event.EventImages)"
                alt="Event image"
                class="event_image"
              />
              <h3>{{ event.EventName }}</h3>
              <p>{{ event.Description }}</p>
              <div class="per_sl">
                <div
                  class="per_sl_now"
                  :style="{
                    width: calculateRegisteredPercentage(event) + '%',
                    backgroundColor: getColorForPercentage(calculateRegisteredPercentage(event)),
                  }"
                ></div>
              </div>
              <div class="footer_card">
                <div class="total_per">
                  {{ event.RegisteredCount }} / {{ event.MaxAttendees }} người đã đăng ký
                </div>
                <btnRegister></btnRegister>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import eventPublicScript from "@/script/eventPublicScript";
import btnRegister from "@/components/btnRegister.vue";
import { getLightMode } from "@/script/theme";

export default {
  components: {
    btnRegister,
  },
  data() {
    return {
      // Khai báo biến isLightMode
      isLightMode: getLightMode(), // Lấy giá trị ban đầu từ theme.js
    };
  },
  methods: {
    updateLightMode() {
      this.isLightMode = getLightMode(); // Cập nhật giá trị isLightMode từ theme.js
      // console.log("Giá trị isLightMode trong public.vue: ", this.isLightMode);
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
      const date = new Date(dateString);
      return date.toLocaleDateString('en-GB', options).replace(/\//g, '/'); // Định dạng ngày theo kiểu DD/MM/YYYY
    },
  },
  mounted() {
    this.updateLightMode();
    window.addEventListener("lightModeChanged", this.updateLightMode);
  },
  beforeUnmount() {
    window.removeEventListener("lightModeChanged", this.updateLightMode);
  },
  mixins: [eventPublicScript],
};
</script>

<style scoped src="../css/eventPublicStyle.css"></style>
