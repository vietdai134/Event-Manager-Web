<!-- RegisterButton.vue -->
<template>
  <button
    :class="
      isLightMode
        ? 'cancel_register_btn light_btn'
        : 'cancel_register_btn dark_btn'
    "
    @click="cancelregisterEvent"
  >
    Huỷ đăng Ký
  </button>
</template>
  
  <script>
import getIsLightMode from "@/script/getIsLightMode";
export default{
  mixins:[getIsLightMode], // Sử dụng mixin
  methods: {
    someMethod() {
      console.log(this.isLightMode);
      this.updateLightMode(); 
    },
  },
}
</script>
  