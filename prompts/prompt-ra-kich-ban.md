# PROMPT — VIẾT KỊCH BẢN (B5)

> Dùng khi hook đã chấm xong, giờ cần phiếu quay được.
>
> ★ **Đầu ra có HAI TẦNG** (`om-I` §1): `TẦNG 1` phiếu order — 1 dòng = 1 clip · `TẦNG 2` kịch bản chi tiết — 1 dòng = 1 nhịp, theo **khuôn nhà**. ⛔ Đừng trộn.

---

## Ra kịch bản chi tiết theo khuôn nhà (tầng 2)

```
Ra kịch bản chi tiết cho clip <mã>, theo đúng khuôn kịch bản của nhà.

- Tra kịch bản mẫu của format đó trước (om-D §7), rồi theo đúng khuôn cột
- Mỗi dòng một nhịp: STT · VOICE · TEXT · FOOTAGE (+ THIẾT KẾ / NOTE tuỳ format)
- VOICE là lời đọc nguyên văn; lấy tiếng thật thì ghi mốc giây
- TEXT ngắn hơn VOICE nhiều, đừng chép lại
- Dùng đúng thuật ngữ nhà: trám full · chia đôi trám hình trên bsi nói ở dưới
  · cho bác sĩ xuống góc · khung box comment · ra beauty
- THIẾT KẾ ghi đúng thông số: Roboto · màu · viền · cỡ chữ
- Footage: ghi MÔ TẢ cần gì + [CHỜ ĐIỀU PHỐI CẤP ĐƯỜNG DẪN] — đừng bịa đường dẫn Z:\
- Kết bằng dòng THUMB
- Cột FIX để trống cho người duyệt
```

### Nếu clip chạy miền Tây
```
Thêm khối TỐI ƯU MIỀN TÂY ở cuối: viết lại VOICE và TEXT bằng giọng miền
(nha · nghen · hông · liền tay). Giữ nguyên footage, thiết kế và thứ tự nhịp.
```

---

## Ra kịch bản cho cả order

```
Hook đã soi xong. Giờ ra phiếu kịch bản sản xuất cho các dòng chấm ✓ và ⚠.

Mỗi phiếu đủ 42 trường, 6 khối. Riêng khối KỊCH BẢN em viết kỹ:
- Lời thoại chia theo mốc giây, đọc được nguyên văn
- Text on screen riêng, không chép lại lời thoại
- Shot list có cỡ cảnh và ghi chú đặc biệt
- CTA nói rõ GỬI GÌ – NHẬN GÌ

Ô nào em suy ra thì ghi (suy ra). Cuối bảng in khối GIẢ ĐỊNH và khối
[CHỜ XÁC NHẬN] kèm ai cấp, chặn mấy phiếu.
```

---

## Ra kịch bản cho một dòng (đi sâu)

```
Viết kỹ một phiếu thôi, dòng này:

CHÂN DUNG : CD3 · Mũi - Sửa lại
NẤC 5A    : A3 · ASK
HOOK      : "Vì sao mũi sửa lần 2 khó hơn lần đầu? Bác sĩ phân tích 1 ca thật"
CTA       : "Gửi ảnh + tiền sử phẫu thuật để bác sĩ đánh giá"
KHU VỰC   : Cả 2

Em muốn lời thoại đủ để bác sĩ đọc thẳng trước camera, không phải đọc rồi tự diễn.
```

---

## Khung 4 khối — nhắc lại để đối chiếu

```
HOOK      0–3s    câu mở, đọc nguyên văn + TEXT ON SCREEN
BỐI CẢNH  3–8s    đặt người nói vào đâu, vì sao nên tin
LÕI       8–40s   ★ CƠ CHẾ — chia mốc giây nhỏ
CTA       40–55s  gửi gì – nhận gì
```

### ⛔ Bốn điều cấm
| Cấm | Vì sao |
|---|---|
| Lời thoại không có mốc giây | Editor không biết cắt ở đâu |
| *"bác sĩ giải thích về filler"* | Đó là mô tả, không phải lời thoại |
| Khối LÕI không có cơ chế, chỉ lời khen | Không tạo niềm tin + rủi ro pháp chế L06 |
| CTA *"inbox ngay"* trơ trọi | Phải nói gửi gì, nhận gì |

---

## Yêu cầu viết lại khi agent viết chung chung

| Agent viết | Nói |
|---|---|
| *"Bác sĩ giải thích về filler"* | `Viết thành câu bác sĩ đọc được nguyên văn.` |
| *"Quay ở phòng khám"* | `Ghi mã bối cảnh + bàn ghế + hướng ngồi + đạo cụ trong khung.` |
| *"Thêm B-roll minh hoạ"* | `Ghi mốc giây + nội dung hình + cỡ cảnh.` |
| *"CTA mạnh"* | `CTA phải nói rõ gửi ảnh gì, nhận lại gì.` |
| Khối LÕI toàn lời khen | `Khối LÕI phải có cơ chế. Giải thích cái gì xảy ra trong cơ thể.` |

---

## Ra call sheet

```
Gom các phiếu này thành call sheet một buổi quay.

Gom theo BỐI CẢNH, không gom theo nhân vật — đổi set 15 phút, đổi người 2 phút.
Xếp S-STUDIO trước (set cố định), bối cảnh di động sau.
Chèn 15 phút đổi set giữa hai nhóm, cộng ước phút quay xem có vừa buổi không.

Phiếu nào cần khách thật thì ghi rõ ⛔ kiểm consent trước giờ quay.
```

---

## Tái dựng từ video cũ

```
Những dòng này có cột LINK — tức là đã có video. Đừng ra kịch bản quay mới.
Cho em biết mỗi dòng nên đi hướng nào:

- PORT khu vực    : giữ thân video, quay lại hook bằng giọng/bối cảnh miền đó
- ĐẶT HOOK MỚI    : giữ thân, làm 2 biến thể hook mới
- DỰNG LẠI        : cắt đoạn vi phạm, thay text overlay

Nhắc em dòng nào cần kiểm thời hạn consent cũ trước khi dùng lại footage khách.
```
