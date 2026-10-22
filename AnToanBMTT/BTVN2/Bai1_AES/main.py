import os
import time
import hashlib
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# ==================================================
# CAU HINH
# ==================================================

THU_MUC_KHOA = Path("keys")
DUONG_DAN_KHOA = THU_MUC_KHOA / "khoa_aes.key"
KICH_THUOC_KHOI = 1024 * 1024  # 1 MiB


# ==================================================
# 1. TAO / DOC / IMPORT KHOA AES-256
# ==================================================

def kiem_tra_khoa(khoa):
    """Kiem tra khoa AES-256 co dung 32 byte khong."""
    if len(khoa) != 32:
        raise ValueError("Khoa AES-256 phai co dung 32 byte.")
    return khoa


def lay_khoa():
    """Doc khoa mac dinh neu co; neu chua co thi tao khoa moi."""
    THU_MUC_KHOA.mkdir(parents=True, exist_ok=True)

    if DUONG_DAN_KHOA.exists():
        khoa = DUONG_DAN_KHOA.read_bytes()
        kiem_tra_khoa(khoa)
        return khoa

    khoa = AESGCM.generate_key(bit_length=256)
    DUONG_DAN_KHOA.write_bytes(khoa)
    print("Da tao khoa AES-256 tai:", DUONG_DAN_KHOA.resolve())
    return khoa


def sinh_khoa_moi():
    """Tao khoa AES-256 moi va luu vao file khoa mac dinh."""
    THU_MUC_KHOA.mkdir(parents=True, exist_ok=True)
    khoa = AESGCM.generate_key(bit_length=256)
    DUONG_DAN_KHOA.write_bytes(khoa)
    print("Da sinh va luu khoa moi tai:", DUONG_DAN_KHOA.resolve())
    print("Luu y: khoa moi khong giai ma duoc du lieu da ma hoa bang khoa cu.")
    return khoa


def import_khoa_tu_file():
    """Doc khoa AES-256 tu mot file do nguoi dung chon."""
    duong_dan = input(
        "Nhap duong dan file khoa (vi du keys\\khoa_aes.key): "
    ).strip().strip('"')

    file_khoa = Path(duong_dan)
    if not file_khoa.is_file():
        print("Khong tim thay file khoa.")
        return None

    try:
        khoa = file_khoa.read_bytes()
        kiem_tra_khoa(khoa)
        print("Import khoa thanh cong tu:", file_khoa.resolve())
        return khoa
    except Exception as loi:
        print("Import khoa that bai:", loi)
        return None


# ==================================================
# 2. MA HOA VAN BAN
# ==================================================

def ma_hoa_van_ban(khoa):
    van_ban = input("Nhap van ban can ma hoa: ")
    nonce = os.urandom(12)
    du_lieu_ma_hoa = AESGCM(khoa).encrypt(
        nonce, van_ban.encode("utf-8"), None
    )
    ket_qua = (nonce + du_lieu_ma_hoa).hex()

    print("\n===== KET QUA MA HOA =====")
    print("Van ban goc:", van_ban)
    print("Chuoi HEX da ma hoa:")
    print(ket_qua)
    print("==========================")
    return ket_qua


# ==================================================
# 3. GIAI MA VAN BAN
# ==================================================

def giai_ma_van_ban(khoa):
    chuoi_hex = input("Nhap chuoi HEX da ma hoa: ").strip()
    try:
        du_lieu = bytes.fromhex(chuoi_hex)
        if len(du_lieu) < 28:
            raise ValueError("Du lieu ma hoa qua ngan.")

        nonce = du_lieu[:12]
        ciphertext_va_tag = du_lieu[12:]
        van_ban_goc = AESGCM(khoa).decrypt(
            nonce, ciphertext_va_tag, None
        )

        print("\n===== KET QUA GIAI MA =====")
        print("Van ban sau giai ma:")
        print(van_ban_goc.decode("utf-8"))
        print("===========================")
    except Exception as loi:
        print("Giai ma that bai. Chuoi HEX, khoa hoac du lieu khong hop le.")
        print("Chi tiet:", loi)


# ==================================================
# 4. MA HOA FILE THONG THUONG
# ==================================================

def ma_hoa_file(khoa):
    duong_dan = input("Nhap duong dan file can ma hoa: ").strip().strip('"')
    file_goc = Path(duong_dan)

    if not file_goc.is_file():
        print("Loi: Khong tim thay file.")
        return

    try:
        du_lieu_goc = file_goc.read_bytes()
        nonce = os.urandom(12)
        ciphertext_va_tag = AESGCM(khoa).encrypt(nonce, du_lieu_goc, None)
        file_dich = Path(str(file_goc) + ".enc")
        file_dich.write_bytes(nonce + ciphertext_va_tag)

        print("\n===== MA HOA FILE THANH CONG =====")
        print("File goc:", file_goc.resolve())
        print("File ma hoa:", file_dich.resolve())
        print(f"Dung luong goc: {len(du_lieu_goc):,} byte")
        print(f"Dung luong ma hoa: {file_dich.stat().st_size:,} byte")
        print("==================================")
    except Exception as loi:
        print("Loi khi ma hoa file:", loi)


