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
        alert(response.data.message); 

        if (response.data.message === "cancel registered successfully") {
          window.location.reload(); 
        }
      } catch (error) {
        console.error('Error registering event:', error);
        alert('Có lỗi xảy ra khi đăng ký sự kiện.');
      }
    },
    someMethod() {
      console.log(this.isLightMode);
      this.updateLightMode(); 
    },
  },
}
</script>
  