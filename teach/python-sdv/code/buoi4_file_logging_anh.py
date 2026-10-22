# ======================================================================
# Buổi 4 - File, logging, xử lý ảnh
# Dán vào Jupyter: mỗi khối "# %%" là một ô code.
# ======================================================================


# %% Ô 1
# === Ô CHUẨN BỊ: chạy ô này đầu tiên ===
# Tạo thư mục data/ (ảnh sản phẩm + file đo) nếu chưa có. Chạy được cả trên máy và trên Colab.
from pathlib import Path
import csv, random
import numpy as np
from PIL import Image

DATA = Path("data"); IMG_DIR = DATA / "images"; CSV_PATH = DATA / "measurements.csv"
NOMINAL, TOLERANCE = 50.0, 0.25

def _tao_du_lieu():
    rng, nprng = random.Random(26), np.random.default_rng(26)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    H, W = 240, 320
    yy, xx = np.mgrid[0:H, 0:W]
    rows = []
    for i in range(1, 13):
        pid = f"SP{i:03d}"
        img = nprng.normal(28, 4, size=(H, W))
        cy, cx = H // 2 + rng.randint(-6, 6), W // 2 + rng.randint(-8, 8)
        r0 = 85 + rng.randint(-3, 3)
        disk = (yy - cy) ** 2 + (xx - cx) ** 2 <= r0 ** 2
        img[disk] = nprng.normal(185, 5, size=disk.sum())
        for _ in range(2 if i in (3, 7) else (1 if i == 10 else 0)):
            a, d = rng.uniform(0, 6.28), rng.uniform(0, r0 * 0.75)
            dy, dx, r = int(cy + d * np.sin(a)), int(cx + d * np.cos(a)), rng.randint(5, 11)
            spot = ((yy - dy) ** 2 + (xx - dx) ** 2 <= r ** 2) & disk
            img[spot] = nprng.normal(55, 6, size=spot.sum())
        Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(IMG_DIR / f"{pid}.png")
        m = round(NOMINAL + nprng.normal(0, 0.08), 2)
        if i in (4, 9):
            m = round(NOMINAL + rng.choice([-1, 1]) * rng.uniform(0.3, 0.5), 2)
        rows.append({"product_id": pid, "line": rng.choice(["L1", "L2"]), "measured_mm": m,
                     "nominal_mm": NOMINAL, "tolerance_mm": TOLERANCE,
                     "operator": rng.choice(["A01", "A02", "B07"])})
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

if not CSV_PATH.exists():
    _tao_du_lieu()
print("Dữ liệu sẵn sàng:", len(list(IMG_DIR.glob("*.png"))), "ảnh,", CSV_PATH)


# %% Ô 2
from pathlib import Path

thu_muc_anh = Path("data") / "images"

print("Thư mục có tồn tại?", thu_muc_anh.exists())
print("Đường dẫn tuyệt đối:", thu_muc_anh.resolve())

danh_sach_anh = sorted(thu_muc_anh.glob("*.png"))      # chỉ lấy file .png, sắp xếp theo tên
print("Số ảnh:", len(danh_sach_anh))

p = danh_sach_anh[0]
print("Tên file     :", p.name)
print("Tên không đuôi:", p.stem)        # SP001 -> chính là mã sản phẩm
print("Phần mở rộng :", p.suffix)


# %% Ô 3
# Tạo thư mục kết quả (không lỗi nếu đã có)
KET_QUA = Path("ket_qua")
(KET_QUA / "anh_ng").mkdir(parents=True, exist_ok=True)
print("Đã chuẩn bị:", KET_QUA.resolve())

# Đặt tên file theo ngày - rất quan trọng khi chạy nhiều ca
from datetime import datetime
hom_nay = datetime.now().strftime("%Y%m%d")
file_bao_cao = KET_QUA / f"ket_qua_{hom_nay}.csv"
print("File báo cáo hôm nay:", file_bao_cao.name)


# %% Ô 4
import csv

with open(CSV_PATH, encoding="utf-8") as f:       # with ... -> tự đóng file, kể cả khi lỗi
    bang_do = list(csv.DictReader(f))              # mỗi dòng thành một dict

