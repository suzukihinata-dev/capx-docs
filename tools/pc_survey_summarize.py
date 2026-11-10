#!/usr/bin/env python3
"""メンバー PC 調査の集計。個人ごとの行は出さず、区分ごとの人数だけを出す。

  python3 pc_survey_summarize.py <answers.csv>
"""
import csv
import sys
from collections import Counter

MIN_VRAM = 16   # GB（基盤イメージ＋小型モデルの開発モードの目安）
MIN_DISK = 100  # GB（基盤イメージ 9GB＋提出イメージ＋重みのキャッシュ）


def num(x: "str | None") -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def classify(r: "dict[str, str]") -> str:
    os_ = (r.get("os") or "").strip().lower()
    has_gpu = bool((r.get("gpu") or "").strip())
    ok_res = num(r.get("vram_gb")) >= MIN_VRAM and num(r.get("free_disk_gb")) >= MIN_DISK
    sudo = (r.get("sudo") or "").strip().lower() == "yes"
    if os_ == "linux" and has_gpu and ok_res and sudo:
        return "A"
    if os_ == "windows" and (r.get("wsl2") or "").strip().lower() == "yes" and has_gpu:
        return "B"
    return "C"


def main() -> int:
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    c = Counter(classify(r) for r in rows)
    print(f"回答 {len(rows)} 人")
    print(f"  区分 A（ローカルで開発モード可）: {c['A']} 人")
    print(f"  区分 B（WSL2 で可能性あり・当面は計算環境）: {c['B']} 人")
    print(f"  区分 C（計算ノードで開発）: {c['C']} 人")
    return 0


if __name__ == "__main__":
    sys.exit(main())
