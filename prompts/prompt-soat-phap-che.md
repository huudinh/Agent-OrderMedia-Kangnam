# PROMPT — SOÁT PHÁP CHẾ (B6, cổng B)

> Chạy được **độc lập** — không cần có kịch bản. Dùng để soát hook, caption, text overlay, hoặc ad đang chạy.

---

## Soát cả order

```
Chỉ soát pháp chế thôi, đừng viết kịch bản.

Soát theo 12 điểm L01–L12. Mỗi dòng gắn một cờ 🟢 / 🟡 / 🔴.

⛔ Cờ nào cũng phải có CÂU THAY THẾ cụ thể — đừng ghi "vi phạm L04" rồi để đó.
Cờ ĐỎ thì đề xuất bản dựng thay thế.

Cuối cùng gom lại: mấy dòng ĐỎ, mấy VÀNG, mấy XANH, và dòng nào chặn vì
thiếu dữ kiện từ om-H (bảng giá, tên bác sĩ, số giấy phép, chính sách bảo hành).

<link sheet hoặc file>
```

---

## Soát một câu

```
Câu này có lên ads được không?

"<dán câu>"

Nói rõ: cờ gì · trúng điểm L nào · câu thay thế là gì.
```

---

## Soát ad đang chạy

```
Những ad này đang chạy. Soát lại pháp chế.

Với ad có cờ ĐỎ: nhắc em là giữ ngân sách hiện tại, KHÔNG tăng, và dựng bản
thay thế — chứ không phải tắt ngay nếu đang ra kết quả.

<link sheet hoặc file>
```

---

## Ba màu cờ

| Cờ | Nghĩa | Bắt buộc kèm |
|---|---|---|
| 🟢 **XANH** | Lên ads được | — |
| 🟡 **VÀNG** | Sửa câu rồi lên | **Câu thay thế cụ thể** |
| 🔴 **ĐỎ** | ⛔ Không lên ads | **Đề xuất bản dựng thay thế** |

---

## Mười dấu hiệu ĐỎ — tra nhanh

```
① tên bác sĩ chưa xác minh            ⑥ cảnh can thiệp / phẫu thuật
② con số không có nguồn               ⑦ hứa đổi vận / tài lộc (CD5)
③ cam kết kết quả                     ⑧ lời chứng thực người bệnh làm QC
④ "bảo hành trọn đời" sai chính sách  ⑨ khách thật chưa có consent
⑤ số suất ưu đãi không thật           ⑩ tỷ lệ thành công không nguồn
```

## Mười hai dấu hiệu VÀNG — tra nhanh

```
"chỉ có... mới"  ·  "tốt nhất"  ·  "duy nhất"  ·  "trọn đời"
"không đau" trên text overlay  ·  hạ thấp phương pháp khác  ·  từ giật gân
tên thương mại vật liệu  ·  ảnh mô phỏng không ghi chú
"đẹp ngay"  ·  tên người nổi tiếng  ·  nội dung hướng dưới 18
```

---

## Xin dữ kiện còn thiếu

```
Liệt kê cho em đúng những thứ cần xin để mở các chặn hiện tại.
Mỗi dòng ghi: xin cái gì · ai cấp · đang chặn mấy phiếu.

Em cần mang danh sách này đi họp.
```

**Đầu ra mong đợi:**
```
[CHỜ XÁC NHẬN] — 5 mục

① Danh sách BS đã xác minh (tên · số CCHN · phạm vi chuyên môn · cơ sở hành nghề
   · văn bản đồng ý dùng hình ảnh)
   ai cấp: khối vận hành + pháp chế     chặn: 4 phiếu

② Bảng giá trọn gói hiện hành + quyền lợi từng gói
   ai cấp: khối vận hành / sales        chặn: 3 phiếu L11 + mọi hook A4

③ Chính sách bảo hành BẰNG VĂN BẢN — thời hạn thật
   ai cấp: pháp chế                     chặn: 2 phiếu
   ⚠️ dữ liệu hiện có ghi cả "trọn đời" và "10 năm" → chắc chắn một cái sai

④ Số giấy phép hoạt động đủ 7 cơ sở (hiện chỉ có 2)
   ai cấp: khối pháp chế                chặn: mọi phiếu local L12 ngoài 2 bệnh viện

⑤ Định nghĩa format L13 · L14 · L15 · L16
   ai cấp: Content Lead                 chặn: 2 phiếu
```

---

## Bắt agent không vượt quyền

Agent **gắn cờ và đề xuất**, ⛔ không ký duyệt. Nếu agent nói *"ad này hợp pháp"* → sửa lại:

```
Em không kết luận hợp pháp. Em chỉ soát theo 12 điểm và đưa câu thay thế.
Ai ký là bác sĩ kiểm duyệt và pháp chế.
```
