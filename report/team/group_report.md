# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: GroupN
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra quyết định.

Nhóm chia theo bốn vai của lab, mỗi người một nhánh và một Pull Request vào `main`; nhóm trưởng review số trước khi merge. Thứ tự: A mở PR sớm để D và E có số dùng; hai người gắn nhãn C làm riêng rồi mới so.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A | `mo_hinh()` tính token và tool trên mọi lần chạy, chia cho số việc thành công; tách theo loại; cộng chi phí cố định 40 triệu/tháng | `src/lab13.py`, `bang_chi_phi.md` |
| B | Gọi lại `mo_hinh()` với một tham số đã đổi cho 9 kịch bản, một cặp, giới hạn 1/2/3 lần chạy, xem lại 100% | `bang_chi_phi.md` |
| C | Hai người gắn nhãn 20 ca độc lập, so nhãn, chốt ca lệch, chọn 5 ca cho bảng khắc phục | `bang_loi.md` |
| D | Tính cỡ mẫu cho ba cách chia, chọn chia theo nhân viên 20 + 20, mde 6 điểm, 3 luật dừng | `pilot_plan.yaml` |
| E | Ba chỉ số tính thử, 11 event có `trace_id`, rủi ro kinh tế từ bảng độ nhạy, hồ sơ bảy mục | `chi_so.md`, `ho_so_launch_v0.md` |

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token chia số yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí [simulated].
- Phạm vi pilot noi_dia + hang_nang: **0,38×** so với nhân viên tự làm, đã cộng chi phí cố định [simulated]. Loại quoc_te (1,88×) và doi_tac (0,85×).
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated]; giá token gấp đôi chỉ +5,6%.
- Gắn nhãn lỗi: đồng thuận **19/20 = 95%**; ca 17 lệch, chốt Ngầm.
- Pilot: 859 yêu cầu mỗi nhóm, mỗi nhân viên ≥ 299 yêu cầu, DE 6,96; power **0,64** nếu tác động thật chỉ 5 điểm.
- Đề xuất cuối: **Go có điều kiện**, với bốn điều kiện có người phụ trách và ngày kiểm tra.
- Buổi lab không tổ chức duyệt chéo Gate 2a, nên nhóm không có kết quả hội đồng và không có phiếu chấm nhóm khác.

### Những điều nhóm tìm ra trong quá trình làm

Rà lại dữ liệu sau khi xong các nhiệm vụ, nhóm thấy sáu điểm mà đáp án và hồ sơ chưa xử lý hết:

1. **Tính trùng chi phí làm lại khi so với nhân viên.** Công thức "cả hệ thống" cộng 12.000 đ cho 222 ca không thành công, trong đó 74 ca `lam_lai` đã có phút làm lại trong tổng chi phí. Tính không trùng: **5.125 đ = 0,43×** thay vì 0,49× [simulated]. Ở B3, giới hạn 2 lần vẫn rẻ nhất (6,09 triệu so với 6,15 triệu ở 3 lần) [simulated], nên kết luận không đổi.
2. **Chỉ số an toàn không thấy lỗi hoàn thừa tiền.** Khách được hoàn thừa thì không mở lại (ca 5, ca 17). Trong 177 yêu cầu được xem lại, nhân viên sửa hoặc bỏ 27%, trong khi tỉ lệ mở lại chỉ 4,25%. Cần dựa thêm vào kiểm tra mẫu hằng tuần.
3. **hang_nang đã vượt trần an toàn.** Tỉ lệ mở lại theo loại: noi_dia 3,2%, **hang_nang 8,2%**, cao hơn trần 6% trong luật dừng; số gộp trong phạm vi (3,97%) che mất điều này.
4. **Xem lại đang giữ an toàn.** Yêu cầu được xem lại có tỉ lệ mở lại 0%, không được xem lại là 5,0%. Giảm xem lại để tiết kiệm (B4) phải làm theo rủi ro: xem lại hết hang_nang và đơn số tiền lớn, chỉ lấy mẫu noi_dia.
5. **Ca chuyển nhân viên không bao giờ đóng trong 24 giờ.** Cả 148 ca `chuyen_nhan_vien` có `dong_trong_24h = 0`. Chạy đủ 3 lần rồi mới chuyển làm khách chờ lâu hơn; giới hạn 2 lần vừa rẻ hơn vừa chuyển sớm hơn.
6. **Baseline 0,70 có thể không đúng cho phạm vi đã thu hẹp.** Chỉ số chính trong phạm vi ở đợt chạy thử là 92,3%. Nếu baseline thật trong phạm vi là 0,85, chỉ cần 686 yêu cầu mỗi nhóm cho mức chênh 5 điểm (107 yêu cầu mỗi nhân viên). Pilot nên đo baseline ở hai bước đầu rồi tính lại cỡ mẫu.

Thêm một con số về rủi ro tiền: mỗi yêu cầu trong phạm vi tiết kiệm khoảng 7.369 đ [simulated], còn một lần hoàn thừa nguyên khoản trung bình là 412.000 đ, bằng tiền tiết kiệm của 56 yêu cầu.

## 5. Khó khăn và cách xử lý

- **Cài thư viện trên Windows.** `import numpy` báo `ImportError: DLL load failed while importing _mt19937: An Application Control policy has blocked this file.` (Smart App Control chặn bản numpy mới). Xử lý: cài `numpy==2.2.6`, `scipy==1.15.3` trong `src/.venv`, sau đó `python -c "import pandas, numpy, scipy, statsmodels"` chạy được.
- **In tiếng Việt ra terminal Windows.** Đặt `PYTHONIOENCODING=utf-8` trước khi chạy `python lab13.py`.
- **Xung đột code giữa B và D.** Hai người cùng viết ngay sau dòng `TODO CP2` trong `src/lab13.py`. Giữ cả hai khối, chạy lại để xác nhận số B và D khớp đáp án rồi mới merge.
- **File đặt sai chỗ.** Bộ nhãn người 1 và bản PDF đề bài nằm ở thư mục gốc; đã chép nhãn vào `bang_loi.md` và xoá hai file thừa.
- **Lệch số giữa các file.** Ngày quyết định trong hồ sơ (2027-01-11) khác `pilot_plan.yaml` (2027-01-05); đã sửa hồ sơ theo `pilot_plan.yaml`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Số phút xem lại và làm lại là giả lập; mọi kết luận về chi phí phải đo lại bằng phút thật sau tuần 1 của pilot.
- ICC 0,02 là giả định của đề. Dữ liệu chạy thử chỉ có 20 nhân viên ở 6 depot, không có đối chứng, nên chưa kiểm được.
- Pilot chạy qua 12.12 và cuối năm, lượng đơn và tỉ trọng loại yêu cầu khác ngày thường; kết quả có thể không đại diện.
- Việc nên làm tiếp: thêm luật dừng cho lỗi hoàn thừa tiền, trần an toàn riêng cho hang_nang, và tách luật dừng tức thời (hoàn trùng, đối soát sổ cái) khỏi luật dựa trên tỉ lệ mở lại 7 ngày.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` của đề bài
