import {getEventById} from '@/api/publicEventsAPI'
import RegisterButton from '@/components/btnRegister.vue';
import DeleteButton from '@/components/btnDelete.vue'
import EditButton from '@/components/btnEdit.vue';
import ListUserButton from '@/components/btnListUser.vue'
import btnCancelRegis from '@/components/btnCancelRegis.vue';

export default {
  components: {  // Sửa từ `component` thành `components`
    RegisterButton,
    DeleteButton,
    EditButton,
    ListUserButton,
    btnCancelRegis
  },
  data() {
    return {
      event: null,
    };
  },
  created() {
    const eventId = parseInt(this.$route.params.id);
    
    this.fetchEvent(eventId);
  },
  methods: {
    // Hàm gọi API để lấy thông tin sự kiện
    async fetchEvent(eventId) {
      try {
        const response = await getEventById(eventId);
        this.event = response.data[0];
      } catch (error) {
        console.error("Lỗi khi lấy dữ liệu sự kiện:", error);
        this.event = null;
      }
    },
    
    getEventImage(image) {
      try {
        return require(`@/assets/img/${image}`);
      } catch (error) {
        console.error("Image not found:", error);
        return null; 
      }
    },
  },
  computed: {
    currentButtonComponents() {
      const buttons = [];
      
      // Kiểm tra URL hiện tại và trả về tên component phù hợp
      if (window.location.href.includes('Events-Public')) {
        buttons.push('RegisterButton');

      } 
      if (window.location.href.includes('Events-Created')) {
        buttons.push('EditButton');
        buttons.push('ListUserButton');
        buttons.push('DeleteButton');
      }
      if (window.location.href.includes('Events-Registered')) {
        buttons.push('btnCancelRegis');
      }
      if (window.location.href.includes('Events-Past')) {
        // buttons.push('EditButton');
      }
      return buttons; // Trả về mảng chứa các button
    }
  }
};