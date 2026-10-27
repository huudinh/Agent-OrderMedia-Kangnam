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
