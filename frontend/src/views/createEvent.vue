<template>
  <div class="container_create">
    <div id="form_create">
      <h1>Thêm Mới Sự Kiện</h1>
      <form @submit.prevent="submitEvent">
        <div class="load_img">
          <img :src="imgSrc" alt="Uploaded Image" />
          <div class="input_top">
            <div class="form_group">
              <label>Tên Sự Kiện <span style="color: red">*</span> : </label>
              <input v-model="eventName" type="text" />
            </div>
            <div class="form_group_checkbox">
              <label>Sự Kiện Công Khai:</label>
              <input v-model="isPublic" type="checkbox" />
            </div>
            <label style="font-weight: bold"
              >Upload Image <span style="color: red">*</span> :</label
            >
            <div class="file-upload">
              <label for="fileInput" class="custom-file-label">Chọn tệp</label>
              <input
                type="file"
                id="fileInput"
                class="custom-file-input"
                @change="handleFileUpload"
              />
              <span class="file-name">{{ fileName }}</span>
            </div>
          </div>
        </div>
        <div class="input_bottom">
          <div class="datetime">
            <div class="form_group date">
              <label
                >Ngày Diễn Ra Sự Kiện <span style="color: red">*</span> :</label
              >
              <input v-model="eventDate" type="date" />
            </div>

            <div class="form_group time">
              <label>Giờ <span style="color: red">*</span> :</label>
              <input v-model="eventTime" type="time" />
            </div>
          </div>
          <div class="quantyti">
            <div class="form_group duration">
              <label
                >Thời Lượng (hours) <span style="color: red">*</span> :</label
              >
              <input
                v-model="eventDuration"
                min="1"
                max="10"
                type="number"
                title="Thời lượng từ 1 đến 10( giờ)"
              />
            </div>
            <div class="form_group maxPart">
              <label
                >Người Tham Gia Tối Đa
                <span style="color: red">*</span> :</label
              >
              <input
                v-model="maxParticipants"
                min="50"
                max="2000"
                type="number"
                title="Số lượng người tham gia từ 50 đến 2000"
              />
            </div>
          </div>

          <div class="location_inputs">
            <div class="form_group">
              <label>Thành Phố <span style="color: red">*</span> :</label>
              <select v-model="selectedCity" @change="onCityChange">
                <option disabled value="">Chọn Thành Phố</option>
                <option v-for="city in cities" :key="city.code" :value="city">
                  {{ city.name }}
                </option>
              </select>
            </div>
            <div class="form_group">
              <label>Quận/ Huyện <span style="color: red">*</span> :</label>
              <select v-model="selectedDistrict" @change="onDistrictChange">
                <option disabled value="">Chọn Quận/ Huyện</option>
                <option
                  v-for="district in districts"
                  :key="district.code"
                  :value="district"
                >
                  {{ district.name }}
                </option>
              </select>
            </div>
            <div class="form_group">
              <label>Phường/ Xã <span style="color: red">*</span> :</label>
              <select v-model="selectedWard">
                <option disabled value="">Chọn Phường/ Xã</option>
                <option v-for="ward in wards" :key="ward.code" :value="ward">
                  {{ ward.name }}
                </option>
              </select>
            </div>
            <div class="form_group">
              <label>Địa chỉ cụ thể <span style="color: red">*</span> :</label>
              <input
                v-model="specificAddress"
                type="text"
                placeholder="Nhập số nhà, Đường "
              />
            </div>
          </div>

          <div class="form_group">
            <label>Mô Tả:</label>
            <textarea v-model="description"></textarea>
          </div>
        </div>
        <div><button id="create_btn" type="submit">Thêm Sự Kiện</button></div>
      </form>
    </div>
  </div>
</template>


<script>
import { addEvent } from "@/api/createdEventsAPI";
import Cookies from "js-cookie";
import { notify, confirmNotify } from "@/script/Notification";