print("Số dòng:", len(bang_do))
print("Các cột:", list(bang_do[0].keys()))
print("Dòng đầu:", bang_do[0])


# %% Ô 5
# Tính toán rồi ghi kết quả ra CSV mới
ket_qua = []
for dong in bang_do:
    do_duoc = float(dong["measured_mm"])
    sai_lech = do_duoc - float(dong["nominal_mm"])
    dat = abs(sai_lech) <= float(dong["tolerance_mm"])
    ket_qua.append({
        "product_id": dong["product_id"],
        "line": dong["line"],
        "measured_mm": do_duoc,
        "deviation_mm": round(sai_lech, 3),
        "result": "OK" if dat else "NG",
    })

with open(file_bao_cao, "w", newline="", encoding="utf-8") as f:   # newline="" để Excel không chèn dòng trống
    writer = csv.DictWriter(f, fieldnames=list(ket_qua[0].keys()))
    writer.writeheader()
    writer.writerows(ket_qua)

print("Đã ghi", len(ket_qua), "dòng vào", file_bao_cao)
print(file_bao_cao.read_text(encoding="utf-8")[:220], "...")


# %% Ô 6
import logging
from logging.handlers import RotatingFileHandler

def tao_logger(ten="tram_kiem_tra", file_log=KET_QUA / "tram.log"):
    """Tạo logger ghi đồng thời ra màn hình và ra file xoay vòng."""
    logger = logging.getLogger(ten)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()        # tránh ghi trùng khi chạy lại ô này trong notebook

    dinh_dang = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    ra_man_hinh = logging.StreamHandler()
    ra_man_hinh.setLevel(logging.INFO)            # màn hình: gọn, chỉ từ INFO trở lên
    ra_man_hinh.setFormatter(dinh_dang)

    ra_file = RotatingFileHandler(file_log, maxBytes=1_000_000, backupCount=5, encoding="utf-8")
    ra_file.setLevel(logging.DEBUG)               # file: ghi đầy đủ để truy vết
    ra_file.setFormatter(dinh_dang)

    logger.addHandler(ra_man_hinh)
    logger.addHandler(ra_file)
    return logger

log = tao_logger()
log.info("Trạm kiểm tra khởi động")


# %% Ô 7
# 5 mức và cách dùng trong nhà máy
log.debug("Ảnh SP001: shape=(240, 320), thời gian xử lý 12 ms")   # chi tiết kỹ thuật, chỉ vào file
log.info("SP001: OK, sai lệch +0.10 mm")                          # diễn biến bình thường
log.warning("SP007: sai lệch +0.23 mm, sát ngưỡng dung sai")      # chưa lỗi nhưng cần để mắt
log.error("Không đọc được ảnh SP013.png - bỏ qua sản phẩm")       # một việc thất bại
log.critical("Mất kết nối camera - dừng dây chuyền")              # phải can thiệp ngay


# %% Ô 8
# Ghi lại lỗi kèm nguyên nhân: logger.exception() lưu cả traceback vào file
def doc_gia_tri(chuoi):
    return float(chuoi)

for gia_tri in ["50.1", "50,1"]:          # dấu phẩy thay vì dấu chấm -> lỗi kinh điển khi nhập tay
    try:
        print("Đọc được:", doc_gia_tri(gia_tri))
    except ValueError:
        log.exception("Giá trị đo không hợp lệ: %r", gia_tri)


# %% Ô 9
# Xem lại file log vừa ghi
print((KET_QUA / "tram.log").read_text(encoding="utf-8")[-900:])


# %% Ô 10
import numpy as np

a = np.array([[12, 15, 18, 20],
              [11, 14, 17, 21],
              [10, 13, 16, 19]])

print("shape:", a.shape, "| dtype:", a.dtype)
print("phần tử hàng 1 cột 2:", a[1, 2])
print("cả cột 1            :", a[:, 1])
print("vùng 2x2 góc trên   :\n", a[0:2, 0:2])
print("cộng 10 cho tất cả  :\n", a + 10)
print("trung bình / lớn nhất:", a.mean(), a.max())
print("mặt nạ a > 15       :\n", a > 15)
print("đếm phần tử > 15    :", (a > 15).sum())


