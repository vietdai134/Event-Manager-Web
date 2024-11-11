<template>
  <div id="bg">
    <div class="mainContent">
      <div id="content">
        <div :key="index" v-for="(ct,index) in contents" :class="{contactLink: ct === 'Liên Hệ Ngay',
                                                                  item0: index === 0,
                                                                  item1: index === 1, 
                                                                  item2: index === 2, 
                                                                  item3: index === 3}">
          <img v-if="ct.startsWith('http')" :src="ct"/>
          <p v-else>{{ ct }}</p>
        </div>
      </div>
      <div class='statis'>
          <div class="statis--info" :key="index" v-for="(achiv, index) in achievements">{{ achiv }}</div>
      </div>
      <div id="why">
        <div id="why--title">
          <p id="why--title__titleSub">Vì sao nên lựa chọn công ty tổ chức sự kiện</p>
          <p id="why--title__titleEx">MDK Group</p>
          <div id="why--title__frame">
            <div id="why--title__content" :key="index" v-for="(exp, index) in exps">
              <img :src="exp.image" alt="">
              <h1>{{ exp.title }}</h1>
              <p>{{ exp.content }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="contactLink pos">Liên Hệ Ngay</div>
      <div class="main--title">Cùng công ty sự kiện MDK Group khám phá thế giới sự kiện đa sắc màu</div>
      
      <div class="events">

        <div class="megaEvent--details" :key="index" v-for="(megaEvent, index) in megaEvents">
          <h2>{{ megaEvent.title }}</h2>
          <p>{{ megaEvent.content }}</p>
          <div :key="imgIndex" v-for="(imgLink, imgIndex) in megaEvent.link">
            <img :id="'megaEvent-'+'-img-'+imgIndex" :src="imgLink" alt="">
          </div>
        </div>

        <div class="launchEvent--details" :key="index" v-for="(launchEvent, index) in launchEvents">
          <h2>{{ launchEvent.title }}</h2>
          <p>{{ launchEvent.content }}</p>
          <div :key="imgIndex" v-for="(imgLink, imgIndex) in launchEvent.link">
            <img :id="'launchEvent-'+'-img-'+imgIndex" :src="imgLink" alt="">
          </div>
        </div>

        <div class="specialEvent--details" :key="index" v-for="(specialEvent, index) in specialEvents">
          <h2>{{ specialEvent.title }}</h2>
          <p>{{ specialEvent.content }}</p>
          <div :key="imgIndex" v-for="(imgLink, imgIndex) in specialEvent.links">
            <img :id="'specialEvent-'+'-img-'+imgIndex" :src="imgLink" alt="">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import HomeScript from '@/script/HomeScript';
export default {
  name: 'HomeView',
  components: {

  },
  mixins: [HomeScript],
  data(){
    return{
      contents: [
        'MDK Group - Nền tảng tổ chức sự kiện chuyên nghiệp',
        'Với đội ngũ nhân viên giàu kinh nghiệm, nhiệt huyết và đầy tâm huyết, MDK Group cam kết mang đến cho bạn những sự kiện ấn tượng, độc đáo và thành công ngoài mong đợi. ',
        'Liên Hệ Ngay',
        'https://ignitionagency.vn/wp-content/uploads/2024/06/TSN.png'
      ],
      achievements: [
        '100+ khách hàng',
        '300+ dự án',
        '95% khách hàng hài lòng',
        '10+ năm trong ngành'
      ],
      exps: [
        {
          image: 'https://ignitionagency.vn/wp-content/uploads/2024/05/Doi-ngu-dang-tin-cay-2.png',
          title: 'Đội ngũ chuyên nghiệp',
          content: 'Đội ngũ nhân viên sáng tạo, nhiệt tình và giàu kinh nghiệm, luôn cập nhật những xu hướng mới nhất.'
        },
        {
          image: 'https://ignitionagency.vn/wp-content/uploads/2024/05/Tap-trung-vao-sang-tao-1.png',
          title: 'Kinh nghiệm dày dặn',
          content: 'Có nhiều năm kinh nghiệm trong lĩnh vực và đã thành công xây dựng hàng trăm phần mềm quản lí sự kiện lớn nhỏ cho các khách hàng trong và ngoài nước.'
        },{
          image: 'https://ignitionagency.vn/wp-content/uploads/2024/05/San-choi-doc-dao.png',
          title: 'Sáng tạo và đổi mới',
          content: 'Luôn không ngừng sáng tạo và đổi mới để mang đến cho khách hàng những sự kiện độc đáo và ấn tượng nhất.'
        },{
          image: 'https://ignitionagency.vn/wp-content/uploads/2024/05/Dich-vu-hoan-hao.png',
          title: 'Cam kết chất lượng',
          content: 'Cam kết cung cấp dịch vụ chất lượng cao với giá cả cạnh tranh.'
        },{
          image: 'https://ignitionagency.vn/wp-content/uploads/2024/05/Su-lua-chon-vuot-troi-2.png',
          title: 'Uy tín và tin cậy',
          content: 'Luôn đặt uy tín và trách nhiệm lên hàng đầu, đảm bảo sự hài lòng tuyệt đối cho khách hàng.'
        }
      ],
      megaEvents:[
        {
          title: 'Các sự kiện công khai',
          content: 'Khám phá các sự kiện công khai đang diễn ra trên nền tảng của chúng tôi. Tại đây, bạn có thể xem chi tiết về từng sự kiện, từ thời gian, địa điểm đến các hoạt động nổi bật. Chúng tôi cung cấp thông tin đầy đủ và dễ hiểu để bạn có thể nhanh chóng lựa chọn và đăng ký tham gia các sự kiện phù hợp với sở thích của mình.',
          link: [
            'https://ignitionagency.vn/wp-content/uploads/2024/06/z5421069476620_29e9997c21f369734e68821e71863dba.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/z5421069456671_b7dcfd8c8fda4d2537f3a37a2e82815d.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/z5421069488476_56cffbf5b2d8f7fd3e14a2d98ee90ddd.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/z5421069459799_cf736b3c2698b420694876ba09c511c1.jpg'
          ]
        }
      ],
      launchEvents:[
        {
          title: 'Sự kiện đã đăng ký',
          content: 'Quản lý các sự kiện bạn đã đăng ký tham gia trong phần này. Tất cả các thông tin về sự kiện, bao gồm thời gian, địa điểm, thông báo từ người tổ chức sẽ được lưu trữ để bạn dễ dàng theo dõi. Tính năng này giúp bạn không bỏ lỡ bất kỳ sự kiện nào mà bạn đã đăng ký, với thông báo nhắc nhở trước mỗi sự kiện.',
          link: [
            'https://ignitionagency.vn/wp-content/uploads/2024/06/PAD9080.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/PAD8837.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/PAD8874.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/PAD9176.jpg'
          ]
        }
      ],
      specialEvents: [
        {
          title: 'Sự kiện đã tạo',
          content: 'Lưu giữ mọi khoảnh khắc đáng nhớ tại các sự kiện bạn đã tham gia. Phần này cung cấp một danh sách tổng hợp các sự kiện trước đây mà bạn từng tham gia, giúp bạn dễ dàng xem lại thông tin và lưu lại những kỷ niệm đáng giá. Đối với người dùng thường xuyên tham dự các sự kiện, tính năng này sẽ trở thành một nơi lưu trữ những trải nghiệm thú vị của bạn.',
          links: [
            'https://ignitionagency.vn/wp-content/uploads/2024/06/FINN0248-2048x1280.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/PHAN8374-Edit-2048x1366.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/z5421104717218_3edd0f6848019b213f0c11e14e253d6d.jpg',
            'https://ignitionagency.vn/wp-content/uploads/2024/06/FINN9906-Enhanced-NR-2048x1280.jpg'
          ]
        }
      ],
      
    }
  }
}
</script>

<style scoped src="../css/main.css">

</style>