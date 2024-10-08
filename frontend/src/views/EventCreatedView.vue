<template>
  <div class="container_public_event">
    <div
      class="list_container"
      v-for="group in groupedEvents"
      :key="group.date"
    >
      <h2 class="event_date">{{ group.date }}</h2>
      <div class="row_container">
        <div class="event_row">
          <router-link
            v-for="event in group.events"
            :key="event.id"
            :to="{ name: 'DetailEventsCreated', params: { id: event.ID } }"
            class="event_card_link"
            exact
          >
            <div class="event_card">
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
                  {{ event.RegisteredCount }} / {{ event.MaxAttendees }} người đã đăng ký
                </div>
                 <!-- <button class="btn_dk" @click.prevent="registerEvent(event.ID)">Đăng Ký</button> -->
              </div>
            </div>
            
          </router-link>
        </div>
      </div>
    </div>
    
  </div>
</template>


<script>
import eventCreateScript from '@/script/eventCreateScript';
export default {
  mixins: [eventCreateScript],
};
</script>

<style scoped src="../css/eventPublicStyle.css"></style>
