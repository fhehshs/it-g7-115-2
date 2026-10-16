# -*- coding: utf-8 -*-
# 第 4 週：儲存單位與周邊設備（課程計畫第 18 週：電腦基本構造、資料處理）
from content._kit import *

CHAPTERS = [
    {'name': '封面', 'start': 1},
    {'name': '第一節：bit 與 Byte', 'start': 2},
    {'name': '第二節：從 KB 到 TB', 'start': 7},
    {'name': '第三節：周邊設備', 'start': 12},
    {'name': '第四節：規格查詢 Lab', 'start': 17},
    {'name': '個人實作', 'start': 20},
]

SLIDES = [
    {'id': 1, 'title': '儲存單位與周邊設備', 'chapter': '封面', 'bg': 'navy',
     'html': cover('💾', '儲存單位與周邊設備', 'Storage Units · Peripheral Devices',
                   ['🟦 bit / Byte', '📏 KB → TB', '⌨️ 輸入輸出', '🔍 規格查詢'], '第 4 週')},

    # ── 第一節 ──
    {'id': 2, 'title': '為什麼電腦只用 0 和 1？', 'chapter': '第一節：bit 與 Byte', 'bg': 'white',
     'html': title('💡 為什麼電腦只用 0 和 1？')
     + lead('📖 電腦裡的開關（電晶體）只有兩種狀態：<strong>通電＝1、不通電＝0</strong>。'
            '只分兩種，電路最簡單、最不容易出錯，這種計數方式叫做<strong>二進位</strong>。')
     + grid(2,
            card('red', '如果用十進位…', '電路要分辨 0～9 共 10 種電壓，只要電壓稍微不穩就會讀錯。', '😵'),
            card('green', '用二進位', '只要分辨「有電／沒電」，就算電壓有點不穩也不會讀錯。', '😎'))
     + note('🗂️ 還記得打孔卡的「有孔／沒孔」嗎？概念完全一樣！')},

    {'id': 3, 'title': 'bit 與 Byte', 'chapter': '第一節：bit 與 Byte', 'bg': 'white',
     'html': title('🟦 bit（位元）與 Byte（位元組）')
     + grid(2,
            card('blue', 'bit 位元（小寫 b）', '最小的資料單位，只能是 <strong>0 或 1</strong>。', '🟦', True),
            card('purple', 'Byte 位元組（大寫 B）', '<strong>1 Byte ＝ 8 bits</strong>，是表示資料的基本單位。', '🟦🟦', True))
     + table(['資料', '大約需要多少空間'],
             [['1 個英文字母（例如 A）', '1 Byte'],
              ['1 個中文字（常用的 UTF-8 編碼）', '3 Bytes'],
              ['1 個表情符號 😀', '4 Bytes']], ['60%', '40%'])
     + note('⚠️ 小心大小寫：網速常用 <strong>Mbps</strong>（小 b＝bit），檔案大小用 <strong>MB</strong>（大 B＝Byte）。100 Mbps 下載速度 ≈ 每秒 12.5 MB。', 'yellow', '')},

    {'id': 4, 'title': '幾個 bit 能表示幾種狀態？', 'chapter': '第一節：bit 與 Byte', 'bg': 'white',
     'html': title('🔢 幾個 bit 可以表示幾種狀態？')
     + table(['bit 數', '所有組合', '種類數'],
             [['1', '0、1', '2'],
              ['2', '00、01、10、11', '4'],
              ['3', '000、001、010、011、100、101、110、111', '8'],
              ['8（1 Byte）', '00000000 ～ 11111111', '256']], ['16%', '62%', '22%'])
     + note('🧠 規律：每多 1 個 bit，種類就<strong>乘以 2</strong>。n 個 bit ＝ 2 的 n 次方種。'
            '1 Byte 有 256 種，剛好夠表示所有英文大小寫字母、數字和符號。')},

    {'id': 5, 'title': '活動：用手指數二進位', 'chapter': '第一節：bit 與 Byte', 'bg': 'white',
     'html': title('✋ 活動：一隻手可以數到 31！')
     + table(['手指', '小指', '無名指', '中指', '食指', '拇指'],
             [['代表的數', '16', '8', '4', '2', '1']])
     + steps([('伸出＝1、彎下＝0', '從右邊的拇指開始，每根手指代表的數是前一根的 2 倍'),
              ('把伸出的手指加起來', '例如只伸出食指和拇指：2 ＋ 1 ＝ 3，寫成二進位就是 00011'),
              ('挑戰', '用手指比出 5、10、19；全部伸出是多少？')], 'green')
     + note('🎉 答案：5＝00101、10＝01010、19＝10011；五根全伸＝16＋8＋4＋2＋1＝<strong>31</strong>。', 'yellow', '')},

    {'id': 6, 'title': '第一節 隨堂測驗', 'chapter': '第一節：bit 與 Byte', 'bg': 'purple', 'quiz': 'q1',
     'html': quiz_cover('第一節 隨堂測驗', 'bit、Byte 與二進位 ｜ 3 題')},

    # ── 第二節 ──
    {'id': 7, 'title': '儲存單位階梯', 'chapter': '第二節：從 KB 到 TB', 'bg': 'white',
     'html': title('📏 儲存單位階梯：每一階約 1,024 倍')
     + table(['單位', '換算', '生活例子（約略）'],
             [['KB 千位元組', '1 KB ＝ 1,024 Bytes', '一則純文字短訊息、一頁純文字筆記'],
              ['MB 百萬位元組', '1 MB ＝ 1,024 KB', '一張手機照片約 2–5 MB、一首 MP3 約 3–5 MB'],
              ['GB 十億位元組', '1 GB ＝ 1,024 MB', '一部高畫質電影約 1–4 GB；手機 RAM 8 GB'],
              ['TB 兆位元組', '1 TB ＝ 1,024 GB', '常見的電腦硬碟容量'],
              ['PB 千兆位元組', '1 PB ＝ 1,024 TB', '大型資料中心、雲端服務']], ['24%', '30%', '46%'])
     + note('🧠 口訣：<strong>K → M → G → T → P</strong>，每往上一階就是約一千倍（精確是 1,024 ＝ 2 的 10 次方）。')},

    {'id': 8, 'title': '為什麼 1 TB 硬碟只顯示 931 GB？', 'chapter': '第二節：從 KB 到 TB', 'bg': 'white',
     'html': title('🤔 買了 1 TB 硬碟，為什麼電腦只顯示約 931 GB？')
     + two_col(
         card('orange', '廠商：用 1,000 算', '硬碟廠商用十進位：<br>1 TB ＝ 1,000,000,000,000 Bytes', '🏭'),
         card('blue', 'Windows：用 1,024 算', '作業系統用二進位：<br>1,000,000,000,000 ÷ 1,024 ÷ 1,024 ÷ 1,024 <br>≈ <strong>931 GB</strong>', '💻'))
     + note('✅ 沒有被偷容量！只是<strong>兩邊的算法不同</strong>。另外系統本身和預裝軟體也會佔用一些空間，所以實際可用的會更少。', 'yellow', '')},

    {'id': 9, 'title': '換算練習', 'chapter': '第二節：從 KB 到 TB', 'bg': 'white',
     'html': title('🧮 換算練習（用約 1,000 倍估算即可）')
     + steps([('一支 64 GB 的隨身碟，大約可以放幾張 4 MB 的照片？', '64 GB ≈ 64,000 MB；64,000 ÷ 4 ＝ <strong>約 16,000 張</strong>'),
              ('一部 2 GB 的電影，128 GB 手機剩 20 GB，可以下載幾部？', '20 ÷ 2 ＝ <strong>10 部</strong>'),
              ('一首 4 MB 的歌，1 GB 大約可以放幾首？', '1 GB ≈ 1,000 MB；1,000 ÷ 4 ＝ <strong>約 250 首</strong>')], 'blue')
     + note('💡 估算時用 1,000 比較好算；要精確時才用 1,024。')},

    {'id': 10, 'title': '我的手機空間去哪了？', 'chapter': '第二節：從 KB 到 TB', 'bg': 'white',
     'html': title('📱 我的手機空間都去哪了？')
     + grid(3,
            card('red', '影片', '1 分鐘 1080p 影片約 60–130 MB；4K 更大', '🎬', True),
            card('yellow', '照片與截圖', '每張數 MB，累積幾千張就是好幾 GB', '🖼️', True),
            card('blue', 'App 與快取', '遊戲 App 常常好幾 GB；社群 App 的快取也會越來越大', '🎮', True))
     + note('🔍 <strong>回家任務</strong>：到手機「設定 → 儲存空間」看看哪一類最佔空間？（只看類別，不用截圖給別人）'
            '<br>💡 整理技巧：刪掉重複照片、清除 App 快取、把影片備份到雲端。')},

    {'id': 11, 'title': '第二節 隨堂測驗', 'chapter': '第二節：從 KB 到 TB', 'bg': 'purple', 'quiz': 'q2',
     'html': quiz_cover('第二節 隨堂測驗', '儲存單位換算 ｜ 3 題')},

    # ── 第三節 ──
    {'id': 12, 'title': '輸入設備', 'chapter': '第三節：周邊設備', 'bg': 'white',
     'html': title('📥 輸入設備：把資料「送進」電腦')
     + lead('📖 <strong>周邊設備</strong>（Peripheral）：主機以外，幫助電腦和外界溝通的設備，分成輸入、輸出、兼具兩者。')
     + grid(3,
            card('blue', '鍵盤、滑鼠', '最基本的輸入工具', '⌨️', True),
            card('blue', '麥克風', '語音輸入、視訊通話', '🎤', True),
            card('blue', '攝影機', '視訊、人臉辨識', '📷', True),
            card('blue', '掃描器', '把紙本圖文變成數位檔', '🖨️', True),
            card('blue', '條碼／QR Code 掃描', '超商結帳、圖書館借書', '🏷️', True),
            card('blue', '感測器', '溫度、光線、動作感測', '🌡️', True))},

    {'id': 13, 'title': '輸出設備', 'chapter': '第三節：周邊設備', 'bg': 'white',
     'html': title('📤 輸出設備：把結果「送出」給人看、聽')
     + grid(4,
            card('green', '螢幕', '液晶、OLED 顯示畫面', '🖥️', True),
            card('green', '印表機', '把資料印在紙上', '🖨️', True),
            card('green', '喇叭／耳機', '輸出聲音', '🔊', True),
            card('green', '投影機', '把畫面投到大螢幕', '📽️', True))
     + note('🤔 <strong>想一想</strong>：3D 印表機算輸入還是輸出設備？（答：輸出——它把電腦裡的設計變成實體物品）')},

    {'id': 14, 'title': '兼具輸入與輸出', 'chapter': '第三節：周邊設備', 'bg': 'white',
     'html': title('🔄 兼具輸入與輸出的設備')
     + grid(3,
            card('purple', '觸控螢幕', '手指觸碰＝輸入；顯示畫面＝輸出。手機、平板、教室觸控大螢幕', '📱', True),
            card('purple', '超商多媒體機', '例如 ibon：觸控選服務（輸入）、顯示並列印單據（輸出）', '🏪', True),
            card('purple', '隨身碟／外接硬碟', '可以讀取（輸入）也能寫入（輸出）資料', '🔌', True))
     + note('🧠 判斷方法：看資料<strong>流動的方向</strong>。資料進電腦＝輸入、出電腦＝輸出、兩個方向都有＝兼具。', 'yellow', '')},

    {'id': 15, 'title': '分類挑戰', 'chapter': '第三節：周邊設備', 'bg': 'white',
     'html': title('🧩 分類挑戰：輸入？輸出？兼具？')
     + table(['設備', '你的答案', '理由'],
             [['捷運閘門的悠遊卡感應器', '？', '？'],
              ['智慧手錶', '？', '？'],
              ['VR 頭戴裝置', '？', '？'],
              ['電子白板', '？', '？']], ['36%', '22%', '42%'])
     + note('🗣️ 小組討論 2 分鐘。參考答案：感應器＝輸入（讀取卡片資料）；智慧手錶、VR 頭戴裝置、電子白板＝兼具（有感測／觸控，也有螢幕顯示）。', 'yellow', '')},

    {'id': 16, 'title': '第三節 隨堂測驗', 'chapter': '第三節：周邊設備', 'bg': 'purple', 'quiz': 'q3',
     'html': quiz_cover('第三節 隨堂測驗', '輸入、輸出與兼具設備 ｜ 3 題')},

    # ── 第四節 ──
    {'id': 17, 'title': 'Windows 規格查詢', 'chapter': '第四節：規格查詢 Lab', 'bg': 'white',
     'html': title('🔍 規格查詢：Windows 電腦')
     + grid(3,
            card('blue', '方法 1：設定', '開始 → 設定 → 系統 → 系統資訊<br>看到：處理器、已安裝的 RAM、裝置名稱', '⚙️'),
            card('green', '方法 2：系統資訊', '按 Win＋R → 輸入 <code>msinfo32</code> → Enter<br>看到：完整硬體規格', 'ℹ️'),
            card('purple', '方法 3：工作管理員', '按 Ctrl＋Shift＋Esc → 效能<br>看到：CPU 使用率、記憶體用量、磁碟', '📊'))
     + note('💡 打開工作管理員後，同時開幾個網頁，觀察 CPU 和記憶體使用率怎麼變化！')},

    {'id': 18, 'title': 'Chromebook 與手機規格查詢', 'chapter': '第四節：規格查詢 Lab', 'bg': 'white',
     'html': title('🔍 規格查詢：Chromebook 與手機')
     + table(['裝置', '查詢方法', '可以看到'],
             [['Chromebook', '設定 → 關於 ChromeOS；或在網址列輸入 <code>chrome://system</code>', '作業系統版本、CPU、記憶體'],
              ['Chromebook', '開啟「診斷」App', 'CPU、記憶體、電池即時狀態'],
              ['Android 手機', '設定 → 關於手機', '型號、處理器、RAM、儲存空間'],
              ['iPhone', '設定 → 一般 → 關於本機', '型號、容量、可用空間']], ['18%', '50%', '32%'])
     + note('🔒 <strong>隱私提醒</strong>：關於本機頁面也會顯示<strong>序號、IMEI</strong>，這些是裝置的身分證，不要拍照上傳或給別人。', 'red', '⚠️')},

    {'id': 19, 'title': '第四節 隨堂測驗', 'chapter': '第四節：規格查詢 Lab', 'bg': 'purple', 'quiz': 'q4',
     'html': quiz_cover('第四節 隨堂測驗', '規格查詢 ｜ 3 題')},

    # ── 個人實作 ──
    {'id': 20, 'title': '個人實作：電腦教室規格調查', 'chapter': '個人實作', 'bg': 'white',
     'html': title('📝 個人實作：電腦教室規格調查表')
     + "<div style='background:#eff6ff;border-radius:12px;padding:16px;margin-bottom:12px;'>"
       "<p style='color:#1e40af;font-size:.9rem;font-weight:700;margin-bottom:8px;'>📋 在 Google 文件完成以下表格</p>"
     + table(['項目', '查到的規格', '用哪個方法查到的'],
             [['處理器（CPU）', '', ''], ['記憶體（RAM）', '', ''], ['儲存裝置與容量', '', ''],
              ['可用空間', '', ''], ['連接的周邊設備（列出 3 種並分類）', '', '']], ['34%', '36%', '30%'])
     + "</div>"
     + two_col(
         "<div style='background:#f0fdf4;border-radius:10px;padding:14px;'><strong style='color:#166534;font-size:.9rem;'>🧠 思考題（寫在表格下方）</strong>"
         "<ul style='color:#334155;font-size:.8rem;line-height:1.85;padding-left:18px;margin:6px 0 0;'>"
         "<li>這台電腦的硬碟可以放幾部 2 GB 的電影？寫出算式</li>"
         "<li>如果要拿來剪輯影片，你建議升級哪個零件？為什麼？</li></ul></div>",
         rubric_box('規格完整正確，換算與建議有清楚根據', '表格完成且正確', '引導下完成大部分表格', '僅完成部分表格', '📏 評分（規準：資料處理）'))},

    {'id': 21, 'title': '本章重點回顧', 'chapter': '個人實作', 'bg': 'navy',
     'html': recap('第 4 週 重點回顧',
                   [('bit 與 Byte', '1 Byte ＝ 8 bits；n 個 bit 可表示 2 的 n 次方種狀態'),
                    ('單位階梯', 'KB → MB → GB → TB → PB，每階約 1,024 倍'),
                    ('周邊設備', '輸入（鍵盤、麥克風）、輸出（螢幕、喇叭）、兼具（觸控螢幕、隨身碟）'),
                    ('規格查詢', 'Windows：設定／msinfo32／工作管理員；Chromebook：chrome://system')],
                   '預算 3 萬元，怎麼用試算表挑出最適合的電腦？',
                   '下一週：夢想電腦 Dream PC 試算表')},
]

