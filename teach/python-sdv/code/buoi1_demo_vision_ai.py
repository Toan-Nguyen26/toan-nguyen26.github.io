# ======================================================================
# Buổi 1 - Demo Vision AI trong nhà máy
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
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

anh = np.array(Image.open(IMG_DIR / "SP001.png"))   # ảnh xám

print("Kiểu dữ liệu :", type(anh))
print("Kích thước   :", anh.shape, "-> (số hàng = chiều cao, số cột = chiều rộng)")
print("Kiểu phần tử :", anh.dtype, "-> mỗi pixel là số nguyên 0..255")
print("Tối nhất/sáng nhất:", anh.min(), anh.max())

plt.figure(figsize=(4, 3))
plt.imshow(anh, cmap="gray", vmin=0, vmax=255)
plt.title("SP001 - ảnh camera")
plt.axis("off")
plt.show()


# %% Ô 3
# Phóng to một vùng 6x8 pixel ở giữa ảnh: đây đúng là "bảng số" mà máy nhìn thấy
print(anh[118:124, 156:164])


# %% Ô 4
from scipy import ndimage

NGUONG_SANG = 110      # pixel sáng hơn mức này coi là thuộc sản phẩm
MM_PER_PIXEL = 0.1     # hiệu chuẩn camera: 1 pixel = 0.1 mm
GIOI_HAN_LOI = 3.0     # mm2 - quá ngưỡng này thì NG

def kiem_tra_be_mat(anh):
    vung_sang = anh > NGUONG_SANG                      # mặt nạ sản phẩm (còn thủng chỗ lỗi)
    san_pham = ndimage.binary_fill_holes(vung_sang)    # lấp lỗ -> biên ngoài sản phẩm
    loi = san_pham & ~vung_sang                        # phần tối nằm bên trong = khuyết tật
    dien_tich_mm2 = loi.sum() * MM_PER_PIXEL ** 2
    return san_pham, loi, dien_tich_mm2

san_pham, loi, dien_tich = kiem_tra_be_mat(anh)
print(f"Diện tích khuyết tật: {dien_tich:.2f} mm2")
print("Kết luận:", "NG" if dien_tich > GIOI_HAN_LOI else "OK")


# %% Ô 5
# Chạy cho cả lô và hiển thị vài ca điển hình
import glob

for ten in ["SP001", "SP003", "SP010"]:
    a = np.array(Image.open(IMG_DIR / f"{ten}.png"))
    sp, lo, dt = kiem_tra_be_mat(a)
    ket_luan = "NG" if dt > GIOI_HAN_LOI else "OK"

    fig, ax = plt.subplots(1, 3, figsize=(9, 2.6))
    ax[0].imshow(a, cmap="gray", vmin=0, vmax=255); ax[0].set_title(f"{ten} - ảnh gốc")
    ax[1].imshow(sp, cmap="gray");                  ax[1].set_title("vùng sản phẩm")
    ax[2].imshow(lo, cmap="hot");                   ax[2].set_title(f"khuyết tật: {dt:.2f} mm2 -> {ket_luan}")
    for t in ax: t.axis("off")
    plt.tight_layout(); plt.show()


# %% Ô 6
import csv

with open(CSV_PATH, encoding="utf-8") as f:
    bang_do = list(csv.DictReader(f))

so_ng = 0
for dong in bang_do:
    sai_lech = float(dong["measured_mm"]) - float(dong["nominal_mm"])
    dat = abs(sai_lech) <= float(dong["tolerance_mm"])
    so_ng += 0 if dat else 1
    print(f'{dong["product_id"]}  đo {dong["measured_mm"]:>6}  sai lệch {sai_lech:+.2f} mm  ->  {"PASS" if dat else "FAIL"}')

print(f"\nTổng: {len(bang_do)} sản phẩm, NG = {so_ng}, tỉ lệ NG = {so_ng / len(bang_do) * 100:.1f}%")


# %% Ô 7
hang1 = np.hstack([np.array(Image.open(IMG_DIR / f"SP00{i}.png")) for i in [1, 2, 3]])
hang2 = np.hstack([np.array(Image.open(IMG_DIR / f"SP00{i}.png")) for i in [5, 6, 8]])
khay = np.vstack([hang1, hang2])

nhan, so_vat_the = ndimage.label(khay > NGUONG_SANG)
print("Số sản phẩm đếm được:", so_vat_the)

plt.figure(figsize=(7, 3.2))
plt.imshow(nhan, cmap="nipy_spectral")
plt.title(f"Mỗi màu = 1 sản phẩm -> đếm được {so_vat_the}")
plt.axis("off"); plt.show()


# %% Ô 8
try:
    import cv2
except ImportError:
    print("Chưa có OpenCV. Chạy:  pip install opencv-python   (trên Colab: !pip install opencv-python)")
    cv2 = None

if cv2 is not None:
    noi_dung = "SP001|L1|2026-10-22|OK"
    anh_qr = cv2.QRCodeEncoder.create().encode(noi_dung)                      # mã QR gốc: 29x29 pixel
    anh_qr = cv2.copyMakeBorder(anh_qr, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=255)   # chừa viền trắng
    anh_qr = cv2.resize(anh_qr, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)  # phóng to cho đủ nét

    doc_duoc, *_ = cv2.QRCodeDetector().detectAndDecode(anh_qr)
    print("Nội dung giải mã được:", doc_duoc)
    # Thử bỏ 2 dòng viền + phóng to ở trên: mã quá nhỏ -> đọc ra chuỗi rỗng.
    # Đây chính là bài học "độ phân giải và vùng trắng quanh mã" khi lắp camera thật.

    plt.figure(figsize=(2.6, 2.6)); plt.imshow(anh_qr, cmap="gray"); plt.axis("off"); plt.show()
