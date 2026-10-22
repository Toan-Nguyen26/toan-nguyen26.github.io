"""Sinh dữ liệu mẫu cho khóa Python cho kỹ sư SDV.

Chạy một lần:  python make_data.py
Tạo ra:
  data/images/*.png   - ảnh sản phẩm giả lập (một số có khuyết tật)
  data/measurements.csv - bảng đo kích thước của lô sản phẩm
Chỉ cần numpy + Pillow (Colab có sẵn cả hai).
"""
import csv
import random
from pathlib import Path

import numpy as np
from PIL import Image

RNG = random.Random(26)
NP_RNG = np.random.default_rng(26)

OUT = Path(__file__).parent / "data"
IMG_DIR = OUT / "images"
IMG_DIR.mkdir(parents=True, exist_ok=True)

H, W = 240, 320
NOMINAL = 50.0          # kích thước danh nghĩa (mm)
TOLERANCE = 0.25        # dung sai cho phép (mm)


def make_product_image(defects: int) -> np.ndarray:
    """Tạo ảnh xám: nền tối, sản phẩm hình tròn sáng, defects chấm tối trên bề mặt."""
    img = NP_RNG.normal(28, 4, size=(H, W))          # nền + nhiễu cảm biến
    yy, xx = np.mgrid[0:H, 0:W]
    cy, cx = H // 2 + RNG.randint(-6, 6), W // 2 + RNG.randint(-8, 8)
    radius = 85 + RNG.randint(-3, 3)
    disk = (yy - cy) ** 2 + (xx - cx) ** 2 <= radius ** 2
    img[disk] = NP_RNG.normal(185, 5, size=disk.sum())

    for _ in range(defects):
        angle = RNG.uniform(0, 6.28)
        dist = RNG.uniform(0, radius * 0.75)
        dy = int(cy + dist * np.sin(angle))
        dx = int(cx + dist * np.cos(angle))
        r = RNG.randint(5, 11)
        spot = (yy - dy) ** 2 + (xx - dx) ** 2 <= r ** 2
        img[spot & disk] = NP_RNG.normal(55, 6, size=(spot & disk).sum())

    return np.clip(img, 0, 255).astype(np.uint8)


def main() -> None:
    rows = []
    for i in range(1, 13):
        product_id = f"SP{i:03d}"
        # 3 sản phẩm có khuyết tật rõ, phần còn lại sạch
        defects = 2 if i in (3, 7) else (1 if i == 10 else 0)
        Image.fromarray(make_product_image(defects)).save(IMG_DIR / f"{product_id}.png")

        measured = round(NOMINAL + NP_RNG.normal(0, 0.08), 2)
        if i in (4, 9):                      # cố tình cho 2 sản phẩm out-of-tolerance
            measured = round(NOMINAL + RNG.choice([-1, 1]) * RNG.uniform(0.3, 0.5), 2)
        rows.append({
            "product_id": product_id,
            "line": RNG.choice(["L1", "L2"]),
            "measured_mm": measured,
            "nominal_mm": NOMINAL,
            "tolerance_mm": TOLERANCE,
            "operator": RNG.choice(["A01", "A02", "B07"]),
        })

    with open(OUT / "measurements.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Đã tạo {len(rows)} ảnh trong {IMG_DIR} và {OUT / 'measurements.csv'}")


if __name__ == "__main__":
    main()
