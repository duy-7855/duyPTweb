from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
import time


# ==============================
# DỮ LIỆU THỬ NGHIỆM
# ==============================
message = "Đây là dữ liệu dùng để so sánh tốc độ mã hóa AES và DES."

data = message.encode("utf-8")


# ==============================
# AES
# AES-256, chế độ ECB
# ==============================
aes_key = get_random_bytes(32)

# Padding cho AES
aes_padding = 16 - (len(data) % 16)
aes_data = data + bytes([aes_padding]) * aes_padding

start = time.perf_counter()

aes_cipher = AES.new(aes_key, AES.MODE_ECB)
aes_encrypted = aes_cipher.encrypt(aes_data)

aes_encrypt_time = time.perf_counter() - start


start = time.perf_counter()

aes_cipher = AES.new(aes_key, AES.MODE_ECB)
aes_decrypted = aes_cipher.decrypt(aes_encrypted)

aes_decrypt_time = time.perf_counter() - start

aes_decrypted = aes_decrypted[:-aes_decrypted[-1]]


# ==============================
# DES
# DES, chế độ ECB
# ==============================
des_key = get_random_bytes(8)

# Padding cho DES
des_padding = 8 - (len(data) % 8)
des_data = data + bytes([des_padding]) * des_padding

start = time.perf_counter()

des_cipher = DES.new(des_key, DES.MODE_ECB)
des_encrypted = des_cipher.encrypt(des_data)

des_encrypt_time = time.perf_counter() - start


start = time.perf_counter()

des_cipher = DES.new(des_key, DES.MODE_ECB)
des_decrypted = des_cipher.decrypt(des_encrypted)

des_decrypt_time = time.perf_counter() - start

des_decrypted = des_decrypted[:-des_decrypted[-1]]


# ==============================
# HIỂN THỊ KẾT QUẢ
# ==============================

print("========================================")
print(" SO SÁNH THỜI GIAN AES VÀ DES")
print("========================================")

print("\nThông điệp:")
print(message)

print("\n---------- AES ----------")
print("Thời gian mã hóa : {:.9f} giây".format(aes_encrypt_time))
print("Thời gian giải mã: {:.9f} giây".format(aes_decrypt_time))
print("Giải mã đúng     :", aes_decrypted == data)

print("\n---------- DES ----------")
print("Thời gian mã hóa : {:.9f} giây".format(des_encrypt_time))
print("Thời gian giải mã: {:.9f} giây".format(des_decrypt_time))
print("Giải mã đúng     :", des_decrypted == data)

print("\n========================================")
print(" KẾT LUẬN")
print("========================================")
print("AES sử dụng khóa 256 bit.")
print("DES sử dụng khóa 64 bit (56 bit hiệu dụng).")
print("AES có mức độ an toàn cao hơn DES.")
print("DES hiện nay không còn được khuyến nghị cho hệ thống mới.")
