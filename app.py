from flask import Flask

app = Flask(__name__)

# Dữ liệu thực đơn (Giả lập cơ sở dữ liệu)
MENU = [
    {
        "id": 1,
        "name": "Phở Bò Gia Truyền",
        "price": "50.000 VNĐ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pho_Bo_-_Beef_Noodle_Soup.jpg/640px-Pho_Bo_-_Beef_Noodle_Soup.jpg",
        "desc": "Nước dùng đậm đà, thịt bò mềm tan."
    },
    {
        "id": 2,
        "name": "Bánh Mì Thập Cẩm",
        "price": "25.000 VNĐ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/B%C3%A1nh_m%C3%AC_th%E1%BA%ADp_c%E1%BA%A9m.jpg/640px-B%C3%A1nh_m%C3%AC_th%E1%BA%ADp_c%E1%BA%A9m.jpg",
        "desc": "Vỏ giòn, pate béo ngậy, full topping."
    },
    {
        "id": 3,
        "name": "Bún Chả Hà Nội",
        "price": "45.000 VNĐ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Bun_Cha.jpg/640px-Bun_Cha.jpg",
        "desc": "Chả nướng than hoa thơm lừng."
    },
    {
        "id": 4,
        "name": "Cơm Tấm Sài Gòn",
        "price": "40.000 VNĐ",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/C%C6%A1m_T%E1%BA%A5m_Ba_Ghi%E1%BB%8Bn.jpg/640px-C%C6%A1m_T%E1%BA%A5m_Ba_Ghi%E1%BB%8Bn.jpg",
        "desc": "Sườn bì chả, mỡ hành chan nước mắm."
    }
]

# Giao diện HTML (Nhúng trực tiếp vào Python để đơn giản hóa việc deploy)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ngự Thiện Phòng Online</title>
    <!-- Nhúng Bootstrap CSS để giao diện đẹp ngay lập tức -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .hero-banner {
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
            background-size: cover;
            color: white;
            padding: 100px 0;
            text-align: center;
            margin-bottom: 30px;
        }
        .card { transition: transform 0.3s; border: none; shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .card:hover { transform: scale(1.03); }
        .card-img-top { height: 200px; object-fit: cover; }
        .btn-order { background-color: #ff6b6b; color: white; border: none; }
        .btn-order:hover { background-color: #ee5253; color: white; }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">👑 Ngự Thiện Phòng</a>
        </div>
    </nav>

    <!-- Banner -->
    <div class="hero-banner">
        <h1 class="display-4">Món Ngon Dâng Vua</h1>
        <p class="lead">Đặt món trực tuyến - Giao hàng hỏa tốc bằng Ngựa Chiến</p>
    </div>

    <!-- Menu -->
    <div class="container mb-5">
        <h2 class="text-center mb-4">Thực Đơn Hôm Nay</h2>
        <div class="row">
            {% for item in menu %}
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm">
                    <img src="{{ item.image }}" class="card-img-top" alt="{{ item.name }}">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ item.name }}</h5>
                        <p class="card-text text-muted">{{ item.desc }}</p>
                        <div class="mt-auto d-flex justify-content-between align-items-center">
                            <span class="fw-bold text-danger">{{ item.price }}</span>
                            <button class="btn btn-order btn-sm" onclick="alert('Bệ hạ đã chọn món: {{ item.name }}. Thần đang chuẩn bị!')">Đặt Ngay</button>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>&copy; 2025 Ngự Thiện Phòng - Azure App Service Demo</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

from flask import render_template_string

@app.route('/')
def home():
    # Render HTML từ chuỗi string và truyền dữ liệu MENU vào
    return render_template_string(HTML_TEMPLATE, menu=MENU)

if __name__ == '__main__':
    app.run(debug=True)