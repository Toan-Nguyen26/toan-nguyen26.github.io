# Python cho kỹ sư SDV — giáo án & notebook

Tài liệu giảng dạy cho khóa **Python + Vision AI cơ bản** dành cho kỹ sư nhà máy.
Bám theo lịch 2 ngày đã chốt; có sẵn phương án rút gọn còn **1.5 ngày**.

```
teach/python-sdv/
├── 00_demo_vision_ai.ipynb          # buổi 1 - demo mở màn (~30 phút)
├── 01_moi_truong_va_code_dau_tien.ipynb  # buổi 2 - cài đặt + code đầu tiên
├── 02_python_co_ban.ipynb           # buổi 3 - chuỗi, list, dict, if/for, hàm
├── 03_file_logging_anh.ipynb        # buổi 4 - file, CSV, logging, NumPy + ảnh
├── make_data.py                     # sinh dữ liệu mẫu (12 ảnh + measurements.csv)
└── data/                            # dữ liệu mẫu đã sinh sẵn
```

Mỗi notebook **tự tạo lại `data/` nếu thiếu** (ô đầu tiên), nên upload thẳng lên Colab là chạy được, không cần kèm file.

---

## 1. Lịch gốc và notebook tương ứng

| Buổi | Theo lịch | Notebook | Trọng tâm |
|---|---|---|---|
| D1 sáng | Khai mạc / tổng quan + ứng dụng Vision AI | `00_demo_vision_ai.ipynb` | tạo động lực, cho **thấy** trước khi học |
| D1 chiều | Cài đặt, làm quen môi trường Python | `01_moi_truong_va_code_dau_tien.ipynb` | 100% học viên chạy được code |
| D2 sáng | Lập trình Python cơ bản | `02_python_co_ban.ipynb` | biến, list, dict, if/for, hàm |
| D2 chiều | File, logging, thư viện xử lý ảnh | `03_file_logging_anh.ipynb` | ghép thành trạm kiểm tra mini |

---

## 2. Giáo án chi tiết từng buổi (~2 giờ/buổi)

### Buổi 1 — Khai mạc & Vision AI trong nhà máy

| Phút | Nội dung | Công cụ |
|---|---|---|
| 0–15 | Khai mạc, giới thiệu, **khảo sát nhanh**: ai đã từng viết code? ai dùng Excel/VBA? | miệng + giơ tay |
| 15–20 | Mục tiêu khóa học + cam kết đầu ra: cuối khóa tự viết được chương trình quét thư mục ảnh và xuất báo cáo OK/NG | slide |
| 20–60 | 5 bài toán Vision AI trong xưởng: kiểm lỗi bề mặt, phân loại, đếm sản phẩm, đọc QR/Barcode, OCR — mỗi bài 1 ví dụ có thật | slide (`Python basic.pptx` slide 5, 72–77) |
| 60–75 | **4 nhóm biến động phải khóa**: hình học, chiếu sáng, camera, sai khác sản phẩm. Thông điệp: ảnh vào ổn định thì luật đơn giản cũng chạy tốt | slide 74 |
| 75–105 | **Demo chạy trực tiếp** notebook 00: ảnh là bảng số → đo khuyết tật → so dung sai → đếm sản phẩm → đọc QR | `00_demo_vision_ai.ipynb` |
| 105–120 | Hỏi đáp + **giao việc chuẩn bị buổi chiều**: mang laptop, có quyền cài phần mềm, hoặc tài khoản Google để dùng Colab | checklist in sẵn |

> **Phát cho học viên:** link notebook 00 + bản PDF slide. Chưa cần họ code gì.

### Buổi 2 — Môi trường & những dòng code đầu tiên

| Phút | Nội dung |
|---|---|
| 0–30 | Cài đặt: Python 3.11/3.12 (Windows nhớ tick *Add to PATH*), VS Code + extension Python & Jupyter, `python -m venv .venv`, `pip install numpy opencv-python matplotlib` |
| 30–40 | Ai kẹt quyền cài đặt → chuyển sang **Google Colab** ngay, không để ai ngồi chờ |
| 40–50 | Notebook khác script thế nào; chọn đúng Python Interpreter trong VS Code |
| 50–60 | Chạy ô "kiểm tra môi trường" trong notebook 01 — **mục tiêu: không còn dòng `[THIẾU]` nào trong lớp** |
| 60–100 | `print` → phép toán → biến & kiểu dữ liệu → ép kiểu → f-string → `input()` |
| 100–110 | 3 lỗi chắc chắn gặp: `IndentationError`, `NameError`, `TypeError` — cách đọc thông báo lỗi (đọc dòng cuối trước) |
| 110–120 | Bài thực hành *Phiếu kiểm tra sản phẩm* + checklist cuối buổi |

> **Rủi ro lớn nhất của cả khóa nằm ở buổi này.** Nếu cuối buổi còn người chưa chạy được code, sáng hôm sau lớp sẽ tách làm hai tốc độ.
> Cách phòng: chuẩn bị sẵn **1 USB có bộ cài offline** và **1 link Colab** mở sẵn.

### Buổi 3 — Python cơ bản cho kỹ sư

