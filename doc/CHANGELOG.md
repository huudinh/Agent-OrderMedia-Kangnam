# CHANGELOG

---

## v1.0 — 2026-10-27

Bản đầu. Dựng từ sáu nguồn tri thức thật của khối Ads/Content Kangnam + tri thức sản xuất media có sẵn trong project.

### Dựng mới

| Thành phần | Nội dung |
|---|---|
| `SYSTEM-PROMPT.md` | Bộ não brand-neutral, 15 mục. Quy trình 7 bước, hai cổng chặn, chế độ AUTO |
| `SYSTEM-PROMPT-NGAN.md` | Bản nén **6.072 ký tự** cho ChatGPT Custom GPT *(giới hạn 8.000)* |
| `knowledge/om-A` … `om-H` | 8 sổ tri thức, ~100 KB |
| `prompts/` | 6 prompt mẫu theo bước |
| `tools/om.py` | Đọc order CSV/XLSX/Google Sheet → chuẩn hoá → cổng A → điền ô suy ra → chấm hook & soát pháp chế sơ bộ |
| `tools/gop-tham-khao.py` | Gộp 8 sổ thành `goi/GOP-tri-thuc.md` |

### Nguồn tri thức đã nạp

| Nguồn | Vào sổ |
|---|---|
| Sheet 1 · Chân dung khách hàng mũi (6 tệp CD1–CD6) | `om-C` §1 |
| Sheet 2 · Hành trình 5A × 6 tệp — ma trận thông điệp | `om-C` §3 |
| Sheet 3 · Ngân hàng hook (**91 ad đã chấm TỐT/BT/KÉM**) | ★ `om-C` §5 |
| Sheet 4 · Format mẫu L01–L12 | `om-D` §1 |
| Sheet 5 · Kế hoạch Ads — ma trận 5A × VIEW/PERF + kho tệp | `om-F` |
| Sheet 7 · Pilot nội dung Ads mũi — 2 sprint | `om-C` §4 · `om-F` §6 |
| Website Kangnam — chi nhánh, chuyên khoa, giới thiệu | `om-H` §1–3 |
| `Agent-Media/knowledge/media-production.md` | `om-D` §5–6 · `om-E` §5 · `om-G` §1 |

### Quyết định thiết kế đáng ghi lại

**① Nguyên tắc tối thượng rút từ dữ liệu, không từ lý thuyết**
*"Hook kể TÌNH TRẠNG thì khách nhận ra mình. Hook kể TÍNH TỪ thì khách lướt qua."*
Đối chiếu 91 ad đã chấm: hook gọi tình trạng (*"mũi thấp tẹt, đầu mũi hếch"*) chấm TỐT; hook dùng tính từ (*"vạn người mê"*, *"SLAY nét căng"*) chấm KÉM — không có ngoại lệ trong bộ dữ liệu.

**② Thành phần ① là CỔNG, không phải "một trong bốn"**
Bản nháp đầu chấm `✓` khi hook có ≥2 trong 4 thành phần. Chạy thử trên order thật: 16/22 dòng bị chấm `⚠`, trong đó có những hook thực tế đã chấm **TỐT** *(vd "Mũi từng nâng nhưng không đẹp thì bao lâu sửa lại được?"* — chỉ có ① mà TỐT*)*.
→ Sửa luật: **có ① dù một mình → `✓`**. Sau sửa: 14 `✓` · 3 `⚠` · 5 `✗`, khớp cảm nhận thực tế.

**③ Format của ô camp là ƯU TIÊN, không phải danh sách đóng**
Bản nháp đầu chặn mọi format ngoài danh sách của ô → 14/22 dòng bị gắn cờ, quá ồn. Dữ liệu thật cho thấy `L01` chạy ở `P2`/`P3` vẫn chấm TỐT dù không nằm trong danh sách ưu tiên.
→ Hạ từ **chặn** xuống **ghi chú**: agent nêu ra, không tự đổi format của người order.

