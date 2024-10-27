<template>
  <div class="container_create">
    <div id="form_create">
      <h1>Create Event</h1>
      <form @submit.prevent="submitEvent">
        <div class="load_img">
          <img :src="imgSrc" alt="Uploaded Image" />
          <div class="input_top">
            <div class="form_group">
              <label>Event Name: </label>
              <input v-model="eventName" type="text" required />
            </div>
            <div class="form_group_checkbox">
              <label>Public Event:</label>
              <input v-model="isPublic" type="checkbox" />
            </div>
            <label style="font-weight: bold">Upload Image:</label>
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
              <label>Event Date:</label>
              
              <input v-model="eventDate" type="date" required />
            </div>

            <div class="form_group time">
              <label>Time:</label>
              <input v-model="eventTime" type="time" required />
            </div>
          </div>
          <div class="quantyti">
            <div class="form_group duration">
              <label>Duration (hours):</label>
              <input
                v-model="eventDuration"
                min="1"
                max="6"
                type="number"
                required
              />
            </div>
            <div class="form_group maxPart">
              <label>Max Participants:</label>
              <input
                v-model="maxParticipants"
                min="31"
                max="4000"
                type="number"
                required
              />
            </div>
          </div>

          <div class="location_inputs">
            <div class="form_group">
              <label>City:</label>
              <select v-model="selectedCity" @change="onCityChange" required>
                <option disabled value="">Select City</option>
                <option v-for="city in cities" :key="city.code" :value="city">
                  {{ city.name }}
                </option>
              </select>
            </div>
            <div class="form_group">
              <label>District:</label>
              <select
                v-model="selectedDistrict"
                @change="onDistrictChange"
                required
              >
                <option disabled value="">Select District</option>
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
              <label>Ward:</label>
              <select v-model="selectedWard" required>
                <option disabled value="">Select Ward</option>
                <option v-for="ward in wards" :key="ward.code" :value="ward">
                  {{ ward.name }}
                </option>
              </select>
            </div>
            <div class="form_group">
              <label>Specific Address:</label>
              <input
                v-model="specificAddress"
                type="text"
                placeholder="Nhập số nhà, Đường "
                required
              />
            </div>
          </div>

          <div class="form_group">
            <label>Description:</label>
            <textarea v-model="description" required></textarea>
          </div>
        </div>

        <button id="create_btn" type="submit">Create Event</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      eventName: "",
      eventDate: "",
      eventTime: "",
      eventDuration: 1,
      // eventLocation: "",
      isPublic: false,
      maxParticipants: 0,
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
      eventLocation: "",
      specificAddress: "",
    };
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

        // Tạo một URL tạm thời để hiển thị ảnh đã chọn
        const reader = new FileReader();
        // console.log("reader: ", reader);
        reader.onload = (e) => {
          this.imgSrc = e.target.result; // Cập nhật đường dẫn ảnh
        };
        reader.readAsDataURL(file);
      } else {
        this.fileName = "Không có tệp nào được chọn";
        this.imgSrc = require("../assets/img/default_img_create.jpg"); // Đặt lại ảnh mặc định nếu không có file nào
      }
    },
  },
};
</script>
<style scoped src="../css/createEvent.css">
</style>
