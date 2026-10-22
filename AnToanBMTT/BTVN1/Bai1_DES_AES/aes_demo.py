from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


# ==============================
# HÀM MÃ HÓA AES
# ==============================
def encrypt_aes(plain_text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode("utf-8"))

    return (
        base64.b64encode(cipher.nonce).decode("utf-8"),
        base64.b64encode(ciphertext).decode("utf-8"),
        base64.b64encode(tag).decode("utf-8")
    )


# ==============================
# HÀM GIẢI MÃ AES
# ==============================
def decrypt_aes(nonce, ciphertext, tag, key):
    nonce = base64.b64decode(nonce)
    ciphertext = base64.b64decode(ciphertext)
    tag = base64.b64decode(tag)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode("utf-8")


# ==============================
# CHƯƠNG TRÌNH CHÍNH
# ==============================

# AES-256 sử dụng khóa 32 byte
key = get_random_bytes(32)

message = "Đây là bài thực hành mã hóa AES."

print("========== AES DEMO ==========")
print("Thông điệp gốc:")
print(message)

print("\nKhóa AES:")
print(base64.b64encode(key).decode("utf-8"))

# Mã hóa
nonce, ciphertext, tag = encrypt_aes(message, key)

print("\n--- SAU KHI MÃ HÓA ---")
print("Nonce:")
print(nonce)

print("Ciphertext:")
print(ciphertext)

print("Tag:")
print(tag)

# Giải mã
decrypted_message = decrypt_aes(
    nonce,
    ciphertext,
    tag,
    key
)

print("\n--- SAU KHI GIẢI MÃ ---")
print(decrypted_message)

# Kiểm tra
if message == decrypted_message:
    print("\nKẾT QUẢ: Mã hóa và giải mã AES thành công!")
else:
    print("\nKẾT QUẢ: Có lỗi!")
