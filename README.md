# 🎬 AGENT-ORDERMEDIA-KANGNAM — Từ order thành phiếu quay

> Version 1.0 · AI nhận **một file order nội dung** (sheet/excel: hook, CTA, chân dung, nấc 5A) → chấm hook theo **công thức rút từ 91 ad thật đã chấm** → xuất **phiếu kịch bản sản xuất 42 trường** + **call sheet gom theo bối cảnh** + **bảng cờ pháp chế có câu thay thế**.
>
> ⛔ **Dịch order thành phiếu quay được — KHÔNG sáng tác tự do.** Agent gắn cờ và đề xuất; bác sĩ kiểm duyệt và pháp chế ký; ekip bấm máy.

Kiến trúc **BRAIN brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **module đơn vị tách riêng** ([`knowledge/om-H-dich-vu-kangnam.md`](knowledge/om-H-dich-vu-kangnam.md)) → đổi đơn vị hoặc đổi dịch vụ chỉ cần thay module đó.

**Phục vụ:** khối Content & Media — Bệnh viện Thẩm mỹ Kangnam.

---

## Nguyên tắc tối thượng

> ### Hook kể **TÌNH TRẠNG** thì khách nhận ra mình. Hook kể **TÍNH TỪ** thì khách lướt qua.

Đây không phải quan điểm — đây là kết luận từ 91 ad đã chấm:

| | Hook | Chấm |
|---|---|---|
| ✓ | *"Mũi thấp tẹt, đầu mũi hếch sửa sao cho đẹp"* | **TỐT** — winner rõ nhất hệ |
| ✓ | *"Mũi tẹt, cánh mũi to nên nâng mũi hay cắt cánh?"* | **TỐT** |
| ✗ | *"Làm sao để có chiếc mũi vạn người mê"* | **KÉM** |
| ✗ | *"Sở hữu dáng mũi SLAY nét căng"* | **KÉM** |
| ✗ | *"Hành trình nâng mũi của tôi"* | **KÉM** |

→ Vì vậy agent **chấm hook ở bước B4, trước khi viết kịch bản**. Viết một kịch bản đẹp cho một hook KÉM là đốt một buổi quay.

---

## Vào gì — ra gì

```
ĐẦU VÀO                          ĐẦU RA
file order 17 cột          →      ① phiếu kịch bản 42 trường / 6 khối
(hook · CTA · chân dung           ② call sheet gom theo BỐI CẢNH
 · nấc 5A · camp đích · …)        ③ bảng chấm hook ✓ / ⚠ / ✗
                                  ④ bảng cờ pháp chế + CÂU THAY THẾ
                                  ⑤ khối GIẢ ĐỊNH
                                  ⑥ khối [CHỜ XÁC NHẬN] — ai cấp, chặn gì
```

**Người order điền 5 ô. Agent điền 27 ô còn lại.** Mọi ô agent suy ra đều in kèm `(suy ra)`.

---

## Bắt đầu nhanh

### 1. Nạp bộ não vào nền tảng AI
Copy toàn bộ khối giữa hai vạch ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) vào:
- **Claude Project** → ô *Custom instructions*
- **ChatGPT Custom GPT** → ô *Instructions* (⚠️ giới hạn 8.000 ký tự → dùng [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md))
- **Gemini Gem** → ô *Chỉ dẫn*

Rồi nạp **8 file `knowledge/` + 6 file `prompts/`** vào phần *Knowledge / Tri thức*.
Nền tảng chỉ cho nạp ít file → dùng bản gộp [`goi/GOP-tri-thuc.md`](goi/GOP-tri-thuc.md).

### 2. Gõ một câu
```
Ra kịch bản sản xuất cho order này.
<link sheet hoặc file excel>
```
Agent tự dẫn từng bước, hỏi tối đa 3 câu một lượt, mỗi câu có `d) Để em chọn mặc định`.

### 3. (Tuỳ chọn) Chạy script tiền xử lý
```bash
python tools/om.py <file.csv|file.xlsx>
python tools/om.py --sheet-id <ID> --gid <GID>
```
Script làm **B1–B3** (nạp · chuẩn hoá · cổng A) + điền sẵn các ô suy ra + chấm hook sơ bộ + soát pháp chế sơ bộ. Agent chỉ còn làm phần sáng tạo **B4–B7**.

