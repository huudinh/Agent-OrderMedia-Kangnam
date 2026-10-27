# CHANGELOG

---

## v1.2.1 — 2026-10-27

Thêm **trang hướng dẫn** dạng artifact, theo đúng khuôn dùng chung của bộ agent.

| Thành phần | Nội dung |
|---|---|
| `tools/trang-huong-dan.py` | Copy generator dùng chung từ `Agent-QC-Telesale` · **thêm `<meta name="viewport">`** |
| `tools/huong-dan.json` | Nội dung trang: 3 thẻ · 16 file · 31 prompt · 12 câu smoke · 5 điều phải biết · 6 mục chặn |
| `README.md` | Khối *"📘 Hướng dẫn sử dụng"* + link artifact |
| `.gitignore` | ⛔ `tools/huong-dan.html` — artifact sinh ra, không phải nguồn |

**Trang:** https://claude.ai/artifact/1A4tfwpJZSPKJ4g8mq3omG

### ⚠️ Sửa một lỗi của generator dùng chung

Generator gốc *(đang dùng ở `Agent-QC-Telesale`, `Agent-Order-SoLieu`…)* **không phát `<meta name="viewport">`** → trang bị thu nhỏ trên điện thoại, chữ không đọc được mà không zoom. Bản trong repo này đã thêm.
→ **Nên đồng bộ sang các agent khác** — lỗi này ảnh hưởng mọi trang hướng dẫn đã publish.

### Vì sao nút Copy không bao giờ lệch

Generator **đọc thẳng file nguồn** *(bộ não, 10 sổ, 6 prompt)* để nhúng vào nút Copy, chỉ lấy câu chữ từ JSON. Sửa `knowledge/` thì chạy lại generator là nút Copy tự đúng — ⛔ không phải sửa JSON theo.

---

## v1.2 — 2026-10-27

Mở **chuyên khoa thứ hai: MẮT**.

### Dựng mới

| Thành phần | Nội dung |
|---|---|
| `knowledge/om-J-chan-dung-mat.md` | 6 chân dung mắt · 5A mắt · ★ từ vựng tình trạng mắt · dịch vụ & giá · lỗ hổng phễu mắt |
| `om-C` header | Khoanh phạm vi: §1–§4 là **mũi**; §5–§6 *(công thức hook)* dùng cho **mọi dịch vụ** |
| `SYSTEM-PROMPT` §9b | Luật chọn module theo dịch vụ + nói rõ độ tin cậy |
| `tools/om.py` | Định tuyến chân dung theo dịch vụ · sửa ánh xạ `sụp mí`/`lão hoá` · cảnh báo `CD5` lệch + bệnh nền |

### ⚠️ Sửa một lỗi ánh xạ của v1.0

```
v1.0 :  "sụp mí"  → CD1      "lão hóa" → CD1      ← SAI, gộp ba tệp khác nhau vào một mã
v1.2 :  "sụp mí"  → CD6      "lão hóa" → CD5
```
Sụp mí là **bệnh lý ảnh hưởng chức năng** → thuộc `CD6`. Lão hoá là tệp riêng với nỗi sợ riêng *(tuổi cao, bệnh nền)*.

### ⚠️ Một chỗ LỆCH quy ước — cần khối Ads chốt

```
Mũi : CD5 = Phong thuỷ / tướng số
Mắt : không có dữ liệu phong thuỷ, nhưng order có tệp "Mắt - Lão hóa" rất rõ
→ Agent tạm xếp CD5 mắt = Lão hoá, và IN CẢNH BÁO mỗi lần xuất phiếu CD5 mắt.
```
Hệ quả nếu để lệch: báo cáo so `CD5` giữa mũi và mắt sẽ so **hai tệp khác hẳn nhau**. Ba hướng xử ở `om-J` §1 — ⛔ agent không tự chuyển hướng khi chưa được chốt.

### Phát hiện về chuyên khoa mắt

