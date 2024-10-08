<template>
    <footer class="footer">
      <p>Footer Content Here</p>
    </footer>
</template>

<script>
export default {
    name: "appFooter"
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
