# PROMPT — LẤP LỖ HỔNG PHỄU (loại yêu cầu ③)

> Dùng khi không có order sẵn, mà cần biết **đang thiếu content ở đâu** rồi mới làm.

---

## Dựng ma trận

```
Dựng ma trận chân dung × 5A từ file này. Đếm số content đang giữ trong từng ô.
Ô nào = 0 thì đánh dấu.

Rồi nói cho em ba điều:
- Chân dung nào đang gánh quá nhiều (rủi ro tập trung)
- Nấc nào đang trống cả hàng
- Chân dung nào chưa có dữ liệu để biết nên giữ hay bỏ

Đừng viết kịch bản. Em muốn thấy bức tranh trước.

<link sheet hoặc file>
```

---

## Ví dụ bức tranh thật (pilot mũi, 34 content)

| Nấc | CD1 | CD2 | CD3 | CD4 | CD5 | CD6 |
|---|---|---|---|---|---|---|
| A1 | 4 | **0** | **0** | **0** | **0** | 1 |
| A2 | 14 | **0** | 2 | 1 | **0** | 1 |
| A3 | 6 | **0** | **0** | 1 | **0** | **0** |
| A4 | 3 | **0** | **0** | 1 | **0** | **0** |
| A5 | **0** | **0** | **0** | **0** | **0** | **0** |

**Ba kết luận đọc ra ngay:**
1. **CD1 chiếm 27/34** — phễu dựa gần như toàn bộ vào một chân dung
2. **Cả hàng A5 trống** — không nuôi khách đã làm, mất hết cross-sell
3. **CD2 và CD5 = 0** — chưa có dữ liệu để quyết giữ hay bỏ

---

## Đề xuất lấp

```
Giờ đề xuất kế hoạch lấp. Luật:

- ⛔ Đừng lấp mọi ô cùng lúc
- Theo tỷ trọng đã kiểm chứng: CD1 ~50% · CD3+CD6 ~25% · CD4 ~12% · CD2+CD5 ~12% (test nhỏ)
- Ưu tiên ô nào có đòn bẩy cao nhất trước, nói rõ vì sao
- Mỗi ô đề xuất 1–2 hook, ghi [HOOK AGENT ĐỀ XUẤT — chưa qua duyệt]
- Gắn luôn ô camp, format, nhiệt cho từng hook

Cho em biết sprint 1 làm gì, sprint 2 làm gì.
```

---

## Ba ô đáng lấp trước — và vì sao

| Ô | Vì sao có đòn bẩy cao |
|---|---|
| **A5 · bất kỳ CD** | Tệp `CUST` đã có sẵn, chi phí thấp nhất, mở đường cross-sell. Đang trống hoàn toàn. |
| **A4 nhắm `BOOKED-NS`** | Khách đã đặt lịch nhưng chưa đến, **no-show ~28%**. Doanh thu gần chốt — đòn bẩy cao nhất. |
| **A3 · CD3 / CD6** | `P3` chiếm **48% ngân sách**, và KPI pilot đòi *"≥1 hook CD3/CD6 đạt mục tiêu P3"*. |

---

## Trước khi đề xuất ô mới — kiểm có nên PORT thay vì viết mới

```
Trước khi viết hook mới, quét lại các ad đã chấm TỐT.

Có hook nào đã TỐT ở một khu vực mà có thể PORT sang khu vực khác không?
Port rẻ hơn viết mới: giữ thân video, chỉ quay lại hook.

Nhắc em: một hook TỐT ở miền Nam không tự động TỐT ở miền Bắc — port thì
phải quay lại hook bằng giọng và bối cảnh miền đó.
```

---

## Luật viết hook mới cho ô trống

1. **Lấy nỗi sợ chi phối** của chân dung ở nấc đó — ⛔ không lấy khát khao, nỗi sợ bán tốt hơn
2. **Viết lại thành câu khách tự gõ** — dùng đúng từ khách dùng (*"mũi tẹt"*, *"bóng đỏ"*, *"co rút"*)
3. **Gắn một thành phần** kỹ thuật hoặc bằng chứng
4. **Soát qua 7 kiểu KÉM** (`H1`–`H7`)
5. **Gắn CTA theo nấc**, ưu tiên *"gửi ảnh tình trạng"*

⛔ Mỗi hook mới ghi `[HOOK AGENT ĐỀ XUẤT — chưa qua duyệt]`.
⛔ Hook mới chỉ lên ads khi `DUYỆT = 🟢 XANH` — lịch duyệt **thứ Tư hằng tuần**.

---

## Hướng hook vừa chạy được vừa sạch pháp chế

Khi bí, đi hướng **"dám nói điều bất lợi cho mình"**. Dữ liệu thật cho thấy hướng này chạy được và an toàn nhất:

```
"Khi nào bác sĩ khuyên CHƯA NÊN mổ?"
"Tại sao bác sĩ không khuyến khích nâng mũi theo trend"
"Mũi cao chưa chắc đã đẹp — đây là 3 kiểu mũi cao mà vẫn xấu"
"Tôi từ chối 30% ca đến tư vấn — vì sao?"
```

Ca từ chối, chống chỉ định, giới hạn của phương pháp — đây là nguồn niềm tin lớn nhất.