| Phát hiện | Ý nghĩa |
|---|---|
| ★ **Nỗi sợ `A3` của mắt khác mũi**: mắt = **chi phí phát sinh**; mũi = *"không ai chịu trách nhiệm"* | Hook `A3` mắt nên mở bằng **giá trọn gói**; mũi mở bằng **bảo hành** |
| **`CD3` mắt là tệp có hook mạnh nhất** — kịch bản `L03` có 4 hook sẵn *("tại sao cắt mí rồi mắt vẫn chưa đẹp", "có nếp mí rõ mà mắt vẫn nhỏ")* — nhưng order **chưa có dòng nào** | Lỗ hổng đáng lấp nhất của mắt |
| **`CD4` mắt đã có case quay xong** *("Đàn ông không có quyền làm đẹp?")* nhưng order chưa có dòng | Chỉ cần dựng, không cần quay mới |
| ★ **Insight đắt nhất của `CD3` mắt:** vấn đề thường **không ở nếp mí** mà ở tương quan cung mày · hốc mắt sâu · góc mắt · da chùng | Nhóm này muốn **lời giải thích** trước khi muốn dịch vụ |
| **`CD5` mắt có nỗi sợ không nhóm nào khác có:** *"bệnh huyết áp/tiểu đường nhẹ có cắt mí được không?"* | 🔴 Câu về bệnh nền **phải do BS duyệt** |
| **Lát cắt SINH VIÊN** trong `CD1` — có kịch bản riêng, giọng tự trào, thời điểm **nghỉ hè**, trigger trả góp | Không phải chân dung riêng, là lát cắt theo ngân sách |
| ⚠️ **Order mắt chưa dòng nào có cột `HIỆU QUẢ`** | Công thức hook `om-C` §5 rút từ **91 ad mũi** → áp sang mắt là **suy luận, chưa phải bằng chứng**. Agent phải nói rõ điều này |

### 🔴 Bản ngắn đã ĐẦY

`SYSTEM-PROMPT-NGAN` 7.523 → **7.987 / 8.000 ký tự — còn 13.**
→ Thêm dòng nào cũng phải **cắt một dòng khác**. Nếu cần thêm nhiều: bỏ bớt mục khỏi bản ngắn, để agent tra trong `knowledge/` — bản ngắn chỉ nên giữ **luật chặn** và **con trỏ sang sổ**.

`goi/GOP-tri-thuc.md` 118,8 → **137,4 KB** · 10 sổ.

---

## v1.1 — 2026-10-27

Nạp **thư viện kịch bản thật** của khối (mục lục `1g4ti7tIY0...`, 11 kịch bản chuyên khoa mắt + sheet *Quy định text*).

### Dựng mới

| Thành phần | Nội dung |
|---|---|
| `knowledge/om-I-khuon-kich-ban-nha.md` | ★ Khuôn kịch bản thật — hai tầng đầu ra · khuôn cột theo format · thuật ngữ dựng · quy định text · nguồn footage · dòng THUMB · khối TỐI ƯU MIỀN TÂY · đối chiếu cổng B |
| `om-D` §7 | Mục lục kịch bản mẫu theo format + cảnh báo mượn khuôn ≠ mượn nội dung |
| `om-H` §6a–6b | **Bảng giá mắt thật** + phát hiện ba mức bảo hành xung đột |
| `om-H` §7 | Bốn quyền lợi riêng cho tệp Việt kiều |
| `SYSTEM-PROMPT` §8b | Hai tầng đầu ra · khuôn nhà · thuật ngữ · quy định text |

### ★ Quyết định thiết kế lớn nhất: đầu ra có HAI TẦNG

Bản v1.0 thiết kế đầu ra là **một bảng phẳng 42 trường, 1 dòng = 1 clip**. Đọc kịch bản thật mới thấy nhà đang làm khác: **1 dòng = 1 NHỊP**, mỗi clip là một sheet riêng, một clip `L03` có 20–25 nhịp.

→ Hai cái **không thay thế nhau, mà bổ sung**:

```
TẦNG 1  PHIẾU ORDER        1 dòng = 1 clip · 42 trường   → quản lý & điều phối
TẦNG 2  KỊCH BẢN CHI TIẾT  1 dòng = 1 NHỊP · khuôn nhà   → editor & DOP
```

Trường `LỜI THOẠI THEO MỐC GIÂY` ở tầng 1 trở thành **con trỏ** sang sheet tầng 2, không phải chỗ nhét cả 25 nhịp.

### Khuôn nhà đã rút được

