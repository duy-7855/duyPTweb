from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64


# ==============================
# HÀM PADDING
# DES yêu cầu dữ liệu có độ dài
# là bội số của 8 byte
# ==============================
def pad(data):
    padding_length = 8 - (len(data) % 8)
    return data + bytes([padding_length]) * padding_length


# ==============================
# HÀM BỎ PADDING
# ==============================
def unpad(data):
    return data[:-data[-1]]


# ==============================
# HÀM MÃ HÓA DES
# ==============================
def encrypt_des(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)

    data = plain_text.encode("utf-8")
    data = pad(data)

    ciphertext = cipher.encrypt(data)

    return base64.b64encode(ciphertext).decode("utf-8")


# ==============================
# HÀM GIẢI MÃ DES
# ==============================
def decrypt_des(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)

    ciphertext = base64.b64decode(ciphertext)

    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext)

    return plaintext.decode("utf-8")


# ==============================
# CHƯƠNG TRÌNH CHÍNH
# ==============================

# DES sử dụng khóa 8 byte
key = get_random_bytes(8)

message = "Đây là bài thực hành mã hóa DES."

print("========== DES DEMO ==========")

print("Thông điệp gốc:")
print(message)

print("\nKhóa DES:")
print(base64.b64encode(key).decode("utf-8"))


# Mã hóa
ciphertext = encrypt_des(message, key)

print("\n--- SAU KHI MÃ HÓA ---")
print("Ciphertext:")
print(ciphertext)


# Giải mã
decrypted_message = decrypt_des(ciphertext, key)

print("\n--- SAU KHI GIẢI MÃ ---")
print(decrypted_message)


# Kiểm tra
if message == decrypted_message:
    print("\nKẾT QUẢ: Mã hóa và giải mã DES thành công!")
else:
    print("\nKẾT QUẢ: Có lỗi!")
