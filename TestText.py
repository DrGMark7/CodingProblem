def split(word): # ฟังก์ชั่นแยกตัวอักษร ออกจากคำ
    return [char for char in word]

def split_2(word): # ฟังก์ชั่นแยกตัวอักษร ออกจากคำ
    A = [] # ทำเป็นลิสต์ขึ้นมาก่อน
    for i in range(len(word)): # ไล่อ่านทีละตัว
        A.append(word[i]) # เพิ่มทีละตัวเข้าไปใน ลิสต์ที่สร้างขึ้นมา
    return A

Bucket_TH = ['ๅ', '/', '-', 'ภ', 'ถ', 'ุ', 'ึ', 'ค', 'ต', 'จ', 'ข', 'ช'
            ,'+', '๑', '๒', '๓', '๔', 'ู', '฿', '๕', '๖', '๗', '๘', '๙'
            ,'ๆ', 'ไ', 'ำ', 'พ', 'ะ', 'ั', 'ี', 'ร', 'น', 'ย', 'บ', 'ล', 'ฃ'
            ,'๐', '"', 'ฎ', 'ฑ', 'ธ', 'ํ', '๊', 'ณ', 'ฯ', 'ญ', 'ฐ', ',', 'ฅ'
            ,'ฟ', 'ห', 'ก', 'ด', 'เ', '้', '่', 'า', 'ส', 'ว', 'ง'
            ,'ฤ', 'ฆ', 'ฏ', 'โ', 'ฌ', '็', '๋', 'ษ', 'ศ', 'ซ', '.'
            ,'ผ', 'ป', 'แ', 'อ', 'ิ', 'ื', 'ท', 'ม', 'ใ', 'ฝ'
            ,'(', ')', 'ฉ', 'ฮ', 'ฺ', '์', '?', 'ฒ', 'ฬ', 'ฦ',' ']

Bucket_EN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='
            ,'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'
            ,'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'
            ,'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'
            ,'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"
            ,'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'
            ,'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'
            ,'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?',' ']

Bucket_KR = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='
            ,'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'
            ,'ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', '쇼', 'ㅕ', 'ㅑ', 'ㅐ', 'ㅔ', '[', ']', '\\'
            ,'ㅃ', 'ㅉ', 'ㄸ', 'ㄲ', 'ㅆ', '', '', '', 'ㅒ', 'ㅖ', '{', '}', '|'
            ,'ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', '호', 'ㅓ', 'ㅏ', 'ㅣ', ';', "'"
            ,'', '', '', '', '', '', '', '', '', ':', '"'
            ,'\\', 'ㅋ', 'ㅌ', 'ㅊ', '퓨', 'ㅜ', 'ㅡ', ',', '.', '/'
            ,'|', '', '', '', '', '', '', '', '<', '>', '?',' ']

