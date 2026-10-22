# BÀI TẬP 2: MÃ HÓA RSA-2048

## 1. Giới thiệu

Xây dựng chương trình mã hóa và giải mã RSA-2048 bằng ngôn ngữ C# trên nền tảng .NET 10. Chương trình hỗ trợ tạo khóa, mã hóa văn bản, băm SHA-256, ký số RSA-PSS và xác minh chữ ký.

<<<<<<< HEAD
## 1. Giới thiệu
=======
## 2. Công nghệ sử dụng
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)

- Ngôn ngữ: C#
- Nền tảng: .NET 10
- Mã hóa: RSA-2048, OAEP-SHA256
- Băm dữ liệu: SHA-256
- Chữ ký số: RSA-PSS-SHA256
- Thư viện: `System.Security.Cryptography`

## 3. Các chức năng chính

1. Tạo cặp khóa RSA-2048.
2. Xuất và nhập khóa PEM.
3. Mã hóa và giải mã văn bản.
4. Tính giá trị băm SHA-256.
5. Ký số và xác minh chữ ký.
6. Đo thời gian mã hóa, giải mã.
7. Xem và phân tích file PEM.
8. Ký RSA-PSS hai lần và so sánh chữ ký.

## 4. Kết quả kiểm thử

### 4.1. Mã hóa và giải mã

<<<<<<< HEAD
## 2. Công nghệ sử dụng
=======
- Văn bản thử nghiệm: `hello, toi la Duy`
- Kết quả: Giải mã thành công và khôi phục đúng văn bản ban đầu.
- Khóa RSA-2048 được tạo và xuất ra hai file PEM.
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)

### 4.2. Băm SHA-256

Văn bản đầu vào:

<<<<<<< HEAD
- Ngôn ngữ lập trình: C#

- Nền tảng: .NET 10

- Thuật toán mã hóa khóa công khai: RSA-2048

- Thuật toán băm: SHA-256

- Cơ chế mã hóa: RSA-OAEP với SHA-256

- Cơ chế ký số: RSA-PSS với SHA-256

- Công cụ biên dịch: .NET SDK



## 3. Các chức năng chính


1. Tạo cặp khóa RSA-2048.

2. Xuất khóa công khai và khóa riêng ra file PEM.

3. Nhập khóa từ file PEM.

4. Mã hóa văn bản.

5. Giải mã dữ liệu Base64.

6. Tính giá trị băm SHA-256.

7. Ký số bằng RSA-PSS.

8. Xác minh chữ ký số.

9. Đo thời gian mã hóa và giải mã.

10. Xem và phân tích thông tin khóa PEM.

11. Thực hiện ký RSA-PSS hai lần và so sánh chữ ký.



## 4. Cấu trúc thư mục



- `Program.cs`: Mã nguồn chính của chương trình.

- `Bai2\_RSA.csproj`: File cấu hình dự án C#.

- `.gitignore`: Quy định các file và thư mục không đưa lên Git.

- `ciphertext.txt`: File lưu dữ liệu mã hóa thử nghiệm.

- `signature.txt`: File lưu chữ ký số thử nghiệm.

- `keys/`: Thư mục lưu khóa RSA trên máy chạy chương trình; không đưa khóa riêng lên GitHub.

- `bin/`, `obj/`: Các thư mục được tạo tự động khi biên dịch.



## 5. Cách chạy chương trình



Mở PowerShell tại thư mục `Bai2\_RSA`, sau đó thực hiện:



```powershell

 "C:\\Program Files\\dotnet\\dotnet.exe" build

=======
```text
hello, toi yeu Huyen
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)
```

Giá trị băm thu được:

<<<<<<< HEAD

Nếu biên dịch thành công, chạy chương trình bằng lệnh:



```powershell

 "C:\\Program Files\\dotnet\\dotnet.exe" run

