#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dem-ngan.py — dem so ky tu khoi COPY cua SYSTEM-PROMPT-NGAN.md

ChatGPT Custom GPT gioi han 8.000 ky tu o o Instructions. Ban ngan dang gan day,
nen chay lai script nay sau MOI lan sua file do.

    python tools/dem-ngan.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

GIOI_HAN = 8000


def main() -> None:
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8", errors="replace")

    f = Path(__file__).resolve().parent.parent / "SYSTEM-PROMPT-NGAN.md"
    if not f.exists():
        sys.exit(f"Khong thay file: {f}")

    # Lay khoi ``` LON NHAT — khoi COPY, khong phai vi du trong phan huong dan.
    khoi = re.findall(r"```[a-z]*\n(.*?)\n```", f.read_text(encoding="utf-8"), re.S)
    if not khoi:
        sys.exit("Khong tim thay khoi ``` nao trong file.")
    n = len(max(khoi, key=len))

    con = GIOI_HAN - n
    print(f"\n  Khoi COPY : {n:,} ky tu")
    print(f"  Gioi han  : {GIOI_HAN:,}")
    if con < 0:
        print(f"  >> VUOT {-con:,} ky tu — PHAI CAT BOT truoc khi dung.\n")
        sys.exit(1)
    canh = "  (gan day — them dong nao thi phai cat dong khac)" if con < 300 else ""
    print(f"  Con lai   : {con:,}{canh}\n")


if __name__ == "__main__":
    main()
