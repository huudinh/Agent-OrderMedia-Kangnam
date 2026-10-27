# PROMPT — ĐỌC & CHUẨN HOÁ ORDER (B1–B3)

> Dùng khi chỉ muốn **kiểm order đã đủ để viết kịch bản chưa**, chưa cần kịch bản.

---

## Prompt

```
Đọc file order này. Chưa cần viết kịch bản.

Làm ba việc:
1. Báo số dòng đọc được / số dòng bỏ qua + lý do bỏ.
2. Chuẩn hoá: chân dung về CD1–CD6, nấc về A1–A5. Suy ra nhiệt · ô camp ·
   format · tệp vào/loại trừ · ngưỡng. Ô nào em suy ra thì ghi (suy ra).
3. Chạy cổng A 8 ô cho từng dòng. Chỉ rõ dòng nào thiếu ô nào.

Cuối cùng liệt kê riêng:
- Dòng có mâu thuẫn (vd A1 + PERF, format không thuộc ô camp)
- Dòng thiếu CHÂN DUNG hoặc NẤC 5A — đây là hai ô chặn
- Dòng cần khách hàng thật nhưng chưa rõ consent

<link sheet hoặc file>
```

---

## Biến thể

### Chỉ muốn xem lỗ hổng phễu

```
Đọc order này rồi dựng ma trận chân dung × 5A. Ô nào = 0 thì chỉ ra.
Đừng viết kịch bản. Chỉ nói em đang thiếu content ở đâu và nên lấp ô nào trước.
```

### Muốn đối chiếu với ad đã chạy

```
File này có cột HIỆU QUẢ của các ad đã chạy. Quét qua rồi nói cho em:
- Hook mới nào đang trùng kiểu với hook đã chấm KÉM
- Hook mới nào trùng công thức với hook đã chấm TỐT
- Hook nào đã TỐT ở một khu vực mà nên PORT sang khu vực khác thay vì viết mới

Dẫn chứng rõ hook cũ nào, khu vực nào, chấm gì.
```

### Order dán trực tiếp, không có file

```
Em đếm lại số dòng rồi báo cho anh xác nhận trước khi làm gì tiếp — anh dán tay
nên có thể mất dòng.
```

---

## Đầu ra mong đợi

```
ĐỌC ĐƯỢC: 18 dòng · BỎ QUA: 1 dòng (dòng 29 — trống mọi ô trừ Ngày order)

CỔNG A
┌──────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ Dòng │ A1 │ A2 │ A3 │ A4 │ A5 │ A6 │ A7 │ A8 │
├──────┼────┼────┼────┼────┼────┼────┼────┼────┤
│  4   │ ✓  │ ✓  │ ✓  │ ✓  │ ✓  │ ✓  │ —  │ ✗  │
│ 12   │ ✗  │ ✗  │ ✓  │ ✓  │ ✓  │ ✓  │ —  │ ✗  │
└──────┴────┴────┴────┴────┴────┴────┴────┴────┘

⛔ CHẶN — 3 dòng thiếu CHÂN DUNG + NẤC 5A (dòng 12, 13, 14)
   → em suy từ INSIGHT là CD1 · A2, nhưng cần anh xác nhận.

⚠️ MÂU THUẪN — 1 dòng
   dòng 7: A1 · AWARE + CAMP ĐÍCH = PER → A1 + PERF không chạy được.
   Đề xuất: đổi sang VIEW (ô V1), hoặc đẩy nấc lên A2.

⚠️ CẦN CONSENT — 2 dòng (L06/L07 có khách thật)
```
