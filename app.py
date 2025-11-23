from flask import Flask, render_template_string

app = Flask(__name__)

# Dữ liệu thực đơn phong phú và hiện đại hơn
MENU = [
    {"id": 1, "category": "main", "name": "Burger Bò Phô Mai", "price": "65.000 đ", "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=500&q=60", "desc": "Thịt bò nướng lửa hồng, phô mai cheddar tan chảy."},
    {"id": 2, "category": "noodle", "name": "Mì Ý Carbonara", "price": "80.000 đ", "image": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=500&q=60", "desc": "Sốt kem béo ngậy, thịt xông khói giòn rụm."},
    {"id": 3, "category": "rice", "name": "Cơm Gà Teriyaki", "price": "55.000 đ", "image": "https://images.unsplash.com/photo-1564486054185-bc502a95c8ba?auto=format&fit=crop&w=500&q=60", "desc": "Gà sốt Nhật Bản đậm đà, ăn kèm salad."},
    {"id": 4, "category": "drink", "name": "Trà Sữa Trân Châu", "price": "35.000 đ", "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=500&q=60", "desc": "Đường đen, sữa tươi nguyên kem."},
    {"id": 5, "category": "main", "name": "Pizza Pepperoni", "price": "120.000 đ", "image": "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=500&q=60", "desc": "Đế mỏng giòn, xúc xích cay nồng."},
    {"id": 6, "category": "drink", "name": "Nước Ép Cam", "price": "30.000 đ", "image": "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=500&q=60", "desc": "Cam vàng nguyên chất, bổ sung Vitamin C."},
    {"id": 7, "category": "noodle", "name": "Phở Bò Đặc Biệt", "price": "60.000 đ", "image": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=500&q=60", "desc": "Hương vị truyền thống Việt Nam."},
    {"id": 8, "category": "rice", "name": "Cơm Sườn Bì Chả", "price": "50.000 đ", "image": "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?auto=format&fit=crop&w=500&q=60", "desc": "Sài Gòn đặc biệt, nước mắm kẹo."}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Foodie Express - Giao Đồ Ăn Nhanh</title>
    <!-- Bootstrap 5 & Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Poppins', sans-serif; background-color: #f8f9fa; }
        
        /* Navbar */
        .navbar { box-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 15px 0; }
        .navbar-brand { font-weight: 700; color: #ff4757 !important; font-size: 1.5rem; }
        .nav-link { font-weight: 600; color: #2f3542 !important; }
        .cart-badge { background-color: #ff4757; font-size: 0.8rem; }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 120px 0;
            border-radius: 0 0 30px 30px;
        }
        
        /* Product Card */
        .card {
            border: none;
            border-radius: 15px;
            transition: all 0.3s ease;
            background: white;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            overflow: hidden;
        }
        .card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .card-img-top { height: 200px; object-fit: cover; }
        .price-tag { color: #ff4757; font-weight: 700; font-size: 1.1rem; }
        .btn-add { 
            background-color: #ff4757; color: white; border-radius: 50px; 
            padding: 8px 20px; font-weight: 600; border: none; width: 100%;
        }
        .btn-add:hover { background-color: #ff6b81; color: white; }

        /* Filter Buttons */
        .nav-pills .nav-link { 
            color: #57606f; border-radius: 50px; padding: 8px 25px; margin: 0 5px; 
            background: white; border: 1px solid #dfe4ea;
        }
        .nav-pills .nav-link.active { background-color: #2ed573; color: white; border-color: #2ed573; }

        /* Toast Notification */
        .toast-container { position: fixed; bottom: 20px; right: 20px; z-index: 9999; }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="bi bi-rocket-takeoff-fill"></i> Foodie Express</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto align-items-center">
                    <li class="nav-item"><a class="nav-link" href="#">Trang chủ</a></li>
                    <li class="nav-item"><a class="nav-link" href="#menu">Thực đơn</a></li>
                    <li class="nav-item ms-3">
                        <button class="btn btn-outline-dark position-relative">
                            <i class="bi bi-cart3"></i> Giỏ hàng
                            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill cart-badge" id="cart-count">
                                0
                            </span>
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Banner -->
    <header class="hero text-center mb-5">
        <div class="container">
            <h1 class="display-3 fw-bold mb-3">Thèm là có - Ăn là ngon</h1>
            <p class="lead mb-4">Giao món ăn nóng hổi đến tận cửa nhà bạn trong 30 phút.</p>
            <a href="#menu" class="btn btn-light btn-lg rounded-pill fw-bold text-danger px-5">Đặt Ngay</a>
        </div>
    </header>

    <!-- Menu Section -->
    <div class="container mb-5" id="menu">
        <div class="text-center mb-5">
            <h2 class="fw-bold">Thực Đơn Hôm Nay</h2>
            <p class="text-muted">Được chế biến bởi các đầu bếp hàng đầu</p>
            
            <!-- Filter Tabs -->
            <ul class="nav nav-pills justify-content-center mt-4" id="pills-tab" role="tablist">
                <li class="nav-item"><button class="nav-link active" data-filter="all">Tất cả</button></li>
                <li class="nav-item"><button class="nav-link" data-filter="main">Món chính</button></li>
                <li class="nav-item"><button class="nav-link" data-filter="noodle">Mì & Phở</button></li>
                <li class="nav-item"><button class="nav-link" data-filter="rice">Cơm</button></li>
                <li class="nav-item"><button class="nav-link" data-filter="drink">Đồ uống</button></li>
            </ul>
        </div>

        <div class="row g-4" id="food-grid">
            {% for item in menu %}
            <div class="col-md-3 col-sm-6 filter-item" data-category="{{ item.category }}">
                <div class="card h-100">
                    <img src="{{ item.image }}" class="card-img-top" alt="{{ item.name }}">
                    <div class="card-body d-flex flex-column">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <h5 class="card-title fw-bold mb-0">{{ item.name }}</h5>
                        </div>
                        <p class="card-text text-muted small flex-grow-1">{{ item.desc }}</p>
                        <div class="mt-3">
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="price-tag">{{ item.price }}</span>
                                <span class="badge bg-light text-dark">⭐ 4.8</span>
                            </div>
                            <button class="btn btn-add" onclick="addToCart('{{ item.name }}')">
                                <i class="bi bi-plus-circle"></i> Thêm vào giỏ
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-white py-4 mt-auto border-top">
        <div class="container text-center">
            <p class="mb-0 text-muted">&copy; 2025 Foodie Express. Developed with Python & Azure.</p>
        </div>
    </footer>

    <!-- Toast Notification -->
    <div class="toast-container">
        <div id="liveToast" class="toast align-items-center text-white bg-success border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    <i class="bi bi-check-circle-fill me-2"></i> Đã thêm <strong id="toast-item-name"></strong> vào giỏ hàng!
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Logic Giỏ hàng giả lập
        let cartCount = 0;
        const toastEl = document.getElementById('liveToast');
        const toast = new bootstrap.Toast(toastEl);

        function addToCart(itemName) {
            // Tăng số lượng giỏ hàng
            cartCount++;
            document.getElementById('cart-count').innerText = cartCount;
            
            // Hiện thông báo
            document.getElementById('toast-item-name').innerText = itemName;
            toast.show();
        }

        // Logic Lọc món ăn (Frontend Filter)
        const filterButtons = document.querySelectorAll('.nav-link[data-filter]');
        const items = document.querySelectorAll('.filter-item');

        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Xử lý active class
                filterButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                const category = button.getAttribute('data-filter');

                items.forEach(item => {
                    if (category === 'all' || item.getAttribute('data-category') === category) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, menu=MENU)

if __name__ == '__main__':
    app.run(debug=True)