- **Lõi chung 4 cột:** `STT · VOICE/NỘI DUNG · TEXT · FOOTAGE/FT`, biến thể thêm `THIẾT KẾ` · `NOTE` · `FIX`
- **Thuật ngữ dựng:** `trám full` · `trám cận` · `chia đôi, trám hình trên, bsi nói ở dưới` · `cho bác sĩ xuống góc` · `tách nền bác sĩ` · `khung box comment` · `Text nền FT` · `biến đổi trc sau` · `ra beauty` · `multi pic`
- **Quy định text cứng:** Roboto · `#114D8F` / `#ef6103` / trắng-đen · viền 20/30 · cỡ 15 · subtext `X:0 Y:-1050` · tool khung câu hỏi TikTok `65%, X:-200 Y:-840` · ⛔ **không dùng khung, không thiết kế**
- **Dòng `THUMB` bắt buộc**, text ≤2 dòng in hoa
- **Khối `TỐI ƯU MIỀN TÂY`** — viết lại giọng miền, giữ nguyên footage
- **Cột `FIX`** là vòng feedback của người duyệt → ⛔ agent để trống
- **Voice AI** cho câu hỏi; lời bác sĩ/khách giữ tiếng thật, cắt theo mốc giây

### ⚠️ Phát hiện mới

| Phát hiện | Xử lý |
|---|---|
| **Bảo hành có BA mức đang cùng chạy:** *3 năm* (kịch bản `L11` mắt) · *10 năm* (CD3 mũi) · *trọn đời* (hook mũi) | `om-H` §6b — mắt dùng `3 năm` kèm cảnh báo; mũi ⛔ không dùng số nào. Đẩy lên **chặn số ① cấp bách nhất** |
| **Có bảng giá mắt thật**: Plasma 8tr · 6D 12,8tr · +tạo khoé 13,6tr · +cấy mỡ 17,9tr · nâng cung mày 8,8tr | `om-H` §6a — mở một phần chặn giá, vẫn phải đối chiếu bản chính thức |
| ★ **Kịch bản thật đang chứa nhiều câu mà cổng B gắn cờ**: *"Không đau - Không sưng bầm"* làm text thương hiệu · *"VÔ KHUẨN 100%"* · *"Đường sẹo tàng hình"* · *"7 NGÀY LÀ ĐẸP"* · *"15+ năm kinh nghiệm, 20.000+ khách hàng"* · tên BS chưa xác minh | `om-I` §9 — agent **vẫn chấm cờ cho clip mới**, nêu kèm dẫn chứng, ⛔ không tự sửa kho cũ. Rà kho cũ là quyết định của khối + pháp chế |
| **`L01` chưa có kịch bản mẫu** — ô link trong mục lục trống, dù đây là format xương sống | `om-D` §7 — dùng khuôn `L03` rút gọn, ghi rõ là khuôn mượn. Thêm vào chặn ⑥ |
| **Kịch bản mẫu toàn bộ là chuyên khoa MẮT** | `om-D` §7 — mượn **khuôn**, ⛔ không mượn nội dung y khoa và con số |
| **Bốn quyền lợi Việt kiều** chưa được hook mũi khai thác: giấy xác nhận phẫu thuật · hỗ trợ hải quan · đưa đón sân bay · tư vấn online | `om-H` §7 — lỗ hổng đáng lấp, **sạch pháp chế** vì là quyền lợi dịch vụ |

### Số liệu

`SYSTEM-PROMPT-NGAN` 6.072 → **7.523 ký tự** *(giới hạn 8.000, còn 477)*.
`goi/GOP-tri-thuc.md` 99,6 KB → **118,8 KB** · 9 sổ.

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

## Dự kiến v1.3

- [ ] **Chốt chính sách bảo hành** — chặn cấp bách nhất, ba mức đang cùng chạy trên ads
- [ ] **Chốt hướng xử `CD5` mắt** — `om-J` §1, ba hướng A/B/C
- [ ] **Xin sheet chân dung mắt chính thức** + chấm `HIỆU QUẢ` cho ad mắt → `om-J` §0
- [ ] Mở các chặn còn lại khi được cấp 6 thứ ở `om-H` §8
- [ ] Định nghĩa `L13`–`L16` + kịch bản mẫu `L01`
- [ ] Thay ngưỡng giả định ở `om-F` §3 bằng số thật 3 tháng
- [ ] Thêm `tools/kich-ban.py` — sinh khung kịch bản tầng 2 đúng khuôn cột theo từng format
- [ ] Thêm `tools/call-sheet.py` — gom phiếu thành call sheet, tính giờ và số lần đổi set
- [ ] Nối ngược với `Agent-AdsReport-Kangnam` để tự nạp cột `HIỆU QUẢ` sau mỗi kỳ
