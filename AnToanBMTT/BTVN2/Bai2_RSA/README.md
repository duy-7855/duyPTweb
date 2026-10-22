# BÀI TẬP 2: MÃ HÓA RSA-2048

## 1. Giới thiệu

Xây dựng chương trình mã hóa và giải mã RSA-2048 bằng ngôn ngữ C# trên nền tảng .NET 10. Chương trình hỗ trợ tạo khóa, mã hóa văn bản, băm SHA-256, ký số RSA-PSS và xác minh chữ ký.

## 2. Công nghệ sử dụng

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

- Văn bản thử nghiệm: `hello, toi la Duy`
- Kết quả: Giải mã thành công và khôi phục đúng văn bản ban đầu.
- Khóa RSA-2048 được tạo và xuất ra hai file PEM.

### 4.2. Băm SHA-256

Văn bản đầu vào:

```text
hello, toi yeu Huyen
```

Giá trị băm thu được:

```text
8af6f89703b91f6e7d84b210ade7bea843d74c56453331e90abbd2df29258697
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

Thời gian trên là kết quả của lần chạy thử nghiệm trên máy thực hành, có thể thay đổi tùy môi trường.

### 4.5. Kiểm thử chữ ký RSA-PSS hai lần

Kết quả kiểm thử:

```text
Hai chu ky khac nhau: True
Chu ky 1 hop le: True
Chu ky 2 hop le: True
```

Hai chữ ký có thể khác nhau do RSA-PSS sử dụng thành phần ngẫu nhiên, nhưng cả hai đều xác minh hợp lệ.

## 5. Hướng dẫn chạy chương trình

Mở PowerShell tại thư mục `Bai2_RSA` và chạy lệnh biên dịch:

```powershell
& "C:\Program Files\dotnet\dotnet.exe" build
```

Kết quả kiểm tra: dự án `Bai2_RSA` biên dịch thành công với cấu hình `net10.0`.

Chạy chương trình:

```powershell
& "C:\Program Files\dotnet\dotnet.exe" run
```

Sau đó chọn chức năng tương ứng trong menu hiển thị.

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