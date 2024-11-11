<template>
    <footer>
      <div id="footer--background" :key="index" v-for="(footer, index) in footers" class="footer">
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
    font-family: Arial, sans-serif;
}

.app {
    display: flex;
    flex-direction: column;
    min-height: 100vh; /* Ensures full-page height layout */
}

footer {
    margin-top: auto; /* Push footer to the bottom */
    background-color: #f1f1f1; /* Footer background color */
    padding: 20px 0; /* Space around footer content */
    width: 100%; /* Make footer span the full width */
}

#footer--background {
    display: flex;
    justify-content: space-around; /* Space out menu and support evenly */
    padding: 10px 0; /* Space between sections */
}

.footer--background__menu,
.footer--background__support {
    flex: 1; /* Ensure both sections take equal space */
    text-align: left; /* Align text to the left for clarity */
}

#menu div,
#sp div {
    margin-bottom: 8px; /* Space between menu/support items */
}

#icon {
    margin-top: 20px;
    display: flex;
    justify-content: center; /* Center social icons */
    gap: 15px; /* Space between icons */
}

#icon span {
    font-size: 20px; /* Adjust icon size */
    cursor: pointer; /* Make icons clickable */
    transition: transform 0.2s ease;
}

#icon span:hover {
    transform: scale(1.2); /* Slightly enlarge icons on hover */
}

</style>
