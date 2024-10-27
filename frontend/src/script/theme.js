// theme.js
let isLightMode = true; // Mặc định là chế độ sáng

export function setLightMode(value) {
  isLightMode = value; // Gán giá trị mới cho isLightMode
}

export function getLightMode() {
  return isLightMode; // Trả về giá trị hiện tại của isLightMode
}
