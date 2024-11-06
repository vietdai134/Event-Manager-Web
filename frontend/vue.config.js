const { defineConfig } = require('@vue/cli-service');

module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'https://apps.emaillistverify.com',
        changeOrigin: true, // Đảm bảo rằng các yêu cầu từ localhost được gửi tới đúng server
        pathRewrite: {
          '^/api': '', // Xóa '/api' khỏi đường dẫn khi gửi yêu cầu
        },
        secure: false, // Nếu API không sử dụng HTTPS, bạn có thể thiết lập secure: false
      },
    },
  },
};

