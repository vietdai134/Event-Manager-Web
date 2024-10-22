<template>
  <div >
    <appHeader></appHeader>
    <router-view></router-view>
    <AppFooter ></AppFooter>
  </div>
  
</template>

<script>

import appHeader from './components/appHeader.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import AppFooter from './components/appFooter.vue';



export default {
  components:{
    appHeader,
    AppFooter

  }
  
};
</script>

<style>

</style>
