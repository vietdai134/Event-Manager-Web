<template>
    <footer>
      <div id="footer--background" :key="index" v-for="(footer, index) in footers" class="footer">
        <div>
          <div class="footer--background__update">
            {{ footer.update }}
          </div>
        </div>
        <div id="menu">
          <div class="footer--background__menu" :key="i" v-for="(menu,i) in footer.menues">
            <div>{{ menu }}</div>
          </div>
        </div>
        <div id="sp">
          <div class="footer--background__support" :key="i" v-for="(sp,i) in footer.supports">
            <div>{{ sp }}</div>
          </div>
        </div>
      </div>
      <div id="form">
        <input type="text" placeholder="Enter Your Email" required v-model="email">
      </div>
      <div id="icon">
        <span class="ti-credit-card"></span>
        <span class="ti-linkedin"></span>
        <span class="ti-pinterest"></span>
        <span class="ti-vimeo-alt"></span>
        <span class="ti-twitter"></span>
        <span class="ti-instagram"></span>
        <span class="ti-facebook"></span>
        <span class="ti-github"></span>
      </div>
    </footer>
</template>

<script>
export default {
    name: "appFooter",
    data(){
        return{
            footers: [
                {
                update: 'Get updates on fun stuff you probably want to know about in your inbox.',
                menues: [
                    'Shop All',
                    'About Us',
                    'Community',
                    'Vibes'
                ],
                supports: [
                    'Shipping & Returns',
                    'Help & FAQ',
                    'Terms & Conditions',
                    'Privacy Policy',
                    'Contact',
                    'Login'
                ]
                }
            ]
        }
    }
}
</script>

<style>
html, body {
    height: 100%;
    margin: 0;
}

.app {
    display: flex;
    flex-direction: column;
    min-height: 100vh; /* Tạo chiều cao tối thiểu cho toàn bộ trang */
}

.footer {
    margin-top: auto; /* Đẩy footer xuống dưới cùng */
    background-color: #f1f1f1; /* Màu nền cho footer */
    padding: 10px; /* Khoảng cách bên trong footer */
    text-align: center; /* Canh giữa nội dung */
}
</style>
