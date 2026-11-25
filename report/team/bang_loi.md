# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

<<<<<<< HEAD
Người gắn nhãn 1: NMCcg · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |
=======
Người gắn nhãn 1: NMCcg · Người gắn nhãn 2: Bùi Đức Tuấn (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Giới hạn hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |
>>>>>>> 7ee9d841a0cbc52f0db726ed01c026f69261f89a

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 17 (người 1: Ngầm, người 2: Giới hạn hệ thống) → chốt **Ngầm**. Bảng giá mới đã có nên trợ lý làm được nhưng làm sai, và 212 đơn lệch không ai nhận ra cho tới khi kiểm tra. Quy tắc: Giới hạn hệ thống là không thể làm được và lộ ra ngay; sai mà không khách nào, cảnh báo nào nhận ra là Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_bank_rejected` (ngân hàng trả lỗi sai số tài khoản) theo ngày; cảnh báo khi vượt 1% số lệnh hoàn | Kiểm tra độ dài và checksum số tài khoản trước khi tạo lệnh, hỏi khách nhập lại; ưu tiên hoàn về ví đã xác minh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin "đã hoàn" không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả `ok`; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do "sai số tiền" mà kiểm tra lại thấy đúng, theo tuần; ngưỡng 1% số yêu cầu | Mẫu tin nhắn luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ, theo mục giao trễ 24–48 giờ" | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = ngoai_12_thang`, đếm theo tuần và theo loại | Giữ cách chuyển nhân viên kèm tóm tắt; nói rõ giới hạn 12 tháng ngay câu đầu | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn mỗi tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch tiền | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace để đối soát | Kế toán trưởng |
