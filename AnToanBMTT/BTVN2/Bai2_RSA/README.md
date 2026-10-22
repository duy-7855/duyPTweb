\# BÀI TẬP 2: MÃ HÓA RSA-2048



\## 1. Giới thiệu



Xây dựng chương trình ứng dụng thuật toán RSA-2048 bằng ngôn ngữ C# trên nền tảng .NET. Chương trình minh họa các chức năng mã hóa, giải mã, băm dữ liệu và ký số nhằm tìm hiểu các ứng dụng cơ bản của mật mã khóa công khai.



\## 2. Công nghệ sử dụng



\- Ngôn ngữ lập trình: C#

\- Nền tảng: .NET 10

\- Thuật toán mã hóa khóa công khai: RSA-2048

\- Thuật toán băm: SHA-256

\- Cơ chế mã hóa: RSA-OAEP với SHA-256

\- Cơ chế ký số: RSA-PSS với SHA-256

\- Công cụ biên dịch: .NET SDK



\## 3. Các chức năng chính



1\. Tạo cặp khóa RSA-2048.

2\. Xuất khóa công khai và khóa riêng ra file PEM.

3\. Nhập khóa từ file PEM.

4\. Mã hóa văn bản.

5\. Giải mã dữ liệu Base64.

6\. Tính giá trị băm SHA-256.

7\. Ký số bằng RSA-PSS.

8\. Xác minh chữ ký số.

9\. Đo thời gian mã hóa và giải mã.

10\. Xem và phân tích thông tin khóa PEM.

11\. Thực hiện ký RSA-PSS hai lần và so sánh chữ ký.



\## 4. Cấu trúc thư mục



\- `Program.cs`: Mã nguồn chính của chương trình.

\- `Bai2\_RSA.csproj`: File cấu hình dự án C#.

\- `.gitignore`: Quy định các file và thư mục không đưa lên Git.

\- `ciphertext.txt`: File lưu dữ liệu mã hóa thử nghiệm.

\- `signature.txt`: File lưu chữ ký số thử nghiệm.

\- `keys/`: Thư mục lưu khóa RSA trên máy chạy chương trình; không đưa khóa riêng lên GitHub.

\- `bin/`, `obj/`: Các thư mục được tạo tự động khi biên dịch.



\## 5. Cách chạy chương trình



Mở PowerShell tại thư mục `Bai2\_RSA`, sau đó thực hiện:



```powershell

\& "C:\\Program Files\\dotnet\\dotnet.exe" build

```



Nếu biên dịch thành công, chạy chương trình bằng lệnh:



```powershell

\& "C:\\Program Files\\dotnet\\dotnet.exe" run

```



Chọn chức năng tương ứng trong menu hiển thị trên màn hình.



\## 6. Lưu ý bảo mật



\- Không chia sẻ khóa riêng RSA.

\- Không đưa khóa riêng hoặc thông tin bí mật lên GitHub.

\- Thư mục `keys/`, `bin/` và `obj/` được loại trừ khỏi Git bằng file `.gitignore`.

\- Chương trình được xây dựng phục vụ mục đích học tập và thực hành mật mã.



\## 7. Kết luận



Bài tập giúp tìm hiểu cách sử dụng RSA-2048 để mã hóa, giải mã và ký số, đồng thời thực hành SHA-256, quản lý khóa PEM và đánh giá thời gian xử lý của các thao tác mật mã.

