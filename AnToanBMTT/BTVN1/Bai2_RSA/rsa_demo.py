from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# ==========================================
# 1. TẠO CẶP KHÓA RSA
# ==========================================

key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()


# ==========================================
# 2. LƯU KHÓA RA FILE
# ==========================================

with open("private_key.pem", "wb") as f:
    f.write(private_key)

with open("public_key.pem", "wb") as f:
    f.write(public_key)


print("========== RSA DEMO ==========")

print("\nĐã tạo cặp khóa RSA 2048 bit.")
print("Private key: private_key.pem")
print("Public key : public_key.pem")


# ==========================================
# 3. THÔNG ĐIỆP GỐC
# ==========================================

message = "Đây là bài thực hành mã hóa RSA."

print("\nThông điệp gốc:")
print(message)


# ==========================================
# 4. MÃ HÓA BẰNG PUBLIC KEY
# ==========================================

recipient_public_key = RSA.import_key(public_key)

cipher_encrypt = PKCS1_OAEP.new(recipient_public_key)

encrypted_message = cipher_encrypt.encrypt(
    message.encode("utf-8")
)

print("\n--- SAU KHI MÃ HÓA ---")
print(base64.b64encode(encrypted_message).decode("utf-8"))


# ==========================================
# 5. GIẢI MÃ BẰNG PRIVATE KEY
# ==========================================

sender_private_key = RSA.import_key(private_key)

cipher_decrypt = PKCS1_OAEP.new(sender_private_key)

decrypted_message = cipher_decrypt.decrypt(
    encrypted_message
).decode("utf-8")


print("\n--- SAU KHI GIẢI MÃ ---")
print(decrypted_message)


# ==========================================
# 6. KIỂM TRA
# ==========================================

if message == decrypted_message:
    print("\nKẾT QUẢ: Mã hóa và giải mã RSA thành công!")
else:
    print("\nKẾT QUẢ: Có lỗi!")
