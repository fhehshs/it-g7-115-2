# 資訊科技 7 年級第二學期 課程網站（115 學年度）

對應課程計畫第 15–29 週：電腦基本構造與資料處理 → 演算法與流程圖 → Scratch 循序與重複結構。
架構與第一學期（it-g7-115-1）、城市科技網站相同。

## 本機預覽（互動版）

```
pip install flask
python app.py
```
瀏覽器開 http://localhost:5000

## 修改內容

| 要改什麼 | 檔案 |
|---|---|
| 各章投影片與隨堂測驗 | `content/ch01.py` ～ `content/ch10.py` |
| 共用版型（卡片、流程圖、Scratch 積木樣式） | `content/_kit.py` |
| 首頁章節卡片、開放章數（`PUBLISHED`） | `templates/home.html` |
| 評量規準 | `templates/rubric.html` |
| 補充影片 | `content/enhancements.py` |

改完先跑 `python validate_site.py .`，顯示「通過 ✅」再匯出。

## 發布給學生（GitHub Pages）

1. `python make_static.py` → 產生 `docs/`（資料已內嵌，直接雙擊 `docs/index.html` 也能離線看）
2. 第一次上架：GitHub 新增 repo（例如 `it-g7-115-2`，Public），在此資料夾執行
   ```
   git init
   git add .
   git commit -m "資訊科技 7 年級第二學期課程網站"
   git branch -M main
   git remote add origin https://github.com/fhehshs/it-g7-115-2.git
   git push -u origin main
   ```
3. GitHub → repo → Settings → Pages → Source 選 **Deploy from a branch**，Branch 選 `main`、資料夾 **/docs** → Save
4. 學生網址：`https://fhehshs.github.io/it-g7-115-2/`

之後更新：改內容 → `python make_static.py` → `git add . && git commit -m "更新" && git push`。

## 注意
- 第 5 章 Dream PC 試算表的價格是**教學示範數字**，不是實際報價；學生要自己查價並記錄日期與來源。
- 影片使用「YouTube 搜尋按鈕」而非固定影片，避免影片下架失效；要嵌入指定影片，把該頁的 `'video'` 改成 `{'type': 'youtube', 'id': '影片ID', 'title': '…'}`（該頁 html 要有 `video_slot(頁碼)`，可參考 ch01 第 9 頁）。
- 隨堂測驗成績只存在學生的瀏覽器，不會回傳；要收成績請用 Google 表單。
