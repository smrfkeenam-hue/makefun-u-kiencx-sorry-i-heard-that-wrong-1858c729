import os

# One line, 1-140 chars, no trailing newline: the gate rejects anything else.
ENTRY = "Sorry, you said 'call Mom,' I heard 'call a mob.' They arrive at six. I have already apologised to them."

assert 1 <= len(ENTRY) <= 140
assert "\n" not in ENTRY

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