**④ Module đơn vị tách riêng (`om-H`)**
Mọi dữ kiện Kangnam — chi nhánh, giấy phép, bảng giá, trạng thái xác minh bác sĩ — dồn vào một file. Đổi đơn vị hoặc mở dịch vụ mới chỉ thay `om-H`, không sửa bộ não.

**⑤ Chân dung dùng chung mã CD1–CD6 cho mọi dịch vụ**
Không đẻ mã mới cho mắt/hàm/da. `CD1` khuyết điểm cơ bản · `CD2` nghề hình ảnh · `CD3` đã làm cần sửa · `CD4` nam giới · `CD5` phong thuỷ · `CD6` ca khó/bệnh lý. Giữ mã chung để **so sánh hiệu suất chéo tuyến** — cùng lý do thư viện format giữ `L01`–`L16`.

### ⚠️ Lỗ hổng dữ liệu phát hiện khi dựng

| Phát hiện | Ảnh hưởng |
|---|---|
| **Format `L13` `L14` `L15` được dùng trong kế hoạch Ads (sheet 5) nhưng thư viện Format chỉ định nghĩa tới `L12`** | Các ô `V3`/`P3`/`V4`/`P4`/`V5` trỏ tới format không tồn tại → agent gắn cờ, hỏi lại |
| **Chính sách bảo hành xuất hiện hai mức khác nhau** trong cùng bộ dữ liệu: *"trọn đời"* và *"10 năm"* | Chắc chắn một cái sai → `om-H` §6 chặn mọi phiếu nói về bảo hành |
| **Chưa có bác sĩ mũi nào được xác minh** | 🔴 Chặn mọi phiếu có tên bác sĩ; nhiều ad đang chạy đã bị gắn cờ vì lý do này |
| **Chỉ có số giấy phép của 2/7 cơ sở** (HN `194/BYT-GPHĐ` · SG `287/BYT-GPHĐ`) | Chặn phiếu local `L12` của 5 cơ sở còn lại — số giấy phép là thông tin **bắt buộc** trong QC dịch vụ KCB |
| **Giá *"31TR"* lưu hành rộng trong ad cũ nhưng chưa đối chiếu bảng giá hiện hành** | `om-H` §6: hook cũ **không phải nguồn giá** |
| **Cả hàng `A5 · ADVOCATE` trống hoàn toàn** (0/6 chân dung) | Không nuôi khách đã làm → mất toàn bộ cross-sell. Lỗ hổng rẻ nhất để lấp |
| **`CD1` chiếm 27/34 content đang giữ** | Phễu dựa gần như toàn bộ vào một chân dung — rủi ro tập trung |

### Kiểm thử

Chạy `tools/om.py` trên file order thật *(22 dòng, sheet `gid=0`)*:

```
DOC DUOC : 22 dong · BO QUA: 1 dong
CONG A — CHAN                : 0
B4 SOI HOOK                  : 14 ✓ · 3 ⚠ · 5 ✗
B6 PHAP CHE                  : 4 🔴 · 0 🟡 · 18 🟢
CAN CONSENT                  : 9 phieu
```

Bốn cờ 🔴 đều là vi phạm thật trong order: *"đẹp ngay sau 60 phút"* ×2 *(cam kết kết quả)* · *"Cam kết bảo hành"* · *"bác sĩ Chí"* *(tên BS chưa xác minh)*.

---

## Dự kiến v1.1

- [ ] Mở các chặn khi được cấp 5 thứ ở `om-H` §8
- [ ] Bổ sung `om-C` cho chuyên khoa **mắt** *(order đã có dòng mắt: sụp mí, lão hoá, khuyết điểm)*
- [ ] Định nghĩa `L13`–`L16` sau khi Content Lead chốt
- [ ] Thay ngưỡng giả định ở `om-F` §3 bằng số thật 3 tháng
- [ ] Thêm `tools/call-sheet.py` — gom phiếu thành call sheet, tính giờ và số lần đổi set
- [ ] Nối ngược với `Agent-AdsReport-Kangnam` để tự nạp cột `HIỆU QUẢ` sau mỗi kỳ
