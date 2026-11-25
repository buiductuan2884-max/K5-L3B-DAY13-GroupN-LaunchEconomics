"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
KHOI_LUONG_THANG = 45000      # yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
CHI_PHI_CO_DINH = 40_000_000  # đồng mỗi tháng (vận hành, giám sát, cập nhật chính sách)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn, yêu cầu vượt coi là chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def kiem_tra_a2(kq):
    """Đối chiếu A2 với số trên slide chữa, lệch không quá 2%."""
    mau = dict(token=245585, tool=84000, chay_lai=93804, xem_lai=1780000,
               lam_lai=2264000, tong=4373585, thanh_cong=978, cps=4472)
    for ten, gia_tri in mau.items():
        assert abs(kq[ten] / gia_tri - 1) <= 0.02, f'A2 lệch quá 2% ở {ten}: {kq[ten]:,.0f} so với {gia_tri:,}'
    print('A2 khớp đáp án (lệch ≤ 2%): ĐẠT')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps là simulated)')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    kiem_tra_a2(ket_qua)
    print(f"cps / hoá đơn mỗi yêu cầu = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for ten in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"Tỉ trọng {ten:8s} {ket_qua[ten] / ket_qua['tong'] * 100:5.1f}%")
    he_thong = (ket_qua['tong'] + (len(reqs) - ket_qua['thanh_cong']) * BASELINE) / len(reqs)
    print(f'Cả hệ thống mỗi yêu cầu (cộng {BASELINE:,} đ cho ca không thành công) = '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')

    # Nhiệm vụ A3: tách theo loại yêu cầu
    print('\nA3 · Theo loại      n  thành công  lần chạy/yc   cps [sim]  so với 12.000')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        con = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, con)
        lan_chay = runs['request_id'].isin(con['request_id']).sum() / len(con)
        print(f"{loai:12s} {len(con):6d} {kq['thanh_cong'] / len(con):10.1%} {lan_chay:12.2f} "
              f"{kq['cps']:11,.0f} {kq['cps'] / BASELINE:10.2f}×")
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('Tỉ lệ ok theo lần thử:\n' + (ok_theo_lan * 100).round(1).to_string())

    # Nhiệm vụ A4: cộng chi phí cố định cho phạm vi pilot noi_dia + hang_nang
    pham_vi = mo_hinh(runs, reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])])
    viec_thang = KHOI_LUONG_THANG * pham_vi['thanh_cong'] / len(reqs)
    print(f"\nA4 · Phạm vi noi_dia + hang_nang: {pham_vi['thanh_cong']} việc thành công, "
          f"cps {pham_vi['cps']:,.0f} đ [simulated]")
    for nhan, viec in [('45.000 yc/tháng', viec_thang), ('Một nửa khối lượng', viec_thang / 2)]:
        co_dinh = CHI_PHI_CO_DINH / viec
        tong_viec = pham_vi['cps'] + co_dinh
        print(f'{nhan:20s} {viec:8,.0f} việc/tháng  cố định {co_dinh:6,.0f} đ/việc  '
              f'cộng cố định {tong_viec:6,.0f} đ = {tong_viec / BASELINE:.2f}× [simulated]')
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.

    # Nhiệm vụ D · Cỡ mẫu và kiểm tra ngưỡng an toàn (CP4)
    from statistics import NormalDist
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        _co_statsmodels = True
    except ImportError:
        _co_statsmodels = False

    def co_mau(p1, p2, alpha=0.05, power=0.80):
        """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ p1, p2."""
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    p1, icc = 0.70, 0.02
    n_5pt = co_mau(p1, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_nv_75 = math.ceil(n_5pt * de_75)
    max_20nv = 20 / icc
    max_6depot = 6 / icc
    n_6pt = co_mau(p1, 0.76)
    m_min_6pt = math.ceil(n_6pt * (1 - icc) / (20 - n_6pt * icc))
    de_6pt = 1 + (m_min_6pt - 1) * icc

    print('\nD1 · Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,80; ICC 0,02)')
    print(f'a) Theo yêu cầu (+5 điểm):          {n_5pt:,} yêu cầu/nhóm')
    print(f'b) Theo nhân viên (m=75, DE={de_75:.2f}): {n_nv_75:,} yêu cầu/nhóm (~{math.ceil(n_nv_75 / 75)} nhân viên/nhóm > 40)')
    print(f'c) Tối đa với 20 nhân viên/nhóm:    {max_20nv:,.0f} hiệu dụng (< {n_5pt:,}: không đạt)')
    print(f'd) Tối đa với 6 depot/nhóm:         {max_6depot:,.0f} hiệu dụng (< {n_5pt:,}: không đạt)')
    print(f'e) Mức chênh 6 điểm ({n_6pt}/nhóm), 20 nhân viên/nhóm: cần m >= {m_min_6pt} yêu cầu/người (DE={de_6pt:.2f})')
    if _co_statsmodels:
        pw_5pt = NormalIndPower().power(effect_size=proportion_effectsize(0.75, p1), nobs1=n_6pt, alpha=0.05)
        print(f'   Power thực tế tại n={n_6pt} nếu tác động thật chỉ 5 điểm: {pw_5pt:.2f}')

    mo_lai_all = reqs['mo_lai_trong_7_ngay'].mean()
    pham_vi_d = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai_pv = pham_vi_d['mo_lai_trong_7_ngay'].mean()
    print(f"D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại: toàn mẫu {mo_lai_all:.2%} "
          f"({reqs['mo_lai_trong_7_ngay'].sum()}/{len(reqs)}), "
          f"phạm vi pilot {mo_lai_pv:.2%} ({pham_vi_d['mo_lai_trong_7_ngay'].sum()}/{len(pham_vi_d)})")
