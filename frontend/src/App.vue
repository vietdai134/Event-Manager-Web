<template>
  <AppHeader :user="user" />
  <router-view @user-logged-in="handleUserLoggedIn" />
  <AppFooter />
</template>

<script>
import AppHeader from "./components/appHeader.vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import AppFooter from "./components/appFooter.vue";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      user: null, // chưa đăng nhập
    };
  },
  methods: {
    handleUserLoggedIn(userInfo) {
      this.user = userInfo; 
    },
  },
};
</script>

<style>
</style>
