# ======================================================================
# Buổi 3 - Python cơ bản cho kỹ sư
# Dán vào Jupyter: mỗi khối "# %%" là một ô code.
# ======================================================================


# %% Ô 1
ma = "  sp002-l1  "

print(repr(ma.strip()))            # bỏ khoảng trắng 2 đầu
print(ma.strip().upper())          # viết hoa
print(ma.strip().upper().split("-"))   # tách theo dấu -

ma_sach = ma.strip().upper()
ma_sp, line = ma_sach.split("-")
print("Mã:", ma_sp, "| Chuyền:", line)

print(ma_sp.startswith("SP"), len(ma_sp))
print("Số thứ tự:", int(ma_sp[2:]))        # cắt chuỗi: lấy từ ký tự thứ 2 đến hết
print("Tên file ảnh:", f"SP{7:03d}.png")   # 03d = chèn số 0 cho đủ 3 chữ số


# %% Ô 2
kich_thuoc = [50.10, 49.96, 50.00, 49.58, 49.95, 50.04, 50.23, 49.94, 49.68, 50.02, 50.16, 49.88]

print("Số phần tử   :", len(kich_thuoc))
print("Giá trị đầu  :", kich_thuoc[0])
print("Giá trị cuối :", kich_thuoc[-1])
print("3 cái đầu    :", kich_thuoc[:3])     # cắt lát: từ 0 đến trước 3
print("Từ thứ 4 trở đi:", kich_thuoc[3:])


# %% Ô 3
# Các phép thống kê nhanh
print("Nhỏ nhất :", min(kich_thuoc))
print("Lớn nhất :", max(kich_thuoc))
print("Trung bình:", sum(kich_thuoc) / len(kich_thuoc))
print("Sắp xếp  :", sorted(kich_thuoc)[:5], "...")

# Thêm / sửa / xóa
kich_thuoc.append(50.07)        # thêm 1 sản phẩm vừa đo xong
# Lưu ý notebook: chạy lại ô này lần nữa sẽ thêm TIẾP một phần tử.
# Đây là bẫy kinh điển của notebook - trạng thái còn giữ trong bộ nhớ.
# Muốn làm lại từ đầu: Kernel > Restart và chạy lần lượt từ ô trên xuống.
print("Sau khi thêm:", len(kich_thuoc), "phần tử")


# %% Ô 4
# Duyệt danh sách
DANH_NGHIA, DUNG_SAI = 50.0, 0.25

for gia_tri in kich_thuoc[:5]:
    print(gia_tri, "->", "PASS" if abs(gia_tri - DANH_NGHIA) <= DUNG_SAI else "FAIL")

print()
# enumerate: cần cả số thứ tự
for i, gia_tri in enumerate(kich_thuoc[:5], start=1):
    print(f"Sản phẩm thứ {i}: {gia_tri}")


# %% Ô 5
# TODO: làm ở đây


# %% Ô 6
san_pham = {
    "ma": "SP002",
    "chuyen": "L1",
    "kich_thuoc": 49.58,
    "dien_tich_loi": 1.2,
    "ca": "A",
}

print(san_pham["ma"])                      # lấy theo khóa
print(san_pham.get("nhiet_do", "chưa đo")) # .get -> không có khóa cũng không lỗi

san_pham["ket_luan"] = "NG"                # thêm khóa mới
san_pham["kich_thuoc"] = 49.60             # sửa giá trị

for khoa, gia_tri in san_pham.items():
    print(f"  {khoa:16}: {gia_tri}")


# %% Ô 7
# Bảng ngưỡng theo mã hàng - rất hay gặp: mỗi mã hàng một bộ tham số
NGUONG = {
    "SP-A": {"danh_nghia": 50.0, "dung_sai": 0.25, "gioi_han_loi": 3.0},
    "SP-B": {"danh_nghia": 75.0, "dung_sai": 0.40, "gioi_han_loi": 5.0},
}

ma_hang = "SP-B"
cau_hinh = NGUONG[ma_hang]
print(f"{ma_hang}: {cau_hinh['danh_nghia']} ± {cau_hinh['dung_sai']} mm, lỗi tối đa {cau_hinh['gioi_han_loi']} mm2")


# %% Ô 8
# Dict làm bộ đếm: thống kê nguyên nhân NG (biểu đồ Pareto bắt đầu từ đây)
nguyen_nhan = ["kich_thuoc", "be_mat", "kich_thuoc", "ban", "kich_thuoc", "be_mat"]

dem = {}
for nn in nguyen_nhan:
    dem[nn] = dem.get(nn, 0) + 1          # chưa có thì coi như 0, rồi +1

