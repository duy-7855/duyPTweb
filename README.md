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

```json
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