| Phút | Nội dung | Ví dụ dùng tại lớp |
|---|---|---|
| 0–15 | Chuỗi: `strip`, `upper`, `split`, cắt chuỗi, `f"SP{i:03d}"` | làm sạch mã sản phẩm nhập tay |
| 15–40 | List: chỉ số, cắt lát, `append`, `len/min/max/sum/sorted`, duyệt + `enumerate` | 12 kết quả đo của một lô |
| 40–45 | **Bài tập nhanh**: đếm FAIL và tính tỉ lệ NG | |
| 45–70 | Dict: hồ sơ sản phẩm, bảng ngưỡng theo mã hàng, dict làm bộ đếm → Pareto | mỗi mã hàng một bộ dung sai |
| 70–90 | `if/elif/else` (OK / REWORK / NG), `for`, `while`, `break/continue`, `zip` | vòng lặp chờ kết nối camera |
| 90–110 | Hàm: `def`, tham số mặc định, docstring, trả về nhiều giá trị — **vì sao tách hàm**: đổi dung sai chỉ sửa một chỗ | `kiem_tra_san_pham(...)` |
| 110–120 | Giao bài tập tổng hợp (báo cáo lô hàng) — ai chưa xong làm tiếp đầu giờ chiều | |

> Nhịp dạy đề nghị: **5 phút giảng → 5 phút gõ theo → 1 câu hỏi nhanh**. Không giảng liền quá 10 phút.

### Buổi 4 — File, logging, xử lý ảnh

| Phút | Nội dung |
|---|---|
| 0–15 | `pathlib`: `Path`, `glob("*.png")`, `.stem` = mã sản phẩm, tạo thư mục kết quả, đặt tên file theo ngày |
| 15–40 | CSV: `csv.DictReader` / `DictWriter`, bẫy "mọi giá trị đọc lên là chuỗi", `encoding="utf-8"`, khi nào mới cần `pandas` |
| 40–70 | **Logging**: vì sao không dùng `print` ở xưởng, 5 mức log, format có timestamp, ghi ra file, `RotatingFileHandler`, `logger.exception()` để lưu traceback |
| 70–100 | NumPy + ảnh: `shape/dtype`, cắt ROI, mặt nạ `anh > 110`, đếm pixel → mm², khoanh vùng khuyết tật, lưu ảnh NG. Ba điều phải nhớ với OpenCV: `imread` trả `None`, thứ tự **BGR**, chỉ số `[y, x]` |
| 100–120 | Bài tập tổng hợp **trạm kiểm tra mini**: quét thư mục ảnh → kiểm tra → CSV + log + ảnh NG → tổng kết tỉ lệ NG |
| cuối | Chốt khóa + hướng đi tiếp (pandas, OpenCV nâng cao, PyQt6 HMI, deep learning) |

---

## 3. Nếu chỉ còn 1.5 ngày đứng lớp

Gộp còn 3 buổi, bỏ phần đánh dấu *(cắt)*:

| Buổi | Nội dung giữ lại |
|---|---|
| 1 (sáng) | Khai mạc rút còn 10 phút + demo notebook 00 (30 phút) + **cài đặt luôn trong buổi này** (60 phút) |
| 2 (chiều) | Notebook 01 (nhanh, 30 phút) + notebook 02 phần A–E |
| 3 (sáng hôm sau) | Notebook 02 phần F (bài tập tổng hợp) + notebook 03 |

*(cắt)* khi thiếu giờ, theo thứ tự ưu tiên cắt: `while` → OCR/QR → Pareto theo chuyền → `RotatingFileHandler` (chỉ nói miệng).
**Không cắt:** phần cài đặt, hàm, và bài tập tổng hợp buổi cuối — đó là ba thứ quyết định học viên có dùng được sau khóa hay không.

---

## 4. Việc cần làm trước khi lên lớp

- [ ] Chạy thử cả 4 notebook trên **đúng máy sẽ dùng để trình chiếu** (một lần `Restart & Run All`).
- [ ] Chuẩn bị **ảnh thật của xưởng** (10 OK + 10 NG) thay cho ảnh giả lập ở phần demo — giá trị thuyết phục khác hẳn.
- [ ] In checklist cài đặt phát đầu buổi 2.
- [ ] Mở sẵn một tab Colab đã đăng nhập, dùng khi có người không cài được.
- [ ] Chuẩn bị USB bộ cài Python + VS Code offline (mạng xưởng thường chậm hoặc bị chặn).
- [ ] Nhờ 1–2 học viên khá làm trợ giảng ngồi rải trong lớp.

## 5. Chạy notebook

```bash
# tạo lại dữ liệu mẫu nếu cần
python make_data.py

# mở bằng VS Code, hoặc
jupyter notebook
```

Trên Colab: `File > Upload notebook` rồi chạy ô đầu tiên — dữ liệu sẽ tự sinh.

Thư viện cần: `numpy`, `pillow`, `matplotlib`, `scipy`, và `opencv-python` (chỉ dùng cho phần QR và `imread`; các notebook đều có nhánh dự phòng dùng Pillow nếu thiếu OpenCV).
