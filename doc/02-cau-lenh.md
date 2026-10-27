# ② DÒNG LỆNH

> Bốn script. Tất cả chỉ cần **Python 3.9+**; đọc `.xlsx` cần thêm `pip install openpyxl`.

---

## `tools/om.py` — đọc order, chuẩn hoá, cổng A

Làm **B1–B3** rồi điền sẵn mọi ô suy ra được, cộng chấm hook và soát pháp chế **sơ bộ**.
Agent chỉ còn làm phần sáng tạo **B4–B7**.

### Cú pháp

```bash
python tools/om.py <file>            [--sheet TÊN] [--out ĐƯỜNG_DẪN]
python tools/om.py --sheet-id <ID> --gid <GID>  [--out ĐƯỜNG_DẪN]
```

| Tham số | Nghĩa | Mặc định |
|---|---|---|
| `<file>` | File `.csv` · `.xlsx` · `.xlsm` | — |
| `--sheet` | Tên tab trong file xlsx | tab đầu tiên |
| `--sheet-id` | Google Spreadsheet ID | — |
| `--gid` | `gid` của tab *(lấy từ URL)* | — |
| `--out` | Nơi ghi kết quả | `out/phieu-kich-ban.csv` |

### Ví dụ

```bash
# file excel, tab cụ thể
python tools/om.py order-T11.xlsx --sheet "KẾ HOẠCH SẢN XUẤT"

# Google Sheet — tab phải ở chế độ xem được bằng link
python tools/om.py --sheet-id 1qMdt0gmUATqaY2JpZzozgKFVQuVfbY7ppD_M28Q6cdU --gid 0

# đặt tên file ra
python tools/om.py order.csv --out out/phieu-tuan-45.csv
```

### Lấy `gid` ở đâu

```
https://docs.google.com/spreadsheets/d/1qMdt0gm...Q6cdU/edit?gid=0#gid=0
                                      └──── sheet-id ────┘      └ gid
```

### Đọc báo cáo trên màn hình

```
  DOC DUOC : 22 dong   ·   BO QUA: 1 dong
  GHI RA   : out\phieu-kich-ban.csv

  CONG A — CHAN (thieu chan dung / nac 5A) : 0
```
→ **Số dòng chặn ở cổng A.** Khác 0 thì đó là việc đầu tiên phải xử — agent không viết được kịch bản cho những dòng này.

```
  B4 SOI HOOK — X DOI HOOK: 5   ! SUA ROI QUAY: 3   V QUAY DUOC: 14
      KB-MAT1-A4-018  H7 tu giat gan    Hội thảo lột xác 18/10 - Cắt mí giá sốc
```
→ Chấm **sơ bộ bằng từ khoá**. Cột `KIEU KEM TRUNG` cho biết trúng kiểu nào (`H1`–`H7`).

```
  B6 PHAP CHE — DO: 4   VANG: 0   XANH: 18
      [DO   ] KB-MUI1-A4-003  'dep ngay': cam ket ket qua, sai thuc te hau phau
```
→ Cờ ĐỎ phải xử trước khi phiếu rời khỏi agent.

```
  GHI CHU FORMAT (khong chan, chi de biet) : 14 dong
```
→ Format nằm ngoài danh sách **ưu tiên** của ô. **Không phải lỗi** — nhiều ad dùng format ngoài danh sách vẫn chấm TỐT.

```
  CAN CONSENT (format co KH that) : 9
```
→ ⛔ Những phiếu này **không được xếp lịch quay** khi chưa có consent đã ký.

### ⚠️ Giới hạn của script

| Script làm được | Script KHÔNG làm được |
|---|---|
| Chuẩn hoá chân dung, nấc, camp, format | Hiểu ngữ cảnh một hook |
| Suy ra nhiệt · ô camp · tệp · ngưỡng · bối cảnh · đạo cụ · phút quay | Viết lời thoại |
| Bắt cổng A 8 ô | Quyết hook nào nên bỏ cả ý, hook nào giữ ý quay lại |
| Chấm hook theo **từ khoá** | Chấm hook theo **ý nghĩa** |
| Bắt cờ pháp chế theo **từ khoá** | Bắt câu vi phạm diễn đạt vòng |

Ví dụ: script bắt được *"đẹp ngay"*, **không** bắt được *"kết quả thấy liền sau một tiếng"*.
→ **Agent vẫn phải soi lại toàn bộ.** Script chỉ để khỏi bỏ sót và khỏi gõ tay.

---

## `tools/gop-tham-khao.py` — gộp tri thức

```bash
python tools/gop-tham-khao.py
```

Gộp **10 sổ `knowledge/`** theo thứ tự `om-A` → `om-J` thành [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md), kèm mục lục và neo liên kết.

```
  Da gop 10 so  ->  goi\GOP-tri-thuc.md
  137.4 KB · 2216 dong
```

**Chạy lại mỗi lần sửa `knowledge/`.** File gộp sinh tự động — ⛔ đừng sửa trực tiếp trong đó.

Dùng khi nền tảng chỉ cho nạp ít file *(ChatGPT, Gemini)*.

