# Import module Flask
from flask import Flask # type: ignore

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa một route (đường dẫn) cho trang chủ
# Khi người dùng truy cập /, hàm home() sẽ được gọi
@app.route('/')
def home():
    # Hàm này trả về nội dung sẽ được hiển thị trên trình duyệt
    return "<h1>Xin chào, đây là trang web mẫu bằng Python!</h1><p>Sử dụng framework Flask.</p>"

# Chạy ứng dụng
# Điều kiện if __name__ == '__main__': đảm bảo rằng ứng dụng chỉ chạy khi bạn thực thi file này trực tiếp.
if __name__ == '__main__':
    # debug=True cho phép bạn thấy lỗi và tự động tải lại server khi có thay đổi trong code
    app.run(debug=True)