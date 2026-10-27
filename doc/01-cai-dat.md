# ① CÀI ĐẶT

---

## Tên & mô tả — dán sẵn

**Tên agent**
```
Agent-OrderMedia-Kangnam
```

**Mô tả ngắn** *(dán vào ô Description)*
```
Nhận file order nội dung (sheet/excel: hook, CTA, chân dung, nấc 5A) → chấm hook
theo công thức rút từ 91 ad thật đã chấm → xuất phiếu kịch bản sản xuất 42 trường,
call sheet gom theo bối cảnh, và bảng cờ pháp chế kèm câu thay thế.
Dịch order thành phiếu quay được — không sáng tác tự do.
```

---

## Nạp theo nền tảng

### Claude Project *(khuyến nghị)*

| Bước | Việc |
|---|---|
| 1 | Tạo Project mới, đặt tên như trên |
| 2 | Mở [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md), copy **toàn bộ khối giữa hai vạch ▼▲** → dán vào **Custom instructions** |
| 3 | Kéo **10 file** trong [`knowledge/`](../knowledge/) vào phần **Project knowledge** |
| 4 | Kéo thêm **6 file** trong [`prompts/`](../prompts/) |
| 5 | Chạy smoke test (§cuối) |

### ChatGPT Custom GPT

| Bước | Việc |
|---|---|
| 1 | Tạo GPT mới |
| 2 | ⚠️ Ô *Instructions* giới hạn **8.000 ký tự** → dùng [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) *(7.987 ký tự — ⚠️ gần đầy)*, **không** dùng bản đầy đủ |
| 3 | Upload **10 file `knowledge/` + 6 file `prompts/`** vào *Knowledge* |
| 4 | Giới hạn số file → upload **một file** [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md) *(~100 KB)* |

### Gemini Gem

| Bước | Việc |
|---|---|
| 1 | Tạo Gem mới |
| 2 | Dán khối ▼▲ của [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) vào **Chỉ dẫn** |
| 3 | Thêm file vào **Kiến thức** — ưu tiên bản gộp `goi/GOP-tri-thuc.md` |

### Claude Code *(trong repo này)*

Không cần cài gì. Mở thư mục repo rồi gõ:
```
Đọc SYSTEM-PROMPT.md và các sổ knowledge/, rồi ra kịch bản cho order này: <link>
```

---

## Ba thẻ copy bộ não

| Thẻ | File | Khi nào dùng |
|---|---|---|
| **Đầy đủ** | [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) | Claude · Gemini · Claude Code — mặc định |
| **Ngắn** | [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) | ChatGPT Custom GPT *(giới hạn 8.000 ký tự)* |
| **Gộp tri thức** | [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md) | Nền tảng chỉ cho nạp 1–2 file |

⚠️ Bản gộp **sinh tự động**. Sửa `knowledge/` rồi chạy lại:
```bash
python tools/gop-tham-khao.py
```

---

## Mười sáu file tri thức

### `knowledge/` — 10 sổ
```
om-A-vai-tro-quy-trinh.md       vai trò · 7 bước · hai cổng · ★ AUTO
om-B-doc-dau-vao.md             17 cột order · chuẩn hoá · ★ 10 ô suy ra
om-C-tri-thuc-khach-hang.md     chân dung MŨI · 5A · ★ công thức hook thắng/thua
om-D-thu-vien-format.md         format L01–L16 · cấu trúc giây · đạo cụ · batch
om-E-kich-ban-san-xuat.md       4 khối lời thoại · ★ 42 trường đầu ra · call sheet
om-F-to-chuc-ads.md             ô camp · kho tệp · ngưỡng · nhịp vận hành
om-G-phap-che-ranh-gioi.md      ⛔ 12 điểm L · cờ 🟢🟡🔴 · câu thay thế
om-H-dich-vu-kangnam.md         module đơn vị — đổi đơn vị chỉ thay file này
om-I-khuon-kich-ban-nha.md      ★ khuôn kịch bản thật — ĐỌC TRƯỚC om-E
om-J-chan-dung-mat.md           chân dung MẮT — ⚠️ đọc §0, phần lớn là suy ra
```

### `prompts/` — 6 prompt
```
prompt-auto.md             ★ một câu là đủ
prompt-doc-order.md        kiểm order (B1–B3)
prompt-soi-hook.md         chấm hook, viết hook mới (B4)
prompt-ra-kich-ban.md      lời thoại, shot list, call sheet (B5)
prompt-soat-phap-che.md    cổng B — chạy độc lập được (B6)
prompt-lap-lo-hong.md      ma trận lỗ hổng phễu
```

---

## Script tiền xử lý *(tuỳ chọn, nhưng nên dùng)*

Yêu cầu: **Python 3.9+**. Đọc `.xlsx` cần thêm:
```bash
pip install openpyxl
```

```bash
# từ file
python tools/om.py order.xlsx --sheet "KẾ HOẠCH SẢN XUẤT"

# từ Google Sheet (tab phải ở chế độ xem được bằng link)
python tools/om.py --sheet-id 1qMdt0gm... --gid 0
```

Script làm **B1–B3** rồi ghi ra `out/phieu-kich-ban.csv` với các ô suy ra đã điền sẵn, cộng chấm hook và soát pháp chế **sơ bộ**. Đưa file đó cho agent để chạy **B4–B7**.

⚠️ Script chấm **sơ bộ bằng từ khoá** — agent vẫn phải soi lại. Script bắt được *"đẹp ngay"*, không bắt được *"kết quả thấy liền sau một tiếng"*.

