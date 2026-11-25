# Team

## Thông tin nhóm

- Tên nhóm: GroupN
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-GroupN-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/buiductuan2884-max/K5-L3B-DAY13-GroupN-LaunchEconomics · `main` · commit cuối trên `main` trước 23h59 ngày lab

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Bùi Đức Tuấn | 2A2020603902 | buiductuan2884@gmail.com | buiductuan2884-max | Người gắn nhãn 2, kiêm giữ hồ sơ (nhóm trưởng) |
|   2 | Nguyễn Đình Minh | 2A202603898 | | MinhNGD76 | Người viết code |
|   3 | Khương Hoàng Nguyên | 2A202603987 | 26ai.nguyenkh@vinuni.edu.vn | NguyenGL03 | Người kiểm số |
|   4 | | | | NMCcg | Người gắn nhãn 1 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## BuiDucTuan-2A2020603902

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ; nhóm trưởng: tạo repo, chia việc, review và merge PR.

### Đóng góp cụ thể

- `PHAN_CONG.md`: phân bốn vai, file phụ trách và thứ tự phụ thuộc.
- Gắn nhãn 20 ca độc lập; cùng NMCcg chốt ca 17 (đồng thuận 19/20 = 95%).
- `chi_so.md` (3 chỉ số tính thử, 2 chỉ số tự đề xuất, 11 event, 3 dòng rủi ro), `ho_so_launch_v0.md` (7 mục, Go có điều kiện), `TEAM.md`.
- Review số A, B, D trước khi merge PR #1–#4.

### Bằng chứng

- Commit `2c4121c`, `48f7458`, `a3c4acf`; báo cáo `report/team/2A2020603902_BuiDucTuan.md`.

## NguyenDinhMinh-2A202603898

### Phần việc phụ trách

- Người viết code: `src/lab13.py` phần A, B; `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- A1–A4: ba phép thử ĐẠT; chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token; tách theo loại; cộng chi phí cố định.
- B1–B4: bảng độ nhạy 9 kịch bản, cặp token + xem lại, giới hạn 1/2/3 lần, xem lại 100% (11.743 đ = 0,98×; 12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated].

### Bằng chứng

- PR #1 (https://github.com/buiductuan2884-max/K5-L3B-DAY13-GroupN-LaunchEconomics/pull/1), PR #4 (https://github.com/buiductuan2884-max/K5-L3B-DAY13-GroupN-LaunchEconomics/pull/4); báo cáo `report/team/2A202603898_NguyenDinhMinh.md`.

## KhuongHoangNguyen-2A202603987

### Phần việc phụ trách

- Người kiểm số: tính tay đối chiếu A2; `src/lab13.py` phần D1; `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Tính tay A2 ra 4.472 đ [simulated], khớp code của MinhNGD76.
- D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299), D2, tỉ lệ mở lại hiện tại 4,25%; `pilot_plan.yaml` chia theo nhân viên 20 + 20, mde 0,06, 3 luật dừng.

### Bằng chứng

- PR #3 (https://github.com/buiductuan2884-max/K5-L3B-DAY13-GroupN-LaunchEconomics/pull/3); báo cáo `report/team/2A202603987_KhuongHoangNguyen.md`.

## NMCcg

### Phần việc phụ trách

- Người gắn nhãn 1: nhiệm vụ C; `report/team/phieu_cham.md` (duyệt chéo).

### Đóng góp cụ thể

- Gắn nhãn 20 ca độc lập (bộ nhãn người 1 trong `report/team/bang_loi.md`); cùng Bùi Đức Tuấn chốt ca 17.

### Bằng chứng

- PR #2 (https://github.com/buiductuan2884-max/K5-L3B-DAY13-GroupN-LaunchEconomics/pull/2).
