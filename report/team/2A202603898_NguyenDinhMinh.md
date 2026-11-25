# Báo cáo cá nhân — MinhNGD76

> Bản nháp. Đổi tên file thành `MSSV_HoTenKhongDau.md` sau khi điền MSSV và họ tên. Giữ nguyên file mẫu `MSSV_HoTen.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đình Minh
- MSSV: 2A202603898
- Email: [điền]
- GitHub: MinhNGD76
- Vai trong nhóm: Người viết code (nhiệm vụ A và B)

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): mô hình chi phí mỗi việc thành công, gồm A1–A4. Đã merge vào `main`.
- Nhiệm vụ B (CP2): bảng độ nhạy, gồm B1–B4. Đang ở nhánh `minh`, chưa merge.
- File phụ trách: `src/lab13.py` (phần A và B), `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- **A1:** viết ba hàm chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`). Ba phép thử đạt: 1,20 · 1,25 · 1,25.
- **A2:** viết `mo_hinh()` với tham số giá, hệ số và `max_lan_chay` để nhiệm vụ B dùng lại. Viết `kiem_tra_a2()` để đối chiếu với đáp án, lệch không quá 2%.
- **A3:** tách theo loại yêu cầu, kèm tỉ lệ ok theo từng lần thử.
- **A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`, ở hai mức khối lượng.
- **B1–B2:** chạy 9 kịch bản đổi từng yếu tố và cặp kịch bản. Kiểm tra mỗi cặp "gấp đôi / giảm một nửa" có tổng khớp.
- **B3:** tính chi phí cả hệ thống cho giới hạn 1, 2, 3 lần chạy.
- **B4:** tính xem lại 100% cho `noi_dia` + `hang_nang`, với hai mức phút làm lại (9 và 15,3).
- Điền A1–B4 vào `report/team/bang_chi_phi.md`. Mọi số lấy từ cột `_simulated` đều có nhãn `simulated`.

## 4. Bằng chứng

- Commit nhiệm vụ A: `f1992ed` (đã merge vào `main` qua `4f086b4`).
- Nhiệm vụ B: [điền hash commit sau khi commit].
- Output của `python lab13.py` (phần A1, A2, A3, A4, B1, B2, B3, B4) khớp với đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Số chính để đối chiếu:
  - Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn.
  - Giới hạn 2 lần chạy rẻ nhất cho công ty: 6.901.220 đ [simulated].
  - Xem lại 100%: 0,98× đến 1,03× so với 12.000 đ [simulated].
- Các điểm lệch nhỏ đã ghi chú: B4 với 15,3 phút làm lại ra 12.415 đ, còn hướng dẫn ghi 12.414 đ (chênh 1 đ, do làm tròn). Câu B3 có hai mốc so sánh (85 yêu cầu so với 2 lần, 97 so với 3 lần), đã ghi rõ mốc.

## 5. Công cụ AI đã dùng

- **Claude Code** (các model Claude trong phiên làm việc). Dùng để:
  - Đọc tài liệu và tổng hợp kế hoạch.
  - Viết code `lab13.py` cho A và B.
  - Soạn các bảng trong `bang_chi_phi.md` và viết phần này.
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py` và đối chiếu từng số với hướng dẫn, lệch không quá 2%.
  - Kiểm tra cặp "giảm một nửa" bằng nửa mức tăng của "gấp đôi".
  - Tự tính tay một số để đối chiếu với code. Ví dụ: chi phí mỗi việc thành công = (token + tool + xem lại + làm lại) ÷ 978, cho ra 4.472 đ.
  - Kiểm tra bằng `grep` rằng không có từ "production" trong `report/team`.

## 6. Tự đánh giá

**Làm tốt:**

- Nhiệm vụ A đã merge vào `main`. Số A2 khớp với phép tính tay của Khương Hoàng Nguyên (tổng 4.373.585 đ, 978 việc thành công, 4.472 đ mỗi việc). Chạy lại `lab13.py` hôm nay cho cùng kết quả, A2 đạt sai số dưới 2%.
- Các số B1–B4 khớp với hướng dẫn: 4.237 đ (giới hạn 2 lần), 6.901.220 đ (rẻ nhất cho công ty), 11.743 đ và 12.414 đ (xem lại 100%).
- Mỗi cặp "gấp đôi / giảm một nửa" được kiểm tra bằng cách so với nửa mức tăng. Số lệch 1 đ ở B4 (12.415 so với 12.414) đã ghi chú là do làm tròn.
- Mọi số lấy từ cột mô phỏng đều có nhãn `[simulated]`.

**Còn thiếu:**

- Nhiệm vụ B vẫn ở nhánh `minh` (commit `e322432`), chưa merge. Mục 4 còn placeholder "[điền hash commit sau khi commit]", cần điền `e322432`.
- `lab13.py` sẽ có lỗi `UnicodeEncodeError` khi chạy trên console Windows mặc định (cp1252). Phải đặt `PYTHONIOENCODING=utf-8` thì máy chấm mới có thể tránh được lỗi tương tự.
- Email ở mục 1 vẫn là "[điền]".

**Rút kinh nghiệm:**

- Đối chiếu từng nhóm số với hướng dẫn ngay sau khi chạy, không dồn lại cuối.
- Script có in tiếng Việt thì nên đặt encoding UTF-8 ngay từ đầu, để chạy được trên mọi máy.
