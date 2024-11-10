import "vue3-toastify/dist/index.css";
import { toast } from 'vue3-toastify';
import "../css/createEvent.css"
export const notify = (message, type) => {
    toast(message, {
        autoClose: 2000,
        type: type,
    });
};
export const confirmNotify = (message, onConfirm, onCancel) => {
    const toastId = toast(
        <div>
            <p>{message}</p>
            <div style={{ textAlign: "center", marginTop: "10px" }}>
                <button id="toast_btn"
                    onClick={() => {
                        onConfirm();  // Xử lý xác nhận
                        toast.remove(toastId);  // Đóng thông báo khi xác nhận
                    }}
                    style={{ margin: "0 10px", padding: "7px 20px", background: "linear-gradient(90deg, rgba(32, 59, 232, 1) 0%, rgba(32, 59, 232, 0.4) 100%)", color: "white", border: "none", cursor: "pointer",borderRadius: "10px"}}
                >
                    Xác nhận
                </button>
                <button id="toast_btn"
                    onClick={() => {
                        onCancel();  // Xử lý hủy
                        toast.remove(toastId);  // Đóng thông báo khi hủy
                    }}
                    style={{ margin: "0 10px", padding: "7px 20px", background: "linear-gradient(90deg, rgba(32, 59, 232, 1) 0%, rgba(32, 59, 232, 0.4) 100%)", color: "white", border: "none", cursor: "pointer",borderRadius: "10px" }}
                >
                    Hủy
                </button>
            </div>
        </div>,
        {
            autoClose: false,  // Không tự động đóng
            closeButton: false,  // Tắt nút đóng mặc định
        }
    );
};
