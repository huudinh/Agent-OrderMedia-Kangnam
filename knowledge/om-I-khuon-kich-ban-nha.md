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
