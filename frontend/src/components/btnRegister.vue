<!-- RegisterButton.vue -->
<template>
  <button
    :class="isLightMode ? 'register_btn light_btn' : 'register_btn dark_btn'"
    @click="registerEvent"
  >
    Đăng Ký
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
  