# ==================================================
# 5. GIAI MA FILE THONG THUONG
# ==================================================

def giai_ma_file(khoa):
    duong_dan = input("Nhap duong dan file .enc can giai ma: ").strip().strip('"')
    file_ma_hoa = Path(duong_dan)

    if not file_ma_hoa.is_file():
        print("Loi: Khong tim thay file ma hoa.")
        return

    try:
        du_lieu = file_ma_hoa.read_bytes()
        if len(du_lieu) < 28:
            raise ValueError("File ma hoa khong hop le.")

        nonce = du_lieu[:12]
        ciphertext_va_tag = du_lieu[12:]
        du_lieu_goc = AESGCM(khoa).decrypt(nonce, ciphertext_va_tag, None)

        ten_file_goc = file_ma_hoa.name
        if ten_file_goc.endswith(".enc"):
            ten_file_goc = ten_file_goc[:-4]

        file_khoi_phuc = file_ma_hoa.with_name(ten_file_goc + ".dec")
        file_khoi_phuc.write_bytes(du_lieu_goc)

        print("\n===== GIAI MA FILE THANH CONG =====")
        print("File ma hoa:", file_ma_hoa.resolve())
        print("File khoi phuc:", file_khoi_phuc.resolve())
        print(f"Dung luong khoi phuc: {len(du_lieu_goc):,} byte")
        print("===================================")
    except Exception as loi:
        print("Giai ma file that bai.")
        print("Khoa sai, file bi loi hoac du lieu da bi thay doi.")
        print("Chi tiet:", loi)


# ==================================================
# 6. HAM KIEM TRA FILE THEO SHA-256 VA BYTE
# ==================================================

def tinh_sha256(duong_dan_file, kich_thuoc_khoi=KICH_THUOC_KHOI):
    sha = hashlib.sha256()
    with open(duong_dan_file, "rb") as file:
        while True:
            khoi = file.read(kich_thuoc_khoi)
            if not khoi:
                break
            sha.update(khoi)
    return sha.hexdigest()


def so_sanh_byte(file_a, file_b, kich_thuoc_khoi=KICH_THUOC_KHOI):
    """So sanh noi dung theo tung khoi byte, khong nap ca file vao RAM."""
    path_a = Path(file_a)
    path_b = Path(file_b)

    if not path_a.is_file() or not path_b.is_file():
        return False

    if path_a.stat().st_size != path_b.stat().st_size:
        return False

    with open(path_a, "rb") as a, open(path_b, "rb") as b:
        while True:
            khoi_a = a.read(kich_thuoc_khoi)
            khoi_b = b.read(kich_thuoc_khoi)
            if khoi_a != khoi_b:
                return False
            if not khoi_a:
                return True


# ==================================================
# 7. THU NGHIEM FILE LON THEO TUNG KHOI
# ==================================================

