# 讀取 CP950.TXT，提取第二欄 Unicode 編碼並轉成文字後輸出成 U.txt

input_file = "CP950.txt"
output_file = "U.txt"

unicode_chars = []

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2 and parts[1].startswith("0x"):
            try:
                codepoint = int(parts[1], 16)
                char = chr(codepoint)
                unicode_chars.append(char)
            except:
                continue

# 將字元組合成字串寫入檔案
with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(unicode_chars))

print(f"已輸出 {len(unicode_chars)} 個字元到 {output_file}")
