# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: GroupN · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ ở 45.000 yêu cầu/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8% · xem lại ×2: +40,7% · lương +25%: +23,1% [simulated]; giá token ×2 chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]; quoc_te 1,88×, doi_tac 0,85× nên loại khỏi phạm vi; xem lại 100% thì 0,98–1,03× [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (3,97% trong phạm vi); 10 event có trace_id | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại PAIR; bảng khắc phục 5 ca, mỗi ca có ngưỡng phát hiện; hai bộ nhãn độc lập chưa gắn | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, mde 6 điểm, 859/nhóm, m ≥ 299, DE 6,96; power chỉ 0,64 nếu tác động thật là 5 điểm; 3 luật dừng; quyết định 2027-01-11 | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ · xem lại 100% → 12.415 đ = 1,03× · khối lượng còn nửa → +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang, chia theo nhân viên 20 + 20, bắt đầu 2026-12-07. Không mở cho quoc_te và doi_tac.

- Sửa khoá chống trùng (ca 20) và chỉ báo "đã hoàn" khi sổ cái trả `ok` (ca 7), kiểm thử với 0 ca lệch · Kỹ sư trưởng agent · kiểm tra 2026-12-04.
- Ký chấp nhận mde 6 điểm, biết power chỉ 0,64 nếu tác động thật là 5 điểm · Giám đốc vận hành LogiX-VN · kiểm tra 2026-12-04.
- Bật đủ 10 event có trace_id; thay phút simulated bằng phút đo thật từ `staff_review_decision` sau tuần 1 · PM trợ lý hoàn phí · kiểm tra 2026-12-14.
- Giảm xem lại theo bậc vì xem lại 100% tốn 1,03× (đắt hơn nhân viên tự làm) [simulated]; cuối bước 0.25 phải còn ≤ 50% yêu cầu được xem lại · Trưởng nhóm CSKH · kiểm tra 2026-12-21.
