# 定義檔案路徑
big5_file = 'U.txt'
train_file = 'S.txt' #原本是chinese_character.txt
val_file = 'V.txt'

# 讀取big5檔案內容，逐字處理
with open(big5_file, 'r', encoding='utf-8') as f:
    big5_content = set(f.read().strip())

# 讀取train檔案內容，逐字處理
with open(train_file, 'r', encoding='utf-8') as f:
    train_content = set(f.read().strip())

# 計算差集(big5 - train)
val_content = big5_content - train_content

# 將結果寫入val.txt
with open(val_file, 'w', encoding='utf-8') as f:
    f.write(''.join(val_content))

print(f"已將差集保存到 {val_file} 檔案中。")