---

## ⛔ Trước khi dùng thật — đọc mục này

Agent có **sáu chặn đang mở**, in ra mỗi lần xuất phiếu. Mang danh sách này đi họp trước khi chạy order thật:

| # | Cần xin | Ai cấp |
|---|---|---|
| 🔴 ① | **Chính sách bảo hành bằng văn bản** — ⚠️ **cấp bách nhất**, ba mức đang cùng chạy: *3 năm* / *10 năm* / *trọn đời* | Pháp chế |
| 🔴 ② | Danh sách **bác sĩ đã xác minh** — tên · số CCHN · phạm vi chuyên môn · cơ sở hành nghề · văn bản đồng ý dùng hình ảnh | Vận hành + pháp chế |
| 🔴 ③ | **Bảng giá hiện hành các dịch vụ ngoài mắt** *(mắt đã có số nháp)* | Vận hành / sales |
| 🔴 ④ | **Số giấy phép hoạt động đủ 7 cơ sở** (hiện chỉ có 2) | Pháp chế |
| 🟡 ⑤ | **Định nghĩa format `L13` `L14` `L15` `L16`** | Content Lead |
| 🟡 ⑥ | **Kịch bản mẫu cho `L01`** — ô link trong mục lục đang trống | Content Lead |

Chi tiết: [`knowledge/om-H-dich-vu-kangnam.md`](../knowledge/om-H-dich-vu-kangnam.md) §8.

---

## Smoke test — 12 câu

Chạy lần lượt. Agent trả **sai** câu nào thì tri thức chưa nạp đủ.

| # | Hỏi | Phải trả |
|---|---|---|
| 1 | *"Order ghi nấc A1, camp đích PER. Chạy được không?"* | ⛔ **Không** — A1 + PERF không chạy; đề xuất đổi sang `V1` hoặc đẩy nấc lên `A2` |
| 2 | *"Hook 'Sở hữu dáng mũi SLAY nét căng' chấm thế nào?"* | `✗ ĐỔI HOOK` — trúng `H1` tính từ chung chung, dẫn chứng ad cũ chấm KÉM |
| 3 | *"Hook 'Mũi từng nâng nhưng không đẹp thì bao lâu sửa lại được?'"* | `✓ QUAY ĐƯỢC` — có thành phần ① gọi tình trạng; ① một mình là đủ |
| 4 | *"Viết kịch bản có bác sĩ Harvey Nguyễn phân tích ca mũi hỏng."* | 🔴 **ĐỎ** — chưa có BS mũi xác minh (`om-H` §4); viết *"bác sĩ chuyên khoa"*, không nêu tên |
| 5 | *"Chân dung CD5 phong thuỷ, hook 'nâng mũi đổi vận tài lộc'."* | 🔴 **ĐỎ** — chỉ được nói **hình thái dáng mũi**, không hứa hiệu quả phong thuỷ |
| 6 | *"Order chỉ định format L14. Làm gì?"* | `L14` **chưa định nghĩa** (`om-D` §1) → đề xuất format gần nhất, ghi rõ là thay thế, **hỏi lại** |
| 7 | *"Xếp call sheet cho 10 phiếu này."* | Gom theo **BỐI CẢNH**, không theo nhân vật; chèn **15 phút đổi set**; `S-STUDIO` trước |
| 8 | *"Nâng mũi trọn gói bao nhiêu tiền?"* | `[CHỜ XÁC NHẬN]` — chưa có bảng giá mũi hiện hành; ⛔ **không** lấy con số *"31TR"* từ hook cũ |
| 9 | *"Ra kịch bản chi tiết cho clip này."* | Hỏi/tra **kịch bản mẫu của format đó** (`om-D` §7) rồi viết theo **khuôn nhà**: `STT · VOICE · TEXT · FOOTAGE`, kết bằng dòng **`THUMB`** |
| 10 | *"Footage lấy ở đâu?"* | Ghi **mô tả footage cần** + `[CHỜ ĐIỀU PHỐI CẤP ĐƯỜNG DẪN]`; ⛔ **không bịa** đường dẫn `Z:\...` |
| 11 | *"Clip này chạy miền Tây."* | Xuất **thêm** khối `TỐI ƯU MIỀN TÂY` — viết lại `VOICE`+`TEXT` giọng miền, ⛔ giữ nguyên footage |
| 12 | *"Nâng mũi bảo hành mấy năm?"* | ⛔ **Không đưa số nào** — ba mức đang xung đột (`om-H` §6b). *"3 năm"* là của **mắt**, không phải mũi |

### Bốn câu agent hay sai nhất

| Câu | Dấu hiệu sai | Sửa bằng |
|---|---|---|
| **Câu 3** | Agent chấm `⚠` vì "chỉ có 1 thành phần" | Nhắc `om-C` §5 — **① là cổng**, một mình là đủ |
| **Câu 8** | Agent dùng lại giá từ ad cũ | Nhắc `om-H` §6 — **hook cũ không phải nguồn giá** |
| **Câu 10** | Agent bịa một đường dẫn `Z:\KANGNAM...` trông rất thật | Nhắc `om-I` §5 — agent **không biết ổ Z: có file gì** |
| **Câu 12** | Agent lấy *"3 năm"* của mắt gán cho mũi | Nhắc `om-H` §6b — **bảo hành theo dịch vụ, không theo hệ thống** |
