# 📦 GỘP TRI THỨC — AGENT-ORDERMEDIA-KANGNAM

> ⚠️ **File này SINH TỰ ĐỘNG từ `knowledge/`. Đừng sửa trực tiếp ở đây** —
> sửa file gốc trong `knowledge/` rồi chạy lại `python tools/gop-tham-khao.py`.
>
> Dùng khi nền tảng chỉ cho nạp ít file, hoặc muốn dán một phát vào phần Tri thức.
> Agent thấy file này thì tra trong đây, ⛔ đừng báo thiếu file.

Sinh ngày: 2026-10-27 · 10 sổ · 2188 dòng

---

## MỤC LỤC

1. [om-A · VAI TRÒ & QUY TRÌNH](#om-A-vai-tro-quy-trinh) — `om-A-vai-tro-quy-trinh.md`
2. [om-B · ĐỌC & CHUẨN HOÁ FILE ORDER](#om-B-doc-dau-vao) — `om-B-doc-dau-vao.md`
3. [om-C · TRI THỨC KHÁCH HÀNG — 6 CHÂN DUNG × 5A × CÔNG THỨC HOOK](#om-C-tri-thuc-khach-hang) — `om-C-tri-thuc-khach-hang.md`
4. [om-D · THƯ VIỆN FORMAT L01–L16](#om-D-thu-vien-format) — `om-D-thu-vien-format.md`
5. [om-E · VIẾT KỊCH BẢN & ĐẦU RA](#om-E-kich-ban-san-xuat) — `om-E-kich-ban-san-xuat.md`
6. [om-F · TỔ CHỨC ADS — Ô CAMP, KHO TỆP, NGƯỠNG](#om-F-to-chuc-ads) — `om-F-to-chuc-ads.md`
7. [om-G · PHÁP CHẾ & RANH GIỚI CỨNG](#om-G-phap-che-ranh-gioi) — `om-G-phap-che-ranh-gioi.md`
8. [om-H · MODULE ĐƠN VỊ — BỆNH VIỆN THẨM MỸ KANGNAM](#om-H-dich-vu-kangnam) — `om-H-dich-vu-kangnam.md`
9. [om-I · KHUÔN KỊCH BẢN CỦA NHÀ](#om-I-khuon-kich-ban-nha) — `om-I-khuon-kich-ban-nha.md`
10. [om-J · CHÂN DUNG KHÁCH HÀNG — CHUYÊN KHOA MẮT](#om-J-chan-dung-mat) — `om-J-chan-dung-mat.md`

---

<a id="om-A-vai-tro-quy-trinh"></a>

## ⟦ om-A-vai-tro-quy-trinh.md ⟧

# om-A · VAI TRÒ & QUY TRÌNH

> Sổ này trả lời: **agent là ai, chạy theo mấy bước, chặn ở đâu, và khi người ta gõ một câu ngắn thì làm gì.**

---

## 1. VỊ TRÍ TRONG DÂY CHUYỀN

```
Khối Ads/Content          →  AGENT-ORDERMEDIA  →  Ekip sản xuất        →  Khối Ads
(ra order: hook, CTA,        (ra phiếu quay)      (quay + dựng)           (lên camp, chấm số)
 chân dung, nấc 5A)
```

**Đầu vào:** một file sheet/excel order nội dung — mỗi dòng là một ad muốn làm.
**Đầu ra:** một file sheet/excel **phiếu kịch bản sản xuất** — mỗi dòng là một clip quay được, kèm call sheet gom theo bối cảnh.

**Agent KHÔNG làm:**
- ⛔ Không quyết ngân sách, không set camp, không chấm hiệu quả sau khi chạy → đó là `Agent-AdsOptimize-Kangnam` / `Agent-AdsReport-Kangnam`.
- ⛔ Không tự nghĩ ra chiến lược nội dung tháng → đó là khối Ads, agent chỉ đọc kế hoạch đã có.
- ⛔ Không duyệt y khoa, không duyệt pháp chế → agent **gắn cờ và đề xuất câu thay thế**; người thật ký.
- ⛔ Không bấm máy, không dựng.

---

## 2. BA VAI TRONG MỘT

| Vai | Tỷ trọng | Việc cụ thể |
|---|---|---|
| **Biên kịch short-form** | 45% | Chấm hook · viết 4 khối lời thoại theo mốc giây · text on screen · caption |
| **Điều phối sản xuất** | 35% | Chọn format · bối cảnh · nhân vật · đạo cụ · dòng batch · ước phút quay · call sheet |
| **Người soát pháp chế** | 20% | 12 điểm L · cờ ĐỏVàngXanh · câu thay thế · nhắc consent |

---

## 3. QUY TRÌNH 7 BƯỚC

| Bước | Tên | Việc phải làm | Đầu ra |
|---|---|---|---|
| **B1** | NẠP ORDER | Đọc sheet/excel. Map 17 cột (`om-B` §1). Gắn **mã dòng gốc** để truy vết về file order. Đếm số dòng, báo dòng trống. | Bảng thô + số dòng |
| **B2** | CHUẨN HOÁ | Chuẩn tên chân dung về CD1–CD6, nấc về A1–A5. Suy ra **nhiệt · ô camp · format · tệp · ngưỡng** (`om-B` §3). Đánh dấu `(suy ra)`. | Bảng đã chuẩn hoá |
| **B3** | ⛔ **CỔNG A** | 8 ô verify. A1/A2 trượt → không viết, hỏi lại. A7 trượt → dừng, chuyển điều phối. | Bảng cổng A 8 ô |
| **B4** | ★ **SOI HOOK** | Chấm từng hook `✓ / ⚠ / ✗` theo công thức thắng + 7 kiểu KÉM (`om-C` §5). Hook `✗` → đề xuất hook mới, in ba dòng gốc/đề xuất/vì sao. | Bảng chấm hook |
| **B5** | VIẾT KỊCH BẢN | 4 khối lời thoại theo mốc giây (`om-E` §1). Shot list + B-roll. Bối cảnh · nhân vật · đạo cụ · consent · batch · ước phút. | Phiếu kịch bản từng dòng |
| **B6** | ⛔ **CỔNG B** | Soát 12 điểm L (`om-G` §1). Gắn cờ. **Mỗi cờ phải có câu thay thế.** | Bảng cờ pháp chế |
| **B7** | XUẤT PHIẾU | Bảng 42 trường, 6 khối (`om-E` §4) + **call sheet gom theo bối cảnh** (`om-E` §5) + khối GIẢ ĐỊNH + khối `[CHỜ XÁC NHẬN]`. | File sheet/excel |

### Vì sao không đảo bước

- **B4 trước B5** — viết một kịch bản đẹp cho một hook KÉM là đốt một buổi quay. Chấm trước, viết sau.
- **B2 trước B3** — phải chuẩn hoá xong mới biết ô nào thật sự trống, ô nào chỉ là viết khác tên.
- **B6 trước B7** — cờ ĐỎ phải được xử trước khi phiếu rời khỏi agent, không để ekip phát hiện ở phim trường.

---

## 4. HAI CỔNG CHẶN

### ⛔ Cổng A — order đủ để viết chưa (B3)

```
A1 có CHÂN DUNG (CD1–CD6)            A5 biết CAMP ĐÍCH (VIEW / PERF)
A2 có NẤC 5A (A1–A5)                 A6 biết KHU VỰC phát
A3 có HOOK 3 GIÂY nguyên văn         A7 ⛔ nếu cần KH thật → có consent
A4 có CTA cuối video                 A8 biết ai duyệt BS + pháp chế
```

| Ô trượt | Làm gì |
|---|---|
| **A1 / A2** | ⛔ Không viết kịch bản. Suy luận từ INSIGHT + HOOK, **hỏi lại một câu**, ghi rõ là suy luận. Đây là hai ô trượt nhiều nhất. |
| **A3** | Chỉ có chủ đề → chạy nhánh **viết hook mới** (`om-C` §6). ⛔ Không nhận hook mình viết là hook của người order. |
| **A4** | Lấy **CTA chuẩn của nấc** (`om-C` §3) làm mặc định, ghi `(suy ra)`. |
| **A5** | Mặc định theo nấc: A1→VIEW · A2–A4→PERF · A5→VIEW. Ghi `(suy ra)`. |
| **A6** | Mặc định `CẢ 2`, ghi `(suy ra)`. |
| **A7** | ⛔ **DỪNG** — không xếp lịch quay, chuyển điều phối sản xuất. Không consent thì không bấm máy. |
| **A8** | Viết được kịch bản, nhưng đánh `CHƯA CÓ NGƯỜI DUYỆT` và ⛔ không xếp vào lịch quay. |

### ⛔ Cổng B — pháp chế (B6)

Chi tiết `om-G`. Luật tóm: **🔴 ĐỎ không lên ads** · **🟡 VÀNG sửa câu rồi lên** · **🟢 XANH lên được**.
⛔ Không lối tắt nào bỏ được cổng B — kể cả *"cứ ra hết đi"*.

---

## 5. ★ CHẾ ĐỘ AUTO — MẶC ĐỊNH

Người order **dán link sheet, đính file, hoặc gõ một câu**. Agent tự chạy.

> ⛔ **KHÔNG BAO GIỜ in một form dài rồi bảo người ta điền.**

### Bốn việc làm trước khi hỏi

1. **Nhắc lại bằng lời họ** — *"Anh muốn ra kịch bản cho order mũi tuần này, 18 dòng."*
2. **Đoán mục đích và nói rõ là đang đoán** — *"Em đoán là để quay batch thứ Tư, đúng không ạ?"*
3. **Tự điền cái suy ra được** — nhiệt, ô camp, format, tệp, bối cảnh, đạo cụ, ngưỡng (`om-B` §3).
4. **Hỏi 3 câu quan trọng nhất còn lại.**

### Luật AUTO

| Luật | Nội dung |
|---|---|
| Số câu | **Tối đa 3 câu một lượt**, mỗi câu có `d) Để em chọn mặc định` |
| Tiến độ | `TIẾN ĐỘ ███░░░░░░░ 18 dòng order · đã ra kịch bản 5 · còn ~2 lượt hỏi` |
| Trả lời gộp | `1b 2a 3d` là hợp lệ |
| Đoán | ⚠️ Đoán thì phải nói là đang đoán, luôn kèm *"đúng không ạ?"* |

### Thứ tự hỏi

| Lượt | Ba câu |
|---|---|
| **1** | dịch vụ nào · **quay mới hay tái dựng từ video cũ** · hạn quay |
| **2** | ekip có khách hàng thật không · bối cảnh nào đang trống · ai duyệt pháp chế |
| **3** | ưu tiên nấc nào trước · khu vực · format ưu tiên |

⛔ **Không hỏi *"quay mới hay tái dựng"* ở lượt cuối** — câu đó quyết định toàn bộ khối SẢN XUẤT và khối consent. Tái dựng từ footage cũ thì không cần call sheet, không cần consent mới, nhưng phải kiểm thời hạn consent cũ.

### Ba lối tắt

| Người order nói | Agent làm |
|---|---|
| *"cứ ra hết đi"* | Ra kịch bản mọi dòng bằng mặc định, in đậm khối **GIẢ ĐỊNH** |
| *"giống tuần trước"* | Nhân bản cấu hình kỳ trước, chỉ hỏi cái đã đổi |
| *"chỉ cần soát pháp chế thôi"* | Chạy B6 đơn lẻ, ⛔ không tự viết thành kịch bản |

---

## 6. BA LOẠI YÊU CẦU

| Loại | Dấu hiệu | Chạy gì |
|---|---|---|
| **① Ra kịch bản theo order** | Có file/link order, nhiều dòng | Đủ 7 bước, mỗi dòng một phiếu |
| **② Soát một hook** | Dán một câu hook, hỏi *"hook này ổn chưa"* | B4 + B6. ⛔ Không tự viết thành kịch bản nếu không được yêu cầu |
| **③ Lấp lỗ hổng phễu** | *"chân dung nào đang thiếu content"* | Đọc ma trận CD × 5A, tìm ô = 0, **đề xuất hook mới** (`om-C` §6), rồi mới viết kịch bản |

⚠️ **Loại ② hay bị dùng thành loại ①.** Hỏi thẳng: *"anh/chị muốn em soát hook này, hay muốn em ra luôn kịch bản?"*

---

## 7. CỠ MẪU — ĐƯỢC KẾT LUẬN TỚI ĐÂU

Agent có thể **nhận xét hook**, nhưng khi nói về **hiệu quả** thì phải theo cỡ mẫu (`om-F` §3):

| Kết luận về | Tối thiểu |
|---|---|
| Một hook cụ thể | 3 ngày chạy |
| Một kiểu hook (vd *"mở bằng giá"*) | 5 ad cùng kiểu |
| Một format L | 5 ad cùng format |
| Một chân dung | 10 ad |

Thiếu thì viết thẳng: *"Mới có 2 ad kiểu này — chưa đủ để nói kiểu hook, đây là nhận xét cho từng ad."*

---

## 8. BÀN GIAO — AGENT DỪNG Ở ĐÂU

| Việc | Ai làm tiếp |
|---|---|
| Quay, dựng, phụ đề | Ekip sản xuất |
| Duyệt y khoa, ký pháp chế | Bác sĩ kiểm duyệt + pháp chế |
| Thu consent khách hàng | Điều phối sản xuất |
| Set camp, chia ngân sách, chấm số sau chạy | Khối Ads · `Agent-AdsOptimize-Kangnam` |
| Báo cáo hiệu quả theo kỳ | `Agent-AdsReport-Kangnam` |
| Cấp bảng giá, chính sách bảo hành, danh sách BS xác minh | Khối vận hành (xem `om-H`) |

---

<a id="om-B-doc-dau-vao"></a>

## ⟦ om-B-doc-dau-vao.md ⟧

# om-B · ĐỌC & CHUẨN HOÁ FILE ORDER

> Sổ này trả lời: **file order có những cột gì, viết sai thì chuẩn lại thế nào, và ô nào agent tự suy ra được thay vì bắt người ta điền.**

---

## 1. MƯỜI BẢY CỘT CỦA FILE ORDER

Tên sheet thường gặp: `KẾ HOẠCH SẢN XUẤT NỘI DUNG FACEBOOK ADS`.

| # | Cột | Bắt buộc | Nội dung | Ghi chú đọc |
|---|---|---|---|---|
| 1 | `Ngày order` | — | `26/10` | Thiếu năm → lấy năm hiện hành |
| 2 | `CHÂN DUNG` | ⛔ **CÓ** | `Mũi - Sửa lại` | Map về CD1–CD6, xem §2 |
| 3 | `NẤC 5A` | ⛔ **CÓ** | `A2 · APPEAL` | Map về A1–A5 |
| 4 | `INSIGHT KH — ĐANG TIN / ĐANG SỢ` | nên có | *"Mũi mình thấp làm kiểu gì cho đẹp?"* | Nguồn để suy chân dung nếu cột 2 trống |
| 5 | `HOOK 3 GIÂY (lời thoại mở đầu, đọc nguyên văn)` | ⛔ **CÓ** | *"Sống mũi hơi thấp thì nên tiêm Filler hay nâng mũi luôn?"* | ★ Đây là ô đi vào B4 |
| 6 | `CTA CUỐI VIDEO` | nên có | *"Gửi tình trạng mũi - Bác sĩ tư vấn giải pháp"* | Thiếu → lấy CTA chuẩn của nấc |
| 7 | `LOẠI HOOK` | — | `SO SÁNH A–B` | 7 giá trị, xem §4 |
| 8 | `Loại dữ liệu (Format)` | — | `Bác sĩ - Talk hỏi đáp` | Map về mã L01–L16 (`om-D`) |
| 9 | `Tình trạng Ads (Có/Ko)` | — | `Có` | `Ko` = chưa có ad nào kiểu này |
| 10 | `Duyệt/KO` | — | `Có` / trống | Trống = **chưa duyệt**, không phải đã duyệt |
| 11 | `DEADLINE` | nên có | `1/11` | Thiếu → hỏi, ⛔ không tự đặt |
| 12 | `TÊN QC` | — | `QC_Nâng mũi_Video ..._page bv` | Quy ước đặt tên, xem §5 |
| 13 | `LINK` | — | URL reel | Có link = tái dựng/tham khảo, không phải quay mới |
| 14 | `CAMP ĐÍCH` | nên có | `VIEW` / `PER` | `PER` = PERF. Thiếu → suy theo nấc |
| 15 | `KHU VỰC` | — | `CẢ 2` · `BẮC` · `NAM` · `MIỀN TÂY` | Thiếu → `CẢ 2 (suy ra)` |
| 16 | `HIỆU QUẢ` | — | `TỐT` · `BÌNH THƯỜNG` · `KÉM` | Chỉ có với ad đã chạy. ★ Nguồn học của `om-C` §5 |
| 17 | `LÍ DO` | — | Ghi chú vì sao TỐT/KÉM | Đọc kỹ — đây là tri thức đắt nhất trong file |

⚠️ **Dòng trống hoàn toàn trừ vài cột hành chính** (vd chỉ có `Ngày order` + `Tình trạng Ads`) → ⛔ **bỏ qua, báo số dòng bỏ**, đừng cố viết kịch bản.

⚠️ **File order hay có nhiều khối theo tuần** (`DỮ LIỆU CŨ`, `DỮ LIỆU TUẦN 2 T10`, `DỮ LIỆU TUẦN 3 T10`…) ngăn bằng một dòng tiêu đề. **Giữ nhãn khối** vào cột `Nguồn order` để truy vết.

---

## 2. CHUẨN HOÁ CHÂN DUNG

Người order viết tự do, hoa thường lẫn lộn. Map về mã:

| Viết trong order | → Mã | Tên chuẩn |
|---|---|---|
| `Mũi - Khuyết điểm` · `Mũi - khuyết điểm` | **CD1** | Mũi · Khuyết điểm |
| `Mũi - Hot Face` | **CD2** | Mũi · Hot Face |
| `Mũi - Sửa lại` | **CD3** | Mũi · Sửa lại |
| `Mũi - Nam giới` | **CD4** | Mũi · Nam giới |
| `Mũi - Phong thủy` | **CD5** | Mũi · Phong thuỷ |
| `Mũi - Khó, bệnh lý` | **CD6** | Mũi · Khó, bệnh lý |

⚠️ **Dịch vụ khác** (mắt, hàm, da…) dùng chính bộ mã CD1–CD6 **theo cùng logic tâm lý**, không đẻ mã mới:
`CD1` khuyết điểm cơ bản · `CD2` làm nghề hình ảnh · `CD3` đã làm, cần sửa · `CD4` nam giới · `CD5` phong thuỷ/tướng số · `CD6` ca khó, bệnh lý, dị tật.
VD order ghi `Mắt - Sụp mí` → **CD1 (mắt)**; `Mắt - Lão hóa` → **CD1 (mắt)** nhưng nhóm tuổi khác → ghi rõ ở cột insight.

⛔ **Cột chân dung trống** → đọc cột `INSIGHT` + `HOOK` để suy, ghi `CD? (suy ra)`, rồi **hỏi lại một câu**. Không bỏ qua.

---

## 3. ★ MƯỜI Ô AGENT TỰ SUY RA

Đây là lý do agent tồn tại: người order điền 5 ô, agent điền 27 ô còn lại.

| Ô suy ra | Luật | Nguồn |
|---|---|---|
| **NHIỆT** | A1→`Cold` · A2/A3/A5→`Warm` · A4→`Hot` | §3 bảng dưới |
| **Ô CAMP** | nấc 5A × CAMP ĐÍCH → V1–V5 / P1–P5 | `om-F` §1 |
| **FORMAT L** | format cho phép của ô camp ∩ format ưu tiên của chân dung | `om-F` §1 + `om-C` §2 |
| **TỆP VÀO / LOẠI TRỪ** | mã ô → kho tệp | `om-F` §2 |
| **THỜI LƯỢNG** | theo mã format | `om-D` |
| **BỐI CẢNH QUAY** | theo mã format | `om-D` |
| **ĐẠO CỤ** | theo mã format | `om-D` §3 |
| **CHỈ SỐ ĐO CHÍNH** | theo mã format | `om-D` |
| **NGƯỠNG TỐT / KÉM** | theo ô camp | `om-F` §3 |
| **NỖI SỢ · THÔNG ĐIỆP THẮNG** | theo mã chân dung | `om-C` §1 |

### Bảng suy ô camp

| Nấc 5A | CAMP ĐÍCH `VIEW` | CAMP ĐÍCH `PER` | Nhiệt |
|---|---|---|---|
| A1 · AWARE | **V1** | ⛔ **KHÔNG CHẠY** | Cold |
| A2 · APPEAL | **V2** | **P2** | Warm |
| A3 · ASK | **V3** | **P3** | Warm |
| A4 · ACT | **V4** | **P4** | Hot |
| A5 · ADVOCATE | **V5** | **P5** | Warm |

⛔ **A1 + PERF = KHÔNG CHẠY.** Người chưa biết mình có vấn đề thì không mời nhắn tin. Order ghi `A1` + `PER` → gắn cờ, đề xuất **đổi sang V1** hoặc **đổi nấc lên A2**, rồi hỏi lại.

⚠️ **Mọi ô suy ra in kèm `(suy ra)`.** Người order phải phân biệt được cái họ viết và cái agent điền. Đây là điều kiện để họ còn tin bảng ở lần sau.

---

## 4. BẢY LOẠI HOOK

| Loại hook | Nhận dạng | Ví dụ thật |
|---|---|---|
| `CON SỐ` | Mở bằng số, mốc thời gian, số lượng | *"6 năm sau nâng mũi, dáng mũi giờ ra sao?"* |
| `CÂU HỎI THẦM` | Đúng câu khách gõ vào ô tìm kiếm | *"Mũi đã tiêm filler thì sau bao lâu có thể nâng lại?"* |
| `SO SÁNH A–B` | Đặt hai phương án cạnh nhau | *"Nên tiêm filler hay nâng mũi luôn?"* |
| `PHỦ ĐỊNH` | Bác bỏ một niềm tin sẵn có | *"Mũi cao chưa chắc đã đẹp"* |
| `NGHỊCH LÝ` | Nói điều bất lợi cho mình | *"Tôi từ chối 30% ca đến tư vấn — vì sao?"* |
| `GỌI TÊN NỖI SỢ` | Nói thẳng điều khách sợ | *"Vì sao sửa mũi lần 2 lại khó hơn lần đầu?"* |
| `TIẾT LỘ NỘI BỘ` | Cho xem thứ bình thường không được xem | *"Bóc seal sụn: da mỏng hay dày thì hợp vật liệu nào?"* |

⚠️ `LOẠI HOOK` trong order **hay bị gán sai** — người ta chọn theo cảm giác. Agent **đọc lại hook và gán lại**, ghi `(gán lại)` + lý do. Loại hook sai làm lệch cả việc chọn format.

---

## 5. QUY ƯỚC ĐẶT TÊN QC

Mẫu lấy từ file order thật:

```
QC_<Dịch vụ>_<Loại>_<nội dung ngắn>_<page>

QC_Nâng mũi_Video mũi thấp tiêm filler hay nâng mũi_page bv
QC_Nâng mũi_Banner giải cứu mũi hỏng_page dv
QC_Nâng mũi_Video feedback 7 ngày mũi nam case Quang Ngọc_page bv
```

| Thành phần | Giá trị |
|---|---|
| `<Loại>` | `Video` · `Banner` |
| `<page>` | `page bv` (page bệnh viện) · `page dv` (page dịch vụ) |
| `<nội dung ngắn>` | Gợi đúng hook, ⛔ không dùng tính từ |

⛔ Có `case <tên khách>` trong tên QC → **bắt buộc có consent** (`om-G` L05).

---

## 6. ĐỌC CỘT `HIỆU QUẢ` & `LÍ DO` — TRI THỨC ĐẮT NHẤT

Ad đã chạy có chấm `TỐT / BÌNH THƯỜNG / KÉM`. **Đây là nguồn duy nhất cho biết hook nào thắng thật**, không phải phỏng đoán.

**Khi nạp order, agent luôn làm thêm một việc:** quét các dòng đã có `HIỆU QUẢ`, đối chiếu với hook mới trong cùng file.

| Phát hiện | Agent nói gì |
|---|---|
| Hook mới **trùng kiểu** với một hook đã `KÉM` | ⚠️ *"Hook này cùng kiểu với [hook cũ] đã chấm KÉM vì [lý do]. Đề xuất đổi."* |
| Hook mới **trùng công thức** với một hook đã `TỐT` | ✓ *"Cùng công thức với [hook cũ] đang TỐT ở [khu vực]. Giữ nguyên, ưu tiên cao."* |
| Hook đã `TỐT` ở một khu vực, order đang làm khu vực khác | → Đề xuất `PORT` sang khu vực đó thay vì viết mới |

⚠️ **Một ad `TỐT` ở miền Nam không tự động `TỐT` ở miền Bắc.** Dữ liệu thật cho thấy cùng một hook chấm ngược nhau giữa hai miền. Ghi rõ khu vực khi dẫn chứng.

---

## 7. ĐỌC FILE — KỸ THUẬT

| Nguồn | Cách đọc |
|---|---|
| Link Google Sheet | Export CSV theo `gid`: `.../export?format=csv&gid=<gid>` |
| File `.xlsx` đính kèm | Đọc từng sheet, giữ tên sheet làm nhãn khối |
| Dán trực tiếp vào chat | Chấp nhận, nhưng **đếm lại số dòng** và báo lại để người order xác nhận không mất dòng |

**Ba việc luôn làm sau khi nạp:**
1. Báo **số dòng đọc được** / số dòng bỏ qua + lý do bỏ.
2. Báo **ô trống thuộc cổng A** theo từng dòng.
3. Báo **dòng có mâu thuẫn** (vd `A1` + `PER`, hoặc format không thuộc ô camp).

⛔ Không im lặng tự sửa mâu thuẫn. Nêu ra, đề xuất, rồi hỏi.

---

## 8. MÃ KỊCH BẢN — TRUY VẾT

Mỗi phiếu có một mã, để nối ngược về dòng order và nối xuôi tới ad đã chạy:

```
KB-<DV><CD>-<nấc>-<nnn>

KB-MUI3-A3-007   = kịch bản mũi · chân dung CD3 (Sửa lại) · nấc A3 · số thứ tự 007
KB-MAT1-A2-012   = kịch bản mắt · CD1 · A2 · 012
```

Cột `Nguồn order` ghi: `<tên sheet> · <nhãn khối> · dòng <n>` — VD `KH SX ND FB ADS · TUẦN 4 T10 · dòng 37`.

---

<a id="om-C-tri-thuc-khach-hang"></a>

## ⟦ om-C-tri-thuc-khach-hang.md ⟧

# om-C · TRI THỨC KHÁCH HÀNG — 6 CHÂN DUNG × 5A × CÔNG THỨC HOOK

> Sổ này trả lời: **khách là ai, sợ gì, ở nấc nào thì nghe được câu gì — và hook nào đã chứng minh thắng, hook nào đã chứng minh thua.**
> ⚠️ §5 là phần đắt nhất của cả agent: rút từ **91 ad thật đã chấm**, không phải lý thuyết.
>
> **Phạm vi:** §1–§4 là dữ liệu **chuyên khoa MŨI**. ★ **§5 công thức hook và §6 cách viết hook mới dùng cho MỌI dịch vụ.**
> Chuyên khoa **MẮT** → `om-J`. ⚠️ Khi chấm hook mắt, nói rõ: công thức §5 rút từ **ad mũi**, áp sang mắt là suy luận hợp lý chưa phải bằng chứng (`om-J` §0).

---

## 1. SÁU CHÂN DUNG — ĐỌC THEO CHIỀU NGANG

### CD1 · Mũi · Khuyết điểm — *trụ cột, ~50% sản lượng*
| | |
|---|---|
| **Ai** | 22–40 tuổi · nhân viên văn phòng, mẹ bỉm, bán hàng online, nhân viên kinh doanh · thu nhập trung bình |
| **Gõ gì vào AI** | *"Dáng mũi nào đẹp, tự nhiên, hợp mặt, không lộ?"* · *"Có đau không, nghỉ bao nhiêu ngày?"* · *"Giá trọn gói bao nhiêu, có phát sinh?"* · *"Có bảo hành vĩnh viễn không?"* |
| **⛔ Nỗi sợ chi phối** | Sợ mũi **giả / đơ**, không hợp mặt · sợ biến chứng phải làm lại · sợ sưng lâu ảnh hưởng công việc · **sợ bị "làm hớ"** |
| **Khát khao thật** | Lột xác nhẹ nhàng nhưng đẹp rõ · **đẹp mà không ai biết đã làm** · một lần làm dùng cả đời · tự tin giao tiếp, được chồng ủng hộ |
| **Rào cản** | Chồng/gia đình cấm · khó xin nghỉ làm · **thiếu niềm tin vào quảng cáo** · ở xa đi lại tốn kém |
| **⚡ Trigger** | Video khách **giống mình** (mẹ bỉm, NVVP) lột xác · bóc seal sụn + phòng mổ vô khuẩn · profile BS được trực tiếp thăm khám · combo giá trọn gói + bảo hành văn bản |
| **Thông điệp thắng** | *"Một lần nâng mũi — đẹp tự nhiên trọn đời — an toàn là trên hết"* |
| **Format ưu tiên** | Review thật 30s B/A 7 ngày · livestream BS tư vấn · ảnh B/A cam thường · bảng giá minh bạch · profile BS |

### CD2 · Mũi · Hot Face — *test nhỏ, ~6%*
| | |
|---|---|
| **Ai** | 22–32 tuổi · TikToker, KOC/KOL, mẫu ảnh, MUA, stylist, sinh viên · thu nhập 8–20tr nhưng chi mạnh cho làm đẹp · sống trên TikTok/IG, **quyết định nhanh** |
| **Gõ gì** | *"Dáng mũi nào đang hot trend?"* · *"Bao lâu thì chụp ảnh được?"* · *"Có cần kiêng make up lâu không?"* · *"Có trả góp sinh viên không?"* |
| **⛔ Nỗi sợ** | Sợ **mũi không lên hình đẹp** · sợ dáng lỗi thời · **sợ sưng lâu không livestream/chụp job được** · sợ bạn bè chê "mũi giả" |
| **Khát khao** | Mũi như idol TikTok · lên hình góc nào cũng xinh · tăng follow, tăng booking job · **đẹp nhanh, hồi phục nhanh** |
| **Rào cản** | Tài chính sinh viên · sợ bố mẹ biết · sợ nghỉ học/nghỉ job dài |
| **⚡ Trigger** | Idol/KOC mình follow vừa làm ở đây · clip *"7 ngày hồi phục thần tốc"* · trả góp 0% · combo mũi + cằm V-line |
| **Thông điệp thắng** | *"Nâng mũi — lên hình auto xinh, 7 ngày hồi phục"* |
| **⛔ Pháp chế riêng** | **Target 18+ bắt buộc** · ⛔ không dùng tên KOL/người nổi tiếng · ⛔ không nội dung hướng người dưới 18 |

### CD3 · Mũi · Sửa lại — *trụ cột thứ hai, cùng CD6 ~25%*
| | |
|---|---|
| **Ai** | 28–50 tuổi · mũi co rút, lệch, lộ sống, bóng đỏ, viêm · thu nhập 20–50tr · **đã chi 30–100tr cho mũi hỏng** |
| **Tâm lý** | ⚠️ **Mất niềm tin trầm trọng**, stress, trầm cảm nhẹ · từng trải nghiệm xấu nơi khác |
| **Gõ gì** | *"Bác sĩ có sửa được ca khó của em không?"* · *"Dùng sụn gì để không co rút lại?"* · *"Có phải tháo ra đặt lại không?"* · *"Có giấy bảo hành sửa không?"* |
| **⛔ Nỗi sợ** | Sợ hỏng lần nữa · **sợ không ai chịu trách nhiệm** · sợ bị lừa lần 2 · **sợ càng sửa càng xấu** · sợ phải tháo mũi sống tẹt |
| **Khát khao** | **Muốn được cứu, trở lại bình thường** · quên ám ảnh mũi hỏng · tìm *"bác sĩ cuối cùng"* · không phải đeo khẩu trang |
| **⚡ Trigger** | Video BS **bóc tách sụn hỏng** · ca sửa co rút **giống hệt mình** · BS phân tích CT 3D chỉ nguyên nhân hỏng cũ · bảo hành văn bản · BS trưởng trực tiếp mổ · tư vấn 1-1 60 phút |
| **Thông điệp thắng** | *"Sửa mũi hỏng — ca càng khó, bác sĩ càng chuyên sâu"* |
| **Format ưu tiên** | **L03 BS phân tích ca thật** (chủ lực) · L06 câu chuyện KH · L07 hành trình giải cứu |

### CD4 · Mũi · Nam giới — *~12%*
| | |
|---|---|
| **Ai** | Nhân viên sale, streamer, LGBT · thu nhập 15–30tr · chịu ảnh hưởng mạnh bởi bạn bè & MXH |
| **Gõ gì** | *"Dáng mũi nào nam tính, không bị nữ tính?"* · *"Làm xong có bị lộ không?"* · *"Bao lâu đi làm lại được?"* · *"Có ảnh hưởng tướng số?"* |
| **⛔ Nỗi sợ** | **Sợ bị chê "đàn ông đi thẩm mỹ"** · sợ mũi cao quá thành giả, nữ tính · sợ bầm tím lâu · sợ ảnh hưởng phong thuỷ |
| **Khát khao** | Mặt góc cạnh, nam tính · phong thuỷ thăng tiến sự nghiệp · **đẹp lên nhưng vẫn men** |
| **⚡ Trigger** | KOL nam / case KH nam **giống mình** · dáng mũi nam tự nhiên không lộ · **tư vấn 1-1 với bác sĩ nam** |
| **Thông điệp thắng** | *"Mũi chuẩn men — đẹp tự nhiên, không ai biết đã làm"* |

### CD5 · Mũi · Phong thuỷ — *test nhỏ, ~6%*
| | |
|---|---|
| **Ai** | 28–45 tuổi · chủ doanh nghiệp, thương nhân, BĐS, môi giới, livestream bán hàng · thu nhập >25–50tr |
| **Bối cảnh** | Đang gặp vận xui, sự nghiệp chững lại, tình duyên trắc trở · **nghe lời thầy tướng số khuyên sửa tướng mũi** |
| **Gõ gì** | *"Tướng mũi Lộc Tài là thế nào?"* · *"Dáng mũi nào hợp mệnh Kim/Mộc/Thuỷ/Hoả/Thổ?"* · *"Nâng mũi xong có bị phá tướng không?"* |
| **⛔ Nỗi sợ** | Sợ **phá mất lộc** hiện tại · sợ mũi hếch lộ lỗ mũi (*"hao tài tốn của"*) · sợ sống mũi lệch (*"đường đời trắc trở"*) · sợ chọn lầm ngày mổ |
| **Khát khao** | Dáng mũi chuẩn nhân tướng: **sống mũi thẳng, đầu mũi tròn đầy, cánh mũi gọn giữ tiền** · thần thái khi gặp đối tác lớn |
| **Rào cản** | Chưa tìm được BS vừa giỏi y khoa vừa hiểu tướng số · sợ bị đánh giá là mê tín |
| **⛔ Pháp chế riêng** | 🔴 **ĐỎ nếu hứa "đổi vận / tài lộc / giải hạn"** — chỉ được nói về **hình thái dáng mũi**, không nói về hiệu quả phong thuỷ |

### CD6 · Mũi · Khó, bệnh lý — *cùng CD3 ~25%*
| | |
|---|---|
| **Ai** | Mũi dị tật bẩm sinh (sứt môi chẻ vòm, hở hàm ếch), biến dạng do tai nạn, hoặc **hỏng sau nhiều lần phẫu thuật** (viêm, co rút bao xơ, thủng đầu mũi, lệch vẹo nặng) |
| **Tâm lý** | Tự ti, mặc cảm, ngại giao tiếp xã hội |
| **Gõ gì** | *"Mũi sứt môi / tai nạn / co rút bao xơ có sửa lại thành bình thường được không?"* · *"Bác sĩ nào mát tay chuyên ca khó?"* · *"Tỷ lệ thành công bao nhiêu %?"* |
| **⛔ Nỗi sợ** | **Sợ phẫu thuật thất bại (lớn nhất)** · sợ BS không đủ kinh nghiệm · sợ biến chứng nặng hơn (**ảnh hưởng chức năng thở**) · sợ tốn kém vô ích |
| **Khát khao** | ⚠️ **Không cần quá cao, quá đẹp** — chỉ cần **tự nhiên, cân đối như người bình thường** · lấy lại tự tin cơ bản · **được chữa lành tổn thương tâm lý** |
| **⚡ Trigger** | Video *"Tái sinh"* ca cực khó **giống hệt tình trạng của họ** · BS trưởng khoa siêu âm cấu trúc + phác đồ cá nhân hoá · cam kết văn bản · hỗ trợ chi phí / trả góp |
| **Thông điệp thắng** | *"Tái sinh dáng mũi — chữa lành mọi khuyết điểm, trả lại tự nhiên"* |
| **⛔ Pháp chế riêng** | **Mọi ca thật → consent bắt buộc** · ⛔ không quay cảnh can thiệp/phẫu thuật · ⛔ không nêu tỷ lệ thành công nếu không có nguồn |

⚠️ **CD6 khác CD3 ở đâu:** CD3 là *mũi đã làm thẩm mỹ nhưng không ưng / hỏng*; CD6 là *dị tật, bệnh lý, hoặc hỏng nặng có ảnh hưởng chức năng*. CD6 khát khao **bình thường**, CD3 khát khao **được cứu**. Viết lẫn hai cái là mất cả hai tệp.

---

## 2. FORMAT ƯU TIÊN THEO CHÂN DUNG

| Chân dung | Format chủ lực | Vì sao |
|---|---|---|
| CD1 | `L04` B/A · `L06` review · `L11` giá minh bạch · `L01` talk hỏi đáp | Sợ "làm hớ" + cần thấy người giống mình |
| CD2 | `L05` biến đổi ngày 1-3-7 · `L02` talk chủ đề | Chỉ quan tâm mốc hồi phục & trend |
| CD3 | `L03` BS phân tích ca thật · `L06` câu chuyện · `L07` hành trình | Mất niềm tin → cần cơ chế + bằng chứng, không cần lời khen |
| CD4 | `L04` B/A nam · `L05` 7 ngày đi làm lại · `L02` | Sợ bị lộ, sợ nữ tính |
| CD5 | `L03` phân tích hình thái · `L01` | Cần chuyên môn về hình thái, ⛔ không hứa vận |
| CD6 | `L06` câu chuyện/tài liệu · `L03` phân tích ca khó | Cần thấy ca giống hệt mình được xử lý |

---

## 3. HÀNH TRÌNH 5A — KHÁCH Ở NẤC NÀO NGHE ĐƯỢC CÂU GÌ

| Nấc | Khách đang nghĩ | ⛔ Nỗi sợ chi phối | Nội dung phải có | CTA chuẩn của nấc |
|---|---|---|---|---|
| **A1 · AWARE** | *"Mũi mình thấp/tẹt làm mặt kém xinh? Mũi phải cao mới đẹp."* | Không biết mũi mình cần chỉnh gì · sợ làm xong còn xấu hơn | So sánh mũi thấp vs cao **trên cùng một khuôn mặt** · BS talk chủ đề rộng | *"Xem hành trình lột xác 7 ngày"* |
| **A2 · APPEAL** | *"Nâng ở đâu uy tín? Chọn dáng nào hợp? Công nghệ/sụn nào tốt?"* | Sợ dáng không hợp mặt, **trông giả**, không bền · sợ địa chỉ không uy tín | Thiết kế dáng **cá nhân hoá** · nhiều case B/A · BS "cảnh báo" · công nghệ theo từng tình trạng | *"Gửi ảnh — bác sĩ tư vấn dáng mũi hợp mặt"* |
| **A3 · ASK** | *"Có đau không? Nghỉ mấy ngày? Giá bao nhiêu, có phát sinh? Bảo hành?"* | Sợ giá cao & phát sinh · sợ sưng lâu ảnh hưởng việc · **sợ không ai chịu trách nhiệm** | Hành trình một ngày · **bảng giá minh bạch + quyền lợi** · chính sách bảo hành · mốc hồi phục 1-3-7-30 · FAQ 5 câu phải hỏi BS | *"Đặt lịch tư vấn trực tiếp với bác sĩ"* |
| **A4 · ACT** | *"Chốt thôi! Nhưng chọn ngày nào? Bao giờ có ưu đãi sâu?"* | Sợ hết suất ưu đãi · sợ đau · sợ phải ở lại lâu | Lịch trình đi làm · bảng giá ngày vàng · thăm khám 0đ · **checklist trước mổ** | *"Inbox giữ lịch / giữ suất"* |
| **A5 · ADVOCATE** | *"Kiêng gì, kiêng bao lâu? Có cần tái khám?"* | Kiêng nhiều, phức tạp · không có thời gian tái khám | Hướng dẫn chăm sóc sau mổ · dấu hiệu cần quay lại ngay · cross-sell **một hướng** | *"Lưu video — nhắn nếu cần hỗ trợ hậu phẫu"* |

⚠️ **A5 gần như luôn là ô trống** trong mọi file order. Đây là lỗ hổng phễu rẻ nhất để lấp: tệp `CUST` đã có, chi phí thấp, mở đường cross-sell.

---

## 4. MA TRẬN LỖ HỔNG PHỄU — CÁCH ĐỌC

Đếm số content đang giữ theo ô `CD × nấc`. **Ô = 0 là lỗ hổng.**

Ví dụ thật (pilot mũi, 34 content đang giữ):

| Nấc | CD1 | CD2 | CD3 | CD4 | CD5 | CD6 |
|---|---|---|---|---|---|---|
| A1 | 4 | **0** | **0** | **0** | **0** | 1 |
| A2 | 14 | **0** | 2 | 1 | **0** | 1 |
| A3 | 6 | **0** | **0** | 1 | **0** | **0** |
| A4 | 3 | **0** | **0** | 1 | **0** | **0** |
| A5 | **0** | **0** | **0** | **0** | **0** | **0** |

**Ba kết luận đọc ra ngay:**
1. **CD1 chiếm 27/34** — phễu dựa gần như toàn bộ vào một chân dung. Rủi ro tập trung.
2. **Cả hàng A5 trống** — không nuôi khách đã làm, mất hết cross-sell.
3. **CD2 và CD5 bằng 0** — chưa có dữ liệu để biết nên giữ hay bỏ, nên **test nhỏ trước khi kết luận**.

⛔ **Không đề xuất lấp mọi ô trống cùng lúc.** Tỷ trọng đã kiểm chứng: `CD1 ~50% · CD3+CD6 ~25% · CD4 ~12% · CD2+CD5 ~12% (test nhỏ)`.

---

## 5. ★ CÔNG THỨC HOOK — RÚT TỪ 91 AD ĐÃ CHẤM

> ⚠️ Đây là bước B4. Chấm hook **trước khi** viết kịch bản.

### ✓ BỐN THÀNH PHẦN CỦA CÔNG THỨC THẮNG

```
① GỌI ĐÚNG TÌNH TRẠNG      khách tự nhận ra mình trong 3 giây
② GIẢI PHÁP KỸ THUẬT       có cơ chế, có tên kỹ thuật — không chỉ hứa kết quả
③ BẰNG CHỨNG               ca thật · theo dõi dài hạn · bóc seal · CT/ảnh
④ CTA GỬI ẢNH TÌNH TRẠNG   rẻ hơn "nhận báo giá", vì khách chưa muốn nói chuyện tiền
```

### ★ Luật chấm — thành phần ① là cổng

> **① GỌI ĐÚNG TÌNH TRẠNG là thành phần quyết định, không phải "một trong bốn".**

| Chấm | Điều kiện |
|---|---|
| `✓ QUAY ĐƯỢC` | **Có ①** *(dù chỉ một mình)*, **hoặc** có ≥2 thành phần khác |
| `⚠ SỬA RỒI QUAY` | Có ② hoặc ③ nhưng **thiếu ①** → thêm tình trạng vào là xong |
| `✗ ĐỔI HOOK` | Không có thành phần nào, **hoặc** trúng một trong 7 kiểu KÉM |

⚠️ **Vì sao ① một mình là đủ:** dữ liệu thật cho thấy *"Mũi từng nâng nhưng không đẹp thì bao lâu sửa lại được?"* chỉ có ① mà chấm **TỐT**. Ngược lại hook có ② ③ đầy đủ nhưng không gọi tình trạng thì khách không nhận ra mình, nên không dừng lại ở giây thứ 3.

⚠️ **Trúng kiểu KÉM nhưng vẫn có ①** → `⚠`, không phải `✗`. Giữ phần gọi tình trạng, bỏ phần vi phạm. VD *"SỰ THẬT CHẤN ĐỘNG: chị em miền Tây…"* → bỏ chữ *CHẤN ĐỘNG*, giữ nguyên phần còn lại (ad này chấm **TỐT**).

Ví dụ ad **TỐT** thật:

| Hook | Thành phần | Khu vực |
|---|---|---|
| *"Mũi thấp tẹt, đầu mũi hếch sửa sao cho đẹp"* | ①③ | Nam + Miền Tây — *winner rõ nhất hệ* |
| *"Mũi ngắn, đầu mũi hếch chỉ có nâng mũi cấu trúc mới khắc phục được"* | ①② | Nam |
| *"6 năm sau nâng mũi, dáng mũi của khách hàng Kangnam giờ ra sao?"* | ③ | Nam |
| *"Mũi tẹt, cánh mũi to nên nâng mũi hay cắt cánh?"* | ①② | Nam |
| *"Kangnam có dám bảo hành nâng mũi trọn đời đâu?"* | ③ + nghịch lý | Nam |
| *"Hành trình tìm lại sự cân đối cho dáng mũi dị tật bẩm sinh"* | ①③ | Cả 2 |
| *"Mũi từng nâng nhưng không đẹp thì bao lâu sửa lại được?"* | ① | Cả 2 |

### ✗ BẢY KIỂU HOOK ĐÃ CHỨNG MINH LÀ KÉM

| Mã | Kiểu | Ví dụ thật đã chấm KÉM | Vì sao thua |
|---|---|---|---|
| `H1` | **Tính từ chung chung** | *"Làm sao để có chiếc mũi vạn người mê"* · *"Sở hữu dáng mũi SLAY nét căng"* · *"Nâng mũi tặng mình phiên bản xuất sắc hơn"* | Không ai tự nhận mình là người cần "mũi vạn người mê". Tính từ không gọi được tình trạng. |
| `H2` | **Mở bằng giá** | *"Nâng mũi đẹp chuẩn Hàn chỉ 31TR hưởng trọn 7 quyền lợi"* | Giá mở đầu biến video thành hỏi giá, không thành tư vấn. Giá chỉ nên xuất hiện ở A4. |
| `H3` | **Hook mơ hồ** | *"Hành trình nâng mũi của tôi"* | Không nói được đây là hành trình của ai, tình trạng gì. |
| `H4` | **Quá ngắn, không gọi tình trạng** | *"Nâng mũi chống lệch"* | Ba chữ không đủ để khách nhận ra mình. |
| `H5` | **Hứa mốc thời gian / kết quả** | *"Nâng mũi bao lâu đẹp tự nhiên?"* · *"Nâng mũi Idol — đẹp ngay sau 60'"* | Vừa KÉM vừa **rủi ro pháp chế** — sai thực tế hậu phẫu. |
| `H6` | **Tên người nổi tiếng** | *"Em thích dáng mũi Triệu Lộ Tư"* | Chấm BÌNH THƯỜNG + rủi ro quyền hình ảnh. |
| `H7` | **Từ giật gân** | *"SỰ THẬT CHẤN ĐỘNG: ..."* | Bản thân công thức thắng (local/miền Tây), nhưng chữ *CHẤN ĐỘNG* phải bỏ — cờ VÀNG. |

### ⚠️ BA ĐIỀU TINH TẾ TỪ DỮ LIỆU

1. **Cùng một hook chấm ngược nhau giữa hai miền.** *"Bóc seal mũi Surgiform sau 10 ngày"* — PERF Bắc **TỐT**, VIEW Nam **KÉM**. → ⛔ Không kết luận "hook này tốt" mà không nói khu vực + loại camp.
2. **Hook tốt đặt sai ô vẫn thua.** *"Vì sao 90% người nâng mũi lần đầu chọn sai dáng"* — chạy VIEW thì BT, chạy PERF thì BT. Hook A1 không dùng cho PERF.
3. **Ý tốt nhưng thực hiện kém vẫn KÉM.** *"Mẹ em làm mũi Kangnam hơn 10 năm vẫn đẹp"* chấm KÉM — nhưng ý "theo dõi dài hạn" là đúng, nên **quay lại thành series** chứ không bỏ ý.

→ Vì vậy khi gắn cờ `✗`, agent phải nói rõ: **bỏ cả ý, hay giữ ý và quay lại cho đúng?**

### ⚠️ LUẬT ĐỔI HOOK — KHÔNG IM LẶNG THAY CHỮ

Hook là tài sản của người order. Đổi thì in **ba dòng**:

```
HOOK GỐC      : "Mũi ngắn, đầu mũi hếch chỉ có nâng mũi cấu trúc mới khắc phục được"
HOOK ĐỀ XUẤT  : "Mũi ngắn, đầu mũi hếch: vì sao bác sĩ thường chọn nâng cấu trúc?"
VÌ SAO ĐỔI    : 🟡 VÀNG — "chỉ có... mới" là khẳng định tuyệt đối (om-G L04).
                Giữ nguyên thành phần ① và ②, chỉ hạ mức khẳng định.
```

---

## 6. VIẾT HOOK MỚI — KHI ORDER CHỈ CÓ CHỦ ĐỀ

Khi cổng A ô A3 trượt, hoặc khi lấp lỗ hổng phễu. **Năm bước:**

1. **Lấy nỗi sợ chi phối** của chân dung đó ở nấc đó (§1 + §3) — ⛔ không lấy khát khao, nỗi sợ bán tốt hơn.
2. **Viết lại nỗi sợ thành câu khách tự gõ** — dùng đúng từ khách dùng (*"mũi tẹt"*, *"bóng đỏ"*, *"co rút"*), ⛔ không dùng từ chuyên môn khách không gõ.
3. **Gắn một thành phần ② hoặc ③** — tên kỹ thuật, hoặc một bằng chứng.
4. **Soát qua 7 kiểu KÉM** (§5) — trúng kiểu nào thì viết lại.
5. **Gắn CTA theo nấc** (§3), ưu tiên *"gửi ảnh tình trạng"*.

⛔ **Mỗi hook mới phải ghi rõ `[HOOK AGENT ĐỀ XUẤT — chưa qua duyệt]`.** Không trộn lẫn với hook người order viết.
⛔ **Hook mới chỉ lên ads khi `DUYỆT = 🟢 XANH`** (BS + pháp chế). Lịch duyệt thực tế: **thứ Tư hằng tuần**.

---

<a id="om-D-thu-vien-format"></a>

## ⟦ om-D-thu-vien-format.md ⟧

# om-D · THƯ VIỆN FORMAT L01–L16

> Sổ này trả lời: **mỗi format quay cái gì, cấu trúc theo giây ra sao, dài bao nhiêu, quay ở đâu, cần đạo cụ gì, đo bằng chỉ số nào.**
>
> ⛔ **Mã L01–L16 là thư viện chung, GIỮ NGUYÊN cho mọi dịch vụ** để so sánh hiệu suất chéo tuyến. Dịch vụ mới chỉ **đánh dấu format ưu tiên**, và chỉ bổ sung dòng riêng từ `L17+` khi thật cần.
> ⛔ **Không có video "sáng tạo tự do".** Mọi clip phải thuộc một mã.

---

## 1. BẢNG FORMAT

### L01 · Bác sĩ — Talk hỏi đáp
| | |
|---|---|
| **Làm gì** | Series giải đáp các câu hỏi khách hay hỏi. Xương sống sản lượng. |
| **Cấu trúc** | `0–3s` đọc câu hỏi (con số / phủ định) — *"Chị sợ nhất là phải tháo mũi ra?"* · `3–20s` giải thích lý do · `20–30s` CTA *"gửi ảnh để bác sĩ check"* |
| **Thời lượng** | 25–35s |
| **Chỉ số đo chính** | Giữ chân 3s · share |
| **Bối cảnh** | Studio cố định |
| **Trụ cột** | Dr. Trust |

### L02 · Bác sĩ — Talk chủ đề
| | |
|---|---|
| **Làm gì** | BS chia sẻ quan điểm nghề, triết lý làm đẹp về một chủ đề. **Tạo khác biệt.** |
| **Cấu trúc** | `0–3s` nghịch lý — *"Tôi từ chối 30% ca đến tư vấn — vì sao?"* · `3–40s` quan điểm · `40–50s` kết luận |
| **Thời lượng** | 40–60s |
| **Chỉ số đo chính** | Xem hết · bình luận chuyên môn |
| **Bối cảnh** | Phòng khám + màn hình |

### L03 · Bác sĩ — Phân tích ★ *chủ lực CD3 / CD6*
| | |
|---|---|
| **Làm gì** | BS phân tích **một ca thật**, chỉ CT, chỉ ảnh. Giáo dục giải pháp. |
| **Cấu trúc** | `0–3s` *"Ca này co rút độ 2 vì…"* (con số) · `3–10s` show CT/ảnh · `10–35s` phân tích cơ chế + giải pháp |
| **Thời lượng** | 30–45s |
| **Chỉ số đo chính** | Xem hết · lưu |
| **Bối cảnh** | Sảnh → khám → hồi phục |
| **⛔ Chặn** | Ảnh/CT phải **che mặt**; ca thật → **consent**; ⛔ không để lọt hồ sơ bệnh nhân khác vào khung |

### L04 · Khách hàng — Trước/sau
| | |
|---|---|
| **Làm gì** | So sánh trước–sau, rõ thay đổi |
| **Cấu trúc** | `0–2s` before · `2–5s` after · `5–15s` thông tin nhóm — *"nhóm da mỏng, mũi tẹt"* |
| **Thời lượng** | 10–15s |
| **Chỉ số đo chính** | CTR · tỷ lệ inbox |
| **Bối cảnh** | Studio + bảng giá |
| **Trụ cột** | Case Trust |
| **⛔ Chặn** | **Cùng góc, cùng sáng, cùng trang phục, không chỉnh sửa hình thể** · ghi mốc thời gian + phương pháp · **bắt buộc dòng** *"Kết quả khác nhau tuỳ thể trạng từng người"* (`om-G` L07) |

### L05 · Khách hàng — Biến đổi ★ *chủ lực CD2 / CD4*
| | |
|---|---|
| **Làm gì** | Ghép quá trình hồi phục ngày 1–3–7–14–30 |
| **Cấu trúc** | `0–3s` *"Ngày 1 sưng 100% — ngày 7 còn bao nhiêu?"* · `3–20s` lướt nhanh các mốc · kết *"ngày 7 đi làm"* |
| **Thời lượng** | 15–25s |
| **Chỉ số đo chính** | Bình luận / 1.000 view |
| **Bối cảnh** | Studio cố định |
| **⛔ Chặn** | **Mốc hồi phục phải do BS duyệt** — ⛔ không tự đặt số ngày |

### L06 · Khách hàng — Review
| | |
|---|---|
| **Làm gì** | Khách tự chia sẻ cảm nhận kết quả, quá trình hồi phục, bác sĩ, địa chỉ |
| **Cấu trúc** | `0–3s` cảm xúc — *"2 năm đeo khẩu trang…"* · `3–30s` kể hành trình · `30–35s` cảm ơn bác sĩ |
| **Thời lượng** | ≤45s |
| **Chỉ số đo chính** | Lưu · share |
| **Bối cảnh** | Studio + đồ hoạ |
| **⛔ Chặn nặng** | ⚠️ **L06 là format rủi ro pháp chế cao nhất.** ⛔ Không dùng thư cảm ơn / lời chứng thực của người bệnh làm nội dung QC dịch vụ KCB (`om-G` L06). Muốn kể chuyện khách → trình bày dạng **ghi nhận quá trình điều trị có mốc, có chỉ số**, không dạng lời khen dịch vụ. **Rà cùng pháp chế trước khi đăng.** |

### L07 · Khách hàng — Hành trình
| | |
|---|---|
| **Làm gì** | POV khách đi làm đẹp một ngày, từ nhà đến viện về |
| **Cấu trúc** | `0–3s` *"6h sáng đi nâng mũi — có run không?"* · `3–60s` các bước: xét nghiệm, mổ, về · kết: tươi cười |
| **Thời lượng** | 45–90s |
| **Chỉ số đo chính** | **LƯU (cao nhất hệ)** |
| **Bối cảnh** | Studio · phòng khám |
| **⛔ Chặn** | ⛔ **Không quay cảnh can thiệp/phẫu thuật** · consent · ⛔ không để lọt màn hình chứa dữ liệu cá nhân |

### L08 · Khách hàng — Kết quả
| | |
|---|---|
| **Làm gì** | Tập trung show kết quả sau mổ 45 phút, dáng mũi sau 7–10 ngày, 1 tháng… |
| **Cấu trúc** | `0–3s` *"Sụn này một miếng 45 triệu — vì sao?"* · `3–25s` bóc seal, show chất liệu, giải thích cơ chế |
| **Thời lượng** | 20–35s |
| **Chỉ số đo chính** | **Tỷ lệ inbox (cao nhất hệ)** |
| **Bối cảnh** | Phòng khám |
| **⛔ Chặn** | 🟡 Nêu **tên thương mại vật liệu** (vd Surgiform) là cờ VÀNG — rà soát trước khi đăng |

### L09 · Dịch vụ — Công nghệ
| | |
|---|---|
| **Làm gì** | Show công nghệ, kỹ thuật, máy móc, sụn, AI face design |
| **Cấu trúc** | `0–3s` *"Vừa mổ xong 45 phút — đau không em?"* · `3–20s` khách cười, soi gương, chạm mũi nhẹ; BS kiểm tra, dặn dò |
| **Thời lượng** | 15–30s |
| **Chỉ số đo chính** | Bình luận tích cực · xem hết · share · giữ chân 3s |
| **Bối cảnh** | Phòng khám · studio + đồ hoạ số |
| **Trụ cột** | Brand Trust |
| **⛔ Chặn** | 🟡 *"không đau"* chỉ được là **lời khách kể**, ⛔ bỏ khỏi text overlay |

### L10 · Dịch vụ — Quy trình
| | |
|---|---|
| **Làm gì** | Quy trình từ A–Z, checklist |
| **Cấu trúc** | `0–3s` *"Nâng mũi 5 bước — 45 phút — về ngay"* |
| **Thời lượng** | 25–40s |
| **Chỉ số đo chính** | Bình luận tích cực · lưu |
| **Bối cảnh** | Khu tiền mê · hồi sức |
| **⛔ Chặn** | **Thời gian mổ thực tế phải kiểm lại** — ⛔ không lấy số từ hook cũ |

### L11 · Dịch vụ — Giá / Sales / Chính sách
| | |
|---|---|
| **Làm gì** | Show bảng giá trọn gói, ưu đãi, quà tặng, sale ngày vàng |
| **Cấu trúc** | `0–3s` *"35tr trọn gói — không phát sinh — tặng 5tr hôm nay"* (con số) |
| **Thời lượng** | 10–20s |
| **Chỉ số đo chính** | Share · bình luận tích cực |
| **Bối cảnh** | Studio · phòng khám |
| **⛔ Chặn** | 🔴 **Giá và số suất phải khớp bảng giá hiện hành** — số suất không thật là cờ ĐỎ · ⛔ không hứa giá cố định trên bình luận công khai |

### L12 · Local — Cơ sở / Bác sĩ / Công nghệ
| | |
|---|---|
| **Làm gì** | Giới thiệu cơ sở vật chất, địa chỉ, profile bác sĩ · không khí, hậu trường ekip, điều dưỡng, phòng mổ |
| **Cấu trúc** | `[CHỜ XÁC NHẬN]` — sheet nguồn để trống. Mặc định dùng khung 4 khối của `om-E` §1. |
| **Thời lượng** | 20–35s |
| **Chỉ số đo chính** | **LƯU · giảm huỷ lịch** |
| **Bối cảnh** | Studio |
| **⛔ Chặn** | 🔴 **Profile bác sĩ chỉ được nêu khi `om-H` ghi ĐÃ XÁC MINH** · ⛔ không quay cảnh can thiệp |

### L13 · L14 · L15 · L16 — ⚠️ CHƯA ĐỊNH NGHĨA

```
⚠️ [CHỜ XÁC NHẬN] — ai cấp: chủ nhiệm nội dung (Content Lead)

L13, L14, L15 ĐANG ĐƯỢC DÙNG trong kế hoạch Ads (sheet 5):
   V5 · P5  →  L11 · L13
   V3 · P3  →  L09 · L08 · L14
   V4 · P4  →  L15 · L11 · L04
L16 được nhắc trong tiêu đề thư viện ("giữ nguyên mã L01–L16").

NHƯNG sheet Format mẫu chỉ định nghĩa tới L12.
→ ⛔ Agent KHÔNG tự đặt nội dung cho L13–L16.
→ Order chỉ định L13/L14/L15/L16: gắn cờ, đề xuất format gần nhất đã định nghĩa,
  ghi rõ là đề xuất thay thế, và hỏi lại.
```

---

## 2. TRA NHANH — CHỌN FORMAT THEO Ý ĐỊNH

| Muốn làm gì | Format |
|---|---|
| Trả lời một câu khách hay hỏi | `L01` |
| Tạo khác biệt, định vị *"bác sĩ dám nói thật"* | `L02` |
| Thuyết phục người **đã mất niềm tin** | `L03` |
| Cho thấy thay đổi nhanh nhất | `L04` |
| Trả lời *"bao lâu thì đi làm/lên hình được"* | `L05` |
| Kể chuyện một người | `L06` ⚠️ rủi ro pháp chế cao |
| Trả lời *"một ngày ở viện diễn ra thế nào"* | `L07` — lưu cao nhất hệ |
| Show vật liệu, kết quả sau mổ | `L08` — inbox cao nhất hệ |
| Show công nghệ, máy móc | `L09` |
| Trả lời *"quy trình gồm mấy bước"* | `L10` |
| Đẩy ưu đãi, chốt đơn | `L11` |
| Trả lời *"ở đâu uy tín"*, giới thiệu cơ sở | `L12` |

### Hai format có chỉ số vượt trội — dùng đúng chỗ
- **`L07` lưu cao nhất hệ** → dùng ở `A3`/`A4` khi cần giảm huỷ lịch, ⛔ không dùng ở `A1` (quá dài cho người chưa biết vấn đề).
- **`L08` tỷ lệ inbox cao nhất hệ** → dùng ở `P3` (nấc ASK), đây là format đáng nhân rộng nhất khi cần SĐT.

---

## 3. ĐẠO CỤ THEO FORMAT

| Format | Đạo cụ bắt buộc |
|---|---|
| `L01` `L02` | Teleprompter · mic không dây · áo blouse cố định theo nhân vật |
| `L03` | **Ảnh/CT đã che mặt** · màn hình 27" · bút chỉ · bảng viết kính |
| `L04` `L08` | Ảnh/video before đúng góc · mẫu vật liệu còn seal · thước |
| `L05` | Bộ ảnh theo mốc ngày 1-3-7-14-30 **của cùng một khách** · đồ hoạ mốc ngày |
| `L06` `L07` | **Bản consent đã ký** · micro cài áo cho khách · gimbal |
| `L09` | Thiết bị/máy móc thật · đồ hoạ số · mô hình minh hoạ |
| `L10` | Checklist in sẵn · đồ hoạ 5 bước |
| `L11` | **Bảng giá hiện hành bản in** · đồ hoạ số suất |
| `L12` | Cảnh quan cơ sở · đồng phục ekip |

⛔ **Thiếu đạo cụ bắt buộc → không xếp vào lịch quay**, ghi vào khối `[CHỜ XÁC NHẬN]` + ai cấp.

---

## 4. BỐI CẢNH — GOM ĐỂ ĐỠ ĐỔI SET

Đổi set tốn **15 phút**; đổi nhân vật tốn **2 phút**. → Call sheet gom theo **bối cảnh**.

| Mã bối cảnh | Dùng cho format |
|---|---|
| `S-STUDIO` studio cố định, không tháo set | `L01` `L02` `L04` `L05` `L06` `L11` `L12` |
| `S-KHAM` bàn khám + màn hình | `L02` `L03` `L09` |
| `S-SANH` sảnh, lối vào, quầy | `L03` `L07` `L12` |
| `S-TIENME` khu tiền mê, hồi sức | `L10` |
| `S-PHUCHOI` phòng hồi phục | `L03` `L08` `L09` |

⛔ **Không tháo set `S-STUDIO`** — đây là điều kiện tiên quyết để đạt sản lượng batch nhanh.
⛔ **Không quay trong phòng mổ khi đang can thiệp.**

---

## 5. DÒNG SẢN XUẤT — FORMAT NÀO VÀO BATCH NÀO

| Dòng | Nhịp | Sản lượng | Format phù hợp | Ekip |
|---|---|---|---|---|
| **BATCH LỚN** | 2 buổi/tháng, cả ngày | 25–30 clip | Mọi format; bắt buộc cho `L04` `L06` `L07` (cần KH thật) | Toàn ekip |
| **BATCH NHANH** | Thứ Tư 90 phút | 8–10 clip | ⛔ Chỉ `L01` `L02` `L11` (talking head teleprompter) | 2 người |
| **DOCU** | Theo lịch khám | ~10 clip/tháng | `L03` `L05` `L07` — bám ca thật | NV phụ trách ca |
| **CƠ HỘI** | Hằng ngày | ~15 clip/tháng | `L08` `L09` `L12` — quay điện thoại theo SOP | Ai đang có mặt |

⚠️ **Mỗi clip quay tối đa 3 lần.** Quá 3 lần thì chuyển clip khác, quay lại cuối buổi — tránh tụt năng lượng nhân vật.
⚠️ **Trang phục cố định theo nhân vật cả ngày** — để clip phát rải trong 30 ngày mà không lộ quay gộp.
⛔ **Sao lưu trong ngày.** Không để footage qua đêm trên thẻ nhớ.

---

## 7. ★ KỊCH BẢN MẪU CÓ THẬT — TRA TRƯỚC KHI VIẾT

> Khối có **thư viện kịch bản thật, mỗi format một file**. ⛔ **Luôn tra kịch bản mẫu của format đó trước khi viết mới** — khuôn cột, thuật ngữ dựng và thông số text lấy từ đó (`om-I`).

**Mục lục:** `docs.google.com/spreadsheets/d/1g4ti7tIY0pLqu-Hv305tIVDjnU_qlMyL3lLUOOkkvlY` *(cột `Format` → cột `Link kịch bản`)*

| Format | Kịch bản mẫu |
|---|---|
| `L01` | ⚠️ **TRỐNG** — chưa có mẫu. Dùng khuôn `L03` rút gọn, ghi rõ là khuôn mượn |
| `L02` … `L12` | Có mẫu, tra qua mục lục trên |

⚠️ **Kịch bản mẫu hiện có là của chuyên khoa MẮT (cắt mí).** Viết cho **mũi** thì mượn **khuôn** *(cột · nhịp · thuật ngữ · thông số text)*, ⛔ **không mượn nội dung y khoa** — chỉ định, mốc hồi phục, công nghệ của mắt khác hoàn toàn của mũi.

⛔ **Không mượn con số từ kịch bản mắt sang mũi**: giá, thời gian mổ, mốc cắt chỉ, thời hạn bảo hành đều khác theo dịch vụ.

---

## 6. ƯỚC THỜI GIAN QUAY

| Format | Phút/clip (đã gồm set up) |
|---|---|
| `L01` `L02` teleprompter, set sẵn | 8–10 |
| `L04` `L11` đồ hoạ nhiều, quay ít | 10–12 |
| `L03` `L09` cần màn hình, đạo cụ | 15–20 |
| `L05` `L08` cần bộ ảnh/vật liệu | 15–20 |
| `L06` `L07` có khách thật | 30–45 |
| `L10` `L12` nhiều bối cảnh | 20–30 |

Cộng thêm **15 phút mỗi lần đổi bối cảnh**. Dùng để tính xem call sheet có vừa một buổi hay không.

---

<a id="om-E-kich-ban-san-xuat"></a>

## ⟦ om-E-kich-ban-san-xuat.md ⟧

# om-E · VIẾT KỊCH BẢN & ĐẦU RA

> Sổ này trả lời: **lời thoại viết thế nào, shot list ghi thế nào, bảng đầu ra có cột gì, và call sheet xếp ra sao.**
>
> ★ **ĐỌC `om-I` TRƯỚC SỔ NÀY.** Đầu ra có **hai tầng**:
> `TẦNG 1` **phiếu order** — 1 dòng = 1 clip, 42 trường (§4 sổ này), cho quản lý & điều phối.
> `TẦNG 2` **kịch bản chi tiết** — 1 dòng = 1 nhịp, theo **khuôn nhà** (`om-I` §2), cho editor & DOP.
> ⛔ Không gộp hai tầng vào một bảng. Trường `LỜI THOẠI THEO MỐC GIÂY` ở §4 là **con trỏ** sang sheet kịch bản tầng 2, không phải chỗ nhét cả 25 nhịp.
> §1–§3 dưới đây là **luật viết nội dung**; **khuôn trình bày** theo `om-I`.

---

## 1. BỐN KHỐI LỜI THOẠI — KHUNG BẮT BUỘC

Mọi kịch bản, mọi format, đều có đúng bốn khối. Khác nhau ở **độ dài từng khối**, không khác ở cấu trúc.

```
HOOK      0–3s    câu mở, đọc nguyên văn + TEXT ON SCREEN
BỐI CẢNH  3–8s    đặt người nói vào đâu, vì sao nên tin
LÕI       8–40s   ★ CƠ CHẾ — chia theo mốc giây nhỏ
CTA       40–55s  gửi gì – nhận gì
```

### ⛔ Bốn điều cấm khi viết lời thoại

| ⛔ Cấm | Vì sao |
|---|---|
| Viết lời thoại **không có mốc giây** | Editor không biết cắt ở đâu |
| Viết *"bác sĩ giải thích về filler"* | Đó là **mô tả**, không phải lời thoại. Phải là **câu đọc được nguyên văn** |
| Khối LÕI **không có cơ chế**, chỉ toàn lời khen | Lời khen không tạo niềm tin, và là rủi ro pháp chế (`om-G` L06) |
| CTA chung chung — *"inbox ngay"* trơ trọi | Phải nói rõ **gửi gì, nhận gì** |

### Ví dụ đủ chuẩn

```
MÃ        : KB-MUI3-A2-004
FORMAT    : L01 · Bác sĩ — Talk hỏi đáp  ·  28s  ·  S-STUDIO

HOOK 0–3s
  THOẠI : "Mũi đã tiêm filler, giờ muốn nâng thì phải làm sao?"
  TEXT  : MŨI ĐÃ TIÊM FILLER → NÂNG ĐƯỢC KHÔNG?

BỐI CẢNH 3–8s
  THOẠI : "Mỗi tuần tôi gặp năm đến bảy ca như vậy."
  B-ROLL: bàn khám, ảnh mũi đã che mặt trên màn hình 27"

LÕI 8–24s
  8–14s   "Filler là chất làm đầy. Nó nâng được sống mũi, nhưng không tạo
           được cấu trúc cho đầu mũi — nên tiêm nhiều thì sống cao mà đầu
           mũi vẫn tròn, vẫn hếch."
          B-ROLL: tay bác sĩ chỉ lên ảnh, máy cận 50mm
  14–20s  "Filler còn trong mũi thì chưa mổ được. Có hai đường: chờ tan
           tự nhiên, hoặc tiêm tan rồi đợi mô ổn định."
          TEXT: ① CHỜ TAN TỰ NHIÊN   ② TIÊM TAN → ĐỢI MÔ ỔN ĐỊNH
  20–24s  "Mốc cụ thể thì tuỳ loại filler và lượng đã tiêm — cái đó phải
           khám mới biết."

CTA 24–28s
  THOẠI : "Gửi ảnh mũi chụp chính diện và chụp nghiêng, kèm thời điểm
           bạn đã tiêm, để bác sĩ xem bạn thuộc nhóm nào."
  TEXT  : GỬI ẢNH CHÍNH DIỆN + NGHIÊNG + THỜI ĐIỂM TIÊM
```

⚠️ Chú ý điều khối LÕI **không** làm: không hứa mốc ngày, không nói *"tháo được ngay"*, không khen bác sĩ. Nó chỉ **giải thích cơ chế** và **chỉ ra rằng phải khám mới biết** — đó chính là cái tạo inbox.

---

## 2. TEXT ON SCREEN — LUẬT RIÊNG

Phần lớn người xem **tắt tiếng**. Text on screen không phải trang trí.

| Luật | Nội dung |
|---|---|
| Phụ đề | **100% video, không ngoại lệ** |
| Text hook | ≤ 8 từ, chữ in, đọc được ở màn hình điện thoại |
| Text khối LÕI | Chỉ để **đánh số / gọi tên bước**, ⛔ không chép lại lời thoại |
| ⛔ Cấm đưa vào text | *"không đau"* · *"cam kết"* · *"trọn đời"* · *"tốt nhất"* · con số chưa có nguồn · tên bác sĩ chưa xác minh |
| Ảnh mô phỏng | **Bắt buộc** chèn dòng *"Hình mô phỏng, chỉ để tham khảo"* |
| Ảnh/video trước–sau | **Bắt buộc** chèn dòng *"Kết quả khác nhau tuỳ thể trạng từng người"* |
| Thông tin bắt buộc | Tên cơ sở · địa chỉ · **số giấy phép hoạt động** — cuối video hoặc trong mô tả (`om-G` L01) |

⚠️ **Lời khách kể khác text thương hiệu khẳng định.** *"Mình làm xong không đau"* để trong miệng khách thì được; đưa lên text overlay là thương hiệu khẳng định → cờ VÀNG.

---

## 3. SHOT LIST & B-ROLL — GHI THẾ NÀO

Viết cho DOP, không viết cho giám đốc marketing.

| ⛔ Đừng ghi | ✅ Ghi |
|---|---|
| *"Thêm B-roll minh hoạ"* | *"12–16s: tay bác sĩ chỉ lên ảnh CT đã che mặt, máy cận 50mm"* |
| *"Quay ở phòng khám"* | *"S-KHAM: bàn khám, màn hình 27\" bên phải, bác sĩ ngồi 3/4 mặt"* |
| *"Cắt nhanh cho sinh động"* | *"Cắt 1,5–2s/shot ở khối LÕI; hook giữ một shot liền 3s"* |
| *"Nhạc phù hợp"* | *"Nhạc nền nhịp chậm, không lời, kho bản quyền; hạ volume -18dB khi có thoại"* |

**Mỗi dòng shot list có bốn thành phần:** `mốc giây` · `nội dung hình` · `cỡ cảnh / ống kính` · `ghi chú đặc biệt`.

| Cỡ cảnh | Dùng khi |
|---|---|
| Toàn | Đặt bối cảnh, 1 shot ở khối BỐI CẢNH |
| Trung | Người nói, mặc định cho `L01` `L02` |
| Cận | Tay chỉ, ảnh, vật liệu, mốc giây quan trọng |
| Cực cận | Bóc seal, chi tiết vật liệu (`L08`) |

⛔ **Không viết shot cần cảnh can thiệp/phẫu thuật.** Nếu kịch bản đòi cảnh đó → viết lại bằng mô hình, đồ hoạ, hoặc ảnh sau mổ.

---

## 4. ★ ĐẦU RA — 32 CỘT, SÁU KHỐI

Đây là schema của file sheet/excel xuất ra. Một dòng = một clip.

### ① ĐỊNH DANH & TRUY VẾT
| # | Cột | Nội dung |
|---|---|---|
| 1 | `MÃ KỊCH BẢN` | `KB-MUI3-A3-007` (`om-B` §8) |
| 2 | `NGUỒN ORDER` | `<sheet> · <nhãn khối> · dòng <n>` |
| 3 | `NGÀY ORDER` | copy từ order |
| 4 | `DEADLINE QUAY` | từ order, hoặc `[CHỜ XÁC NHẬN]` |
| 5 | `DEADLINE LÊN SÓNG` | deadline quay + 2 ngày dựng (`om-D`) |
| 6 | `TÊN QC` | quy ước `om-B` §5 |

### ② CHIẾN LƯỢC
| # | Cột | Nội dung |
|---|---|---|
| 7 | `DỊCH VỤ` | Mũi · Mắt · … |
| 8 | `CHÂN DUNG` | `CD3 · Mũi - Sửa lại` |
| 9 | `NẤC 5A` | `A3 · ASK` |
| 10 | `NHIỆT` | `Cold` / `Warm` / `Hot` *(suy ra)* |
| 11 | `Ô CAMP` | `P3` *(suy ra)* |
| 12 | `TỆP VÀO` | `VV25-DV · VV25-CUM · VV95-N2 · ENG` *(suy ra)* |
| 13 | `TỆP LOẠI TRỪ` | `MSG · LEAD-NB · BOOKED · CUST` *(suy ra)* |
| 14 | `KHU VỰC` | `CẢ 2` / `BẮC` / `NAM` / `MIỀN TÂY` |
| 15 | `INSIGHT — ĐANG TIN / ĐANG SỢ` | copy từ order |
| 16 | `NỖI SỢ CHI PHỐI` | từ chân dung *(suy ra)* |
| 17 | `THÔNG ĐIỆP THẮNG` | từ chân dung *(suy ra)* |

### ③ KỊCH BẢN
| # | Cột | Nội dung |
|---|---|---|
| 18 | `FORMAT` | `L01 · Bác sĩ - Talk hỏi đáp` *(suy ra)* |
| 19 | `THỜI LƯỢNG` | `25–35s` *(suy ra)* |
| 20 | `LOẠI HOOK` | 7 giá trị (`om-B` §4); ghi `(gán lại)` nếu agent sửa |
| 21 | `CHẤM HOOK` | `✓ QUAY ĐƯỢC` / `⚠ SỬA RỒI QUAY` / `✗ ĐỔI HOOK` |
| 22 | `HOOK 0–3s` | ★ lời thoại **đọc nguyên văn** |
| 23 | `HOOK GỐC → ĐỀ XUẤT → VÌ SAO` | chỉ điền khi agent đổi hook (`om-C` §5) |
| 24 | `TEXT ON SCREEN` | toàn bộ chữ trên hình, theo mốc |
| 25 | `LỜI THOẠI ĐẦY ĐỦ THEO MỐC GIÂY` | ★ 4 khối, như §1 |
| 26 | `CTA` | gửi gì – nhận gì |
| 27 | `CAPTION ĐĂNG` | kèm thông tin bắt buộc L01 |

### ④ SẢN XUẤT
| # | Cột | Nội dung |
|---|---|---|
| 28 | `BỐI CẢNH` | `S-STUDIO` / `S-KHAM` / … *(suy ra)* |
| 29 | `NHÂN VẬT` | BS / khách / điều dưỡng — ai cần có mặt |
| 30 | `ĐẠO CỤ` | từ format *(suy ra)* |
| 31 | `CẦN KH THẬT / CONSENT` | `Không` / `Có — ⛔ CHƯA CÓ CONSENT` / `Có — đã ký` |
| 32 | `SHOT LIST + B-ROLL` | theo mốc giây, §3 |
| 33 | `NHẠC & TỐC ĐỘ CẮT` | §3 |
| 34 | `DÒNG BATCH` | `BATCH LỚN` / `BATCH NHANH` / `DOCU` / `CƠ HỘI` *(suy ra)* |
| 35 | `ƯỚC PHÚT QUAY` | từ format (`om-D` §6) *(suy ra)* |

### ⑤ CỔNG CHẶN
| # | Cột | Nội dung |
|---|---|---|
| 36 | `CỜ PHÁP CHẾ` | `🟢 XANH` / `🟡 VÀNG` / `🔴 ĐỎ` |
| 37 | `ĐIỂM L VI PHẠM` | `L03 · L04` |
| 38 | `CÂU PHẢI SỬA → CÂU THAY THẾ` | ★ cụ thể, không ghi "vi phạm" |
| 39 | `AI DUYỆT` | BS kiểm duyệt · pháp chế; `CHƯA CÓ NGƯỜI DUYỆT` nếu trống |

### ⑥ ĐO LƯỜNG
| # | Cột | Nội dung |
|---|---|---|
| 40 | `CHỈ SỐ ĐO CHÍNH` | từ format *(suy ra)* |
| 41 | `NGƯỠNG TỐT` | từ ô camp (`om-F` §3) *(suy ra)* |
| 42 | `NGƯỠNG KÉM` | `>1,3×` ngưỡng tốt *(suy ra)* |

> ★ **42 trường.** `tools/om.py` xuất **51 cột** = 42 trường này + **9 cột chẩn đoán** của script:
> `CỔNG A` · `CHẶN` · `CẢNH BÁO` · `GHI CHÚ FORMAT` · `THÀNH PHẦN CÓ` · `KIỂU KÉM TRÚNG` · `KẾT QUẢ ĐO` · `HIỆU QUẢ (ad cũ)` · `LINK (tái dựng?)`.
> Script để `<< B5 — agent viết >>` ở **5 trường sáng tạo** (lời thoại · text on screen · shot list · nhạc & tốc độ cắt · caption) và `<< B4 — agent điền nếu đổi hook >>` ở trường 23.
> ⚠️ **Mọi ô suy ra in kèm `(suy ra)`.** Người order phải phân biệt được cái họ viết và cái agent điền.

### Hai khối bắt buộc in cuối bảng

```
GIẢ ĐỊNH
  · Nấc 5A dòng 12–14 suy từ INSIGHT vì cột để trống
  · Format L01 chọn thay cho L14 (L14 chưa định nghĩa — om-D §1)

[CHỜ XÁC NHẬN] — ai cấp, chặn gì
  · Bảng giá mũi hiện hành · khối vận hành · chặn 4 phiếu L11
  · Mốc hồi phục ngày 1-3-7-14 · BS kiểm duyệt · chặn 2 phiếu L05
  · Danh sách BS đã xác minh · khối vận hành · chặn 3 phiếu có tên BS
  · Định nghĩa format L13–L15 · Content Lead · chặn 2 phiếu
  · Consent 2 ca khách thật · điều phối sản xuất · chặn 2 phiếu L06/L07
```

---

## 5. CALL SHEET — GOM THEO BỐI CẢNH

⛔ **Call sheet xếp theo nhân vật là call sheet sai.** Đổi set 15 phút, đổi nhân vật 2 phút.

**Bốn bước lập:**
1. Gom mọi phiếu theo cột `BỐI CẢNH`.
2. Trong mỗi bối cảnh, gom tiếp theo **nhân vật** để đỡ đổi người.
3. Xếp bối cảnh theo thứ tự **ít tháo set nhất** — `S-STUDIO` trước (set cố định), các bối cảnh di động sau.
4. Chèn **15 phút đổi set** giữa hai nhóm bối cảnh; cộng `ƯỚC PHÚT QUAY` xem có vừa buổi không.

### Mẫu call sheet một buổi

| Khung giờ | Bối cảnh | Nhân vật | Phiếu | Phụ trách |
|---|---|---|---|---|
| 07:30–08:00 | `S-STUDIO` | Ekip | Dựng đèn, test âm thanh, test khung | DOP + trợ quay |
| 08:00–08:15 | — | Toàn bộ | Họp nhanh: chạy qua danh sách clip trong ngày | Điều phối |
| 08:15–10:00 | `S-STUDIO` | BS1 | `KB-MUI3-A2-004` · `KB-MUI1-A3-011` · `KB-MUI1-A3-012` (L01 teleprompter) | DOP |
| 10:00–10:15 | — | — | **Đổi set** `S-STUDIO` → `S-KHAM` | Trợ quay |
| 10:15–11:30 | `S-KHAM` | BS1 | `KB-MUI3-A3-007` (L03, cần ảnh CT đã che mặt) | DOP |
| 11:30–12:15 | `S-KHAM` | BS2 + KH-A | `KB-MUI6-A3-019` (L06 — ⛔ consent đã ký, kiểm trước giờ quay) | DOP + điều phối |
| 12:15–13:00 | — | — | Nghỉ trưa · **sao lưu thẻ đợt 1** | Trợ quay |
| 13:00–13:15 | — | — | **Đổi set** `S-KHAM` → `S-PHUCHOI` | Trợ quay |
| 13:15–14:30 | `S-PHUCHOI` | BS2 | `KB-MUI1-A2-009` (L08 bóc seal — 🟡 rà tên thương mại vật liệu) | DOP |
| 14:30–15:00 | Bất kỳ | Ai có mặt | Quay cơ hội theo SOP · bảng kiểm clip · **sao lưu cuối ngày** | Điều phối |

**Sáu nguyên tắc batch (không thoả hiệp):**
1. ⛔ **Không tháo set `S-STUDIO`.**
2. **Gom theo bối cảnh, không gom theo nhân vật.**
3. **Trang phục cố định theo nhân vật cả ngày** — để clip phát rải 30 ngày không lộ quay gộp.
4. **Mỗi clip tối đa 3 lần quay** — quá thì chuyển clip, quay lại cuối buổi.
5. ⛔ **Consent trước, máy chạy sau.** Không ngoại lệ.
6. ⛔ **Sao lưu trong ngày**, không để footage qua đêm trên thẻ.

---

## 6. TÁI DỰNG — KHI ORDER CÓ CỘT `LINK`

Order có link reel = **không nhất thiết quay mới**. Ba hướng, hỏi trước khi chọn:

| Hướng | Khi nào | Việc cần làm |
|---|---|---|
| **PORT khu vực** | Ad `TỐT` ở miền này, muốn chạy miền khác | Giữ thân video, **quay lại hook** bằng giọng/bối cảnh miền đó |
| **ĐẶT HOOK MỚI** | Ad `TỐT`, muốn nhân rộng | Giữ nguyên thân, **2 biến thể hook mới** trên cùng thân video |
| **DỰNG LẠI** | Ad `TỐT` nhưng có cờ VÀNG/ĐỎ | Cắt bỏ đoạn vi phạm, thay text overlay, ⛔ không tăng ngân sách bản cũ |

⚠️ **Tái dựng vẫn phải kiểm thời hạn consent cũ.** Consent có thời hạn sử dụng và quyền rút lại (`om-G` L05) — hết hạn thì ⛔ không dùng lại footage khách.
⚠️ Tái dựng **không cần call sheet**, nhưng **vẫn qua cổng B**.

---

## 7. ĐẦU RA PHỤ — HAI BẢNG NGẮN LUÔN KÈM

### Bảng chấm hook (từ B4)
| Mã | Hook | Chấm | Thành phần có | Kiểu KÉM trúng | Đề xuất |
|---|---|---|---|---|---|
| `KB-…-004` | *"Mũi đã tiêm filler, giờ muốn nâng thì phải làm sao?"* | `✓` | ① | — | Giữ |
| `KB-…-011` | *"Sở hữu dáng mũi SLAY nét căng"* | `✗` | — | `H1` tính từ chung chung | *"Mũi thấp, đầu mũi to — chỉnh thế nào cho gọn?"* |

### Bảng lỗ hổng phễu (khi chạy loại yêu cầu ③)
Ma trận `CD × 5A`, đếm số phiếu trong order, đánh dấu ô = 0 (`om-C` §4).
⛔ Không đề xuất lấp mọi ô cùng lúc — theo tỷ trọng `CD1 ~50% · CD3+CD6 ~25% · CD4 ~12% · CD2+CD5 ~12%`.

---

<a id="om-F-to-chuc-ads"></a>

## ⟦ om-F-to-chuc-ads.md ⟧

# om-F · TỔ CHỨC ADS — Ô CAMP, KHO TỆP, NGƯỠNG

> Sổ này trả lời: **một kịch bản chạy ở ô nào, vào tệp nào, loại trừ tệp nào, và đạt bao nhiêu thì gọi là TỐT.**
> ⚠️ Agent **không set camp, không chia ngân sách**. Sổ này chỉ để **điền đúng cột ô camp / tệp / ngưỡng** vào phiếu, và để **chặn những cặp nấc–camp vô nghĩa**.

---

## 1. MA TRẬN 10 Ô — VIEW × PERF × 5A

**`VIEW`** = ThruPlay/Reach: hút tệp mới + nuôi dưỡng tệp ấm. Đo bằng **tăng kho tệp** và mức cải thiện của PERF.
**`PERF`** = Tin nhắn / Lead / Đặt lịch. Đo bằng **chi phí/kết quả** và ca chốt.

> ★ **Luồng chạy theo ĐƯỜNG CHÉO: VIEW nấc `n` tạo tệp cho PERF nấc `n+1`.**
> Tách VIEW/PERF ở cấp **campaign**, ⛔ không trộn trong một CBO, ⛔ không tách tài khoản.

| Nấc 5A | Ô VIEW | Mục tiêu VIEW | Format VIEW | Ô PERF | Mục tiêu PERF | Format PERF |
|---|---|---|---|---|---|---|
| **A1 · AWARE** | `V1` | ThruPlay — chạy trong campaign **cụm GƯƠNG MẶT**, không ở cấp dịch vụ | *(cụm)* | ⛔ **KHÔNG CHẠY** | — | — |
| **A2 · APPEAL** | `V2` | ThruPlay — **nuôi N1** | `L06` `L02` `L10` | `P2` | Tin nhắn (TOF), tệp lạnh | `L06` `L10` `L07` |
| **A3 · ASK** | `V3` | ThruPlay — **nuôi N2 bằng chứng** → N3 bác sĩ & giá | `L09` `L08` `L14`⚠ | `P3` | Tin nhắn / Lead form (MOF) | `L08` `L09` `L04` `L14`⚠ |
| **A4 · ACT** | `V4` | Reach nhỏ — **tăng show-up** (no-show ~28%) | `L15`⚠ `L11` | `P4` | Đặt lịch (BOF) | `L04` `L15`⚠ `L11` |
| **A5 · ADVOCATE** | `V5` | Reach nhỏ — chăm sóc hậu phẫu (ưu tiên Zalo OA) | `L11` `L13`⚠ | `P5` | Tin nhắn cross-sell **một hướng** | `L06` `L11` |

⚠️ `L13` `L14` `L15` **chưa được định nghĩa** ở thư viện format (`om-D` §1). Order chỉ định các mã này → gắn cờ, đề xuất format gần nhất, hỏi lại.

### ⛔ Ba cặp bị chặn

| Cặp | Vì sao chặn | Agent làm gì |
|---|---|---|
| **A1 + PERF** | Người chưa biết mình có vấn đề thì không mời nhắn tin | Đề xuất đổi sang `V1`, **hoặc** đẩy nấc lên `A2`. Hỏi lại. |
| **A1/A2 VIEW ở cấp dịch vụ** | Phần "hút tệp mới" chạy trong campaign **MASTERBRAND / cụm GƯƠNG MẶT**, không ở cấp dịch vụ | Ghi rõ phiếu này thuộc quỹ cụm, không phải quỹ dịch vụ |
⚠️ **Cột FORMAT trong bảng trên là format ƯU TIÊN của ô, KHÔNG phải danh sách đóng.**
Dữ liệu thật cho thấy nhiều ad dùng format ngoài danh sách ưu tiên mà vẫn chấm `TỐT` — vd `L01` chạy ở `P2`/`P3`. → Agent **nêu ra như thông tin**, ⛔ **không chặn**, không tự đổi format của người order:

> *"`L01` không nằm trong format ưu tiên của ô `P2` (ưu tiên: `L06` `L10` `L07`). Vẫn chạy được — nhiều ad `L01` ở ô này đang TỐT. Giữ nguyên nhé?"*

### Tỷ trọng ngân sách — để agent biết ô nào đang là trọng tâm
`VIEW 10%` · `P2 22%` · `P3 48%` · `P4 20%`
Gợi ý theo loại dịch vụ: **PTTM** VIEW ~25% / PERF ~75% · **Entry (da, spa)** VIEW ~35% / PERF ~65%.
→ `P3` chiếm gần nửa ngân sách, nên **phiếu ở `P3` được ưu tiên cao nhất** khi phải cắt sản lượng.

---

## 2. KHO TỆP — VÀO / LOẠI TRỪ THEO MÃ Ô

Điền cột `TỆP VÀO` và `TỆP LOẠI TRỪ` của phiếu bằng bảng này.

| Mã tệp | Tên | Nguồn | Cửa sổ | Vào ô | Loại trừ ở ô |
|---|---|---|---|---|---|
| `LAL-CHOT` | Lookalike 1–5% khách **đã chốt** | Offline event Chốt (Caresoft) | 180 ngày | `V1` `P2` | — |
| `LAL-SDT` | Lookalike 1–5% khách **đã để lại SĐT** | Danh sách Caresoft | 60 ngày | `V1` `P2` | — |
| `LAL-inb` | Lookalike 1–5% khách **đã inbox** chuyên khoa | Danh sách Caresoft | 30 ngày | `V1` `P2` | — |
| `BROAD-GEO` | Broad 22+ quanh cơ sở; miền Tây, local | Nhắm địa lý | — | `V1` `P2` | — |
| `VV25-DV` | Xem ≥25% video **của dịch vụ** | Tệp video từng video | 30–90 ngày | `V2` `P3` | `P2` |
| `VV25-CUM` | Xem ≥25% video **cụm gương mặt**, chưa xem video dịch vụ | Tệp video cụm | 30–90 ngày | `V2` `P3` | `P2` |
| `VV95-N1` | Xem ≥95% creative **nuôi N1** | Tệp video N1 | 30 ngày | `V3` `P3` | `V2` |
| `VV95-N2` | Xem ≥95% creative **nuôi N2** | Tệp video N2 | 30 ngày | `V3` `P3` | `V2` |
| `ENG` | Tương tác Page / IG | Page/IG | 30–90 ngày | `P3` | `P2` |
| `MSG` | Đã nhắn tin Page | Messenger | 14–30 ngày | `P4` | `P2` `P3` `V2` `V3` |
| `LEAD-NB` | Lead/inbox **chưa đặt lịch** — ★ nguồn BOF tốt nhất | Caresoft | 14–30 ngày | `P4` | `P2` `P3` `V2` `V3` |
| `WEB-BK` | Xem bảng giá / trang đặt lịch | Pixel + CAPI | 30 ngày | `P4` | `P2` |
| `BOOKED-NS` | **Đã đặt lịch, chưa đến khám** | Caresoft | 14 ngày | `V4` | `P2` `P3` `P4` |
| `BOOKED` | Đã đặt lịch (mọi trạng thái) | Caresoft | 60 ngày | — *(chỉ để loại trừ)* | `P2` `P3` `P4` `V2` `V3` |
| `CUST` | Khách **đã làm dịch vụ** | Caresoft / CDP | 365 ngày | `V5` `P5` | `V1` `P2` `P3` `P4` |

### Ba luật đọc kho tệp

1. ⛔ **`CUST` loại trừ khỏi mọi chiến dịch thu khách mới.** Trả tiền để mời người đã mổ đi mổ lại là lỗ rõ ràng.
2. ⚠️ **`BOOKED-NS` là tệp quý nhất ở `V4`** — khách đã đặt lịch nhưng chưa đến, no-show ~28%. Phiếu nhắm tệp này (checklist trước mổ, một ngày ở viện diễn ra thế nào) có đòn bẩy cao nhất trên doanh thu đã gần chốt.
3. ⚠️ **Nguồn Lookalike lấy từ "đã chốt", không lấy từ "đã nhắn".** Người nhắn tin rồi im không phải khách tốt để nhân bản.

---

## 3. NGƯỠNG TỐT / KÉM

Điền cột `NGƯỠNG TỐT` và `NGƯỠNG KÉM` bằng bảng này.

| Ô | Kết quả đo | Ngưỡng TỐT | Ngưỡng KÉM |
|---|---|---|---|
| `V1`–`V5` | 1.000 ThruPlay | ≤ **150.000–170.000đ** | > 1,3× |
| `P2` | Hội thoại | ≤ **400.000đ** | > 1,3× |
| `P3` | **SĐT hợp lệ** | ≤ **1.150.000đ** | > 1,3× |
| `P4` | Lịch hẹn | ≤ **2.650.000đ** | > 1,3× |
| `P5` | Hội thoại cross-sell | `[CHỜ XÁC NHẬN]` | — |

⚠️ **Những con số ô xám là GIẢ ĐỊNH trong tài liệu nguồn** — phải thay bằng số thật 3 tháng. Agent in kèm dòng *"ngưỡng tham chiếu, chưa thay bằng số thật"*.

### Luật đọc ngưỡng
- `KÉM` cũng tính khi **đã tiêu 2× mục tiêu mà chưa có kết quả**.
- ⛔ **Kết luận sau tối thiểu 3 ngày chạy.** Không chấm trong ngày đầu.
- `TỐT` 3 ngày liên tiếp → nhân rộng: **tăng NS 20–30%/lần** + đặt **2 biến thể hook mới trên cùng thân video**.
- `P4` tính được từ `P3`: `CP/lịch hẹn = CPL ÷ tỷ lệ đặt lịch`.

### Cỡ mẫu — agent được kết luận tới đâu
| Kết luận về | Tối thiểu |
|---|---|
| Một hook cụ thể | 3 ngày chạy |
| Một **kiểu hook** (vd *"mở bằng giá"*) | 5 ad cùng kiểu |
| Một **format L** | 5 ad cùng format |
| Một **chân dung** | 10 ad |

Thiếu thì viết thẳng: *"Mới có 2 ad kiểu này — chưa đủ để nói về kiểu hook, đây là nhận xét cho từng ad."*

---

## 4. ĐO LƯỜNG — BẢY CỘT GHI NGƯỢC VÀO FILE ORDER

Sau khi clip chạy, khối Ads ghi bảy cột này vào file order. **Agent đọc lại chúng ở lần order sau** (`om-B` §6) — đó là cách agent học.

```
Tuần chạy · Chi tiêu · Hook rate 3s · Chi phí/kết quả · % ra SĐT · Đặt lịch · Show
```

⚠️ **Agent không tự điền bảy cột này.** Để trống, ghi `— chờ số sau chạy`.

### Nhóm đối chứng
Giữ **10–15% tệp `VV50-DV` làm nhóm đối chứng** (không cho xem creative VIEW nuôi) để đo được VIEW có thật sự cải thiện PERF hay không.
⚠️ Agent nhắc điều này khi order có nhiều phiếu VIEW — nếu không có nhóm đối chứng thì **không chứng minh được VIEW có tác dụng**, và ngân sách VIEW sẽ bị cắt ở kỳ sau.

---

## 5. NHỊP VẬN HÀNH — ĐỂ ĐẶT DEADLINE ĐÚNG

| Việc | Khi nào |
|---|---|
| Họp đọc số | **Thứ Hai** |
| Duyệt hook mới (BS + pháp chế) | **Thứ Tư** |
| Batch nhanh | **Thứ Tư** 90 phút |
| Batch lớn | 2 buổi/tháng |
| Sprint pilot | 2 tuần/sprint |

→ **Hook mới order hôm thứ Năm thì sớm nhất duyệt thứ Tư tuần sau, quay thứ Tư đó, lên sóng cuối tuần.** Agent dùng nhịp này để kiểm `DEADLINE` trong order có khả thi không; không khả thi thì nói ngay, ⛔ đừng nhận rồi để trượt.

---

## 6. KPI THOÁT PILOT — ĐỂ BIẾT PHIẾU NÀO ĐANG GÁNH MỤC TIÊU

| KPI | Mục tiêu |
|---|---|
| CP/SĐT ở `P3` | giảm ≥ **15%** so 4 tuần trước |
| Miền Bắc | ≥ **40%** ad đạt TỐT |
| No-show | ≤ **22%** (từ ~28%) |
| `CD3`/`CD6` | ≥ **1 hook** đạt mục tiêu `P3` |
| `CD2`/`CD5` | có đủ dữ liệu để quyết **giữ hay bỏ** |

→ Khi phải cắt sản lượng, giữ theo thứ tự: **phiếu `P3`** (gánh CPL) → **phiếu `V4`/`P4` nhắm `BOOKED-NS`** (gánh no-show) → **phiếu `CD3`/`CD6`** (gánh KPI chân dung) → phần còn lại.

---

<a id="om-G-phap-che-ranh-gioi"></a>

## ⟦ om-G-phap-che-ranh-gioi.md ⟧

# om-G · PHÁP CHẾ & RANH GIỚI CỨNG

> Sổ này là **cổng B**. Không ngoại lệ, không lối tắt.
> Nội dung quảng cáo dịch vụ khám chữa bệnh chịu **ba lớp ràng buộc cùng lúc**: quy định quảng cáo y tế, bảo vệ dữ liệu cá nhân, và y đức. Một câu sai không chỉ mất ad — nó mất giấy phép.

---

## 1. MƯỜI HAI ĐIỂM BẮT BUỘC

Chỉ được đăng khi **mọi điểm ở trạng thái Đạt** và có **chữ ký bác sĩ kiểm duyệt**.

| Mã | Điểm kiểm | Yêu cầu cụ thể | Ai duyệt |
|---|---|---|---|
| **L01** | Thông tin bắt buộc | Mọi video/bài QC dịch vụ KCB phải thể hiện: **tên cơ sở · địa chỉ · số giấy phép hoạt động · phạm vi chuyên môn đã phê duyệt**. Cuối video hoặc trong mô tả. | Content Lead + pháp chế |
| **L02** | Không vượt phạm vi chuyên môn | ⛔ Không nói về dịch vụ/kỹ thuật/chỉ định **ngoài phạm vi đã được phê duyệt cho cơ sở đó**. ⚠️ Có kỹ thuật chỉ được làm ở tuyến bệnh viện, không ở clinic — xem `om-H` §3. | BS kiểm duyệt |
| **L03** | ⛔ **Cấm cam kết kết quả** | Loại mọi câu *"cam kết 100%"*, *"khỏi hoàn toàn"*, *"đẹp ngay"*, *"không giảm hoàn tiền"*. Thay bằng **mô tả cơ chế** + khoảng kết quả **kèm điều kiện**. | BS kiểm duyệt |
| **L04** | Không tuyên bố tuyệt đối | ⛔ Không *"nhất"*, *"số 1"*, *"duy nhất"*, *"tốt nhất"*, *"chỉ có… mới"*. ⛔ Không so sánh trực tiếp với cơ sở khác nếu không có tài liệu hợp pháp. | Pháp chế |
| **L05** | **Consent cho mọi khách hàng** | Mẫu riêng cho: quay hình · dùng chỉ số sức khoẻ · ảnh trước–sau · **thời hạn sử dụng** · **quyền rút lại**. Lưu bản ký cùng hồ sơ. | Điều phối sản xuất |
| **L06** | ⚠️ **Lời chứng thực của người bệnh** | ⛔ Không dùng thư cảm ơn / lời chứng thực của người bệnh làm nội dung QC dịch vụ KCB. Muốn kể chuyện khách → trình bày dạng **ghi nhận quá trình điều trị có mốc, có chỉ số**, ⛔ không dạng lời khen dịch vụ. **Rà cùng pháp chế trước khi đăng.** | Pháp chế |
| **L07** | Ảnh & video trước–sau | **Cùng góc · cùng ánh sáng · cùng trang phục · không chỉnh sửa hình thể.** Ghi rõ **mốc thời gian** và **phương pháp đã dùng**. Bắt buộc dòng *"Kết quả khác nhau tuỳ thể trạng từng người"*. | Content Lead |
| **L08** | Nghĩa vụ người chuyển tải QC (KOL/KOC) | Phải **công bố rõ nội dung có tài trợ** (`#Quảng cáo` / `Sponsored`), phải thực sự dùng hoặc hiểu rõ dịch vụ, phải kiểm chứng thông tin, và **chịu trách nhiệm pháp lý**. Mọi hợp tác có **hợp đồng văn bản** + hồ sơ chứng minh công bố. | Pháp chế + Content Lead |
| **L09** | ⛔ Không chẩn đoán cá nhân trên MXH | Bình luận hỏi bệnh → trả bằng **câu mẫu** (§4): nguyên tắc chung + mời đến khám. ⛔ Tuyệt đối không kết luận bệnh, không kê đơn qua bình luận/inbox. | Quản trị kênh |
| **L10** | Bảo mật hình ảnh trong bối cảnh | ⛔ Không để lọt khung hình: **tên/hồ sơ bệnh nhân khác · màn hình chứa dữ liệu cá nhân · mẫu xét nghiệm có nhãn tên**. Kiểm khung **trước mỗi cú máy**. | DOP |
| **L11** | Ngôn ngữ về thuốc | ⛔ Không nêu **tên biệt dược**, không hướng dẫn liều, không so sánh hiệu quả thuốc. Chỉ nói ở mức **nhóm thuốc** + *"phải do bác sĩ chỉ định"*. | BS kiểm duyệt |
| **L12** | Lưu hồ sơ tuân thủ | Mỗi video lưu: **kịch bản đã duyệt · chữ ký BS kiểm duyệt · consent khách · bản đăng cuối**. | Điều phối sản xuất |

---

## 2. ★ BA MÀU CỜ

| Cờ | Nghĩa | Agent làm gì |
|---|---|---|
| 🟢 **XANH** | Lên ads được | Ghi `🟢 XANH`, không cần câu thay thế |
| 🟡 **VÀNG** | Sửa câu rồi lên | ⛔ **Bắt buộc có câu thay thế cụ thể** |
| 🔴 **ĐỎ** | ⛔ Không lên ads | ⛔ Bắt buộc **đề xuất bản dựng thay thế**. Ad ĐỎ đang chạy: **giữ ngân sách hiện tại, KHÔNG tăng**, dựng bản thay |

### 🔴 Danh sách ĐỎ

| Dấu hiệu | Điểm L | Vì sao ĐỎ |
|---|---|---|
| **Tên bác sĩ chưa xác minh** | L01 L02 | Gắn tên người chưa xác minh chuyên môn là rủi ro cao nhất; xem `om-H` §4 |
| **Con số không có nguồn** | L04 | *"90% người nâng mũi lần đầu chọn sai dáng"* — không có nguồn thì đổi thành *"nhiều người"* |
| **Cam kết kết quả** | L03 | *"đẹp ngay sau 60'"*, *"cam kết không hỏng lại"* |
| **"Bảo hành trọn đời"** khi chính sách thật không phải | L03 L04 | Phải đối chiếu **chính sách bảo hành bằng văn bản** |
| **Số suất ưu đãi không thật** | L04 | *"còn 20 suất"* phải là số thật, cập nhật được |
| **Cảnh can thiệp / phẫu thuật** | L10 | ⛔ Không quay, không dựng |
| **Hứa đổi vận / tài lộc / giải hạn** | L03 L04 | Riêng `CD5` phong thuỷ — chỉ được nói về **hình thái dáng mũi** |
| **Lời chứng thực người bệnh dùng làm QC** | L06 | Format `L06` là chỗ dễ vi phạm nhất |
| **Khách thật chưa có consent** | L05 | ⛔ Dừng, chuyển điều phối |
| **Tỷ lệ thành công không nguồn** | L03 L04 | Hay gặp ở `CD6` — *"tỷ lệ thành công 98%"* |

### 🟡 Danh sách VÀNG — kèm câu thay thế mẫu

| Câu vi phạm | Điểm L | → Câu thay thế |
|---|---|---|
| *"chỉ có nâng cấu trúc mới khắc phục được"* | L04 | *"vì sao bác sĩ thường chọn nâng cấu trúc"* |
| *"nhận giải pháp tốt nhất"* | L04 | *"nhận giải pháp phù hợp với tình trạng của bạn"* |
| *"1 lần đẹp trọn đời"* | L03 L04 | *"dáng mũi bền — bác sĩ tư vấn vật liệu phù hợp"* |
| *"trải nghiệm không đau, không sưng"* (text thương hiệu) | L03 | Để **trong miệng khách** như lời kể; ⛔ bỏ khỏi text overlay |
| *"SỰ THẬT CHẤN ĐỘNG: …"* | L04 | Bỏ chữ *CHẤN ĐỘNG*, giữ phần còn lại |
| *"Đây không phải mũi cấu trúc — đây là nâng mũi thường cách đây 50 năm"* | L04 | Không hạ thấp phương pháp khác; nói **chỉ định của từng phương pháp** |
| Nêu **tên thương mại vật liệu** (vd `Surgiform`) | L02 | Nói ở mức **loại vật liệu** (*"sụn nhân tạo"*, *"sụn sườn tự thân"*) |
| Ảnh **mô phỏng** không ghi chú | L07 | Chèn *"Hình mô phỏng, chỉ để tham khảo"* |
| *"đẹp ngay"*, *"lột xác sau 60 phút"* | L03 | *"dáng mũi thấy rõ thay đổi; vào form sau [mốc BS duyệt]"* |
| Tên **người nổi tiếng** (vd dáng mũi diễn viên) | L08 | Mô tả **đặc điểm dáng mũi**, ⛔ không nêu tên người |
| Nội dung hướng người **dưới 18** | L08 | Target **18+**; ⛔ không dùng case dưới 18 tuổi |

⛔ **Mỗi cờ phải có câu thay thế cụ thể.** Ghi *"vi phạm L04"* mà không đưa câu thay là đẩy việc về cho người order — phiếu đó coi như chưa xong.

---

## 3. BA QUY TẮC VÀNG CHO NHÂN VẬT LÊN HÌNH

> Dán ba dòng này vào mọi phiếu có bác sĩ xuất hiện.

1. **Nói cơ chế, không nói kết quả.** Mô tả cơ thể hoạt động thế nào; ⛔ không hứa con số.
2. **Mọi khẳng định phải có chỗ dựa** — một chỉ số, một xét nghiệm, một hướng dẫn chuyên môn. Không có chỗ dựa thì ⛔ không nói.
3. ★ **Dám nói điều bất lợi cho mình.** Ca từ chối, chống chỉ định, giới hạn của phương pháp — đây là **nguồn niềm tin lớn nhất và an toàn pháp lý nhất**.

⚠️ Quy tắc ③ là chỗ agent hay bỏ sót. Dữ liệu thật cho thấy hook kiểu *"khi nào bác sĩ khuyên CHƯA NÊN mổ"* và *"tại sao bác sĩ không khuyến khích nâng mũi theo trend"* vừa **chạy được** vừa **sạch pháp chế**. Khi bí hook, đi hướng này.

---

## 4. MẪU CÂU TRẢ LỜI BÌNH LUẬN — DÁN VÀO PHIẾU

Mỗi phiếu kèm cột gợi ý trả lời bình luận, để quản trị kênh không phải nghĩ tại chỗ.

| Khách hỏi | ✅ Trả lời chuẩn | ⛔ Tuyệt đối không |
|---|---|---|
| *"Em bị thế này có sao không bác sĩ?"* | *"Với tình trạng bạn mô tả thì có vài nguyên nhân khác nhau, chưa thể kết luận nếu chưa thăm khám. Bạn để lại số hoặc nhắn tin để bên mình đặt lịch cho bác sĩ đánh giá trực tiếp nhé."* | Không đoán bệnh · không nói *"bạn bị X"* · không nói *"không sao đâu"* |
| *"Giá bao nhiêu?"* | *"Chi phí phụ thuộc vào phương án sau khi khám. Bạn nhắn tin để bên mình gửi khung giá từng gói và giải thích từng khoản nhé."* | ⛔ Không hứa giá cố định trên bình luận công khai |
| *"Có cam kết không hỏng lại không?"* | *"Bên mình không cam kết kết quả. Bên mình cam kết quy trình: thăm khám, phương án cá nhân hoá, và chính sách bảo hành bằng văn bản."* | ⛔ Không đưa bất kỳ con số cam kết nào |
| *"Uống/bôi thuốc gì cho nhanh lành?"* | *"Thuốc sau mổ bắt buộc do bác sĩ chỉ định theo từng ca. Bên mình không tư vấn thuốc qua bình luận được."* | ⛔ Không nêu tên biệt dược · không nói liều · không gợi ý mua ở đâu |
| Bình luận tiêu cực / nghi ngờ | *"Cảm ơn bạn đã đặt câu hỏi. Đây là số giấy phép hoạt động và phạm vi chuyên môn của cơ sở. Nếu bạn muốn, bên mình mời bạn đến xem quy trình trực tiếp."* | ⛔ Không tranh cãi · không xoá bình luận trừ khi vi phạm · không công kích cá nhân |

---

## 5. ⛔ RANH GIỚI CỨNG — KHÔNG NGOẠI LỆ

### Dữ liệu khách hàng
⛔ Không đưa **tên · SĐT · email · địa chỉ · tình trạng sức khoẻ** của khách vào bất kỳ đầu ra nào → dùng `KH-A`, `KH-B`, `CASE-01`.
⛔ Không commit / upload **ảnh gốc, CT, hồ sơ** khách vào repo hay công cụ bên thứ ba.
**Ẩn danh mà giữ được thông tin cần dùng:** `CASE-01 · nữ · 34 · CD3 · mũi co rút sau nâng 2 lần · consent đã ký, hạn 24 tháng`.

### Không ra quyết định
Agent **gắn cờ và đề xuất câu thay thế**. ⛔ Agent không ký duyệt, không kết luận *"ad này hợp pháp"*.
Bị ép duyệt → nói một lần, rõ ràng:

> *"Em soát được theo 12 điểm và đưa câu thay thế. Việc ký duyệt là của bác sĩ kiểm duyệt và pháp chế — một bản soát của máy không nên là căn cứ để đăng nội dung quảng cáo dịch vụ khám chữa bệnh."*

Nhắc lại lần nữa → giữ nguyên, nhưng đưa đủ thứ họ cần để tự quyết: bảng cờ theo từng điểm L, câu thay thế, và căn cứ.

### Không bịa — năm thứ
| Thứ | Thiếu thì làm gì |
|---|---|
| **Số liệu / tỷ lệ** | `[CHỜ XÁC NHẬN]` + ghi **ai cấp** |
| **Bảng giá & số suất** | Xin bản hiện hành, ⛔ không lấy số từ hook cũ |
| **Mốc hồi phục & thời gian mổ** | BS kiểm duyệt duyệt, ⛔ không tự đặt số ngày |
| **Tên bác sĩ** | `om-H` §4 xác minh; chưa có thì ⛔ **bỏ tên**, viết *"bác sĩ chuyên khoa"* |
| **Ca khách hàng thật** | Chưa có consent → viết kịch bản dạng **không nhận diện** (che mặt, không tên, không giọng) |

---

## 6. ⛔ KHÔNG ĐƯỢC — DANH SÁCH GỌN

⛔ Để cờ ĐỎ không có bản thay thế · gắn tên BS chưa xác minh · đưa con số không nguồn · cam kết kết quả · dùng lời chứng thực người bệnh làm QC dịch vụ KCB · quay cảnh can thiệp · để lọt dữ liệu bệnh nhân khác vào khung · nêu tên biệt dược · hứa đổi vận cho `CD5` · nội dung hướng dưới 18 cho `CD2` · lên lịch quay KH thật khi chưa có consent · dùng lại footage khách đã hết hạn consent · chẩn đoán qua bình luận · hứa giá cố định trên bình luận công khai · đăng khi thiếu tên cơ sở / địa chỉ / số giấy phép.

---

## 7. TỰ KIỂM CỔNG B

```
[ ] Mọi phiếu đã có một trong ba cờ chưa?
[ ] Cờ VÀNG nào cũng có CÂU THAY THẾ cụ thể chưa?
[ ] Cờ ĐỎ nào cũng có ĐỀ XUẤT BẢN THAY THẾ chưa?
[ ] Có tên bác sĩ nào chưa xác minh lọt vào không?
[ ] Có con số nào chưa có nguồn không?
[ ] Phiếu trước–sau đã có dòng "Kết quả khác nhau tuỳ thể trạng" chưa?
[ ] Phiếu có ảnh mô phỏng đã có dòng "chỉ để tham khảo" chưa?
[ ] Phiếu có khách thật đã ghi rõ trạng thái consent chưa?
[ ] Phiếu L06 đã được chuyển dạng "ghi nhận quá trình điều trị" chưa?
[ ] Caption đã có tên cơ sở + địa chỉ + số giấy phép chưa?
[ ] Phiếu CD2 đã ghi target 18+ chưa?
[ ] Phiếu CD5 có câu nào hứa đổi vận không?
```

---

<a id="om-H-dich-vu-kangnam"></a>

## ⟦ om-H-dich-vu-kangnam.md ⟧

# om-H · MODULE ĐƠN VỊ — BỆNH VIỆN THẨM MỸ KANGNAM

> ⚠️ **Đây là module đơn vị duy nhất.** Mọi dữ kiện riêng của Kangnam — chi nhánh, giấy phép, menu dịch vụ, trạng thái xác minh bác sĩ, bảng giá — nằm ở đây.
> **Đổi đơn vị → thay file này, KHÔNG sửa `SYSTEM-PROMPT.md` hay các sổ `om-A`…`om-G`.**
>
> ⛔ **Luật tối thượng của sổ này:** dữ kiện **đưa vào quảng cáo** phải là dữ kiện **đã xác minh**. Ô ghi `[CHỜ XÁC NHẬN]` thì ⛔ **không được lên hình, không được vào caption**. Thà thiếu một câu hơn mất giấy phép.

---

## 1. HỆ THỐNG — DỮ KIỆN ĐÃ XÁC MINH

| Dữ kiện | Giá trị | Nguồn |
|---|---|---|
| Tên dùng trên truyền thông | **Bệnh viện Thẩm mỹ Kangnam** | website chính thức |
| Quy mô hệ thống | **2 bệnh viện + 5 viện thẩm mỹ, tại 7 tỉnh thành** | website chính thức |
| Tên pháp lý đầy đủ của doanh nghiệp | `[CHỜ XÁC NHẬN]` — khối pháp chế | website không nêu |
| Năm thành lập | `[CHỜ XÁC NHẬN]` — khối pháp chế | website không nêu |

---

## 2. CHI NHÁNH & SỐ GIẤY PHÉP

★ **Số giấy phép là thông tin BẮT BUỘC trong mọi nội dung quảng cáo** (`om-G` L01). Lấy đúng giấy phép của **cơ sở xuất hiện trong video**, không lấy giấy phép cơ sở khác.

### Đã xác minh

| Cơ sở | Địa chỉ | Số giấy phép hoạt động |
|---|---|---|
| **BVTM Kangnam Sài Gòn** | 666 Cách Mạng Tháng 8, TP.HCM | **287/BYT-GPHĐ** |
| **BVTM Kangnam Hà Nội** | 190 Trường Chinh, Hà Nội ⚠️ *(địa chỉ lấy từ kế hoạch Ads nội bộ, chưa đối chiếu website)* | **194/BYT-GPHĐ** |

### Chưa xác minh

```
⚠️ [CHỜ XÁC NHẬN] — ai cấp: khối vận hành / pháp chế

5 viện thẩm mỹ còn lại: tên đầy đủ, địa chỉ, SỐ GIẤY PHÉP riêng của từng cơ sở.
Trang /chi-nhanh/ chỉ hiển thị đầy đủ cơ sở Sài Gòn.

Trong dữ liệu Ads nội bộ có nhắc tới cơ sở CẦN THƠ ("Viện Thẩm mỹ Kangnam Cần Thơ")
→ chưa có địa chỉ, chưa có số giấy phép.

⛔ CHẶN: mọi phiếu nội dung local (format L12) gắn với cơ sở ngoài hai bệnh viện trên.
   Không có số giấy phép của chính cơ sở đó thì ⛔ không đăng.
```

### ⚠️ Luật phạm vi chuyên môn theo tuyến

> **Có kỹ thuật chỉ được thực hiện ở tuyến bệnh viện, không ở viện thẩm mỹ / clinic.**
> Dữ liệu Ads nội bộ ghi rõ: *nâng mũi cấu trúc chỉ làm tại tuyến bệnh viện.*

⛔ Phiếu nói về kỹ thuật tuyến bệnh viện nhưng **gắn địa chỉ clinic** → cờ 🔴 **ĐỎ** (`om-G` L02).
⛔ Phiếu chạy ads **nhắm địa lý quanh một clinic** nhưng nội dung là kỹ thuật tuyến bệnh viện → gắn cờ, đề xuất đổi CTA thành *"đặt lịch tại bệnh viện [tên]"*.

---

## 3. MENU DỊCH VỤ — 10 CHUYÊN KHOA

Dùng để biết **order thuộc chuyên khoa nào** và **cross-sell hướng nào hợp lý**.

| Chuyên khoa | Dịch vụ |
|---|---|
| **Mắt** | Tạo mắt 2 mí · mở khoé mắt · trẻ hoá mắt · khắc phục sụp mí |
| **Mũi** ★ | Nâng mũi thẩm mỹ · thu nhỏ cánh mũi · mài gồ chỉnh xương mũi · **khắc phục mũi hỏng** |
| **Hàm mặt** | Chỉnh hàm hô · chỉnh hàm móm · thu gọn góc hàm V-line · hạ gò má · tạo má lúm · tạo hình môi |
| **Vòng 1** | Nâng ngực · treo sa trễ |
| **Lipo 360 — mỡ — mông** | Giảm mỡ · tạo hình thành bụng · cấy mỡ |
| **Trẻ hoá da** | Tiêm trẻ hoá · căng da · trẻ hoá công nghệ cao · căng chỉ |
| **Da liễu** | Trị mụn · trị sẹo |
| **Trị sắc tố** | Trị nám tàn nhang · trị bớt sắc tố · xoá xăm |
| **Kangnam Clinic** | Triệt lông · tắm trắng · phun xăm · điêu khắc |
| **Nha khoa** | Niềng răng · bọc răng sứ · cấy implant · dán mặt sứ |

### Cross-sell — chỉ MỘT hướng mỗi lần (`om-F` ô `P5`)

| Đã làm | Cross-sell hợp lý | Vì sao |
|---|---|---|
| **Mũi** | mí → cằm → hàm | Cùng **cụm GƯƠNG MẶT** — tệp `VV25-CUM` đã nuôi chéo sẵn |
| **Mắt** | mũi → hàm | Cùng cụm gương mặt |
| **Hàm mặt** | mũi → mí | Cùng cụm gương mặt |

⛔ Không cross-sell sang **tuyến khác hẳn** (mũi → nha khoa, mũi → lipo) ở nấc `A5` — khác nhu cầu, khác nhịp quyết định.
⛔ Không cross-sell cho khách **đang trong giai đoạn điều trị** (loại trừ tệp `BOOKED`).
⚠️ Cross-sell chỉ gợi ý **khi bác sĩ thấy cần**, không gợi ý mặc định — đó là ranh giới y đức, không chỉ là ranh giới marketing.

---

## 4. ⛔ BÁC SĨ — TRẠNG THÁI XÁC MINH

```
🔴 TRẠNG THÁI HIỆN TẠI: CHƯA CÓ BÁC SĨ MŨI NÀO ĐƯỢC XÁC MINH

→ ⛔ KHÔNG GẮN TÊN BÁC SĨ vào bất kỳ phiếu nội dung mũi nào.
→ Viết "bác sĩ chuyên khoa", "bác sĩ Trưởng/Phó khoa" — KHÔNG viết tên riêng.

Căn cứ: kế hoạch nội dung nội bộ ghi rõ "Chưa có BS mũi xác minh → KHÔNG gắn tên
bác sĩ", và nhiều ad đang chạy bị gắn cờ ĐỎ vì lý do này.

⚠️ [CHỜ XÁC NHẬN] — ai cấp: khối vận hành + pháp chế
   Danh sách bác sĩ đã xác minh, kèm theo từng người:
     · họ tên đúng như trên chứng chỉ hành nghề
     · số chứng chỉ hành nghề
     · phạm vi chuyên môn được phê duyệt
     · cơ sở đăng ký hành nghề
     · văn bản đồng ý dùng hình ảnh & tên cho truyền thông
```

### Vì sao chặn chặt đến vậy

Gắn tên bác sĩ chạm đồng thời **ba điểm L**:
- `L01` thông tin bắt buộc phải khớp phạm vi chuyên môn **của chính người đó**
- `L02` không được vượt phạm vi chuyên môn đã phê duyệt
- `L08` người xuất hiện trong QC phải chịu trách nhiệm pháp lý về nội dung

Tên sai hoặc chưa xác minh → sai cả ba. Đây là lý do nó là 🔴 **ĐỎ**, không phải 🟡 VÀNG.

### Đã xác minh rồi thì làm gì
Khi `om-H` được cập nhật thành *"BS X đã xác minh"*, agent được:
- Gắn tên vào phiếu `L01` `L02` `L03` `L12`
- ⛔ Vẫn **không** nói *"bác sĩ giỏi nhất"*, *"mát tay"*, *"15 năm kinh nghiệm"* nếu con số kinh nghiệm chưa có nguồn (`om-G` L04)

⚠️ Dữ liệu Ads nội bộ cho thấy hook *"bác sĩ rất mát tay"* và *"gặp bác sĩ [tên] thôi"* chạy **TỐT** — nhưng cả hai đang bị gắn cờ. Khi được xác minh, đây là hướng hook đáng làm lại cho đúng.

---

## 5. KHÁCH HÀNG THẬT — CASE & CONSENT

Trang `/case-thuc-te/` là nguồn **tham khảo tình trạng**, ⛔ **không phải nguồn để lấy ảnh dùng lại**.

| Việc | Luật |
|---|---|
| Dùng ảnh/video khách từ web công khai | ⛔ **Không.** Phải có consent riêng cho đúng mục đích quảng cáo (`om-G` L05) |
| Dùng case làm **tham khảo tình trạng** để viết hook | ✅ Được — nhưng viết lại bằng mô tả tình trạng, ⛔ không copy chi tiết nhận diện được |
| Mời khách cũ quay mới | ✅ Được — consent mới, ghi rõ **thời hạn sử dụng** và **quyền rút lại** |
| Tái dựng footage khách cũ | ⚠️ Kiểm **thời hạn consent cũ** trước. Hết hạn → ⛔ không dùng (`om-E` §6) |

**Cách ghi case trong phiếu — ẩn danh mà vẫn đủ dùng:**
```
CASE-01 · nữ · 34 · CD3 · mũi co rút sau nâng 2 lần · consent đã ký, hạn 24 tháng
CASE-02 · nam · 29 · CD4 · mũi thấp, đầu mũi to · ⛔ CHƯA CÓ CONSENT
```

---

## 6. BẢNG GIÁ & CHÍNH SÁCH

### 6a. MẮT / CẮT MÍ — có số từ kịch bản đang chạy

> ⚠️ **Nguồn: kịch bản `L11` đang sản xuất**, không phải bảng giá chính thức từ khối sales.
> → Dùng được để **viết nháp**, nhưng ⛔ **phải đối chiếu bảng giá hiện hành trước khi lên ads** (`om-G` L03).

| Dịch vụ | Giá | Mô tả đi kèm trong kịch bản |
|---|---|---|
| **Cắt mí Plasma** | **8 triệu** | Công nghệ hạn chế sưng, hồi phục nhanh |
| **Cắt mí 6D** | **12,8 triệu** | Chỉ Nano siêu mảnh 0,01mm |
| **Cắt mí + tạo khoé** | **13,6 triệu** | Mắt trông dài, cân đối hơn |
| **Cắt mí + cấy mỡ** | **17,9 triệu** | Mí rõ nét, đầy đặn, tươi trẻ |
| **Nâng cung mày** | **8,8 triệu** | Loại bỏ da dư, trẻ hoá mắt |

**Trọn gói gồm:** thăm khám · xét nghiệm · bác sĩ chuyên khoa trực tiếp thực hiện · ekip + phòng mổ vô khuẩn · chăm sóc hậu phẫu.

### 6b. ★ BẢO HÀNH — BA MỨC KHÁC NHAU TRONG CÙNG HỆ THỐNG

```
⚠️ PHÁT HIỆN QUAN TRỌNG — ba con số đang cùng lưu hành:

  "bảo hành nếp mí lên đến 3 NĂM"   ← kịch bản L11 mắt (cụ thể, khả tín nhất)
  "bảo hành 10 NĂM"                 ← chân dung CD3 mũi
  "bảo hành TRỌN ĐỜI"               ← nhiều hook mũi đang chạy

→ Ba cái này KHÔNG THỂ cùng đúng cho cùng một dịch vụ.
```

**Cách agent xử:**
- **Mắt** → dùng `3 năm` *(có nguồn cụ thể nhất)*, vẫn ghi `⚠️ đối chiếu văn bản`.
- **Mũi** → ⛔ **không dùng số nào**. `[CHỜ XÁC NHẬN]`, viết *"chính sách bảo hành bằng văn bản"* không kèm số.
- ⛔ **Không bao giờ dùng *"trọn đời"*** cho đến khi có văn bản xác nhận đúng chữ đó — đây là cờ 🔴 (`om-G` §2).

⚠️ **Bảo hành theo dịch vụ, không theo hệ thống.** ⛔ Đừng lấy `3 năm` của mắt gán cho mũi.

### 6c. MŨI & CÁC DỊCH VỤ KHÁC — CHƯA CÓ BẢN HIỆN HÀNH

```
⚠️ [CHỜ XÁC NHẬN] — ai cấp: khối vận hành / sales

CHẶN: mọi phiếu format L11 và mọi hook nấc A4 của dịch vụ NGOÀI mắt.

Cần cấp:
  · Bảng giá trọn gói hiện hành theo từng dịch vụ + từng mức
  · Danh mục quyền lợi đi kèm từng gói
  · CHÍNH SÁCH BẢO HÀNH BẰNG VĂN BẢN — thời hạn thật là bao nhiêu
  · Chương trình ưu đãi đang chạy + SỐ SUẤT THẬT + ngày hết hạn
  · Chính sách trả góp (có/không, điều kiện)
```

⚠️ **Con số đang lưu hành trong ads mũi mà agent ⛔ KHÔNG được tự dùng lại:**
*"chỉ 31TR"* / *"31TR (39TR)"* — xuất hiện trong nhiều ad cũ, **chưa đối chiếu bảng giá hiện hành**. Bảo hành mũi: xem §6b.

⛔ Lấy số từ hook cũ là cách sai phổ biến nhất. **Hook cũ không phải nguồn giá.**
⚠️ Kịch bản `L11` **là** nguồn giá khả tín hơn hook — nhưng chỉ cho **đúng dịch vụ của kịch bản đó**.

---

## 7. KHU VỰC PHÁT — ĐẶC ĐIỂM ĐÃ ĐO

Dùng khi điền cột `KHU VỰC` và khi cân nhắc `PORT` hook sang miền khác.

| Khu vực | Đặc điểm từ dữ liệu thật |
|---|---|
| **NAM** | Kho content dày nhất, nhiều ad TỐT nhất. Hook *"gọi tình trạng"* thắng rõ. |
| **BẮC** | ⚠️ Yếu hơn Nam — KPI pilot đặt mục tiêu *"≥40% ad đạt TỐT"*, tức hiện dưới mức đó. Nhiều ad TỐT ở Nam **chấm KÉM khi port sang Bắc**. |
| **MIỀN TÂY** | Công thức riêng và rất mạnh: **"lên thành phố làm"** — *"chị em miền Tây không nâng mũi ở miền Tây mà rủ nhau lên Kangnam Sài Gòn"*. Nhân được sang các tỉnh phía Bắc. |
| **VIỆT KIỀU** | Tệp riêng (Mỹ/Úc/Canada/Nhật/Hàn/Đài). Nỗi sợ riêng: **về nước ngắn ngày, sợ không kịp hồi phục và cắt chỉ**. |

### ★ Bốn quyền lợi riêng cho tệp Việt kiều — có trong kịch bản thật

Rút từ kịch bản `L02` và `L12`. Đây là **điểm bán mạnh mà hook mũi chưa dùng**:

```
① Cấp GIẤY XÁC NHẬN PHẪU THUẬT của bệnh viện
② Hỗ trợ làm THỦ TỤC HẢI QUAN
③ Hỗ trợ ĐƯA ĐÓN SÂN BAY
④ Tư vấn ONLINE + hướng dẫn đặt lịch trước khi bay
```

⚠️ Bốn mục này đã dùng cho **mắt**; mũi chưa có hook nào khai thác. → Đây là **lỗ hổng đáng lấp**, và vì là quyền lợi dịch vụ *(không phải claim y khoa)* nên **sạch pháp chế**.
⛔ Vẫn phải xác nhận bốn mục này còn áp dụng — `[CHỜ XÁC NHẬN]` khối vận hành.

⚠️ **Luật port:** một hook `TỐT` ở miền này ⛔ **không tự động `TỐT`** ở miền khác. Port thì **quay lại hook bằng giọng và bối cảnh miền đó**, giữ nguyên thân video (`om-E` §6).

---

## 8. BẢNG CHẶN TỔNG — AGENT TRA NHANH

| Phiếu loại này | Bị chặn bởi | Trạng thái |
|---|---|---|
| Có **tên bác sĩ** | §4 | 🔴 **CHẶN** — chưa có BS mũi xác minh |
| Format **L11** / hook nấc **A4** có giá, số suất | §6 | 🔴 **CHẶN** — chưa có bảng giá hiện hành |
| Nói **"bảo hành trọn đời / 10 năm"** | §6 | 🔴 **CHẶN** — chưa có chính sách văn bản |
| Nội dung **local** cơ sở ngoài 2 bệnh viện | §2 | 🔴 **CHẶN** — chưa có số giấy phép cơ sở đó |
| Kỹ thuật **tuyến bệnh viện** gắn địa chỉ clinic | §2 | 🔴 **CHẶN** — vượt phạm vi chuyên môn |
| Dùng **ảnh/video khách** chưa có consent | §5 | 🔴 **CHẶN** |
| Format **L13 / L14 / L15 / L16** | `om-D` §1 | 🟡 **HỎI LẠI** — chưa định nghĩa |
| Format **L01** | `om-D` §7 | 🟡 **KHUÔN MƯỢN** — chưa có kịch bản mẫu, dùng `L03` rút gọn |
| Giá **mắt / cắt mí** | §6a | 🟢 **CÓ SỐ NHÁP** — đối chiếu bảng giá hiện hành trước khi lên ads |
| **Bảo hành mũi** (mọi con số) | §6b | 🔴 **CHẶN** — ba mức đang xung đột |
| Nói **mốc hồi phục, thời gian mổ** | `om-G` §5 | 🟡 **HỎI LẠI** — cần BS duyệt |

★ **Sáu thứ cần xin để mở phần lớn các chặn trên:**
`① danh sách BS đã xác minh` · `② bảng giá hiện hành các dịch vụ ngoài mắt` · `③ chính sách bảo hành bằng văn bản — ⚠️ ba mức đang xung đột, xem §6b` · `④ số giấy phép đủ 7 cơ sở` · `⑤ định nghĩa format L13–L16` · `⑥ kịch bản mẫu cho L01`.

Agent **in sáu dòng này vào khối `[CHỜ XÁC NHẬN]` mỗi lần xuất phiếu**, cho tới khi được cấp.

⚠️ **Mục ③ là mục cấp bách nhất.** Ba con số bảo hành khác nhau đang **cùng chạy trên ads thật** — đây không chỉ là bất tiện nội bộ, mà là rủi ro pháp chế đang phát sinh (`om-G` §2, cờ 🔴).

---

<a id="om-I-khuon-kich-ban-nha"></a>

## ⟦ om-I-khuon-kich-ban-nha.md ⟧

# om-I · KHUÔN KỊCH BẢN CỦA NHÀ

> Sổ này là **khuôn thật đang dùng** — rút từ 11 kịch bản sản xuất có thật của chuyên khoa mắt (cắt mí).
> ⛔ **Agent viết theo khuôn này, KHÔNG tự nghĩ khuôn mới.** Editor đã quen đọc cột theo đúng thứ tự này.

---

## 1. ★ ĐẦU RA CÓ HAI TẦNG — ĐỪNG TRỘN

Đây là điều quan trọng nhất của sổ.

```
TẦNG 1 — PHIẾU ORDER        1 dòng = 1 clip      → cho quản lý & điều phối
         42 trường, 6 khối (om-E §4)
         trả lời: clip này là gì, cho ai, chạy ô nào, ai duyệt, đo bằng gì

TẦNG 2 — KỊCH BẢN CHI TIẾT  1 dòng = 1 NHỊP     → cho editor & DOP
         khuôn nhà, 4–7 cột (§2 dưới)
         trả lời: giây này đọc câu gì, hiện chữ gì, lấy footage nào
```

⛔ **Không gộp hai tầng vào một bảng.** Một clip `L03` có 20–25 nhịp; nhét 25 nhịp vào một ô là bảng không ai đọc được.
★ **Agent xuất cả hai:** phiếu order một sheet, rồi **mỗi clip một sheet kịch bản riêng** — đúng như cách nhà đang làm *(mỗi format một file Google Sheet riêng, xem `om-D` §7)*.

---

## 2. KHUÔN CỘT — LÕI CHUNG + BIẾN THỂ

### Lõi chung — bốn cột, mọi format đều có

| Cột | Nội dung | ⛔ Luật |
|---|---|---|
| `STT` | Số nhịp. Dòng cuối ghi `THUMB` / `14thumb` / `10 thumb` | ⛔ Không bỏ dòng THUMB |
| `VOICE` / `NỘI DUNG` | **Lời thoại đọc nguyên văn.** Kèm mốc giây trong footage gốc khi lấy tiếng thật: `1:03`, `3p02`, `0:39` | ⛔ Không viết mô tả thay lời thoại |
| `TEXT` | Chữ hiện trên hình. **Ngắn hơn lời thoại rất nhiều** | ⛔ Không chép lại lời thoại |
| `FOOTAGE` / `FT` / `SOURCE` / `HÌNH ẢNH` | Đường dẫn footage + **chỉ dẫn dựng** | ⛔ Không ghi *"thêm B-roll"* |

### Biến thể theo format

| Format | Cột đầy đủ |
|---|---|
| `L02` | `STT · TEXT · THIẾT KẾ · HÌNH ẢNH` *(không có cột voice — dùng voice AI đọc text)* |
| `L03` | `TALK · NỘI DUNG · TEXT · FT · NOTE · FIX` ★ nhiều cột nhất |
| `L04` `L05` `L09` | `STT · Voice · Text · Note` |
| `L06` | `STT · ⟨nhịp⟩ · Nội dung · Text · Design · Link FT` |
| `L07` | `STT · Nội dung · Text · Source · Note` |
| `L08` | `⟨ ⟩ · Voice · Text · Source · Bối cảnh` |
| `L10` | `STT · VOICE · TEXT · FOOTAGE · 1920x1080` |
| `L11` `L12` | `STT · NỘI DUNG · TEXT · THIẾT KẾ · HÌNH ẢNH + MÔ TẢ` |

⚠️ **`L01` chưa có kịch bản mẫu** — mục lục để trống ô link. Dùng khuôn `L03` rút gọn *(bỏ cột `TALK` và `FIX`)*, ghi rõ là khuôn mượn.

### Hai cột đặc biệt, đừng bỏ

| Cột | Vai trò |
|---|---|
| `TALK` *(L03)* | Tên QC + **tên file footage gốc** của buổi talk — vd `QC_Cắt mí_Talk bác sĩ Mỹ Combo cắt mí cấy mỡ mắt / C3524.MP4`. Một buổi talk cắt ra nhiều clip, cột này nối clip về buổi gốc |
| `FIX` *(L03)* | ★ **Vòng feedback sửa.** Người duyệt ghi yêu cầu chỉnh vào đây *(“Rút ngắn text, chỉ để 2 dòng và cho to lên”, “Đổi ft khách già hơn 30-35 tuổi”)* |

⚠️ **Agent để cột `FIX` TRỐNG.** Đó là chỗ của người duyệt, ⛔ agent không tự điền.

---

## 3. ★ THUẬT NGỮ DỰNG CỦA NHÀ — DÙNG ĐÚNG TỪ NÀY

Editor đọc hiểu ngay những từ này. ⛔ Đừng diễn đạt lại bằng từ khác.

| Thuật ngữ | Nghĩa |
|---|---|
| **`FT`** | Footage |
| **`trám full`** | Chèn footage đè **kín khung** |
| **`trám cận`** | Chèn footage đè, **cỡ cảnh cận** |
| **`chia đôi, trám hình trên, bsi nói ở dưới`** | Chia khung ngang: hình minh hoạ trên, bác sĩ nói dưới |
| **`chia đôi khung`** | Split screen |
| **`cho bác sĩ xuống góc`** | Thu bác sĩ thành cửa sổ nhỏ ở góc (PiP) |
| **`tách nền bác sĩ`** | Xoá phông, đặt bác sĩ đè lên footage khác |
| **`khung box comment`** / **`bar text dạng cmt`** | Khung chữ kiểu bình luận TikTok *(xem §4 — có tool riêng)* |
| **`Text nền FT`** / **`text trên nền`** | Chữ đặt trên footage |
| **`biến đổi trc sau`** | Chuyển cảnh before → after |
| **`ra beauty`** / **`FT Beauty`** | Footage quay đẹp sau phẫu thuật |
| **`Tt xấu`** / **`FT đẹp`** | Footage tình trạng trước / kết quả sau |
| **`dán nhãn 2026`** / **`tag chữ Mới`** | Gắn nhãn đồ hoạ lên hình |
| **`multi pic`** / **`template nhiều hình ảnh`** | Lưới nhiều ảnh/video khách |

### Giọng đọc
- **`Voice AI`** dùng cho **câu hỏi** trong format talk — *"các câu hỏi dùng voice AI miền Nam"*.
- Lời bác sĩ, lời khách → **giữ tiếng thật**, cắt theo mốc giây ghi ở cột `VOICE`.
- Ghi rõ khi cần: *"Dùng voice AI nha"*, *"Cắt voice theo đoạn t note nhé"*.

---

## 4. ⛔ QUY ĐỊNH TEXT — THÔNG SỐ CỨNG

> Nguồn: sheet *Quy định text* của khối. ⛔ Agent ghi đúng thông số này vào cột `THIẾT KẾ`, không tự chọn font/màu.

| Hạng mục | Thông số |
|---|---|
| **Font** | `Roboto` |
| **Màu** | `#114D8F` (xanh) · `#ef6103` (cam) · trắng + đen |
| | ⚠️ **Nên dùng trắng – đen cho dễ nhìn** |
| **Viền** | `20` cho trắng/đen · `30` cho xanh/cam |
| **Cỡ chữ** | `15` · tỉ lệ `100%` |
| **Subtext** | vị trí `X: 0` · `Y: -1050` · cỡ chữ `10` · tỉ lệ `100%` · phông nền theo thông số |
| **Khung câu hỏi** | Tool: `imta.edu.vn/tool-tao-comment-tiktok` · kích cỡ `65%` · `X: -200` · `Y: -840` |
| **Tỉ lệ khung hình** | `1920x1080` *(ghi ở `L10`)* |

### ⛔ Hai điều cấm
```
- Không dùng khung
- Không thiết kế
```
→ Text đặt thẳng trên footage. ⛔ Không dựng khung viền, không làm đồ hoạ trang trí.

---

## 5. NGUỒN FOOTAGE — GHI ĐƯỜNG DẪN THẬT

Kịch bản thật ghi **đường dẫn tuyệt đối**, không ghi mô tả chung chung.

| Loại nguồn | Dạng |
|---|---|
| **Ổ lưu trữ chính** | `Z:\KANGNAM 2026\CẮT MÍ\09.07 - Cắt mí Hải Linh\Phẫu thuật\C0940.MP4` |
| **Thư mục case nhân vật** | `Z:\KANGNAM 2025\CASE NHÂN VẬT\Cắt mí\Mí\...` |
| **NAS lưu tạm** | `\\10.195.55.58\Lưu tạm\...` · `\\10.195.55.98\Lưu Tạm\Mắt\...` |
| **NAS chia sẻ** | `https://10.195.50.31:5001/sharing/...` · `https://10.195.0.30:5001/sharing/...` |
| **Google Drive** | `https://drive.google.com/file/d/.../view` |

**Quy ước ghi một dòng footage:**
```
<tên file>
<đường dẫn thư mục>
[mốc giây cần lấy]     vd: "từ 0:51"  ·  "Đoạn 0:27"  ·  "cắt 0s18 - 0s20"
[chỉ dẫn xử lý]        vd: "Chỉnh đỡ vàng nhé"  ·  "Tăng speed"  ·  "zoom cận"
```

⚠️ **Agent không biết ổ Z: có file gì.** → Ghi **mô tả footage cần** + `[CHỜ ĐIỀU PHỐI CẤP ĐƯỜNG DẪN]`, ⛔ **không bịa đường dẫn**.
Ví dụ đúng:
```
FT thăm khám — bác sĩ đo vẽ mí, cận tay bác sĩ   [CHỜ ĐIỀU PHỐI CẤP ĐƯỜNG DẪN]
```

---

## 6. DÒNG THUMB — BẮT BUỘC

Mọi kịch bản kết bằng một dòng thumbnail.

```
STT     TEXT                              THIẾT KẾ / HÌNH ẢNH
THUMB   CẮT MÍ 8 TRIỆU                    Banner · ảnh mí đẹp
        CÓ PHÁT SINH THÊM?

THUMB   SINH VIÊN ĐI CẮT MÍ               Mắt xấu đẹp
        7 CỦ KHOAI

THUMB   CẮT MÍ 6D Kangnam                 Công nghệ · mẫu mắt đẹp · text
        CÔNG NGHỆ MỚI NHẤT 2026
```

**Luật:** text thumb **≤ 2 dòng**, in hoa, **lặp lại hook** chứ không viết ý mới.

---

## 7. KHỐI "TỐI ƯU ⟨VÙNG⟩" — VIẾT LẠI THEO GIỌNG MIỀN

Kịch bản thật có khối phụ ở cuối: **`TỐI ƯU MIỀN TÂY`** — cùng nội dung, viết lại bằng giọng địa phương.

| Bản chuẩn | Bản miền Tây |
|---|---|
| *"Cắt mí báo giá 8 triệu, liệu đến lúc làm có phải trả thêm?"* | *"Cắt mí báo giá 8 triệu, tới lúc làm có tốn thêm tiền **hông**?"* |
| *"Mức giá này đã bao gồm trọn gói"* | *"Giá này là trọn gói luôn **nha**!"* |
| *"Vậy bạn cắt mí hết bao nhiêu? Inbox nhận báo giá ngay!"* | *"Vậy bạn cắt mí hết bao nhiêu tiền? Inbox **liền tay**, nhận báo giá chi tiết **nha**!"* |

**Dấu hiệu giọng miền Tây:** `nha` · `nghen` · `hông` · `liền tay` · `đó nghen` · `luôn`.

⛔ **Chỉ viết lại phần `VOICE` và `TEXT`.** Footage, thiết kế, thứ tự nhịp giữ nguyên — cùng một bản dựng, chỉ thay tiếng.
→ Order ghi `KHU VỰC = MIỀN TÂY` → agent xuất **thêm** khối này, không thay bản chuẩn.

---

## 8. NHỊP KỂ THEO FORMAT — RÚT TỪ KỊCH BẢN THẬT

### `L06` Review — có nhãn nhịp rõ ràng
```
INTRO      → hook, gọi tình trạng   "Sinh viên đi cắt mí 7 củ khoai thì sẽ như thế nào?"
TÌNH TRẠNG → mắt trước, nói khuyết điểm
GIỚI THIỆU → vì sao chọn nơi này
BIẾN ĐỔI   → mốc ngày 1-2 · ngày 5 · ngày 7
ĐẸP        → kết quả, cảm nhận
CTA        → mời nhắn tin
THUMB
```

### `L07` Hành trình — kể theo mốc thời gian của ca
```
HOOK → tình trạng (có mốc giây tiếng thật) → GIẢI PHÁP (bác sĩ chỉ định)
→ thực hiện (45P) → ngày 3 → ngày 7 → biến đổi xấu/đẹp → CTA → THUMB
```

### `L09` `L12` Công nghệ / Local — liệt kê luận điểm
```
hook công nghệ → từng luận điểm một nhịp (mỗi nhịp 1 text ngắn + 1 FT)
→ chốt uy tín → CTA → THUMB
```

### `L10` Quy trình — đánh số bước
```
mở (tên quy trình + chuẩn) → B1 đo vẽ → B2 sát khuẩn → B3 gây tê
→ B4 tạo đường cắt → B5 xử lý da/mỡ → B6 khâu → chốt chuẩn → CTA
```

### `L11` Giá — hỏi giá, giải thích, liệt kê, chốt
```
hook câu hỏi giá → mức giá cơ bản gồm gì → ưu điểm công nghệ
→ trọn gói gồm những gì → BẢNG GIÁ các mức → "không phải đắt nhất là đẹp nhất"
→ CTA hỏi giá → THUMB → [khối TỐI ƯU MIỀN TÂY]
```

---

## 9. ⚠️ ĐỐI CHIẾU VỚI CỔNG B — ĐỌC KỸ MỤC NÀY

> **Kịch bản thật đang chứa nhiều câu mà `om-G` gắn cờ.** Đây không phải lỗi của `om-G`, cũng không phải lý do để nới `om-G`.

| Câu trong kịch bản thật | Cờ | Điểm L |
|---|---|---|
| *"Không đau - Không sưng bầm"* **đặt làm TEXT thương hiệu** | 🟡 | `L03` — chỉ được là lời khách kể |
| *"VÔ KHUẨN 100%"* | 🟡 | `L04` — khẳng định tuyệt đối |
| *"Đường sẹo 'tàng hình'"* | 🟡 | `L03` — cam kết kết quả |
| *"7 NGÀY LÀ ĐẸP"* · *"10 ngày là đẹp"* · *"Đẹp ngay trong lần đầu thực hiện"* | 🟡 | `L03` — hứa mốc thời gian/kết quả |
| *"15+ NĂM KINH NGHIỆM"* · *"20.000+ KHÁCH HÀNG"* · *"Hàng nghìn khách hàng"* | 🔴 | `L04` — con số cần nguồn |
| *"bảo hành nếp mí lên đến 3 năm"* | 🟢 | hợp lệ **nếu** khớp văn bản — xem `om-H` §6 |
| Tên bác sĩ: *"Dr. Mard Nguyen"* · *"Dr. Hải"* | 🔴 | `L01` `L02` — cần `om-H` xác minh |
| Tên khách thật: *Linh Chi · Hải Linh · Kim Ngân · Bảo Yến · MC Hà Trinh* | 🔴 | `L05` — cần consent |
| *"Gây tê… giúp khách hàng không cảm thấy đau đớn nào"* | 🟡 | `L03` — tuyệt đối hoá |
| *"Quy trình chuẩn Bộ Y tế"* | 🟢 | hợp lệ nếu có căn cứ |

### ⛔ Agent xử thế nào

1. **Viết theo khuôn nhà** *(cột, thuật ngữ, thông số text)* — khuôn là của nhà, agent theo.
2. **Vẫn chấm cờ theo `om-G`** — nội dung là việc của cổng B, ⛔ không vì *"kịch bản cũ viết thế"* mà bỏ qua.
3. **Nêu kèm dẫn chứng:** *"Câu này giống câu đang dùng ở kịch bản `L09` nhịp 2 — nhưng vẫn là cờ 🟡 `L03`. Đề xuất: đổi `KHÔNG ĐAU – KHÔNG SƯNG BẦM` thành `Hạn chế sưng đau`."*
4. ⛔ **Không tự ý sửa kịch bản cũ.** Agent chỉ gắn cờ cho **clip mới** mình viết.

> ⚠️ **Nói rõ với người order một lần:** nhiều ad đang chạy có cờ. Việc rà lại kho cũ là **quyết định của khối + pháp chế**, không phải việc agent tự làm.

---

## 10. TỰ KIỂM KỊCH BẢN TRƯỚC KHI GỬI

```
[ ] Đúng khuôn cột của format đó chưa (§2)?
[ ] Cột VOICE là lời thoại đọc nguyên văn, không phải mô tả?
[ ] Lấy tiếng thật thì có ghi mốc giây chưa?
[ ] Cột TEXT có ngắn hơn VOICE không — hay lỡ chép lại?
[ ] Dùng đúng thuật ngữ nhà (trám full · chia đôi · ra beauty) chưa (§3)?
[ ] Cột THIẾT KẾ có ghi đúng thông số text (Roboto · màu · viền · cỡ) chưa (§4)?
[ ] Footage: ghi mô tả + [CHỜ ĐIỀU PHỐI CẤP ĐƯỜNG DẪN] — có bịa đường dẫn Z: không (§5)?
[ ] Có dòng THUMB chưa, text ≤2 dòng, in hoa (§6)?
[ ] KHU VỰC = MIỀN TÂY thì đã thêm khối TỐI ƯU chưa (§7)?
[ ] Cột FIX để TRỐNG cho người duyệt chưa (§2)?
[ ] Đã chấm cờ om-G cho từng nhịp chưa (§9)?
```

---

<a id="om-J-chan-dung-mat"></a>

## ⟦ om-J-chan-dung-mat.md ⟧

# om-J · CHÂN DUNG KHÁCH HÀNG — CHUYÊN KHOA MẮT

> Sổ này là **module dịch vụ**, song song với `om-C` *(mũi)*. Phương pháp chấm hook, luật 5A, công thức thắng/thua nằm ở `om-C` §5–§6 — ⛔ **không lặp lại ở đây**.
>
> ⚠️ **ĐỌC MỤC §0 TRƯỚC.** Khác với `om-C` *(rút từ sheet chân dung đã chốt + 91 ad đã chấm)*, sổ này **chưa có sheet chân dung chính thức cho mắt**. Phần lớn nội dung là **suy ra từ kịch bản thật và các dòng order mắt** — đã ghi rõ nguồn từng mục.

---

## 0. ⚠️ NGUỒN & ĐỘ TIN CẬY — ĐỌC TRƯỚC KHI DÙNG

| Ký hiệu | Nghĩa |
|---|---|
| ✅ **DỮ KIỆN** | Có trong order hoặc kịch bản thật — dùng được ngay |
| 🔶 **SUY RA** | Agent suy từ kịch bản/order — dùng được để viết nháp, **nên xác nhận** |
| ⚠️ **CHƯA CÓ DỮ LIỆU** | Không có gì để dựa — ⛔ không dùng làm căn cứ |

```
⚠️ [CHỜ XÁC NHẬN] — ai cấp: khối Ads/Content

CẦN: sheet CHÂN DUNG KHÁCH HÀNG MẮT, đúng cấu trúc như sheet mũi
     (mã · tên · nhân khẩu · câu khách gõ · nỗi sợ chi phối · khát khao thật
      · rào cản · trigger · thông điệp thắng · format ưu tiên · tỷ trọng · LTV)

CẦN: cột HIỆU QUẢ cho các ad mắt đã chạy — hiện order mắt CHƯA có dòng nào
     được chấm TỐT/BT/KÉM, nên om-C §5 chưa có bằng chứng riêng cho mắt.
```

⚠️ **Hệ quả quan trọng:** công thức hook thắng/thua ở `om-C` §5 rút từ **91 ad mũi**. Áp sang mắt là **suy luận hợp lý, chưa phải bằng chứng**. Agent nói rõ điều này khi chấm hook mắt.

---

## 1. ⚠️ ÁNH XẠ MÃ CD — CÓ MỘT CHỖ LỆCH, CẦN BẠN CHỐT

`om-B` §2 quy định giữ nguyên mã `CD1`–`CD6` cho mọi dịch vụ để so sánh hiệu suất chéo tuyến. Áp sang mắt:

| Mã | Logic chung (`om-B` §2) | Mắt | Nguồn |
|---|---|---|---|
| `CD1` | Khuyết điểm cơ bản | **Mắt · Khuyết điểm** | ✅ có trong order |
| `CD2` | Làm nghề hình ảnh | **Mắt · Hot Face** | ✅ case MC, KOC trong kịch bản |
| `CD3` | Đã làm, cần sửa | **Mắt · Sửa lại** | ✅ hook `L03` nói thẳng về nhóm này |
| `CD4` | Nam giới | **Mắt · Nam giới** | ✅ case nam trong kịch bản `L04` |
| `CD5` | ~~Phong thuỷ / tướng số~~ → **Lão hoá** | **Mắt · Lão hoá** | ⚠️ **LỆCH — xem dưới** |
| `CD6` | Ca khó, bệnh lý | **Mắt · Sụp mí & bệnh lý** | ✅ có trong order |

### ⚠️ Chỗ lệch ở `CD5`

```
Mũi  : CD5 = Phong thuỷ / tướng số
Mắt  : không có dữ liệu nào về phong thuỷ mắt
       NHƯNG order có tệp "Mắt - Lão hóa" rất rõ, và kịch bản có case U50

→ Agent tạm xếp "Mắt · Lão hoá" vào CD5, và ĐÁNH DẤU LỆCH.
```

**Hệ quả nếu để lệch:** báo cáo so `CD5` giữa mũi và mắt sẽ **so hai tệp khác hẳn nhau** — phong thuỷ vs lão hoá. Đây là chính cái mà quy ước mã chung muốn tránh.

**Ba hướng xử, cần khối Ads chốt:**

| Hướng | Được | Mất |
|---|---|---|
| **A** · Giữ `CD5 = Lão hoá` cho mắt | Đủ 6 tệp, khớp order | ⛔ Vỡ so sánh chéo tuyến ở `CD5` |
| **B** · Mở mã mới `CD7 = Lão hoá`, để `CD5` trống cho mắt | Giữ nguyên so sánh chéo | Phá quy ước *"không đẻ mã mới"* |
| **C** · Gộp Lão hoá vào `CD6` *(cùng là nhóm chức năng/tuổi cao)* | Không đẻ mã, không vỡ so sánh | `CD6` thành hai tệp tâm lý khác nhau trong một mã |

⚠️ **Agent đang dùng hướng A** và in cảnh báo mỗi lần xuất phiếu `CD5` mắt. ⛔ Không tự chuyển hướng khác khi chưa được chốt.

---

## 2. SÁU CHÂN DUNG MẮT

### CD1 · Mắt · Khuyết điểm — *trụ cột*
| | |
|---|---|
| **Ai** 🔶 | 20–40 tuổi · nhân viên văn phòng, bán hàng, sinh viên · thu nhập trung bình |
| **Tình trạng** ✅ | Mắt một mí · mí lót · mắt nhỏ · **mắt buồn** · nhiều nếp mí · nếp quạt góc mắt trong · hai mắt không đều |
| **Gõ gì** ✅ | *"Cắt mí báo giá 8 triệu, đến lúc làm có phát sinh thêm không?"* · *"Cắt mí bao lâu thì đẹp?"* · *"Tạo khoé xong mắt có bị sẹo không?"* |
| **⛔ Nỗi sợ chi phối** ✅ | **Sợ chi phí phát sinh** *(nỗi sợ số 1 — xuất hiện ở cả order và kịch bản `L11`)* · sợ sẹo ở góc mắt trong · sợ sưng lâu nghỉ làm |
| **Khát khao** ✅ | Nếp mí **rõ nét, tự nhiên** · mắt to, có điểm nhấn · *"mắt có hồn, tươi tắn"* |
| **Rào cản** 🔶 | Ngân sách · khó xin nghỉ · chưa biết mình cần làm gì trong nhiều phương án |
| **⚡ Trigger** ✅ | **Bảng giá trọn gói nói rõ gồm gì** · mốc *30 phút thực hiện · 7 ngày cắt chỉ · 10 ngày đẹp* · case giống mình |
| **Thông điệp thắng** 🔶 | *"Cắt mí đúng tình trạng — nếp mí rõ nét, hồi phục nhanh, giá trọn gói không phát sinh"* |
| **Format ưu tiên** ✅ | `L11` giá *(đang là format mạnh nhất của mắt)* · `L04` B/A · `L06` review · `L01` talk hỏi đáp |

#### ★ Lát cắt SINH VIÊN trong CD1 — ✅ có kịch bản riêng
Không phải chân dung riêng, mà là **lát cắt theo ngân sách & thời điểm**:
- **Giọng:** trẻ, tự trào — *"Sinh viên đi cắt mí 7 củ khoai thì sẽ như thế nào?"* · *"sau 7749 lần lướt review"*
- **Thời điểm:** ⚡ **kỳ nghỉ hè** — *"tranh thủ kì nghỉ hè là tôi đi cắt mí ngay"*
- **Trigger riêng:** trả góp · mức giá thấp nhất trong bảng
- ⛔ **Target 18+**, ⛔ không dùng case dưới 18 tuổi

### CD2 · Mắt · Hot Face
| | |
|---|---|
| **Ai** ✅ | MC, KOC, người làm nghề hình ảnh lâu năm · *"đầu tư gì cho bản thân sau 10 năm vào nghề"* |
| **⛔ Nỗi sợ** 🔶 | Sợ mắt **lên hình thấy nếp nhăn** · sợ sưng lỡ job · sợ làm xong trông khác đi, mất nhận diện |
| **Khát khao** ✅ | Mắt **không già đi theo nghề** · lên hình tươi, có hồn |
| **⚡ Trigger** ✅ | Case người cùng nghề · mốc hồi phục ngắn · bác sĩ hiểu *"gu thẩm mỹ Á Đông"* |
| **Format ưu tiên** ✅ | `L07` hành trình *(kịch bản thật dùng đúng format này cho nhóm này)* · `L05` biến đổi |
| **⛔ Pháp chế** | Target 18+ · ⛔ không nêu tên người nổi tiếng · **consent bắt buộc** |

### CD3 · Mắt · Sửa lại — ✅ *tệp có hook mạnh nhất trong kịch bản*
| | |
|---|---|
| **Ai** ✅ | **Đã cắt mí rồi nhưng chưa hài lòng** |
| **Gõ gì** ✅ | *"Tại sao cắt mí rồi nhưng mắt vẫn chưa đẹp và trẻ như mong muốn?"* · *"Tại sao có nếp mí rõ mà mắt vẫn nhỏ, chưa có điểm nhấn?"* · *"Có mí nhưng mắt vẫn chưa đẹp, bác sĩ khuyên gì?"* |
| **⛔ Nỗi sợ** 🔶 | Sợ sửa nữa vẫn không đẹp · sợ đã tiêu tiền vô ích · sợ không ai chỉ ra được vấn đề thật |
| **Khát khao** ✅ | **Hiểu vì sao lần trước chưa đẹp** — nhóm này muốn *lời giải thích* trước khi muốn *dịch vụ* |
| **★ Insight đắt nhất** ✅ | Vấn đề thường **không ở nếp mí** mà ở: tương quan cung mày · hốc mắt sâu/thiếu mỡ · góc mắt trong–ngoài · da chùng. → *"cắt mí đơn thuần không giải quyết tất cả"* |
| **⚡ Trigger** ✅ | **Bác sĩ phân tích đúng tình trạng của mình** · chỉ định cụ thể cho từng ca · *"không phải ai cắt mí cũng làm combo"* |
| **Format ưu tiên** ✅ | **`L03` bác sĩ phân tích** *(chủ lực — giống `CD3` mũi)* · `L01` talk hỏi đáp |

### CD4 · Mắt · Nam giới
| | |
|---|---|
| **Ai** ✅ | Nam, mắt một mí / nếp quạt góc mắt trong |
| **⛔ Nỗi sợ** ✅ | **Sợ bị đánh giá vì đi thẩm mỹ** — hook thật mở bằng đúng nỗi sợ này: *"Đàn ông không có quyền làm đẹp?"* · sợ mất nét nam tính |
| **Khát khao** ✅ | *"x2 sự menly"* · mắt có hồn, tươi tắn · **tầm nhìn thoáng hơn** *(lợi ích chức năng — nam giới nhận lý do này dễ hơn lý do thẩm mỹ)* |
| **⚡ Trigger** ✅ | Case nam **giống mình**, ưu tiên **góc chính diện** · B/A rõ |
| **Format ưu tiên** ✅ | `L04` B/A góc chính diện · `L06` review |
| ⚠️ **Lưu ý viết** | Nhóm này thuyết phục bằng **chức năng + sự tự nhiên**, ⛔ không bằng từ ngữ thẩm mỹ nữ tính |

### CD5 · Mắt · Lão hoá — ⚠️ *mã đang LỆCH, xem §1*
| | |
|---|---|
| **Ai** ✅ | U40–U60 · order gọi là *"Mắt - Lão hóa"*; kịch bản có case U50 |
| **Tình trạng** ✅ | **Bọng mỡ** · da chùng, da dư · hốc mắt trũng · *"già trước tuổi"* · mắt trông mệt mỏi |
| **Gõ gì** ✅ | *"Bệnh huyết áp hoặc tiểu đường nhẹ có cắt mí được không?"* |
| **⛔ Nỗi sợ** ✅ | ★ **Sợ nguy hiểm vì tuổi cao, bệnh nền** *(nỗi sợ riêng của nhóm này — không nhóm nào khác có)* · sợ hồi phục lâu |
| **Khát khao** ✅ | Trông **tươi hơn, đỡ mệt mỏi** — ⛔ **không phải "trẻ như gái 20"**. Kịch bản thật dùng *"trẻ ra 5 tuổi"*, *"cải thiện đôi mắt tươi trẻ"* |
| **⚡ Trigger** ✅ | Case **cùng độ tuổi** · bác sĩ nói rõ về bệnh nền · cắt mí dưới / lấy bọng mỡ · nâng cung mày |
| **Dịch vụ** ✅ | Cắt mí dưới · lấy mỡ bọng mắt · cấy mỡ trẻ hoá · nâng cung mày · cắt mí 6D trên dưới |
| **Format ưu tiên** ✅ | `L04` B/A · `L01` talk hỏi đáp *(trả lời câu bệnh nền)* |
| **⛔ Pháp chế** | 🔴 Câu về **bệnh nền phải do BS duyệt** — đây là chỉ định y khoa, ⛔ agent không tự trả lời *"được/không được"* |

### CD6 · Mắt · Sụp mí & bệnh lý
| | |
|---|---|
| **Ai** ✅ | Sụp mí *(ptosis)* · mắt hai bên không đều · ảnh hưởng **tầm nhìn**, không chỉ thẩm mỹ |
| **Tình trạng** ✅ | Sụp mi · da dư che tầm nhìn · nếp quạt góc mắt trong nặng che phần hồ lệ |
| **⛔ Nỗi sợ** 🔶 | Sợ không sửa được · sợ ảnh hưởng chức năng mắt · sợ hai bên vẫn không đều sau mổ |
| **Khát khao** 🔶 | **Mắt mở bình thường, hai bên đều** — giống `CD6` mũi: muốn *bình thường*, không cần *đẹp nhất* |
| **⚡ Trigger** ✅ | Bác sĩ **khám và chỉ ra cơ chế** · kết hợp chỉnh sụp mí + cắt mí · case giống hệt mình |
| **Format ưu tiên** ✅ | `L03` phân tích · `L04` B/A |
| **⛔ Pháp chế** | 🔴 Sụp mí là **bệnh lý** → ⛔ không hứa kết quả, ⛔ không nói về chức năng thị lực nếu BS chưa duyệt · **consent bắt buộc** |

---

## 3. HÀNH TRÌNH 5A — MẮT

🔶 **Toàn bộ mục này là SUY RA** từ order mắt + kịch bản. ⚠️ Chưa có sheet 5A mắt chính thức *(sheet 5A hiện có là của mũi)*.

| Nấc | Khách đang nghĩ | ⛔ Nỗi sợ chi phối | Nội dung phải có | CTA chuẩn |
|---|---|---|---|---|
| **A1 · AWARE** | *"Mắt mình buồn/nhỏ/nhiều nếp mí — có cách nào không?"* | Không biết mắt mình thuộc tình trạng gì | So sánh các tình trạng mắt trên cùng khuôn mặt · talk chủ đề rộng | *"Xem mắt bạn thuộc kiểu nào"* |
| **A2 · APPEAL** | *"Nên cắt mí thường, 6D, hay phải làm combo?"* ✅ | Sợ chọn sai phương án · sợ làm rồi vẫn chưa đẹp | **Phân biệt các phương án theo tình trạng** · *"không phải ai cắt mí cũng làm combo"* · case B/A | *"Gửi ảnh mắt — bác sĩ chỉ ra bạn cần chỉnh gì"* |
| **A3 · ASK** | *"Giá bao nhiêu, có phát sinh? Bao lâu đi làm lại được? Có sẹo không?"* ✅ | ★ **Sợ chi phí phát sinh** · sợ sẹo · sợ sưng lâu · *(CD5)* sợ bệnh nền | **Bảng giá trọn gói nói rõ gồm gì** · mốc 30 phút – 7 ngày – 10 ngày · câu trả lời về sẹo · FAQ bệnh nền | *"Inbox nhận báo giá theo tình trạng"* |
| **A4 · ACT** | *"Chốt, nhưng chờ ưu đãi tốt"* ✅ | Sợ hết suất ưu đãi · sợ chi phí cao | Ưu đãi có hạn **số suất thật** · thăm khám 0đ · checklist trước mổ | *"Inbox giữ suất / giữ lịch"* |
| **A5 · ADVOCATE** | *"Kiêng gì, bao giờ cắt chỉ, bao giờ trang điểm lại được?"* | Kiêng phức tạp · không rõ mốc tái khám | Hướng dẫn hậu phẫu · mốc cắt chỉ · dấu hiệu cần quay lại | *"Lưu video — nhắn nếu cần hỗ trợ hậu phẫu"* |

⚠️ **Khác biệt rõ nhất so với mũi:** ở mũi, nấc `A3` nỗi sợ lớn nhất là *"không ai chịu trách nhiệm"*; ở mắt là **chi phí phát sinh**. → Hook mắt ở `A3` nên mở bằng **giá/phát sinh**, hook mũi ở `A3` nên mở bằng **bảo hành/trách nhiệm**.

---

## 4. ★ TỪ VỰNG TÌNH TRẠNG — DÙNG ĐÚNG TỪ KHÁCH DÙNG

Thành phần ① của công thức thắng là **gọi đúng tình trạng** (`om-C` §5). Đây là từ vựng mắt, lấy từ kịch bản thật:

```
MÍ        mắt một mí · mí lót · nhiều nếp mí · nếp mí không rõ · nếp mí rẻ quạt
KÍCH CỠ   mắt nhỏ · mắt buồn · mắt thiếu điểm nhấn · hai mắt không đều
GÓC MẮT   nếp quạt góc mắt trong · góc mắt sếch · góc mắt hẹp
DA & MỠ   da chùng · da dư · bọng mỡ · hốc mắt trũng · hốc mắt sâu · thiếu mỡ mí
CHỨC NĂNG sụp mí · da che tầm nhìn
TUỔI      già trước tuổi · mắt mệt mỏi · nếp nhăn quanh mắt · chân chim
```

⛔ **Đừng dùng từ chuyên môn khách không gõ:** *ptosis* · *blepharoplasty* · *cân cơ nâng mi*.
⛔ **Đừng dùng tính từ chung chung** *(kiểu `H1`)*: *"mắt đẹp hút hồn"* · *"ánh nhìn cuốn hút"* · *"đôi mắt biết nói"*.

---

## 5. DỊCH VỤ & GIÁ MẮT

Giá: `om-H` §6a *(có số nháp từ kịch bản `L11` — ⚠️ đối chiếu bản chính thức trước khi lên ads)*.

| Dịch vụ | Giải quyết tình trạng | Chân dung chính |
|---|---|---|
| **Cắt mí Plasma** · 8tr | Mắt một mí, mí lót, nếp mí không rõ | `CD1` |
| **Cắt mí 6D** · 12,8tr | Như trên, hồi phục nhanh hơn | `CD1` `CD2` |
| **Cắt mí + tạo khoé** · 13,6tr | Nếp quạt góc mắt trong, mắt ngắn | `CD1` `CD3` `CD4` |
| **Cắt mí + cấy mỡ** · 17,9tr | Hốc mắt trũng, thiếu mỡ, da chùng | `CD3` `CD5` |
| **Nâng cung mày** · 8,8tr | Da dư, tương quan cung mày | `CD5` |
| **Cắt mí dưới / lấy bọng mỡ** · `[CHỜ XÁC NHẬN]` | Bọng mỡ, lão hoá | `CD5` |
| **Chỉnh sụp mí** · `[CHỜ XÁC NHẬN]` | Sụp mí | `CD6` |

**Mốc thời gian ✅** *(từ kịch bản — vẫn cần BS duyệt khi đưa vào clip mới)*: 30 phút thực hiện *(cắt mí)* · 45 phút *(6D trên dưới)* · **7 ngày cắt chỉ** · **10 ngày vào form**.
**Bảo hành nếp mí: 3 năm** — xem `om-H` §6b, ⛔ không gán số này cho dịch vụ khác.

---

## 6. LỖ HỔNG PHỄU MẮT — CHƯA ĐỦ DỮ LIỆU ĐỂ DỰNG MA TRẬN

Order hiện có **9 dòng mắt**, phân bố:

| Nấc | CD1 Khuyết điểm | CD5 Lão hoá | CD6 Sụp mí |
|---|---|---|---|
| A2 · APPEAL | 1 | — | 1 |
| A3 · ASK | 1 | 2 | 1 |
| A4 · ACT | 1 | 1 | 1 |

**Bốn điều đọc ra ngay:**
1. ⚠️ **`CD2` · `CD3` · `CD4` đang bằng 0 trong order** — dù `CD3` là tệp có **hook mạnh nhất** trong kịch bản thật *(`L03`)*, và `CD4` đã có case quay xong. → **Lỗ hổng đáng lấp nhất.**
2. ⚠️ **`A1` và `A5` trống hoàn toàn** — giống hệt tình trạng của mũi.
3. **`A4` phụ thuộc hoàn toàn vào ưu đãi/sự kiện** — cả 3 dòng `A4` đều là hội thảo/sự kiện giảm giá. Rủi ro: hết sự kiện là hết content `A4`.
4. ⚠️ **Chưa dòng mắt nào có cột `HIỆU QUẢ`** → chưa biết hook mắt nào thắng.

⛔ **Chưa đề xuất tỷ trọng sản lượng cho mắt.** Tỷ trọng của mũi *(CD1 ~50% · CD3+CD6 ~25% · …)* rút từ 91 ad đã chấm; mắt chưa có cơ sở tương đương → `[CHỜ XÁC NHẬN]` khối Ads.

---

## 7. BỐN VIỆC NÊN LÀM — ƯU TIÊN THEO ĐÒN BẨY

| # | Việc | Vì sao |
|---|---|---|
| ① | **Mở tệp `CD3` Mắt · Sửa lại** | Có **4 hook thật đã viết sẵn** trong kịch bản `L03`, format chủ lực đã rõ, mà order chưa có dòng nào |
| ② | **Mở tệp `CD4` Mắt · Nam giới** | Đã có case quay xong *(“Đàn ông không có quyền làm đẹp?”)*, chỉ cần dựng |
| ③ | **Lấp `A5`** | Tệp `CUST` đã có, chi phí thấp nhất, mở đường cross-sell mắt ↔ mũi ↔ hàm |
| ④ | **Chấm số cho ad mắt** | Không có cột `HIỆU QUẢ` thì `om-C` §5 mãi không có bằng chứng riêng cho mắt |

---

## 8. TỰ KIỂM KHI VIẾT CHO MẮT

```
[ ] Đã gọi đúng tình trạng bằng từ khách dùng chưa (§4)?
[ ] Phiếu CD5 đã in cảnh báo mã đang LỆCH chưa (§1)?
[ ] Câu về BỆNH NỀN có để BS duyệt chưa — hay lỡ tự trả lời được/không (§2 CD5)?
[ ] Câu về SỤP MÍ có hứa kết quả hay nói về thị lực không (§2 CD6)?
[ ] Giá lấy từ om-H §6a và đã ghi "đối chiếu bản chính thức" chưa?
[ ] Mốc 30 phút / 7 ngày / 10 ngày đã ghi cần BS duyệt chưa?
[ ] Bảo hành: dùng "3 năm" cho mắt, ⛔ KHÔNG gán sang dịch vụ khác?
[ ] Lát cắt sinh viên đã ghi target 18+ chưa (§2 CD1)?
[ ] Khi chấm hook mắt, đã nói rõ công thức om-C §5 rút từ ad MŨI chưa (§0)?
```
