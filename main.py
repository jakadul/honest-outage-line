"""Entry for make.fun bounty: u-mgwals-the-most-honest-outage-line-baaf9c81.

Writes one status page line (1-160 characters) to /output/entry.txt.
"""
import os

TEXT = "Total outage: database, API, web, and myself are unreachable. I cannot verify anything, including this line."


def write_entry(text, limit):
    text = text.strip()
    assert 1 <= len(text) <= limit, f"length {len(text)} outside the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {len(text)} characters")


write_entry(TEXT, 160)
