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

export default {
  name: 'HomeView',
  components: {

  },
  data(){
    return{
      contents: [
        'MDK Group - Dịch vụ tổ chức sự kiện nâng tầm đẳng cấp',
        'Với đội ngũ nhân viên giàu kinh nghiệm, nhiệt huyết và đầy tâm huyết, Ignition Group cam kết mang đến cho bạn những sự kiện ấn tượng, độc đáo và thành công ngoài mong đợi. ',
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
          content: 'Đội ngũ nhân viên sáng tạo, nhiệt tình và giàu kinh nghiệm, luôn cập nhật những xu hướng mới nhất trong lĩnh vực tổ chức sự kiện.'
        },
        {
          image: 'https://ignitionagency.vn/wp-content/uploads/2024/05/Tap-trung-vao-sang-tao-1.png',
          title: 'Kinh nghiệm dày dặn',
          content: 'Có nhiều năm kinh nghiệm trong lĩnh vực tổ chức sự kiện và đã thành công tổ chức hàng trăm sự kiện lớn nhỏ cho các khách hàng trong và ngoài nước.'
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
          title: 'Mega Event',
          content: 'Biến ý tưởng táo bạo thành sự kiện bùng nổ, khuấy động mọi giác quan với sức hút không thể cưỡng lại. Ignition Group sở hữu năng lực tổ chức các sự kiện quy mô lớn, đảm bảo an toàn, chuyên nghiệp, ấn tượng và thành công. ',
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
          title: 'Launch Event',
          content: 'Ignition Group giúp bạn tạo ấn tượng mạnh mẽ khi giới thiệu sản phẩm mới, khai trương cửa hàng hoặc dịch vụ… Chúng tôi thiết kế các sự kiện độc đáo, thu hút sự chú ý của công chúng và truyền thông, đảm bảo sản phẩm của bạn được chào đón nồng nhiệt. ',
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
          title: 'Special Event',
          content: 'Kỷ niệm những dấu mốc quan trọng, truyền tải thông điệp ý nghĩa với các sự kiện đặc biệt được thiết kế riêng. Ignition Group thấu hiểu mong muốn của bạn và sáng tạo những ý tưởng độc đáo, giúp sự kiện trở thành trải nghiệm khó quên.',
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

<style>

</style>