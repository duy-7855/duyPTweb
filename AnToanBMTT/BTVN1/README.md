# BÀI TẬP AN TOÀN VÀ BẢO MẬT THÔNG TIN

## 1. Giới thiệu

Thư mục `AnToanBMTT` chứa các bài thực hành môn **An toàn và Bảo mật Thông tin**, được thực hiện bằng ngôn ngữ lập trình Python.

Nội dung bài tập gồm:

- Bài 1: DES và AES
- Bài 2: RSA
- Bài 3: Ứng dụng RSA và so sánh RSA với AES

Các chương trình được xây dựng nhằm minh họa quá trình mã hóa, giải mã, xác thực chữ ký và so sánh đặc điểm của các thuật toán mật mã.

---

## 2. Cấu trúc thư mục

    AnToanBMTT/
    ├── Bai1_DES_AES/
    │   ├── aes_demo.py
    │   ├── des_demo.py
    │   └── so_sanh.py
    │
    ├── Bai2_RSA/
    │   ├── rsa_demo.py
    │   ├── public_key.pem
    │   └── .gitignore
    │
    ├── Bai3_UngDung_RSA/
    │   ├── ung_dung_rsa.py
    │   └── so_sanh_rsa_aes.py
    │
    └── README.md

---

# 3. Bài 1 - DES và AES

## 3.1. DES

DES (Data Encryption Standard) là thuật toán mã hóa đối xứng.

Đặc điểm:

- Sử dụng cùng một khóa cho mã hóa và giải mã.
- Kích thước khối dữ liệu: 64 bit.
- Khóa có độ dài 64 bit, trong đó 56 bit được sử dụng thực tế.
- Thuật toán thực hiện 16 vòng xử lý.
- DES hiện nay không còn được khuyến nghị cho các hệ thống bảo mật mới do kích thước khóa nhỏ.

File thực hiện:

    Bai1_DES_AES/des_demo.py

Chương trình thực hiện:

1. Sinh khóa DES.
2. Mã hóa dữ liệu.
3. Hiển thị dữ liệu mã hóa dạng Base64.
4. Giải mã dữ liệu.
5. Kiểm tra dữ liệu sau giải mã có giống dữ liệu ban đầu hay không.

---

## 3.2. AES

AES (Advanced Encryption Standard) là thuật toán mã hóa đối xứng hiện đại.

Đặc điểm:

- Sử dụng cùng một khóa để mã hóa và giải mã.
- Kích thước khối dữ liệu: 128 bit.
- Hỗ trợ khóa 128, 192 và 256 bit.
- Trong bài thực hành sử dụng AES-256.
- AES có tốc độ xử lý nhanh và được sử dụng rộng rãi trong thực tế.

Các bước chính của AES gồm:

- SubBytes
- ShiftRows
- MixColumns
- AddRoundKey

Số vòng xử lý:

| Khóa | Số vòng |
|---|---:|
| AES-128 | 10 |
| AES-192 | 12 |
| AES-256 | 14 |

File thực hiện:

    Bai1_DES_AES/aes_demo.py

Chương trình thực hiện:

1. Sinh khóa AES-256.
2. Mã hóa thông điệp.
3. Hiển thị dữ liệu mã hóa.
4. Giải mã.
5. Kiểm tra kết quả.

---

## 3.3. So sánh DES và AES

File:

    Bai1_DES_AES/so_sanh.py

Chương trình thực hiện mã hóa và giải mã bằng DES và AES để quan sát sự khác biệt về thời gian xử lý.

Kết quả thực nghiệm phụ thuộc vào máy tính và môi trường chạy chương trình.

AES có kích thước khóa lớn hơn và phù hợp hơn với các hệ thống bảo mật hiện đại so với DES.

---

# 4. Bài 2 - RSA

## 4.1. Giới thiệu RSA

RSA là thuật toán mật mã khóa công khai (mật mã bất đối xứng).

RSA sử dụng hai khóa:

- Public Key: khóa công khai.
- Private Key: khóa bí mật.

Dữ liệu được mã hóa bằng khóa công khai có thể được giải mã bằng khóa bí mật tương ứng.

---

## 4.2. Tạo khóa RSA

Trong chương trình sử dụng:

    RSA 2048 bit

Quá trình tạo khóa gồm:

1. Sinh hai số nguyên tố lớn `p` và `q`.
2. Tính:

    n = p × q

3. Tính:

    φ(n) = (p - 1)(q - 1)

4. Chọn số mũ công khai `e`.
5. Tính số mũ bí mật `d` sao cho:

    e × d ≡ 1 (mod φ(n))

Khóa công khai:

    (n, e)

Khóa bí mật:

    (n, d)

---

## 4.3. Mã hóa và giải mã RSA

File:

    Bai2_RSA/rsa_demo.py

Chương trình:

1. Sinh cặp khóa RSA 2048 bit.
2. Lưu Public Key vào `public_key.pem`.
3. Lưu Private Key vào `private_key.pem`.
4. Sử dụng Public Key để mã hóa.
5. Sử dụng Private Key để giải mã.
6. Kiểm tra dữ liệu sau giải mã.