---

## Bảy bước

```
B1 NẠP ORDER        → đọc sheet/excel, map 17 cột, gắn mã dòng gốc
B2 CHUẨN HOÁ        → CD1–CD6 · nấc 5A · ô camp · nhiệt · format
B3 ⛔ CỔNG A        → order đủ để viết kịch bản chưa (8 ô)
B4 SOI HOOK         ★ chấm theo công thức thắng/thua — BƯỚC QUYẾT ĐỊNH
B5 VIẾT KỊCH BẢN    → 4 khối theo giây + shot list + đạo cụ + nhân vật
B6 ⛔ CỔNG B PHÁP CHẾ → 12 điểm L + cờ 🟢🟡🔴 + câu thay thế
B7 XUẤT PHIẾU       → bảng 42 trường + call sheet gom theo BỐI CẢNH
```

**Hai cổng chặn:** cổng A chặn *"viết mò vì thiếu chân dung/nấc"* · cổng B chặn *"câu sai lọt ra ads"*.
⛔ Không lối tắt nào bỏ được cổng B.

---

## Tám sổ tri thức

| Sổ | Nội dung |
|---|---|
| [`om-A`](knowledge/om-A-vai-tro-quy-trinh.md) | Vai trò · 7 bước · hai cổng · ★ chế độ AUTO · ba loại yêu cầu |
| [`om-B`](knowledge/om-B-doc-dau-vao.md) | 17 cột order · chuẩn hoá chân dung · ★ 10 ô agent tự suy ra · 7 loại hook |
| [`om-C`](knowledge/om-C-tri-thuc-khach-hang.md) | ★ 6 chân dung CD1–CD6 · 5A · **công thức hook thắng/thua từ 91 ad thật** |
| [`om-D`](knowledge/om-D-thu-vien-format.md) | Thư viện format L01–L16 · cấu trúc theo giây · đạo cụ · bối cảnh · dòng batch |
| [`om-E`](knowledge/om-E-kich-ban-san-xuat.md) | 4 khối lời thoại · shot list · ★ 42 trường đầu ra · call sheet · tái dựng |
| [`om-F`](knowledge/om-F-to-chuc-ads.md) | Ô V1–V5/P1–P5 · kho tệp vào/loại trừ · ngưỡng TỐT/KÉM · nhịp vận hành |
| [`om-G`](knowledge/om-G-phap-che-ranh-gioi.md) | ⛔ 12 điểm L01–L12 · cờ 🟢🟡🔴 · câu thay thế mẫu · mẫu trả lời bình luận |
| [`om-H`](knowledge/om-H-dich-vu-kangnam.md) | **Module đơn vị** — chi nhánh · giấy phép · menu dịch vụ · trạng thái xác minh BS |

---

## Sáu prompt mẫu

| Prompt | Dùng khi |
|---|---|
| [★ AUTO](prompts/prompt-auto.md) | Không muốn nghĩ — một câu là đủ |
| [Đọc order](prompts/prompt-doc-order.md) | Chỉ muốn kiểm order đã đủ để viết chưa (B1–B3) |
| [Soi hook](prompts/prompt-soi-hook.md) | Chấm hook, viết hook mới (B4) |
| [Ra kịch bản](prompts/prompt-ra-kich-ban.md) | Viết lời thoại, shot list, call sheet (B5) |
| [Soát pháp chế](prompts/prompt-soat-phap-che.md) | Cổng B — chạy độc lập được (B6) |
| [Lấp lỗ hổng](prompts/prompt-lap-lo-hong.md) | Chưa có order, cần biết thiếu content ở đâu |

---

## ⛔ Năm điều agent không được làm

① Viết kịch bản cho dòng order **chưa có chân dung + nấc 5A**
② **Gắn tên bác sĩ** khi `om-H` chưa ghi là đã xác minh
③ **Đổi hook của người order mà không khai** — phải in gốc → đề xuất → vì sao
④ Để **cam kết kết quả / con số không nguồn / lời chứng thực người bệnh** đi qua cổng pháp chế
⑤ **Bịa** chỉ số, bảng giá, số suất ưu đãi, mốc hồi phục

