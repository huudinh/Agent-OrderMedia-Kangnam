#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gop-tham-khao.py — gop 8 file knowledge/ thanh mot ban goi/GOP-tri-thuc.md

Dung khi nen tang AI chi cho nap it file, hoac khi muon dan mot phat vao
phan Tri thuc. Chay lai moi lan sua knowledge/.

    python tools/gop-tham-khao.py
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

THU_TU = [
    "om-A-vai-tro-quy-trinh.md",
    "om-B-doc-dau-vao.md",
    "om-C-tri-thuc-khach-hang.md",
    "om-D-thu-vien-format.md",
    "om-E-kich-ban-san-xuat.md",
    "om-F-to-chuc-ads.md",
    "om-G-phap-che-ranh-gioi.md",
    "om-H-dich-vu-kangnam.md",
    "om-I-khuon-kich-ban-nha.md",
    "om-J-chan-dung-mat.md",
]

DAU_TRANG = """# 📦 GỘP TRI THỨC — AGENT-ORDERMEDIA-KANGNAM

> ⚠️ **File này SINH TỰ ĐỘNG từ `knowledge/`. Đừng sửa trực tiếp ở đây** —
> sửa file gốc trong `knowledge/` rồi chạy lại `python tools/gop-tham-khao.py`.
>
> Dùng khi nền tảng chỉ cho nạp ít file, hoặc muốn dán một phát vào phần Tri thức.
> Agent thấy file này thì tra trong đây, ⛔ đừng báo thiếu file.

Sinh ngày: {ngay} · {so_file} sổ · {so_dong} dòng

---

## MỤC LỤC

{muc_luc}

---

"""


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8", errors="replace")

    goc = Path(__file__).resolve().parent.parent
    kn = goc / "knowledge"
    if not kn.is_dir():
        sys.exit(f"Khong thay thu muc: {kn}")

    phan: list[str] = []
    muc: list[str] = []
    thieu: list[str] = []

    for i, ten in enumerate(THU_TU, 1):
        f = kn / ten
        if not f.exists():
            thieu.append(ten)
            continue
        noi_dung = f.read_text(encoding="utf-8").strip()
        tieu_de = next((l.lstrip("# ").strip() for l in noi_dung.splitlines()
                        if l.startswith("# ")), ten)
        neo = ten.removesuffix(".md")
        muc.append(f"{i}. [{tieu_de}](#{neo}) — `{ten}`")
        phan.append(f'<a id="{neo}"></a>\n\n## ⟦ {ten} ⟧\n\n{noi_dung}')

    if thieu:
        print(f"CANH BAO: thieu {len(thieu)} file: {', '.join(thieu)}",
              file=sys.stderr)
    if not phan:
        sys.exit("Khong gop duoc file nao.")

    than = "\n\n---\n\n".join(phan)
    ra = DAU_TRANG.format(
        ngay=date.today().isoformat(),
        so_file=len(phan),
        so_dong=than.count("\n") + 1,
        muc_luc="\n".join(muc),
    ) + than + "\n"

    dich = goc / "goi" / "GOP-tri-thuc.md"
    dich.parent.mkdir(parents=True, exist_ok=True)
    dich.write_text(ra, encoding="utf-8")

    kb = len(ra.encode("utf-8")) / 1024
    print(f"  Da gop {len(phan)} so  ->  {dich.relative_to(goc)}")
    print(f"  {kb:.1f} KB · {ra.count(chr(10)) + 1} dong")


if __name__ == "__main__":
    main()