print(dem)
for nn, so_lan in sorted(dem.items(), key=lambda x: x[1], reverse=True):
    print(f"{nn:12} {'#' * so_lan} ({so_lan})")


# %% Ô 9
def xep_loai(sai_lech, dien_tich_loi):
    if abs(sai_lech) > 0.25:
        return "NG"            # sai kích thước -> loại bỏ
    elif dien_tich_loi > 3.0:
        return "NG"
    elif dien_tich_loi > 1.5:
        return "REWORK"        # lỗi nhẹ -> đánh bóng lại
    else:
        return "OK"

for sl, dt in [(0.05, 0.0), (0.05, 2.0), (0.05, 4.0), (0.42, 0.0)]:
    print(f"sai lệch {sl:+.2f} mm, lỗi {dt:.1f} mm2 -> {xep_loai(sl, dt)}")


# %% Ô 10
# while: lặp đến khi thỏa điều kiện - hay dùng khi chờ thiết bị
so_lan_thu = 0
ket_noi = False
while not ket_noi and so_lan_thu < 3:
    so_lan_thu += 1
    print(f"Lần {so_lan_thu}: đang kết nối camera...")
    ket_noi = so_lan_thu == 2          # giả lập: lần thứ 2 thì được
print("Kết nối:", "thành công" if ket_noi else "thất bại")


# %% Ô 11
# break / continue
for i, gia_tri in enumerate(kich_thuoc, start=1):
    if gia_tri > 50.2:
        continue                       # bỏ qua, xét sản phẩm tiếp theo
    if gia_tri < 49.6:
        print(f"Dừng dây chuyền tại sản phẩm thứ {i}: {gia_tri} mm")
        break                          # thoát hẳn vòng lặp

# zip: ghép 2 danh sách song song
ma_list = ["SP001", "SP002", "SP003"]
do_list = [50.10, 49.96, 50.00]
for ma_sp, do in zip(ma_list, do_list):
    print(ma_sp, do)


# %% Ô 12
def kiem_tra_san_pham(do_duoc, dien_tich_loi, danh_nghia=50.0, dung_sai=0.25, gioi_han_loi=3.0):
    """Kiểm tra một sản phẩm.

    Trả về (ket_luan, ly_do) với ket_luan là "OK" hoặc "NG".
    """
    sai_lech = do_duoc - danh_nghia
    ly_do = []

    if abs(sai_lech) > dung_sai:
        ly_do.append("kích thước vượt dung sai")
    if dien_tich_loi > gioi_han_loi:
        ly_do.append("khuyết tật bề mặt vượt giới hạn")

    ket_luan = "NG" if ly_do else "OK"
    return ket_luan, ", ".join(ly_do)


print(kiem_tra_san_pham(50.10, 0.0))
print(kiem_tra_san_pham(49.58, 0.0))
print(kiem_tra_san_pham(49.58, 6.9))
print(kiem_tra_san_pham(75.30, 0.0, danh_nghia=75.0, dung_sai=0.40))   # đổi mã hàng, không sửa code


# %% Ô 13
LO_HANG = [
    {"ma": "SP001", "chuyen": "L1", "do": 50.10, "loi": 0.00},
    {"ma": "SP002", "chuyen": "L2", "do": 49.96, "loi": 0.00},
    {"ma": "SP003", "chuyen": "L1", "do": 50.00, "loi": 6.94},
    {"ma": "SP004", "chuyen": "L2", "do": 49.58, "loi": 0.00},
    {"ma": "SP005", "chuyen": "L2", "do": 49.95, "loi": 0.00},
    {"ma": "SP006", "chuyen": "L1", "do": 50.04, "loi": 0.00},
    {"ma": "SP007", "chuyen": "L1", "do": 50.23, "loi": 5.26},
    {"ma": "SP008", "chuyen": "L2", "do": 49.94, "loi": 0.00},
    {"ma": "SP009", "chuyen": "L1", "do": 49.68, "loi": 0.00},
    {"ma": "SP010", "chuyen": "L1", "do": 50.02, "loi": 3.77},
    {"ma": "SP011", "chuyen": "L1", "do": 50.16, "loi": 0.00},
    {"ma": "SP012", "chuyen": "L1", "do": 49.88, "loi": 0.00},
]

# TODO 1: in bảng kết quả từng sản phẩm (dùng hàm kiem_tra_san_pham ở phần E)

# TODO 2: đếm OK / NG và tỉ lệ NG

# TODO 3: thống kê nguyên nhân NG

# TODO 4: so sánh NG giữa chuyền L1 và L2
