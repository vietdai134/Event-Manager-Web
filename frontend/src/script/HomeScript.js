import Cookies from 'js-cookie'; 
import { getEventIDRegisteredByGmail } from "@/api/registeredEventsAPI";
import { getEventById } from '@/api/publicEventsAPI';
import { sendEmail } from '@/api/sendNoti';
export default {
  props: ['user'],
  data() {
    return {
        list_eventID:[],
        list_event:[],
        gmail:"",
        currentTime: new Date(),
        message:""
    };
  },
  created() {
    this.gmail=Cookies.get('email');
    if (this.gmail){
      getEventIDRegisteredByGmail(this.gmail)
      .then(response => {
        this.list_eventID = response.data; // Assign data to Past_events
        // console.log(this.list_eventID)
        for(let i=0;i<this.list_eventID.length;i++){
            // console.log(this.list_eventID[i].EventID)
            getEventById(this.list_eventID[i].EventID)
            .then(response => {
                
                this.list_event = response.data; 
                // console.log(this.list_event)
                this.message=`${this.list_event[0].EventName} sắp diễn ra xin vui lòng đến tham dự`
                
                const currentTime = new Date(this.currentTime); 
                const eventStartTime = new Date(this.list_event[0].StartTime);

                const timeDifference = eventStartTime - currentTime; 
                const timeDifferenceInHours = timeDifference / (60 * 60 * 1000); // Đổi sang giờ
                // Kiểm tra nếu chênh lệch lớn hơn 0 và nhỏ hơn hoặc bằng 1 giờ
                if (timeDifferenceInHours > 0 && timeDifferenceInHours <= 1) {
                  // console.log("OK"); 
                  sendEmail("vietnguyentran134@gmail.com","Thông báo sự kiện", this.message)
                }
                
               
              })
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });

      

    }
    
  },
};