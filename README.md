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

http://site1.test

Website 2:

http://site2.test

Mỗi website sử dụng một thư mục HTML riêng.

---

# 3. Bài tập 2

## 3.1. Tạo API bằng Node-RED

Sử dụng các node:

HTTP In
→ Function
→ HTTP Response

API:

GET /api/tacke

Kết quả:

```json
{
    "ok": 1,
    "msg": "thành công",
    "dssv": [
        {
            "name": "Duy",
            "money": 123
        },
        {
            "name": "David",
            "money": 456
        }
    ]
}