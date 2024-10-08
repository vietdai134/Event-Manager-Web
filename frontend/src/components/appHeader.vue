<template>
  <div>
    <nav class="navbar navbar-expand-lg" :class="{'bg-primary text-white': isLightMode, 'bg-light text-dark': !isLightMode}">
      <div class="container-fluid">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Home' }">Home </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'About' }">About </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'EventsPublic' }">Sự kiện công khai </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'EventsRegistered' }">Sự kiện đã đăng ký </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'EventsPast' }">Sự kiện đã tham gia </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'EventsCreated' }">Sự kiện đã tạo </router-link>
          </li>
          
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'InfoUser' }">Thông tin người dùng</router-link>
          </li>
        </ul>
        <button @click="toggleTheme" :class="isLightMode ? 'btn btn-outline-light btn-light-mode' : 'btn btn-outline-dark btn-dark-mode'" type="button" style="position: relative; display: flex; align-items: center;">
          <i :class="isLightMode ? 'fas fa-sun' : 'fas fa-moon'" style="font-size: 1.5em;"></i>
          <span class="ms-2">Chuyển chế độ</span>
        </button>
      </div>
    </nav>
  </div>
</template>

<script>
import appHeaderScript from '@/script/appHeaderScript';

export default {
  mixins: [appHeaderScript],
  
};
</script>

<style scoped src="../css/appHeaderStyle.css">

</style>