---

## `tools/dem-ngan.py` — đếm ký tự bản ngắn

```bash
python tools/dem-ngan.py
```

```
  Khoi COPY : 7,987 ky tu
  Gioi han  : 8,000
  Con lai   : 13  (gan day — them dong nao thi phai cat dong khac)
```

🔴 **`SYSTEM-PROMPT-NGAN.md` đang gần đầy.** Chạy script này **sau mỗi lần sửa** file đó — ChatGPT Custom GPT cắt phần vượt **không báo lỗi**, nên vượt mà không biết là mất luật chặn ở cuối prompt.

Script trả **exit code 1** khi vượt → dùng được trong hook hoặc CI.

---

## `tools/trang-huong-dan.py` — sinh trang hướng dẫn

```bash
python tools/trang-huong-dan.py              # ghi ra tools/huong-dan.html
python tools/trang-huong-dan.py <đường_dẫn>  # ghi ra chỗ khác
```

```
tools\huong-dan.html — 423 KB
  3 thẻ · 16 file tri thức · 31 prompt · 12 câu smoke test
```

Đọc nội dung từ [`tools/huong-dan.json`](../tools/huong-dan.json) + **đọc thẳng các file nguồn** *(bộ não, 10 sổ, 6 prompt)* để nhúng vào nút Copy → **nút Copy luôn khớp file nguồn**, không bao giờ lệch.

| Việc | Ở đâu |
|---|---|
| Sửa **nội dung** trang *(câu chữ, smoke test, prompt, mục chặn)* | `tools/huong-dan.json` |
| Sửa **style/layout** | `tools/trang-huong-dan.py` — ⚠️ generator **dùng chung** với các agent khác |
| Sửa tri thức | `knowledge/` → nút Copy tự cập nhật, không phải sửa JSON |

**Quy trình đăng lại sau khi sửa:**
```bash
python tools/gop-tham-khao.py      # gộp lại tri thức trước
python tools/dem-ngan.py           # canh giới hạn bản ngắn
python tools/trang-huong-dan.py    # rồi mới sinh trang
```
Xong thì publish lại `tools/huong-dan.html` vào **đúng URL artifact cũ** để link trong README không đổi.

⛔ `tools/huong-dan.html` **không commit** — nó là artifact sinh ra, không phải nguồn.

> ⚠️ **Generator này dùng chung với `Agent-QC-Telesale`, `Agent-Order-SoLieu`…** Bản trong repo này đã thêm `<meta name="viewport">` *(bản gốc thiếu, làm trang bị thu nhỏ trên điện thoại)*. Nếu sửa style, cân nhắc đồng bộ sang các agent kia.

---

## Quy trình đầy đủ — một lần chạy

```bash
# 1. tiền xử lý order
python tools/om.py --sheet-id <ID> --gid 0 --out out/phieu-tuan-45.csv

# 2. đọc báo cáo, xử cổng A + cờ ĐỎ trước
#    (hỏi khối Ads về các dòng thiếu chân dung / nấc 5A)

# 3. đưa file cho agent chạy B4–B7
```

Rồi trong agent:
```
Đây là phiếu đã qua B1–B3 từ tools/om.py. Chạy B4–B7:
soi lại hook, viết lời thoại theo mốc giây, shot list, call sheet gom theo bối cảnh,
và bảng cờ pháp chế kèm câu thay thế.

Cuối bảng in khối GIẢ ĐỊNH và khối [CHỜ XÁC NHẬN] kèm ai cấp, chặn mấy phiếu.
```

---

## ⛔ Lưu ý bảo mật

`out/`, ảnh, footage và file order gốc **không commit** — xem [`.gitignore`](../.gitignore).

Phiếu kịch bản có thể chứa **tên khách hàng, mã case, và dữ liệu giá**. Trước khi gửi ra ngoài khối:
- Đổi tên khách thành `CASE-01`, `KH-A`
- ⛔ Không gửi kèm ảnh/CT gốc
- ⛔ Không upload file order lên công cụ bên thứ ba chưa được duyệt

---

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Sửa |
|---|---|---|
| `Khong tim duoc dong tieu de` | File không có hàng tiêu đề nhận ra được, hoặc tiêu đề nằm sau dòng 40 | Kiểm lại tab; `--sheet` đúng tên chưa |
| `Thieu openpyxl` | Đọc `.xlsx` mà chưa cài | `pip install openpyxl` |
| `CANH BAO: khong tim thay cot {...}` | Tên cột trong order khác chuẩn | Kiểm [`om-B`](../knowledge/om-B-doc-dau-vao.md) §1; đổi tên cột hoặc thêm từ khoá vào `COT_CAN` trong `om.py` |
| `HTTP 401/403` khi tải Google Sheet | Tab chưa mở quyền xem bằng link | Đổi quyền, hoặc tải CSV về rồi chạy trên file |
| Chữ hiện thành `?` trên màn hình | Console Windows cp1252 | Script đã tự xử; còn lỗi thì chạy `chcp 65001` trước |
