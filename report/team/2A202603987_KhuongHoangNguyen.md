# Báo cáo cá nhân — Khương Hoàng Nguyên - 2A202603987

## 1. Thông tin thành viên

- Họ tên: Khương Hoàng Nguyên
- MSSV: 2A202603987
- Email: (cập nhật nếu cần)
- GitHub: `NguyenGL03`
- Vai trong nhóm: Người kiểm số (Nhiệm vụ D & tính tay đối chiếu A2)

## 2. Phần việc phụ trách

- Tính tay đối chiếu chỉ số chi phí mỗi việc thành công ở Nhiệm vụ A2.
- Viết phần code cỡ mẫu D1 tại `TODO CP4` trong `src/lab13.py` (sau khi PR phần A được merge).
- Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (D1, D2, đánh đổi, ngưỡng an toàn, 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, và các trường còn dấu `?`).

## 3. Đóng góp cụ thể

### Tính tay đối chiếu A2
Từ dữ liệu `src/logix_runs.csv` (1.624 lần chạy) và `src/logix_requests.csv` (1.200 yêu cầu), áp dụng bảng giá giả định (`26 đ / 1.000 token vào`, `130 đ / 1.000 token ra`, `15 đ / lần gọi tool`, `2.000 đ / phút nhân viên`):

- Token (mọi lần chạy, kể cả lần lỗi): `245.585,13 đ` (đo từ trace)
- Tool (5.600 lần gọi $\times$ 15 đ): `84.000 đ` (đo từ trace)
- Xem lại (890 phút $\times$ 2.000 đ): `1.780.000 đ` [simulated]
- Làm lại (1.132 phút $\times$ 2.000 đ): `2.264.000 đ` [simulated]
- Tổng chi phí: `245.585,13 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585,13 đ` (có phần simulated)
- Số việc thành công (`ket_qua == 'thanh_cong'`): `978` yêu cầu
- **Chi phí mỗi việc thành công:** `4.373.585,13 / 978 = 4.471,97 đ` ($\approx$ **4.472 đ** [simulated])

### Đối chiếu A2 với bài làm của MinhNGD76
- Đã pull bản merge Nhiệm vụ A từ `main` (commit `4f086b4`) và đối chiếu [bang_chi_phi.md](bang_chi_phi.md) với phần tính tay:
  - Token `245.585 đ`, Tool `84.000 đ`, Xem lại `1.780.000 đ` [simulated], Làm lại `2.264.000 đ` [simulated], Tổng `4.373.585 đ`, Số việc thành công `978`, Chi phí mỗi việc thành công `4.472 đ` [simulated]. Kết quả khớp 100% (sai số 0%).

### Nhiệm vụ D (`src/lab13.py` và `report/team/pilot_plan.yaml`)
- Bổ sung code tính 5 câu D1 và tỉ lệ `mo_lai_trong_7_ngay` hiện tại vào `src/lab13.py` (phần CP4).
- Tính 5 câu D1: chia theo yêu cầu cần `1.251` yêu cầu/nhóm; chia theo nhân viên ($m=75$) cần `3.103` yêu cầu/nhóm (42 người/nhóm, vượt quá 40 nhân viên hiện có); giới hạn 20 nhân viên/nhóm chỉ đạt tối đa `1.000` hiệu dụng; giới hạn 6 depot/nhóm đạt tối đa `300`; chấp nhận mức chênh 6 điểm (`859`/nhóm) với 20 nhân viên/nhóm cần $m \ge 299$ yêu cầu/người ($\text{DE} = 6,96$).
- Hoàn thiện 5 câu kiểm tra D2 ("tách được tác động"), tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu; `3,97%` trong phạm vi `noi_dia` + `hang_nang`), và điền đầy đủ các trường cùng 3 luật dừng đủ 4 vế trong `report/team/pilot_plan.yaml`.

## 4. Bằng chứng

- Nhánh làm việc: `nguyen/pilot_plan`.
- File đã hoàn thiện: `src/lab13.py` (phần D1), `report/team/pilot_plan.yaml` (không còn dấu `?` ngoài dòng chú thích, đã kiểm tra đọc bằng `yaml.safe_load`).
- Đã kiểm tra cú pháp `src/lab13.py` (`py_compile`) và đối chiếu số liệu A2, D1 trực tiếp từ CSV.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Antigravity) để rà soát yêu cầu bài lab, đối chiếu công thức D1 và kiểm tra cú pháp YAML.
- Cách tự kiểm tra: tự chạy script Python đọc trực tiếp `src/logix_runs.csv` và `src/logix_requests.csv` để xác nhận toàn bộ các con số A2, A3, D1 và tỉ lệ `mo_lai_trong_7_ngay`; chạy `yaml.safe_load` để kiểm tra tính hợp lệ của `report/team/pilot_plan.yaml`, kiểm tra không còn dấu `?` ngoài chú thích và không có từ cấm.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các phần việc không phụ thuộc (đối chiếu A2, hoàn thiện `report/team/pilot_plan.yaml`, lập báo cáo cá nhân).
- Sẵn sàng `git pull` phần A ngay khi được merge để bổ sung nốt code D1 vào `src/lab13.py` và mở PR hoàn chỉnh.
