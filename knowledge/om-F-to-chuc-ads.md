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
| **Format ngoài danh sách của ô** | Format không khớp nhiệt của tệp | Đề xuất format trong danh sách, ghi `(gán lại)` + lý do |

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
