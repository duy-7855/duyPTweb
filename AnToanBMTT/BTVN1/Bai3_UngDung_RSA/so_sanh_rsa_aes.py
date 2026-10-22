from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import time


# =========================
# CHUẨN BỊ DỮ LIỆU
# =========================

message = "Đây là dữ liệu dùng để so sánh RSA và AES.".encode("utf-8")

# =========================
# TẠO KHÓA RSA
# =========================

rsa_key = RSA.generate(2048)
rsa_public_key = rsa_key.publickey()

rsa_encryptor = PKCS1_OAEP.new(rsa_public_key)
rsa_decryptor = PKCS1_OAEP.new(rsa_key)

# =========================
# TẠO KHÓA AES
# =========================

aes_key = get_random_bytes(32)  # AES-256


# =========================
# ĐO THỜI GIAN RSA
# =========================

so_lan = 100

start = time.perf_counter()

rsa_ciphertexts = []

for _ in range(so_lan):
    ciphertext = rsa_encryptor.encrypt(message)
    rsa_ciphertexts.append(ciphertext)

rsa_encrypt_time = time.perf_counter() - start


start = time.perf_counter()

rsa_plaintexts = []

for ciphertext in rsa_ciphertexts:
    plaintext = rsa_decryptor.decrypt(ciphertext)
    rsa_plaintexts.append(plaintext)

rsa_decrypt_time = time.perf_counter() - start


# =========================
# ĐO THỜI GIAN AES
# =========================

start = time.perf_counter()

aes_ciphertexts = []

for _ in range(so_lan):
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)

    aes_ciphertexts.append(
        (cipher.nonce, ciphertext, tag)
    )

aes_encrypt_time = time.perf_counter() - start


start = time.perf_counter()

aes_plaintexts = []

for nonce, ciphertext, tag in aes_ciphertexts:
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    aes_plaintexts.append(plaintext)

aes_decrypt_time = time.perf_counter() - start


# =========================
# KIỂM TRA KẾT QUẢ
# =========================

rsa_correct = all(
    plaintext == message
    for plaintext in rsa_plaintexts
)

aes_correct = all(
    plaintext == message
    for plaintext in aes_plaintexts
)


# =========================
# HIỂN THỊ KẾT QUẢ
# =========================

print("=" * 60)
print("SO SÁNH RSA 2048 VÀ AES-256")
print("=" * 60)

print(f"Số lần thực hiện: {so_lan}")
print(f"Kích thước dữ liệu: {len(message)} byte")

print("\n--- RSA 2048 ---")
print(f"Thời gian mã hóa : {rsa_encrypt_time:.6f} giây")
print(f"Thời gian giải mã: {rsa_decrypt_time:.6f} giây")
print(f"Giải mã đúng     : {rsa_correct}")

print("\n--- AES-256 ---")
print(f"Thời gian mã hóa : {aes_encrypt_time:.6f} giây")
print(f"Thời gian giải mã: {aes_decrypt_time:.6f} giây")
print(f"Giải mã đúng     : {aes_correct}")

print("\n--- NHẬN XÉT ---")
print("RSA phù hợp cho mã hóa khóa, trao đổi khóa và chữ ký số.")
print("AES phù hợp cho mã hóa dữ liệu lớn vì tốc độ xử lý nhanh.")
print("Trong thực tế, RSA và AES thường được sử dụng kết hợp.")
