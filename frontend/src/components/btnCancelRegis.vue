<!-- RegisterButton.vue -->
<template>
  <button
    :class="
      isLightMode
        ? 'cancel_register_btn light_btn'
        : 'cancel_register_btn dark_btn'
    "
    @click="cancelRegisterEvent"
  >
    Huỷ đăng Ký
  </button>
</template>
  
  <script>
import getIsLightMode from "@/script/getIsLightMode";
import Cookies from 'js-cookie'; 
import { cancelRegisterEvent } from "@/api/registeredEventsAPI";
import {notify} from "@/script/Notification"
export default{
  data() {
    return {
      eventId: null,
      gmail:""
    };
  },
  created(){
    this.gmail=Cookies.get('email');
    // console.log(this.gmail);
    this.eventId = parseInt(this.$route.params.id);
  },
  mixins:[getIsLightMode], // Sử dụng mixin
  methods: {
    async cancelRegisterEvent(){
      // console.log(this.eventId+this.gmail )
      try {
        const response = await cancelRegisterEvent(this.eventId, this.gmail);
        // alert(response.data.message); 
        if (response.data.message === "cancel registered successfully") {
          // notify("Hủy Đăng Ký Thành Công!", "success");
          // setTimeout(() => {
          if (window.location.href.includes("Events-Registered")) {
            this.$router.push({ name: "EventsRegistered" });
          }
          // }, 1000);
          localStorage.setItem("updateNotification", "Huỷ đăng ký thành công");
          
        }
      } catch (error) {
        console.error('Error registering event:', error);
        // alert('Có lỗi xảy ra khi đăng ký sự kiện.');
        notify("Lỗi Khi Huỷ đăng Ký!", "error");
      }
    },
    someMethod() {
      console.log(this.isLightMode);
      this.updateLightMode(); 
    },
  },
}
</script>
  