=======
```text
8af6f89703b91f6e7d84b210ade7bea843d74c56453331e90abbd2df29258697
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)
```

### 4.3. Ký số và xác minh chữ ký

- Nội dung ký: `hello, toi yeu Huyen`
- Thuật toán: RSA-PSS kết hợp SHA-256.
- Kết quả kiểm thử: `Chu ky HOP LE`.

### 4.4. Đo thời gian mã hóa và giải mã

Dữ liệu thử nghiệm: `hello, toi yeu Huyền`.

| Thông số | Kết quả |
|---|---:|
| Độ dài dữ liệu UTF-8 | 22 byte |
| Độ dài dữ liệu mã hóa | 256 byte |
| Thời gian mã hóa | 0,0154 ms |
| Thời gian giải mã | 0,5072 ms |
| Khôi phục dữ liệu chính xác | True |

<<<<<<< HEAD
## 6. Lưu ý bảo mật
=======
Thời gian trên là kết quả của lần chạy thử nghiệm trên máy thực hành, có thể thay đổi tùy môi trường.
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)

### 4.5. Kiểm thử chữ ký RSA-PSS hai lần

Kết quả kiểm thử:

<<<<<<< HEAD
- Không chia sẻ khóa riêng RSA.

- Không đưa khóa riêng hoặc thông tin bí mật lên GitHub.

- Thư mục `keys/`, `bin/` và `obj/` được loại trừ khỏi Git bằng file `.gitignore`.

- Chương trình được xây dựng phục vụ mục đích học tập và thực hành mật mã.
=======
```text
Hai chu ky khac nhau: True
Chu ky 1 hop le: True
Chu ky 2 hop le: True
```

Hai chữ ký có thể khác nhau do RSA-PSS sử dụng thành phần ngẫu nhiên, nhưng cả hai đều xác minh hợp lệ.

## 5. Hướng dẫn chạy chương trình

Mở PowerShell tại thư mục `Bai2_RSA` và chạy lệnh biên dịch:
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)

```powershell
& "C:\Program Files\dotnet\dotnet.exe" build
```

Kết quả kiểm tra: dự án `Bai2_RSA` biên dịch thành công với cấu hình `net10.0`.

<<<<<<< HEAD
## 7. Kết luận

Bài tập giúp tìm hiểu cách sử dụng RSA-2048 để mã hóa, giải mã và ký số, đồng thời thực hành SHA-256, quản lý khóa PEM và đánh giá thời gian xử lý của các thao tác mật mã.
=======
Chạy chương trình:

```powershell
& "C:\Program Files\dotnet\dotnet.exe" run
```

Sau đó chọn chức năng tương ứng trong menu hiển thị.
>>>>>>> 713f3b8 (Cap nhat README va ket qua kiem thu RSA)

## 6. Cấu trúc dự án

- `Program.cs`: Mã nguồn chính.
- `Bai2_RSA.csproj`: Cấu hình dự án .NET.
- `README.md`: Tài liệu mô tả và kết quả kiểm thử.
- `.gitignore`: Loại trừ các tệp không cần đưa lên Git.
- `ciphertext.txt`: Dữ liệu mã hóa thử nghiệm.
- `signature.txt`: Chữ ký số thử nghiệm.
- `keys/`: Thư mục lưu khóa PEM trên máy cục bộ.
- `bin/`, `obj/`: Thư mục tự sinh khi biên dịch.

**Lưu ý bảo mật:** Không đưa khóa riêng RSA lên GitHub. Các thư mục `keys/`, `bin/` và `obj/` cần được loại trừ khỏi Git.

## 7. Kết luận

Chương trình đã được biên dịch thành công và các chức năng mã hóa, giải mã, băm SHA-256, ký số và xác minh chữ ký đã được kiểm thử. Qua bài tập, người thực hiện hiểu rõ hơn về RSA-2048 và cách ứng dụng các kỹ thuật mật mã cơ bản trong lập trình C#.