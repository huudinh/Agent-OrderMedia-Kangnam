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