export default {
  data() {
    return {
      eventName: "",
      eventDate: "",
      eventTime: "",
      eventDuration: 1,
      // eventLocation: "",
      isPublic: false,
      description: "",
      eventImage: null,
      imgSrc: require("../assets/img/default_img_create.jpg"),
      fileName: "Không có tệp nào được chọn",
      //location
      cities: [],
      districts: [],
      wards: [],
      selectedCity: null,
      selectedDistrict: null,
      selectedWard: null,
      // eventLocation: "",
      specificAddress: "",
      gmail: "",
      maxParticipants: 50,
    };
  },
  created() {
    this.gmail = Cookies.get("email");
  },
  mounted() {
    this.fetchCities();
  },
  methods: {
    async fetchCities() {
      const response = await fetch(
        "https://provinces.open-api.vn/api/?depth=1"
      );
      this.cities = await response.json();
    },
    async onCityChange() {
      this.selectedDistrict = null;
      this.selectedWard = null;
      const response = await fetch(
        `https://provinces.open-api.vn/api/p/${this.selectedCity.code}?depth=2`
      );
      const data = await response.json();
      this.districts = data.districts;
    },
    async onDistrictChange() {
      this.selectedWard = null;
      const response = await fetch(
        `https://provinces.open-api.vn/api/d/${this.selectedDistrict.code}?depth=2`
      );
      const data = await response.json();
      this.wards = data.wards;
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.fileName = file.name;
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imgSrc = e.target.result; // Cập nhật đường dẫn ảnh để hiển thị
        };
        reader.readAsDataURL(file);
      } else {
        this.fileName = "Không có tệp nào được chọn";
        this.imgSrc = require("@/assets/img/default_img_create.jpg"); // Đảm bảo đường dẫn đúng đến thư mục assets
      }
    },

    async submitEvent() {
      if (!Cookies.get("fullname")) {
        notify("Vui lòng đăng nhập trước thêm sự kiện.", "warning");
        return;
      }
      if (
        !this.eventName ||
        !this.eventDate ||
        !this.eventTime ||
        !this.specificAddress ||
        !this.selectedCity ||
        !this.selectedDistrict ||
        !this.selectedWard
      ) {
        notify("Vui lòng điền đầy đủ thông tin bắt buộc!", "warning");
        return;
      }

      // Kiểm tra tên sự kiện không có số
      const nameRegex =
        /^[a-zA-Zàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệíìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ\s]+$/;
      if (!nameRegex.test(this.eventName)) {
        notify("Tên sự kiện không được chứa số!", "warning");
        return;
      }

      // Kiểm tra ngày bắt đầu không nhỏ hơn ngày hiện tại và cách ngày hiện tại ít nhất 1 ngày
      const currentDate = new Date();
      const selectedDate = new Date(this.eventDate);
      if (selectedDate < currentDate.setDate(currentDate.getDate() + 1)) {
        notify(
          "Ngày sự kiện không được nhỏ hơn ngày hiện tại và phải cách ngày hiện tại ít nhất 1 ngày!",
          "warning"
        );
        return;
      }

      // Kiểm tra thời gian sự kiện từ 1 đến 10 giờ
      if (this.eventDuration < 1 || this.eventDuration > 10) {
        notify("Thời lượng sự kiện phải từ 1 đến 10( giờ)!", "warning");
        return;
      }

      // Kiểm tra số lượng người tham gia tối đa từ 50 đến 2000
      if (this.maxParticipants < 50 || this.maxParticipants > 2000) {
        notify(
          "Số lượng người tham gia tối đa phải từ 50 đến 2000!",
          "warning"
        );
        return;
      }

      // Kiểm tra địa chỉ cụ thể không quá 50 ký tự
      if (this.specificAddress.length > 50) {
        notify("Địa chỉ cụ thể không được quá 50 ký tự!", "warning");
        return;
      }

      // Kiểm tra nếu ảnh đã được chọn
      if (this.fileName === "Không có tệp nào được chọn") {
        notify("Vui lòng chọn ảnh cho sự kiện!", "warning");
        return;
      }

      let eventType = "";
      eventType = this.isPublic ? "PL" : "PR";

      const eventDateTime = `${this.eventDate} ${this.eventTime}`;
      const startDateTime = new Date(eventDateTime);
      const endDateTime = new Date(startDateTime);
      endDateTime.setHours(
        endDateTime.getHours() + parseInt(this.eventDuration, 10)
      );
      const formatDateTime = (date) => {
        const yyyy = date.getFullYear();
        const mm = String(date.getMonth() + 1).padStart(2, "0"); // Month is 0-indexed
        const dd = String(date.getDate()).padStart(2, "0");
        const hh = String(date.getHours()).padStart(2, "0");
        const min = String(date.getMinutes()).padStart(2, "0");
        return `${yyyy}-${mm}-${dd} ${hh}:${min}:00`;
      };
      const formattedStartTime = formatDateTime(startDateTime);
      const formattedEndTime = formatDateTime(endDateTime);

      const Location = `${this.specificAddress},${this.selectedWard?.name},${this.selectedDistrict?.name},${this.selectedCity?.name}`;
      confirmNotify(
        "Bạn có chắc muốn tạo sự kiện?",
        async () => {
          try {
            const response = await addEvent(
              eventType,
              this.eventName,
              formattedStartTime,
              formattedEndTime,
              Location,
              this.fileName,
              this.description,
              this.maxParticipants,
              this.gmail
            );
            // alert(response.data.message);

            if (response.data.message === "event added successfully") {
              if (window.location.href.includes("Create_Event")) {
                this.$router.push({ name: "EventsCreated" });
              }
              localStorage.setItem(
                "updateNotification",
                "Tạo sự kiện thành công"
              );

              // window.location.reload();
            }
          } catch (error) {
            console.error("Error add event:", error);
            notify("Có lỗi xảy ra khi thêm sự kiện.", "error");
          }
        },
        () => {
          console.log("Đã hủy tạo");
        }
      );
    },
  },
};
</script>
<style scoped src="../css/createEvent.css">
</style>
