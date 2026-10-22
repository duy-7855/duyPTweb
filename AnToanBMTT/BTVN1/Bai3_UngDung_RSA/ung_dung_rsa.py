from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64


# ==========================================
# 1. TẠO CẶP KHÓA RSA
# ==========================================

key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

print("========== ỨNG DỤNG RSA - CHỮ KÝ SỐ ==========")

print("\nĐã tạo cặp khóa RSA 2048 bit.")
print("Private Key: dùng để ký")
print("Public Key : dùng để xác thực")


# ==========================================
# 2. NGƯỜI GỬI TẠO THÔNG ĐIỆP
# ==========================================

message = "Xin chào, đây là thông điệp từ người gửi."

print("\n========== NGƯỜI GỬI ==========")
print("Thông điệp:")
print(message)


# ==========================================
# 3. NGƯỜI GỬI TẠO CHỮ KÝ
# ==========================================

hash_message = SHA256.new(message.encode("utf-8"))

signature = pkcs1_15.new(private_key).sign(hash_message)

print("\nChữ ký số:")
print(base64.b64encode(signature).decode("utf-8"))


# ==========================================
# 4. NGƯỜI NHẬN NHẬN THÔNG ĐIỆP
# ==========================================

print("\n========== NGƯỜI NHẬN ==========")
print("Đã nhận thông điệp từ người gửi.")


# ==========================================
# 5. NGƯỜI NHẬN XÁC THỰC CHỮ KÝ
# ==========================================

hash_received_message = SHA256.new(message.encode("utf-8"))

try:
    pkcs1_15.new(public_key).verify(
        hash_received_message,
        signature
    )

    print("Xác thực chữ ký: THÀNH CÔNG")
    print("Thông điệp đúng là do người sở hữu Private Key ký.")

except (ValueError, TypeError):

    print("Xác thực chữ ký: THẤT BẠI")


# ==========================================
# 6. KIỂM TRA TRƯỜNG HỢP THÔNG ĐIỆP BỊ THAY ĐỔI
# ==========================================

tampered_message = "Xin chào, đây là thông điệp đã bị thay đổi."

print("\n========== KIỂM TRA THÔNG ĐIỆP BỊ THAY ĐỔI ==========")
print("Thông điệp mới:")
print(tampered_message)

hash_tampered_message = SHA256.new(
    tampered_message.encode("utf-8")
)

try:
    pkcs1_15.new(public_key).verify(
        hash_tampered_message,
        signature
    )

    print("Xác thực: THÀNH CÔNG")

except (ValueError, TypeError):

    print("Xác thực: THẤT BẠI")
    print("Phát hiện thông điệp đã bị thay đổi.")


print("\n========== KẾT LUẬN ==========")
print("RSA có thể sử dụng chữ ký số để:")
print("1. Xác thực người gửi.")
print("2. Kiểm tra tính toàn vẹn của thông điệp.")