QUIZZES = {
    'q1': {'title': '第一節 隨堂測驗', 'questions': [
        {'q': '1 Byte 等於幾個 bit？',
         'options': ['2', '4', '8', '1,024'],
         'answer': 2,
         'explain': '1 Byte（位元組）＝ 8 bits（位元）。1,024 是相鄰儲存單位（例如 KB 和 Byte）之間的倍數。'},
        {'q': '3 個 bit 最多可以表示幾種不同的狀態？',
         'options': ['3', '6', '8', '9'],
         'answer': 2,
         'explain': '每個 bit 有 0、1 兩種，3 個 bit 就是 2×2×2 ＝ 8 種（000～111）。'},
        {'q': '用手指數二進位（小指 16、無名指 8、中指 4、食指 2、拇指 1），只伸出中指和拇指代表多少？',
         'options': ['3', '5', '6', '41'],
         'answer': 1,
         'explain': '中指 4 ＋ 拇指 1 ＝ 5，二進位寫成 00101。'},
    ]},
    'q2': {'title': '第二節 隨堂測驗', 'questions': [
        {'q': '下列儲存單位由小到大排列，何者正確？',
         'options': ['MB → KB → GB → TB', 'KB → MB → GB → TB', 'GB → MB → TB → KB', 'KB → GB → MB → TB'],
         'answer': 1,
         'explain': 'K（千）→ M（百萬）→ G（十億）→ T（兆），每一階約 1,024 倍。'},
        {'q': '買了 1 TB 的硬碟，Windows 顯示約 931 GB，主要原因是？',
         'options': ['硬碟壞了', '廠商用 1,000 計算、作業系統用 1,024 計算', '被病毒吃掉了', '硬碟需要充電'],
         'answer': 1,
         'explain': '廠商用十進位（1 TB ＝ 10 的 12 次方 Bytes），Windows 用二進位換算，算出來約 931 GB。容量並沒有被偷。'},
        {'q': '手機剩下 12 GB 空間，每部電影約 3 GB，大約還能下載幾部？',
         'options': ['3 部', '4 部', '9 部', '36 部'],
         'answer': 1,
         'explain': '12 ÷ 3 ＝ 4 部。換算時先確認單位相同（都是 GB）再計算。'},
    ]},
    'q3': {'title': '第三節 隨堂測驗', 'questions': [
        {'q': '下列何者屬於「輸出設備」？',
         'options': ['麥克風', '掃描器', '投影機', '鍵盤'],
         'answer': 2,
         'explain': '投影機把電腦的畫面「送出」到螢幕上，是輸出設備。麥克風、掃描器、鍵盤都是把資料送進電腦的輸入設備。'},
        {'q': '手機的觸控螢幕屬於哪一類？',
         'options': ['只算輸入', '只算輸出', '兼具輸入與輸出', '不算周邊設備'],
         'answer': 2,
         'explain': '手指觸碰是輸入，顯示畫面是輸出，所以觸控螢幕兼具輸入與輸出。'},
        {'q': '判斷一個設備是輸入或輸出，最好的方法是？',
         'options': ['看它的顏色', '看資料流動的方向（進電腦或出電腦）', '看它的價格', '看它的重量'],
         'answer': 1,
         'explain': '資料流進電腦＝輸入、流出電腦＝輸出、兩個方向都有＝兼具。用「資料方向」判斷最準確。'},
    ]},
    'q4': {'title': '第四節 隨堂測驗', 'questions': [
        {'q': '在 Windows 按下 Ctrl＋Shift＋Esc 會開啟什麼？可以看到什麼？',
         'options': ['小畫家，可以畫圖', '工作管理員，可以看 CPU 與記憶體使用率', '瀏覽器，可以上網', '計算機，可以算數'],
         'answer': 1,
         'explain': 'Ctrl＋Shift＋Esc 開啟工作管理員，在「效能」分頁可以即時看到 CPU、記憶體、磁碟的使用情況。'},
        {'q': '在 Chromebook 的網址列輸入什麼，可以查看系統資訊？',
         'options': ['chrome://system', 'www.system.com', 'msinfo32', 'cmd'],
         'answer': 0,
         'explain': 'chrome://system 是 ChromeOS 內建的系統資訊頁。msinfo32 是 Windows 的指令，在 Chromebook 不能用。'},
        {'q': '查詢手機規格時，下列哪項資訊「不應該」拍照分享給別人？',
         'options': ['手機品牌', '處理器型號', '序號與 IMEI', 'RAM 容量'],
         'answer': 2,
         'explain': '序號和 IMEI 是裝置獨一無二的身分識別碼，可能被冒用，屬於應保護的資訊。品牌、處理器、RAM 是一般規格，可以分享。'},
    ]},
}
