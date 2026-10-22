# ======================================================================
# Buổi 2 - Môi trường & code đầu tiên
# Dán vào Jupyter: mỗi khối "# %%" là một ô code.
# ======================================================================


# %% Ô 1
import sys

print("Phiên bản Python:", sys.version.split()[0])
print("Đang chạy bằng  :", sys.executable)       # phải trỏ vào .venv nếu bạn đã tạo venv
print()

for ten in ["numpy", "cv2", "matplotlib", "PIL"]:
    try:
        mo_dun = __import__(ten)
        print(f"  [OK]    {ten:12} {getattr(mo_dun, '__version__', '')}")
    except ImportError:
        print(f"  [THIẾU] {ten:12} -> pip install " + {"cv2": "opencv-python", "PIL": "pillow"}.get(ten, ten))


# %% Ô 2
print("Hello, SDV!")
print("Trạm kiểm tra số", 3, "đã sẵn sàng")


# %% Ô 3
# Python cũng là một máy tính bỏ túi
print(50.27 - 50.0)      # sai lệch kích thước
print(12 / 5)            # chia -> luôn ra số thực
print(12 // 5, 12 % 5)   # chia lấy phần nguyên, lấy dư
print(2 ** 10)           # lũy thừa


# %% Ô 4
ma_san_pham = "SP002"      # str   - chuỗi
kich_thuoc  = 50.27        # float - số thực
so_luong    = 120          # int   - số nguyên
dat_chuan   = True         # bool  - đúng/sai

for ten, gia_tri in [("ma_san_pham", ma_san_pham), ("kich_thuoc", kich_thuoc),
                     ("so_luong", so_luong), ("dat_chuan", dat_chuan)]:
    print(f"{ten:12} = {str(gia_tri):8} -> kiểu {type(gia_tri).__name__}")


# %% Ô 5
# Dữ liệu đọc từ file, từ máy đo, từ ô nhập liệu LUÔN là chuỗi -> phải ép kiểu
chuoi_do = "50.27"
print(chuoi_do + "1")           # nối chuỗi, không phải cộng số!
print(float(chuoi_do) + 1)      # ép sang số rồi mới cộng

print(int("120"), float("0.25"), str(50.27))


# %% Ô 6
ma = "SP002"
do_duoc = 50.2734
danh_nghia = 50.0
sai_lech = do_duoc - danh_nghia

print(f"Mã sản phẩm: {ma}")
print(f"Sai lệch: {sai_lech:.2f} mm")        # .2f = làm tròn 2 chữ số thập phân
print(f"Sai lệch: {sai_lech:+.3f} mm")       # +  = luôn hiện dấu
print(f"Tỉ lệ NG: {3/12:.1%}")               # .1% = phần trăm
print(f"|{ma:<10}|{do_duoc:>10.2f}|")        # căn trái / căn phải -> làm bảng


# %% Ô 7
try:
    ma_nhap = input("Nhập mã sản phẩm: ")
except Exception:          # phòng khi notebook chạy tự động, không có người gõ
    ma_nhap = ""

ma_nhap = ma_nhap.strip().upper() or "SP002"    # bỏ khoảng trắng thừa, viết hoa, rỗng thì lấy mặc định
print("Đang kiểm tra:", ma_nhap)


# %% Ô 8
# Thử cho lỗi xảy ra để quen mặt (ô này cố tình sai, chạy xong nhớ đọc dòng cuối)
try:
    print("Kích thước: " + 50.27)
except TypeError as loi:
    print("TypeError ->", loi)
    print("Sửa:", "Kích thước: " + str(50.27))


# %% Ô 9
DANH_NGHIA = 50.0
DUNG_SAI = 0.25
GIOI_HAN_LOI = 3.0

# TODO 1: nhận 3 giá trị (tạm thời gán cứng để thử, sau đó đổi sang input())
ma = "SP002"
do_duoc = 50.27
dien_tich_loi = 2.40

# TODO 2: tính sai lệch, so với dung sai và giới hạn lỗi

# TODO 3: in phiếu kết quả như mẫu