# %% Ô 11
# Đọc ảnh. Dùng OpenCV nếu có, không thì dùng Pillow - kết quả đều là mảng NumPy.
try:
    import cv2
except ImportError:
    cv2 = None
    print("Chưa có OpenCV -> dùng Pillow. Cài bằng: pip install opencv-python")

from PIL import Image

def doc_anh_xam(duong_dan):
    """Đọc ảnh xám, trả về mảng NumPy uint8. Trả None nếu không đọc được."""
    duong_dan = str(duong_dan)
    if cv2 is not None:
        return cv2.imread(duong_dan, cv2.IMREAD_GRAYSCALE)
    anh = Image.open(duong_dan).convert("L")
    return np.array(anh)

anh = doc_anh_xam(IMG_DIR / "SP003.png")

if anh is None:                       # cv2.imread KHÔNG báo lỗi khi sai đường dẫn, chỉ trả None
    log.error("Không đọc được ảnh")
else:
    print("shape:", anh.shape, "| dtype:", anh.dtype, "| min/max:", anh.min(), anh.max())


# %% Ô 12
import matplotlib.pyplot as plt

NGUONG_SANG = 110
MM_PER_PIXEL = 0.1
GIOI_HAN_LOI = 3.0

from scipy import ndimage

vung_sang = anh > NGUONG_SANG                      # mặt nạ: True ở pixel sáng
san_pham = ndimage.binary_fill_holes(vung_sang)    # lấp lỗ -> toàn bộ thân sản phẩm
loi = san_pham & ~vung_sang                        # vết tối nằm trong thân = khuyết tật

dien_tich_mm2 = loi.sum() * MM_PER_PIXEL ** 2
ket_luan = "NG" if dien_tich_mm2 > GIOI_HAN_LOI else "OK"
print(f"Số pixel lỗi: {loi.sum()} -> {dien_tich_mm2:.2f} mm2 -> {ket_luan}")

fig, ax = plt.subplots(1, 3, figsize=(9, 2.6))
ax[0].imshow(anh, cmap="gray", vmin=0, vmax=255); ax[0].set_title("ảnh gốc")
ax[1].imshow(san_pham, cmap="gray");              ax[1].set_title("vùng sản phẩm")
ax[2].imshow(loi, cmap="hot");                    ax[2].set_title(f"khuyết tật {dien_tich_mm2:.2f} mm2")
for t in ax: t.axis("off")
plt.tight_layout(); plt.show()


# %% Ô 13
# Cắt ROI: chỉ kiểm tra vùng quan tâm -> nhanh hơn và ít báo giả hơn
roi = anh[60:180, 80:240]        # [hàng bắt đầu:hàng kết thúc, cột bắt đầu:cột kết thúc]
print("ROI shape:", roi.shape, "| độ sáng trung bình:", round(roi.mean(), 1))

# Khoanh vùng khuyết tật bằng np.where: lấy tọa độ các pixel lỗi
ys, xs = np.where(loi)
if len(ys) > 0:
    y1, y2, x1, x2 = ys.min(), ys.max(), xs.min(), xs.max()
    print(f"Hộp bao khuyết tật: x {x1}-{x2}, y {y1}-{y2}")

    anh_danh_dau = np.dstack([anh, anh, anh])          # xám -> 3 kênh để vẽ màu lên
    anh_danh_dau[y1:y2+1, [x1, x2]] = [255, 0, 0]      # 2 cạnh dọc
    anh_danh_dau[[y1, y2], x1:x2+1] = [255, 0, 0]      # 2 cạnh ngang

    plt.figure(figsize=(4, 3)); plt.imshow(anh_danh_dau); plt.axis("off")
    plt.title("Vị trí khuyết tật"); plt.show()


# %% Ô 14
# Lưu ảnh NG để truy vết sau này
duong_dan_luu = KET_QUA / "anh_ng" / "SP003_ng.png"
Image.fromarray(anh_danh_dau.astype(np.uint8)).save(duong_dan_luu)   # hoặc cv2.imwrite(str(duong_dan_luu), anh)
log.info("Đã lưu ảnh NG: %s", duong_dan_luu)


# %% Ô 15
# TODO: làm ở đây
