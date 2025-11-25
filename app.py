from flask import Flask, render_template_string

app = Flask(__name__)

# Dữ liệu thực đơn (Đã cập nhật ảnh Cơm Gà mới)
MENU = [
    {"id": 1, "category": "main", "name": "Burger Bò Phô Mai", "price": 65000, "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=500&q=60", "desc": "Thịt bò nướng lửa hồng, phô mai cheddar tan chảy."},
    {"id": 2, "category": "noodle", "name": "Mì Ý Carbonara", "price": 80000, "image": "https://images.unsplash.com/photo-1612874742237-6526221588e3?auto=format&fit=crop&w=500&q=60", "desc": "Sốt kem béo ngậy, thịt xông khói giòn rụm."},
    {"id": 3, "category": "rice", "name": "Cơm Gà Teriyaki", "price": 55000, "image": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=500&q=60", "desc": "Gà sốt Nhật Bản đậm đà, ăn kèm salad."}, 
    {"id": 4, "category": "drink", "name": "Trà Sữa Trân Châu", "price": 35000, "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=500&q=60", "desc": "Đường đen, sữa tươi nguyên kem."},
    {"id": 5, "category": "main", "name": "Pizza Pepperoni", "price": 120000, "image": "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=500&q=60", "desc": "Đế mỏng giòn, xúc xích cay nồng."},
    {"id": 6, "category": "drink", "name": "Nước Ép Cam", "price": 30000, "image": "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=500&q=60", "desc": "Cam vàng nguyên chất, bổ sung Vitamin C."},
    {"id": 7, "category": "noodle", "name": "Phở Bò Đặc Biệt", "price": 60000, "image": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=500&q=60", "desc": "Hương vị truyền thống Việt Nam."},
    {"id": 8, "category": "rice", "name": "Cơm Sườn Bì Chả", "price": 50000, "image": "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?auto=format&fit=crop&w=500&q=60", "desc": "Sài Gòn đặc biệt, nước mắm kẹo."}
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
        .navbar { box-shadow: 0 2px 10px rgba(0,0,0,0.1); padding: 15px 0; }
        .navbar-brand { font-weight: 700; color: #ff4757 !important; font-size: 1.5rem; }
        .cart-badge { background-color: #ff4757; font-size: 0.8rem; }
        .hero {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80');
            background-size: cover; background-position: center; color: white; padding: 100px 0; border-radius: 0 0 30px 30px;
        }
        .card { border: none; border-radius: 15px; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0,0,0,0.05); overflow: hidden; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .card-img-top { height: 200px; object-fit: cover; }
        .price-tag { color: #ff4757; font-weight: 700; font-size: 1.1rem; }
        .btn-add { background-color: #ff4757; color: white; border-radius: 50px; padding: 8px 20px; font-weight: 600; border: none; width: 100%; }
        .btn-add:hover { background-color: #ff6b81; color: white; }
        .nav-pills .nav-link.active { background-color: #2ed573; }
        .nav-pills .nav-link { color: #57606f; margin: 0 5px; border-radius: 50px; }
        
        /* Modal Styles */
        .cart-item-img { width: 50px; height: 50px; object-fit: cover; border-radius: 8px; }
        .total-price { font-size: 1.5rem; color: #ff4757; font-weight: bold; }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="bi bi-rocket-takeoff-fill"></i> Foodie Express</a>
            <button class="btn btn-outline-dark position-relative ms-auto" data-bs-toggle="modal" data-bs-target="#cartModal" onclick="renderCart()">
                <i class="bi bi-cart3"></i> Giỏ hàng
                <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill cart-badge" id="cart-count">0</span>
            </button>
        </div>
    </nav>

    <!-- Hero Banner -->
    <header class="hero text-center mb-5">
        <div class="container">
            <h1 class="display-4 fw-bold">Thèm là có - Ăn là ngon</h1>
        </div>
    </header>

    <!-- Menu Section -->
    <div class="container mb-5">
        <ul class="nav nav-pills justify-content-center mb-5" id="pills-tab">
            <li class="nav-item"><button class="nav-link active" data-filter="all">Tất cả</button></li>
            <li class="nav-item"><button class="nav-link" data-filter="main">Món chính</button></li>
            <li class="nav-item"><button class="nav-link" data-filter="noodle">Mì & Phở</button></li>
            <li class="nav-item"><button class="nav-link" data-filter="rice">Cơm</button></li>
            <li class="nav-item"><button class="nav-link" data-filter="drink">Đồ uống</button></li>
        </ul>

        <div class="row g-4">
            {% for item in menu %}
            <div class="col-md-3 col-sm-6 filter-item" data-category="{{ item.category }}">
                <div class="card h-100">
                    <img src="{{ item.image }}" class="card-img-top" alt="{{ item.name }}">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title fw-bold">{{ item.name }}</h5>
                        <p class="card-text text-muted small flex-grow-1">{{ item.desc }}</p>
                        <div class="mt-3">
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="price-tag">{{ "{:,.0f}".format(item.price).replace(',', '.') }} đ</span>
                            </div>
                            <!-- Truyền đầy đủ thông tin món ăn vào hàm addToCart -->
                            <button class="btn btn-add" onclick="addToCart({{ item.id }}, '{{ item.name }}', {{ item.price }}, '{{ item.image }}')">
                                <i class="bi bi-plus-circle"></i> Thêm món
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <!-- CART MODAL (Giao diện Giỏ hàng) -->
    <div class="modal fade" id="cartModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title fw-bold"><i class="bi bi-cart-check"></i> Giỏ hàng của bạn</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <div id="cart-empty-msg" class="text-center py-4 text-muted">
                        <i class="bi bi-cart-x" style="font-size: 3rem;"></i>
                        <p class="mt-2">Giỏ hàng đang trống trơn!</p>
                    </div>
                    <!-- Danh sách món ăn sẽ được render vào đây -->
                    <div id="cart-items-container" style="display: none;">
                        <table class="table align-middle">
                            <tbody id="cart-table-body"></tbody>
                        </table>
                        <div class="d-flex justify-content-end align-items-center mt-3 border-top pt-3">
                            <span class="me-3 fs-5">Tổng cộng:</span>
                            <span class="total-price" id="cart-total">0 đ</span>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Đóng</button>
                    <button type="button" class="btn btn-success px-4 fw-bold" onclick="checkout()" id="btn-checkout" disabled>
                        Thanh toán ngay <i class="bi bi-credit-card"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div class="toast-container position-fixed bottom-0 end-0 p-3">
        <div id="liveToast" class="toast align-items-center text-white bg-success border-0" role="alert">
            <div class="d-flex">
                <div class="toast-body">
                    <i class="bi bi-check-circle-fill me-2"></i> Đã thêm vào giỏ hàng!
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Mảng lưu trữ các món đã chọn
        let cart = [];
        const toastEl = document.getElementById('liveToast');
        const toast = new bootstrap.Toast(toastEl);

        // Hàm thêm vào giỏ hàng
        function addToCart(id, name, price, image) {
            // Kiểm tra xem món này đã có trong giỏ chưa
            const existingItem = cart.find(item => item.id === id);
            
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({ id: id, name: name, price: price, image: image, quantity: 1 });
            }

            // Cập nhật số lượng trên icon giỏ hàng
            updateCartCount();
            
            // Hiện thông báo
            toast.show();
        }

        function updateCartCount() {
            const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
            document.getElementById('cart-count').innerText = totalCount;
        }

        // Hàm hiển thị chi tiết giỏ hàng (khi mở Modal)
        function renderCart() {
            const container = document.getElementById('cart-items-container');
            const emptyMsg = document.getElementById('cart-empty-msg');
            const tbody = document.getElementById('cart-table-body');
            const btnCheckout = document.getElementById('btn-checkout');

            if (cart.length === 0) {
                container.style.display = 'none';
                emptyMsg.style.display = 'block';
                btnCheckout.disabled = true;
                return;
            }

            container.style.display = 'block';
            emptyMsg.style.display = 'none';
            btnCheckout.disabled = false;
            tbody.innerHTML = '';
            
            let total = 0;

            cart.forEach((item, index) => {
                const itemTotal = item.price * item.quantity;
                total += itemTotal;
                
                const row = `
                    <tr>
                        <td style="width: 60px;"><img src="${item.image}" class="cart-item-img"></td>
                        <td>
                            <div class="fw-bold">${item.name}</div>
                            <div class="text-muted small">${item.price.toLocaleString('vi-VN')} đ</div>
                        </td>
                        <td class="text-center" style="width: 120px;">
                            <div class="input-group input-group-sm">
                                <button class="btn btn-outline-secondary" onclick="changeQty(${index}, -1)">-</button>
                                <span class="form-control text-center bg-white">${item.quantity}</span>
                                <button class="btn btn-outline-secondary" onclick="changeQty(${index}, 1)">+</button>
                            </div>
                        </td>
                        <td class="text-end fw-bold" style="width: 100px;">
                            ${itemTotal.toLocaleString('vi-VN')} đ
                        </td>
                        <td style="width: 40px;" class="text-end">
                            <button class="btn btn-sm text-danger" onclick="removeItem(${index})"><i class="bi bi-trash"></i></button>
                        </td>
                    </tr>
                `;
                tbody.innerHTML += row;
            });

            document.getElementById('cart-total').innerText = total.toLocaleString('vi-VN') + ' đ';
        }

        // Hàm thay đổi số lượng trong giỏ
        function changeQty(index, delta) {
            cart[index].quantity += delta;
            if (cart[index].quantity <= 0) {
                cart.splice(index, 1);
            }
            updateCartCount();
            renderCart(); // Vẽ lại bảng
        }

        // Hàm xóa hẳn món khỏi giỏ
        function removeItem(index) {
            cart.splice(index, 1);
            updateCartCount();
            renderCart();
        }

        // Hàm thanh toán (Giả lập)
        function checkout() {
            const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
            const totalStr = total.toLocaleString('vi-VN') + ' đ';
            
            // Tắt Modal
            const modalEl = document.getElementById('cartModal');
            const modal = bootstrap.Modal.getInstance(modalEl);
            modal.hide();

            // Hiện thông báo thanh toán thành công
            alert(`🎉 Cảm ơn Bệ hạ!\n\nĐơn hàng trị giá ${totalStr} đang được Ngự Thiện Phòng chuẩn bị.\nNgựa chiến sẽ giao tới ngay lập tức!`);
            
            // Xóa giỏ hàng sau khi mua
            cart = [];
            updateCartCount();
        }

        // Logic Lọc món ăn
        const filterButtons = document.querySelectorAll('.nav-link[data-filter]');
        const items = document.querySelectorAll('.filter-item');
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
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