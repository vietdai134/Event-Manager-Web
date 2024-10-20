<template>
  <div class="container_public_event">
    <h1
      style="text-align: center; font-size: 2.5em; margin: 20px 0"
      :class="isLightMode ? 'light-text' : 'dark-text'"
    >
      Sự Kiện Đã Đăng Ký
    </h1>
    <div
      class="list_container"
      v-for="group in groupedEvents"
      :key="group.date"
    >
      <h2 :class="isLightMode ? 'event_date_light light-mode-text' : 'event_date_dark dark-mode-text'" >
       {{ formatDate(group.date) }}
      </h2>
      <div class="row_container">
        <div class="event_row">
          <router-link
            v-for="event in group.events"
            :key="event.id"
            :to="{ name: 'DetailEventRegistered', params: { id: event.ID } }"
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
                    backgroundColor: getColorForPercentage(
                      calculateRegisteredPercentage(event)
                    ),
                  }"
                ></div>
              </div>
              <div class="footer_card">
                <div class="total_per">
                  {{ event.RegisteredCount }} / {{ event.MaxAttendees }} người
                  đã đăng ký
                </div>
                <btnCancelRegis></btnCancelRegis>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
  
  
  <script>
import eventRegisteredScript from "@/script/eventRegisteredScript";
import btnCancelRegis from "@/components/btnCancelRegis.vue";
import getIsLightMode from "@/script/getIsLightMode";
export default {
  components: {
    btnCancelRegis,
  },
  
  methods: {
    someMethod() {
      console.log(this.isLightMode);
      this.updateLightMode(); 
    },
    
  },
  mixins: [eventRegisteredScript,getIsLightMode],
};
</script>
  
  <style scoped src="../css/eventPublicStyle.css"></style>
  