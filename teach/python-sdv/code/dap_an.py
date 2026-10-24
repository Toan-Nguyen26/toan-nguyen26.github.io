# ======================================================================
# ĐÁP ÁN các bài tập trong khóa
# ======================================================================


# %% Buổi 2 - Phiếu kiểm tra sản phẩm - đáp án 1
DANH_NGHIA, DUNG_SAI, GIOI_HAN_LOI = 50.0, 0.25, 3.0

ma = input("Nhập mã sản phẩm: ").strip().upper()
do_duoc = float(input("Nhập kích thước đo được: "))
dien_tich_loi = float(input("Nhập diện tích khuyết tật: "))

sai_lech = do_duoc - DANH_NGHIA
dat_kich_thuoc = abs(sai_lech) <= DUNG_SAI
dat_be_mat = dien_tich_loi <= GIOI_HAN_LOI

print(f"\nMã sản phẩm: {ma}")
print(f"Sai lệch kích thước: {sai_lech:.2f} mm")
print(f"Kiểm tra kích thước: {'PASS' if dat_kich_thuoc else 'FAIL'}")
print(f"Kiểm tra bề mặt: {'PASS' if dat_be_mat else 'FAIL'}")

if dat_kich_thuoc and dat_be_mat:
    print("Kết quả cuối cùng: OK")
else:
    print("Kết quả cuối cùng: NG")
    if not dat_kich_thuoc:
        print("Nguyên nhân: Kích thước vượt dung sai")
    if not dat_be_mat:
        print("Nguyên nhân: Khuyết tật bề mặt vượt giới hạn")


# %% Buổi 3 - đáp án 1
fail = []
for gia_tri in kich_thuoc:
    if abs(gia_tri - DANH_NGHIA) > DUNG_SAI:
        fail.append(gia_tri)

print("Số FAIL:", len(fail))
print("Giá trị FAIL:", fail)
print(f"Tỉ lệ NG: {len(fail) / len(kich_thuoc):.1%}")


# %% Buổi 3 - đáp án 2
dem_nguyen_nhan = {}
dem_theo_chuyen = {}
so_ng = 0

print(f"{'Mã':7}{'Đo':>8}{'Sai lệch':>10}{'Lỗi mm2':>9}  {'KL':3} Lý do")
print("-" * 70)

for sp in LO_HANG:
    ket_luan, ly_do = kiem_tra_san_pham(sp["do"], sp["loi"])
    sai_lech = sp["do"] - 50.0
    print(f'{sp["ma"]:7}{sp["do"]:>8.2f}{sai_lech:>+10.2f}{sp["loi"]:>9.2f}  {ket_luan:3} {ly_do}')

    dem_theo_chuyen.setdefault(sp["chuyen"], {"OK": 0, "NG": 0})
    dem_theo_chuyen[sp["chuyen"]][ket_luan] += 1

    if ket_luan == "NG":
        so_ng += 1
        for nn in ly_do.split(", "):
            dem_nguyen_nhan[nn] = dem_nguyen_nhan.get(nn, 0) + 1

print(f"\nTổng {len(LO_HANG)} sản phẩm: OK = {len(LO_HANG) - so_ng}, NG = {so_ng}, "
      f"tỉ lệ NG = {so_ng / len(LO_HANG):.1%}")

print("\nNguyên nhân NG (Pareto):")
for nn, n in sorted(dem_nguyen_nhan.items(), key=lambda x: x[1], reverse=True):
    print(f"  {nn:40} {n}")

print("\nTheo chuyền:")
for chuyen, d in sorted(dem_theo_chuyen.items()):
    tong = d["OK"] + d["NG"]
    print(f"  {chuyen}: {d['NG']}/{tong} NG ({d['NG'] / tong:.1%})")


# %% Buổi 4 - Trạm kiểm tra mini - đáp án 1
# Tra cứu số đo theo mã sản phẩm
so_do = {d["product_id"]: d for d in bang_do}

bao_cao, dem_nguyen_nhan = [], {}

for duong_dan in sorted(IMG_DIR.glob("*.png")):
    ma = duong_dan.stem
    anh = doc_anh_xam(duong_dan)
    if anh is None:
        log.error("Không đọc được ảnh %s", duong_dan.name)
        continue

    vung_sang = anh > NGUONG_SANG
    loi = ndimage.binary_fill_holes(vung_sang) & ~vung_sang
    dien_tich = loi.sum() * MM_PER_PIXEL ** 2

    dong_do = so_do.get(ma)
    sai_lech = float(dong_do["measured_mm"]) - float(dong_do["nominal_mm"]) if dong_do else 0.0
    dung_sai = float(dong_do["tolerance_mm"]) if dong_do else 0.25

    ly_do = []
    if dien_tich > GIOI_HAN_LOI:
        ly_do.append("be_mat")
    if abs(sai_lech) > dung_sai:
        ly_do.append("kich_thuoc")
    ket_luan = "NG" if ly_do else "OK"

    log.info("%s: %s | sai lệch %+.2f mm | lỗi %.2f mm2 %s",
             ma, ket_luan, sai_lech, dien_tich, ("| " + ", ".join(ly_do)) if ly_do else "")

    for nn in ly_do:
        dem_nguyen_nhan[nn] = dem_nguyen_nhan.get(nn, 0) + 1
    if ket_luan == "NG":
        Image.fromarray(anh).save(KET_QUA / "anh_ng" / f"{ma}_ng.png")

    bao_cao.append({"product_id": ma, "deviation_mm": round(sai_lech, 3),
                    "defect_mm2": round(dien_tich, 2), "result": ket_luan,
                    "reason": ",".join(ly_do)})

with open(KET_QUA / "bao_cao_cuoi.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(bao_cao[0].keys()))
    w.writeheader(); w.writerows(bao_cao)

so_ng = sum(1 for d in bao_cao if d["result"] == "NG")
print(f"\nTổng {len(bao_cao)} sản phẩm | OK {len(bao_cao) - so_ng} | NG {so_ng} "
      f"| tỉ lệ NG {so_ng / len(bao_cao):.1%}")
print("Nguyên nhân:", sorted(dem_nguyen_nhan.items(), key=lambda x: -x[1]))
