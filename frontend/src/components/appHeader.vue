<template>
  <div>
    <nav
      class="navbar navbar-expand-lg"
      :class="{
        'bg-primary text-white': isLightMode,
        'bg-light text-dark': !isLightMode,
      }"
    >
      <div class="container-fluid">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <img src="../assets/img/logo2.png" alt="Logo Event" />
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Home' }"
              >Home</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'About' }"
              >About</router-link
            >
          </li>
          <!-- menu sự kiện -->
          <li
            class="nav-item"
            @mouseover="showList = true"
            @mouseleave="showList = false"
          >
            <span style="cursor: pointer">Sự Kiện</span>
            <ul class="menu_events" :class="{ show: showList }">
              <li>
                <i
                  class="fa-solid fa-arrow-right"
                  :style="{ color: isLightMode ? '#74C0FC' : 'black' }"
                ></i>
                <router-link class="menu_item" :to="{ name: 'EventsPublic' }"
                  >Sự kiện công khai</router-link
                >
              </li>
              <li>
                <i
                  class="fa-solid fa-arrow-right"
                  :style="{ color: isLightMode ? '#74C0FC' : 'black' }"
                ></i>
                <router-link
                  class="menu_item"
                  :to="{ name: 'EventsRegistered' }"
                  >Sự kiện đã đăng ký</router-link
                >
              </li>
              <li>
                <i
                  class="fa-solid fa-arrow-right"
                  :style="{ color: isLightMode ? '#74C0FC' : 'black' }"
                ></i>
                <router-link class="menu_item" :to="{ name: 'EventsPast' }"
                  >Sự kiện đã tham gia</router-link
                >
              </li>
              <li>
                <i
                  class="fa-solid fa-arrow-right"
                  :style="{ color: isLightMode ? '#74C0FC' : 'black' }"
                ></i>
                <router-link class="menu_item" :to="{ name: 'EventsCreated' }"
                  >Sự kiện đã tạo</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'InfoUser' }"
              >Thông tin người dùng</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'createEvent' }"
              >Thêm Sự Kiện</router-link
            >
          </li>
        </ul>
        <button
          id="login"
          :class="isLightMode ? 'btn-light-mode' : 'btn-dark-mode'"
          @click="isLoggedIn ? logout() : goToLogin()"
        >
          <span>{{ isLoggedIn ? "Đăng Xuất" : "Đăng Nhập" }}</span>
          <i
            class="fa-solid fa-right-to-bracket"
            :style="{ color: isLightMode ? '#74C0FC' : 'white' }"
          ></i>
        </button>
        <button
          @click="toggleTheme"
          :class="isLightMode ? 'btn btn-light-mode' : 'btn btn-dark-mode'"
          type="button"
          style="position: relative; display: flex; align-items: center"
        >
          <i
            :class="isLightMode ? 'fas fa-sun' : 'fas fa-moon'"
            style="font-size: 1.5em"
          ></i>
          <span class="ms-2">{{ isLightMode ? "Light" : "Dark" }}</span>
        </button>
      </div>
      <div
        v-if="isLoggedIn"
        :class="isLightMode ? 'name_login light' : 'name_login dark'"
      >
        <i class="fa-solid fa-user"></i>
        <span>{{ user_name }}</span>
      </div>
    </nav>
  </div>
</template>

<script>
import appHeaderScript from "@/script/appHeaderScript";
import Cookies from "js-cookie";
import { confirmNotify } from "@/script/Notification";
export default {
  props: ["user"],
  mixins: [appHeaderScript],
  data() {
    return {
      showList: false,
      user_name: null,
      isLoggedIn: false,
      cookieCheckInterval: null,
    };
  },
  created() {
    this.updateLoginStatus();
    this.startCookieWatcher();
  },
  beforeUnmount() {
    clearInterval(this.cookieCheckInterval); // Xóa khoảng thời gian khi component bị hủy
  },
  methods: {
    goToLogin() {
      this.$router.push({ name: "Login" });
      // this.isLoggedIn = true;
      this.updateLoginStatus();
    },
    logout() {
      confirmNotify(
        "Bạn có chắc chắn muốn đăng xuất không?",
        () => {
            Cookies.remove("email");
            Cookies.remove("fullname");
            this.updateLoginStatus();
        },
        () => {
            console.log("Đã hủy đăng xuất");
        }
      );
    },
    updateLoginStatus() {
      const fullNameFromCookie = Cookies.get("fullname");
      if (fullNameFromCookie) {
        this.user_name = fullNameFromCookie;
        this.isLoggedIn = true;
      } else {
        this.user_name = null;
        this.isLoggedIn = false;
      }
    },
    startCookieWatcher() {
      this.cookieCheckInterval = setInterval(() => {
        this.updateLoginStatus();
      }, 100);
    },
  },
};
</script>

<style scoped src="../css/appHeaderStyle.css">
</style>
