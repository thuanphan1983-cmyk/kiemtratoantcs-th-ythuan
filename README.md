# HỆ THỐNG KIỂM TRA TOÁN THCS - KẾT NỐI TRI THỨC (LỚP 6, 7, 8, 9)

Hệ thống kiểm tra định kỳ môn Toán THCS bám sát cấu trúc ma trận mới nhất của Bộ Giáo dục & Đào tạo và bộ sách giáo khoa **Kết nối tri thức với cuộc sống**.

---

## ✨ TÍNH NĂNG NỔI BẬT

1. **Khởi chạy tức thì (Zero-config)**:
   - Chạy trực tiếp bằng cách nháy đúp chuột vào file `run.bat` hoặc mở thẳng `index.html` trong trình duyệt (Chrome, Edge, Opera, Cốc Cốc).
   - Tự động chạy máy chủ HTTP cục bộ bằng Python có sẵn trên máy.

2. **Tích hợp KaTeX hiển thị công thức toán học chuyên nghiệp**:
   - Tự động render tất cả các ký hiệu toán học `$ ... $` và `$$ ... $$` (phân số $\frac{a}{b}$, căn thức $\sqrt{x}$, hệ phương trình, số mũ...).

3. **Ngân hàng chương trình SGK đầy đủ (Cả Tập 1 & Tập 2)**:
   - Bao gồm toàn bộ các chương và hơn 80 bài học của cả 4 khối lớp: **Toán 6, Toán 7, Toán 8, Toán 9**.
   - Mỗi bài học cung cấp **3 đề kiểm tra độc lập** (Bài kiểm tra số 1, số 2, số 3).

4. **Cấu trúc đề chuẩn ma trận 10,0 điểm (Bộ GD&ĐT)**:
   - **Phần I (3,0 điểm):** 12 câu trắc nghiệm nhiều lựa chọn (0,25đ/câu) với cơ chế **khóa tuần tự** (làm câu trước mới mở câu sau).
   - **Phần II (2,0 điểm):** 2 câu trắc nghiệm Đúng/Sai (1,0đ/câu), tính điểm lũy tiến chuẩn Bộ GD&ĐT (0,1 - 0,25 - 0,5 - 1,0đ).
   - **Phần III (2,0 điểm):** 4 câu trả lời ngắn (0,5đ/câu) điền đáp số.
   - **Phần IV (3,0 điểm):** 3 câu tự luận (1,0đ/câu) cho phép chụp ảnh bài làm viết tay để AI Vision chấm điểm và đưa ra nhận xét theo biểu điểm chuẩn.

5. **Xuất bảng điểm ra file Excel (.xlsx), CSV (.csv) & Phiếu kết quả PDF**:
   - Lọc bảng thống kê điểm số theo từng lớp hoặc toàn trường.
   - Xuất file Excel chuẩn font tiếng Việt có định dạng cột chuyên nghiệp cho giáo viên.
   - Xuất phiếu kết quả kiểm tra từng học sinh ra file PDF để in ấn hoặc gửi phụ huynh.

---

## 🚀 HƯỚNG DẪN KHỞI CHẠY

### Cách 1: Chạy nhanh bằng file `run.bat` (Khuyên dùng)
* Nháy đúp chuột vào file **`run.bat`**.
* Hệ thống sẽ tự động bật máy chủ và mở trình duyệt tại `http://localhost:8000`.

### Cách 2: Mở trực tiếp
* Nháy đúp chuột mở file **`index.html`** bằng trình duyệt bất kỳ (Google Chrome, Microsoft Edge, Opera).

---

## 🔑 CẤU HÌNH GEMINI API KEY
* Khi mở ứng dụng, nhập mã **Gemini API Key** vào ô góc trên bên phải để kích hoạt khả năng:
  - Tự động sinh đề mới bám sát bài học.
  - OCR nhận diện chữ viết tay và chấm bài tự luận.
* Nếu chưa có API Key, hệ thống vẫn hoạt động bình thường với đề mẫu chuẩn ma trận có sẵn.
