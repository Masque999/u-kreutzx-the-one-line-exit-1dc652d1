LINE = "Dear boss, I am resigning to pursue my dream of never attending another meeting that could have been an email. My last day was yesterday."

# The entry must be exactly one line of 1-140 characters.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
assert "\n" not in LINE
# The gate also rejects whitespace-only text: pin the no-padding rule
# (first run showed trim==self, now enforced so a stray space fails here).
assert LINE == LINE.strip(), "line has leading/trailing whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