---

## ⚠️ Việc đang chặn — năm thứ cần xin

Agent in năm dòng này vào khối `[CHỜ XÁC NHẬN]` mỗi lần xuất phiếu, cho tới khi được cấp:

| # | Cần | Ai cấp | Đang chặn |
|---|---|---|---|
| 🔴 ① | **Danh sách BS đã xác minh** (tên · số CCHN · phạm vi chuyên môn · cơ sở hành nghề · văn bản đồng ý dùng hình ảnh) | Vận hành + pháp chế | Mọi phiếu có tên bác sĩ |
| 🔴 ② | **Bảng giá trọn gói hiện hành** + quyền lợi từng gói | Vận hành / sales | Mọi phiếu `L11` + mọi hook nấc `A4` |
| 🔴 ③ | **Chính sách bảo hành bằng văn bản** — thời hạn thật | Pháp chế | ⚠️ Dữ liệu hiện có ghi cả *"trọn đời"* và *"10 năm"* → chắc chắn một cái sai |
| 🔴 ④ | **Số giấy phép hoạt động đủ 7 cơ sở** (hiện chỉ có 2: HN `194/BYT-GPHĐ` · SG `287/BYT-GPHĐ`) | Pháp chế | Mọi phiếu local `L12` ngoài hai bệnh viện |
| 🟡 ⑤ | **Định nghĩa format `L13` `L14` `L15` `L16`** | Content Lead | Các ô `V3`/`P3`/`V4`/`P4`/`V5` đang trỏ tới format chưa định nghĩa |

> ⚠️ Mục ⑤ là lỗi dữ liệu thật đã phát hiện khi dựng agent: **kế hoạch Ads dùng `L13`–`L15`, nhưng thư viện Format chỉ định nghĩa tới `L12`.**

---

## Ba lỗ hổng phễu đáng lấp trước

Từ ma trận chân dung × 5A của pilot mũi (34 content đang giữ):

| Ô | Vì sao có đòn bẩy cao |
|---|---|
| **A5 · mọi chân dung** | Trống **hoàn toàn**. Tệp `CUST` đã có, chi phí thấp nhất, mở đường cross-sell. |
| **A4 nhắm `BOOKED-NS`** | Khách đã đặt lịch nhưng chưa đến — **no-show ~28%**. Doanh thu gần chốt. |
| **A3 · CD3 / CD6** | `P3` chiếm **48% ngân sách**, và KPI pilot đòi ≥1 hook CD3/CD6 đạt mục tiêu. |

⚠️ **CD1 đang chiếm 27/34 content** — phễu dựa gần như toàn bộ vào một chân dung.

---

## Bàn giao — agent dừng ở đâu

| Việc | Ai làm tiếp |
|---|---|
| Quay · dựng · phụ đề | Ekip sản xuất |
| Duyệt y khoa · ký pháp chế | Bác sĩ kiểm duyệt + pháp chế |
| Thu consent khách hàng | Điều phối sản xuất |
| Set camp · chia ngân sách · chấm số sau chạy | `Agent-AdsOptimize-Kangnam` |
| Báo cáo hiệu quả theo kỳ | `Agent-AdsReport-Kangnam` |

---

## Cấu trúc repo

```
Agent-OrderMedia-Kangnam/
├── SYSTEM-PROMPT.md          ★ bộ não — copy vào nền tảng AI
├── SYSTEM-PROMPT-NGAN.md       bản <8.000 ký tự cho ChatGPT
├── knowledge/                  8 sổ om-A … om-H
├── prompts/                    6 prompt mẫu
├── goi/GOP-tri-thuc.md         bản gộp (sinh tự động)
├── tools/om.py               ★ đọc order · chuẩn hoá · cổng A · chấm sơ bộ
├── tools/gop-tham-khao.py      gộp lại knowledge/
├── doc/                        cài đặt · dòng lệnh · CHANGELOG
└── out/                        phiếu xuất ra (gitignored)
```

⛔ `out/`, ảnh, footage và file order gốc **không commit** — xem [`.gitignore`](.gitignore).