Kết quả:

    KẾT QUẢ: Mã hóa và giải mã RSA thành công!

### Lưu ý bảo mật

File:

    private_key.pem

không được đưa lên GitHub.

File `.gitignore` được sử dụng để tránh đưa khóa bí mật lên repository.

---

# 5. Bài 3 - Ứng dụng RSA

## 5.1. Xác thực người gửi

File:

    Bai3_UngDung_RSA/ung_dung_rsa.py

Chương trình mô phỏng quá trình gửi thông điệp và xác thực chữ ký số.

Quy trình:

    Người gửi
        |
        | Tạo thông điệp
        v
    Tính SHA-256
        |
        | Ký bằng Private Key
        v
    Chữ ký số
        |
        v
    Người nhận
        |
        | Kiểm tra bằng Public Key
        v
    Xác thực

Chương trình sử dụng:

- RSA 2048 bit
- SHA-256
- Chữ ký RSA PKCS#1 v1.5

Kết quả thử nghiệm:

    Xác thực chữ ký: THÀNH CÔNG

Khi thông điệp bị thay đổi:

    Xác thực: THẤT BẠI
    Phát hiện thông điệp đã bị thay đổi.

Điều này minh họa khả năng của chữ ký số trong:

- Xác thực người gửi.
- Kiểm tra tính toàn vẹn của thông điệp.

---

# 6. So sánh RSA và AES

File:

    Bai3_UngDung_RSA/so_sanh_rsa_aes.py

Chương trình thực hiện 100 lần mã hóa và giải mã để đo thời gian xử lý.

## Kết quả thực nghiệm

Dữ liệu sử dụng có kích thước:

    55 byte

| Thuật toán | Mã hóa 100 lần | Giải mã 100 lần | Kết quả |
|---|---:|---:|---|
| RSA 2048 | 0.107071 giây | 0.216048 giây | Đúng |
| AES-256 | 0.040375 giây | 0.025905 giây | Đúng |

Kết quả trên là kết quả của lần chạy thực nghiệm trong môi trường thực hành. Thời gian thực tế có thể thay đổi tùy thuộc vào máy tính và tải hệ thống.

---

# 7. So sánh đặc điểm RSA và AES

| Tiêu chí | AES | RSA |
|---|---|---|
| Loại mã hóa | Đối xứng | Bất đối xứng |
| Số khóa | Một khóa | Hai khóa |
| Tốc độ | Nhanh | Chậm hơn |
| Mã hóa dữ liệu lớn | Phù hợp | Không phù hợp |
| Trao đổi khóa | Không phải mục đích chính | Phù hợp |
| Chữ ký số | Không phải cơ chế chính | Phù hợp |
| Ứng dụng | Mã hóa dữ liệu | Trao đổi khóa, chữ ký số |

Trong thực tế, AES và RSA thường được sử dụng kết hợp.

Ví dụ:

    RSA
     |
     | Trao đổi khóa AES
     v
    AES
     |
     | Mã hóa dữ liệu
     v
    Dữ liệu được bảo vệ

RSA có thể được sử dụng để bảo vệ hoặc trao đổi khóa phiên, trong khi AES sử dụng khóa phiên đó để mã hóa lượng dữ liệu lớn.

---

# 8. Công nghệ sử dụng

- Python 3.14
- PyCryptodome
- RSA 2048 bit
- AES-256
- DES
- SHA-256
- Git
- GitHub
- Ubuntu trên WSL

Cài đặt thư viện:

    python3 -m pip install pycryptodome --break-system-packages

---

# 9. Cách chạy chương trình

## Bài 1

    cd ~/duyPTweb/AnToanBMTT/Bai1_DES_AES

Chạy AES:

    python3 aes_demo.py

Chạy DES:

    python3 des_demo.py

So sánh:

    python3 so_sanh.py

---

## Bài 2

    cd ~/duyPTweb/AnToanBMTT/Bai2_RSA

Chạy:

    python3 rsa_demo.py

---

## Bài 3

    cd ~/duyPTweb/AnToanBMTT/Bai3_UngDung_RSA

Chạy ứng dụng RSA:

    python3 ung_dung_rsa.py

So sánh RSA và AES:

    python3 so_sanh_rsa_aes.py

---

# 10. Kết luận

Qua các bài thực hành, đã tìm hiểu và triển khai các thuật toán mật mã đối xứng và bất đối xứng.

DES và AES sử dụng cơ chế mã hóa đối xứng, trong đó AES có kích thước khóa lớn hơn và phù hợp hơn với các hệ thống bảo mật hiện đại.

RSA sử dụng cặp khóa công khai và bí mật, phù hợp với các bài toán như trao đổi khóa và chữ ký số.

Thông qua bài thực hành RSA, có thể xác thực người gửi và kiểm tra tính toàn vẹn của thông điệp. Qua thực nghiệm, AES có thời gian xử lý thấp hơn RSA đối với dữ liệu thử nghiệm, phù hợp với vai trò mã hóa dữ liệu lớn.

Các chương trình trong bài tập giúp minh họa những nguyên lý cơ bản của mã hóa, giải mã, chữ ký số và ứng dụng mật mã trong bảo mật thông tin.