def thu_nghiem_file(khoa, duong_dan):
    file_goc = Path(duong_dan)

    if not file_goc.is_file():
        raise FileNotFoundError("Khong tim thay file thu nghiem: " + str(file_goc))
    kiem_tra_khoa(khoa)

    file_ma_hoa = Path(str(file_goc) + ".enc")
    file_khoi_phuc = Path(str(file_goc) + ".dec")
    kich_thuoc_goc = file_goc.stat().st_size
    kich_thuoc_mib = kich_thuoc_goc / (1024 * 1024)

    # Ma hoa theo tung khoi
    nonce = os.urandom(12)
    bo_ma_hoa = Cipher(
        algorithms.AES(khoa), modes.GCM(nonce)
    ).encryptor()

    bat_dau = time.perf_counter()
    with open(file_goc, "rb") as nguon, open(file_ma_hoa, "wb") as dich:
        dich.write(nonce)
        while True:
            khoi = nguon.read(KICH_THUOC_KHOI)
            if not khoi:
                break
            dich.write(bo_ma_hoa.update(khoi))
        dich.write(bo_ma_hoa.finalize())
        dich.write(bo_ma_hoa.tag)
    thoi_gian_ma_hoa = time.perf_counter() - bat_dau

    # Giai ma theo tung khoi va xac thuc tag
    bat_dau = time.perf_counter()
    kich_thuoc_enc = file_ma_hoa.stat().st_size

    try:
        with open(file_ma_hoa, "rb") as nguon:
            nonce_doc = nguon.read(12)
            if len(nonce_doc) != 12 or kich_thuoc_enc < 28:
                raise ValueError("File ma hoa khong hop le.")

            nguon.seek(-16, os.SEEK_END)
            tag = nguon.read(16)
            nguon.seek(12, os.SEEK_SET)
            kich_thuoc_ciphertext = kich_thuoc_enc - 28

            bo_giai_ma = Cipher(
                algorithms.AES(khoa),
                modes.GCM(nonce_doc, tag)
            ).decryptor()

            with open(file_khoi_phuc, "wb") as dich:
                con_lai = kich_thuoc_ciphertext
                while con_lai > 0:
                    khoi = nguon.read(min(KICH_THUOC_KHOI, con_lai))
                    if not khoi:
                        raise ValueError("File ma hoa bi thieu du lieu.")
                    dich.write(bo_giai_ma.update(khoi))
                    con_lai -= len(khoi)
                khoi_cuoi = bo_giai_ma.finalize()
                if khoi_cuoi:
                    dich.write(khoi_cuoi)
    except Exception:
        if file_khoi_phuc.exists():
            file_khoi_phuc.unlink()
        raise

    thoi_gian_giai_ma = time.perf_counter() - bat_dau

    # Kiem tra dung luong, so sanh byte va SHA-256
    sha_goc = tinh_sha256(file_goc)
    sha_khoi_phuc = tinh_sha256(file_khoi_phuc)
    dung_luong_bang_nhau = file_goc.stat().st_size == file_khoi_phuc.stat().st_size
    byte_giong_nhau = so_sanh_byte(file_goc, file_khoi_phuc)
    sha_giong_nhau = sha_goc == sha_khoi_phuc
    giong_nhau = dung_luong_bang_nhau and byte_giong_nhau and sha_giong_nhau

    kich_thuoc_enc = file_ma_hoa.stat().st_size
    chenhlech = kich_thuoc_enc - kich_thuoc_goc
    toc_do_ma_hoa = kich_thuoc_mib / thoi_gian_ma_hoa if thoi_gian_ma_hoa > 0 else 0
    toc_do_giai_ma = kich_thuoc_mib / thoi_gian_giai_ma if thoi_gian_giai_ma > 0 else 0

    print("\n========== KET QUA THU NGHIEM ==========")
    print("File goc:", file_goc.resolve())
    print(f"Dung luong goc: {kich_thuoc_goc:,} byte")
    print(f"Dung luong ma hoa: {kich_thuoc_enc:,} byte")
    print(f"Dung luong tang them: {chenhlech:,} byte")
    print(f"Thoi gian ma hoa: {thoi_gian_ma_hoa:.6f} giay")
    print(f"Thoi gian giai ma: {thoi_gian_giai_ma:.6f} giay")
    print(f"Toc do ma hoa: {toc_do_ma_hoa:.2f} MiB/s")
    print(f"Toc do giai ma: {toc_do_giai_ma:.2f} MiB/s")
    print("File ma hoa:", file_ma_hoa.resolve())
    print("File khoi phuc:", file_khoi_phuc.resolve())
    print("SHA-256 file goc:", sha_goc)
    print("SHA-256 file khoi phuc:", sha_khoi_phuc)
    print("Dung luong hai file bang nhau:", dung_luong_bang_nhau)
    print("So sanh byte truc tiep:", byte_giong_nhau)
    print("SHA-256 trung khop:", sha_giong_nhau)
    print("Du lieu sau giai ma trung khop:", giong_nhau)
    print("========================================")
    return giong_nhau


# ==================================================
# 8. MENU CHINH
# ==================================================

def main():
    try:
        khoa = lay_khoa()
    except Exception as loi:
        print("Khong the khoi tao khoa AES:", loi)
        return

    while True:
        print("\n===== UNG DUNG MA HOA AES-256 =====")
        print("1. Sinh khoa AES-256 moi va luu file")
        print("2. Import khoa AES-256 tu file")
        print("3. Ma hoa van ban")
        print("4. Giai ma van ban")
        print("5. Ma hoa file")
        print("6. Giai ma file")
        print("7. Thu nghiem file lon (theo tung khoi)")
        print("0. Thoat")
        print("===================================")

        lua_chon = input("Nhap lua chon: ").strip()

        try:
            if lua_chon == "1":
                khoa = sinh_khoa_moi()

            elif lua_chon == "2":
                khoa_moi = import_khoa_tu_file()
                if khoa_moi is not None:
                    khoa = khoa_moi
                    print("Chuong trinh dang su dung khoa vua import.")

            elif lua_chon == "3":
                ma_hoa_van_ban(khoa)

            elif lua_chon == "4":
                giai_ma_van_ban(khoa)

            elif lua_chon == "5":
                ma_hoa_file(khoa)

            elif lua_chon == "6":
                giai_ma_file(khoa)

            elif lua_chon == "7":
                duong_dan = input(
                    "Nhap duong dan file can thu nghiem: "
                ).strip().strip('"')
                thu_nghiem_file(khoa, duong_dan)

            elif lua_chon == "0":
                print("Da thoat chuong trinh.")
                break

            else:
                print("Lua chon khong hop le. Hay nhap lai.")

        except Exception as loi:
            print("Da xay ra loi:", loi)


if __name__ == "__main__":
    main()
