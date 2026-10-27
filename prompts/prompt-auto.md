# ★ PROMPT AUTO — MỘT CÂU LÀ ĐỦ

> Dùng khi không muốn nghĩ. Dán một trong các câu dưới, agent tự dẫn từng bước.

---

## Câu ngắn nhất

```
Ra kịch bản sản xuất cho order này.
```
*(kèm link sheet hoặc file excel đính kèm)*

Agent sẽ: đọc file → báo số dòng → chuẩn hoá → chạy cổng A → chấm hook → hỏi tối đa 3 câu → ra phiếu.

---

## Có bối cảnh một chút (tốt hơn)

```
Đây là order nội dung mũi tuần này. Ra kịch bản sản xuất chi tiết để ekip quay
batch thứ Tư. Có 2 khách hàng thật đã đồng ý quay.

<link sheet hoặc file>
```

---

## Ba lối tắt

| Muốn | Gõ |
|---|---|
| Ra hết, không hỏi gì | `Cứ ra hết đi, chỗ nào thiếu thì em tự điền mặc định và in đậm GIẢ ĐỊNH.` |
| Giống kỳ trước | `Làm giống order tuần trước, chỉ hỏi em cái gì đã đổi.` |
| Chỉ soát pháp chế | `Chỉ soát pháp chế thôi, đừng viết kịch bản.` |

---

## Agent sẽ hỏi gì

Tối đa **3 câu một lượt**, mỗi câu luôn có `d) Để em chọn mặc định`. Trả lời gộp được: `1b 2a 3d`.

**Lượt 1** — dịch vụ nào · quay mới hay tái dựng từ video cũ · hạn quay
**Lượt 2** — có khách hàng thật không · bối cảnh nào đang trống · ai duyệt pháp chế
**Lượt 3** — ưu tiên nấc nào · khu vực · format ưu tiên

Thanh tiến độ in kèm mỗi lượt:
```
TIẾN ĐỘ ███░░░░░░░ 18 dòng order · đã ra kịch bản 5 · còn ~2 lượt hỏi
```

---

## Agent sẽ trả về gì

1. **Bảng cổng A** — 8 ô, dòng nào thiếu gì
2. **Bảng chấm hook** — `✓` / `⚠` / `✗` + kiểu KÉM trúng phải + hook đề xuất
3. **Phiếu kịch bản** — 32 trường, 6 khối, mỗi dòng một clip
4. **Call sheet** — gom theo bối cảnh, có khung giờ
5. **Bảng cờ pháp chế** — cờ + điểm L + **câu thay thế**
6. **Khối GIẢ ĐỊNH** + **khối `[CHỜ XÁC NHẬN]`** (ai cấp, chặn mấy phiếu)

---

## Nếu agent làm sai, nói thẳng một câu

| Agent làm sai | Nói |
|---|---|
| In form dài bắt điền | `Đừng in form. Tự điền cái suy ra được rồi hỏi em 3 câu.` |
| Tự đổi hook không khai | `Hook nào em đổi thì in đủ ba dòng gốc / đề xuất / vì sao.` |
| Viết lời thoại chung chung | `Viết lời thoại đọc được nguyên văn, có mốc giây.` |
| Ghi "vi phạm L04" mà không sửa | `Cờ nào cũng phải có câu thay thế cụ thể.` |
| Bịa giá, bịa mốc hồi phục | `Số nào chưa có nguồn thì ghi [CHỜ XÁC NHẬN] + ai cấp.` |
