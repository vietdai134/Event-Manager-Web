<!-- RegisterButton.vue -->
<template>
    <button class="edit_btn" @click="editEvent">Sửa</button>
  </template>
  
  <script>
  export default {
    data() {
    return {
        eventId:null
      };
    },
    created() {
      this.eventId = parseInt(this.$route.params.id);
    },
    methods: {
        editEvent() {
          this.$router.push({ path: `${this.eventId}`+'/editEvent' });
      }
    }
  }
  </script>
  