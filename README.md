# BÀI TẬP LẬP TRÌNH WEB

## 1. Thông tin

Môn học: Lập trình Web

Đề tài: Xây dựng hệ thống Website sử dụng Docker Compose, Nginx và Node-RED API.

---

# 2. Bài tập 1

## 2.1. Giả lập Linux OS

Sử dụng:

- WSL
- Ubuntu Linux

## 2.2. Docker Compose

Các dịch vụ được triển khai:

- Nginx
- Node-RED
- MariaDB
- phpMyAdmin
- Cloudflared

## 2.3. Nginx

Nginx được cấu hình để chạy 2 website:

Website 1:

http://site1.test:8082

Website 2:

http://site2.test:8082

Mỗi website sử dụng một thư mục HTML riêng.

---

# 3. Bài tập 2

## 3.1. Tạo API bằng Node-RED

Sử dụng Node-RED để xây dựng API đơn giản theo yêu cầu của bài tập.

Mỗi API được xây dựng bằng 3 node:

HTTP In

→ Function

→ HTTP Response

### API cho Website 1

Phương thức:

GET

Đường dẫn:

/api/site1/students

API trả về dữ liệu JSON:

{
    "ok": 1,
    "website": "Website 1",
    "dssv": [
        {
            "name": "Nguyễn Văn Duy",
            "money": 123
        },
        {
            "name": "Trần Văn An",
            "money": 456
        },
        {
            "name": "Lê Văn Bình",
            "money": 789
        },
        {
            "name": "Phạm Thị Hoa",
            "money": 321
        },
        {
            "name": "Đỗ Văn Nam",
            "money": 654
        }
    ]
}

### API cho Website 2

Phương thức:

GET

Đường dẫn:

/api/site2/students

API trả về dữ liệu JSON:

{
    "ok": 1,
    "website": "Website 2",
    "dssv": [
        {
            "name": "Nguyễn Thị Mai",
            "money": 900
        },
        {
            "name": "Vũ Văn Hùng",
            "money": 800
        },
        {
            "name": "Bùi Thị Lan",
            "money": 700
        },
        {
            "name": "Hoàng Văn Minh",
            "money": 600
        },
        {
            "name": "Đặng Thị Hương",
            "money": 500
        },
        {
            "name": "Phan Văn Long",
            "money": 400
        }
    ]
}

## 3.2. Cấu hình Nginx kết nối Node-RED

Nginx được cấu hình reverse proxy để chuyển các request API đến Node-RED.

Website gửi request:

/api/...

Nginx chuyển request đến:

Node-RED:1880

## 3.3. JavaScript gọi API

Sử dụng JavaScript với hàm fetch() để gọi API.

Website 1:

fetch("/api/site1/students")

Website 2:

fetch("/api/site2/students")

Sau khi nhận dữ liệu JSON, JavaScript xử lý và hiển thị dữ liệu lên giao diện website.

Luồng hoạt động:

Website

→ JavaScript

→ Nginx

→ Node-RED

→ JSON

→ Website

---

# 4. MariaDB

Sử dụng MariaDB làm hệ quản trị cơ sở dữ liệu.

MariaDB được triển khai bằng Docker Compose.

Cổng sử dụng:

3300

---

# 5. phpMyAdmin

Sử dụng phpMyAdmin để quản lý cơ sở dữ liệu MariaDB.

Địa chỉ:

http://localhost:8081

phpMyAdmin được chạy bằng Docker Compose.

---

# 6. Cloudflared và Domain

Đã đăng ký domain:

duy59kmt.id.vn

Đã cấu hình nameserver Cloudflare:

chelsea.ns.cloudflare.com

michael.ns.cloudflare.com

Đã thêm dịch vụ Cloudflared vào Docker Compose để chuẩn bị kết nối hệ thống với Cloudflare Tunnel.

---

# 7. GitHub

Source code của bài tập được quản lý bằng Git và đưa lên GitHub.

Repository:

duy-7855/duyPTweb

Các thông tin bảo mật như mật khẩu và Tunnel Token được lưu trong file .env và không đưa lên GitHub.

---

# 8. Cấu trúc project

Mon_PTweb

├── docker-compose.yml

├── nginx

│   ├── nginx.conf

│   └── html

│       ├── site1

│       │   └── index.html

│       └── site2

│           └── index.html

├── nodered

│   └── flows.json

├── README.md

└── .gitignore

---

# 9. Kết quả

Đã hoàn thành việc tạo môi trường Linux bằng WSL, cài đặt Docker Compose, triển khai các dịch vụ Nginx, Node-RED, MariaDB, phpMyAdmin và Cloudflared.

Đã cấu hình Nginx chạy 2 website, tạo API riêng cho Website 1 và Website 2 bằng Node-RED.

JavaScript trên cả hai website có thể gọi API và hiển thị dữ liệu JSON.
