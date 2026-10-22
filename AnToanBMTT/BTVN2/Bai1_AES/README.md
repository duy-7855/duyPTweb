# Bài 1 – Mã hóa AES-256

## 1. Giới thiệu

Bài tập xây dựng ứng dụng console bằng Python để thực hiện mã hóa đối xứng bằng thuật toán AES-256. Quá trình mã hóa và giải mã sử dụng cùng một khóa bí mật. Chương trình sử dụng AES-GCM để hỗ trợ xác thực dữ liệu, giúp phát hiện dữ liệu bị thay đổi hoặc khóa không đúng trong quá trình giải mã.

## 2. Chức năng chính

Chương trình thực hiện các chức năng sau:

1. Sinh khóa AES-256 mới.
2. Lưu khóa vào file.
3. Import khóa AES-256 từ file.
4. Mã hóa và giải mã văn bản.
5. Mã hóa và giải mã file.
6. Thử nghiệm với file dung lượng lớn theo từng khối dữ liệu.
7. Đo thời gian mã hóa, thời gian giải mã và tốc độ xử lý.
8. So sánh file gốc với file sau giải mã bằng dung lượng, so sánh byte trực tiếp và mã băm SHA-256.

## 3. Công nghệ sử dụng

- **Ngôn ngữ:** Python
- **Thuật toán:** AES-256
- **Chế độ mã hóa:** AES-GCM
- **Thư viện:** `cryptography`
- **Kiểm tra dữ liệu:** SHA-256 và so sánh byte trực tiếp

## 4. Cài đặt và chạy chương trình

### Yêu cầu

Cài đặt Python và thư viện `cryptography`.

Mở Terminal tại thư mục chứa chương trình, sau đó chạy:

```bash
python -m pip install cryptography
```

Khởi chạy chương trình bằng lệnh:

```bash
python main.py
```

Tên file có thể thay đổi tùy theo file chương trình đang sử dụng.

## 5. Thử nghiệm file dung lượng lớn

Chương trình đã được thử nghiệm với file có dung lượng **1.073.741.824 byte (1 GiB)**.

### Kết quả đo được

| Chỉ tiêu | Kết quả |
|---|---:|
| Dung lượng file gốc | 1.073.741.824 byte |
| Dung lượng file mã hóa | 1.073.741.852 byte |
| Dung lượng tăng thêm | 28 byte |
| Thời gian mã hóa | 2,110132 giây |
| Thời gian giải mã | 2,647292 giây |
| Tốc độ mã hóa | 485,28 MiB/s |
| Tốc độ giải mã | 386,81 MiB/s |

Dung lượng tăng thêm 28 byte gồm:

- **12 byte nonce:** giá trị được lưu kèm để phục vụ quá trình mã hóa/giải mã.
- **16 byte authentication tag:** thẻ xác thực của AES-GCM.

### Kiểm tra tính chính xác

| Phép kiểm tra | Kết quả |
|---|---|
| Dung lượng file gốc và file khôi phục bằng nhau | `True` |
| So sánh byte trực tiếp | `True` |
| Mã băm SHA-256 trùng khớp | `True` |
| Dữ liệu sau giải mã trùng khớp dữ liệu ban đầu | `True` |

SHA-256 của file gốc và file khôi phục:

```text
49bc20df15e412a64472421e13fe86ff1c5165e18b2afccf160d4dc19fe68a14
```

Các kết quả trên cho thấy file sau giải mã giống hệt file gốc trong lần thử nghiệm này.

> **Lưu ý:** File thử nghiệm có thể được tạo bằng cách đặt độ dài file trong PowerShell và chứa toàn byte 0. Kết quả này kiểm tra khả năng xử lý file lớn và tính chính xác của quá trình khôi phục, nhưng chưa đại diện cho mọi loại dữ liệu thực tế. Tốc độ đo được còn phụ thuộc vào cấu hình máy tính, thiết bị lưu trữ và loại dữ liệu.

## 6. Kết luận

Qua bài tập, em đã xây dựng và kiểm tra chương trình mã hóa, giải mã dữ liệu bằng AES-256 kết hợp AES-GCM. Chương trình hỗ trợ sinh, lưu và import khóa; xử lý văn bản và file; đồng thời đo thời gian xử lý file dung lượng lớn.

Trong thử nghiệm file 1 GiB, thời gian mã hóa là khoảng 2,11 giây và thời gian giải mã là khoảng 2,65 giây. Dung lượng file mã hóa tăng thêm 28 byte theo định dạng dữ liệu mà chương trình sử dụng. Các phép kiểm tra bằng dung lượng, so sánh byte trực tiếp và SHA-256 đều xác nhận dữ liệu khôi phục trùng khớp với dữ liệu ban đầu.

Bài tập giúp em hiểu rõ hơn về mã hóa đối xứng, cách quản lý khóa bí mật, xác thực dữ liệu và đánh giá hiệu năng thông qua số liệu thực tế. Khóa AES cần được bảo quản an toàn; người dùng không nên chia sẻ khóa hoặc đưa khóa bí mật lên kho mã nguồn công khai.

**Kết luận chung:** Chương trình đã đáp ứng các chức năng chính của đề bài và cho kết quả thử nghiệm khả quan với file 1 GiB. Nếu cần đánh giá toàn diện hơn, có thể thử nghiệm bổ sung với nhiều kích thước file và các loại dữ liệu khác nhau.

## 7. Lưu ý bảo mật

- Không chia sẻ khóa AES cho người không được phép.
- Không tải file khóa bí mật lên GitHub hoặc kho mã nguồn công khai.
- Nên thêm thư mục chứa khóa và file thử nghiệm vào `.gitignore` nếu chúng không cần nộp.
- Không sinh khóa mới khi cần giải mã dữ liệu đã mã hóa bằng khóa cũ, trừ khi đã lưu giữ khóa cũ an toàn.
