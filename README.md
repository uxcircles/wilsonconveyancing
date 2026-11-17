# Wilson Conveyancing：網站改版概念（UX CIRCLES）

這是 [Wilson Conveyancing](https://www.wilsonconveyancing.com/) 的非官方網站改版概念，由 UX CIRCLES 製作，用來向客戶展示新網站。每一頁頂部都有「概念」標示，並設有 `noindex` 及 `robots.txt`，不會被搜尋引擎收錄。

- 網址：https://uxcircles.github.io/wilsonconveyancing/（英文）、`/zh/`（繁體中文，香港用語）
- 純 HTML / CSS / JS，不需要框架

## 頁面

| 頁面 | 內容 |
| --- | --- |
| `index.html` | 首頁：即時日曆（offer 日期 → 七個步驟 → 拎鎖匙日期）、Wilson 親自跟進、服務、海外買家、Trustpilot 評語、報價表格 |
| `services.html` | 服務及收費（報價包括甚麼） |
| `stamp-duty.html` | 英格蘭印花稅計算機（首次置業、額外物業 5%、非居民 2%） |
| `faqs.html` | 常見問題（原網站六條） |
| `privacy.html` | 私隱及無障礙聲明（草稿） |
| `404.html` | 找不到頁面（「呢一頁甩咗鏈」） |

## 如何修改

所有文字都在 `_build/pages.py`，每句寫成 `L(英文, 中文)`。

```bash
python3 _build/pages.py   # 重建所有頁面（英文及中文）
python3 _build/fonts.py   # 修改中文字後重新下載字型子集
```

修改 CSS / JS 後，把 `pages.py` 裡的 `V` 加一，避免手機讀舊檔。

## 設計概念

- **標誌元素**：Wilson Conveyancing 自己的標誌：一條朱紅色單線畫出的屋仔加心形（「we care」）。整個網站就是這一條線：首頁日曆用它串起七個步驟，終點畫出屋仔；它也出現在頁首、頁尾、favicon、內頁標題下的分隔線及 404 頁（斷開的鏈）。
- **首屏類型**：`calendar-led`。標題用今日日期即時計算：「Offer accepted today? Keys between 12 January and 9 February」／「今日 offer 獲接受，1月12日至2月9日拎鎖匙」。日期依據 Wilson 自己 FAQ 的「8 至 12 星期」。訪客可以改 offer 日期，全部日期跟住變。
- **字型**：Sora（幾何無襯線，呼應標誌的單線畫）＋ Onest（內文）＋ Chiron Hei HK（香港字形）。
- **顏色**：墨黑 `#0e0d0c`（標誌底色）、朱紅 `#ff2903`（從標誌 PNG 取色）、白紙。白底上的紅字用較深的 `#c81d00` 以符合 AA 對比。
- **與之前作品的分別**：之前的物業網站（JoyHome、Withyou、UKPM）全部是文字左、拱形相片右，配海軍藍、紅磚或青綠；最近的律師網站 Chung & Rea 是米白底、襯線字、文件物件。這個網站沒有相片，首屏是一條會動的時間線，黑底朱紅。

## 資料來源及需要客戶確認的地方

- 電話、辦公時間、CLC 牌照號碼 13589、服務列表、七個步驟、FAQ：取自 wilsonconveyancing.com（2026 年 11 月）。
- Trustpilot「Excellent · 4.9」：原網站首頁所寫。四則評語逐字抄自原網站首頁的 Trustpilot 截圖（部分以 […] 刪節）。
- 「從香港或海外買樓」一節：依據原網站「不一定要用本地律師」的 FAQ、服務列表中的「Gifted Deposits」，以及評語中的海外買家。**需要 Wilson 確認是否願意這樣定位。**
- 原網站沒有公開電郵及地址，所以表格只經 WhatsApp 發送，亦沒有地圖。另附原有的 Google Forms 報價表格連結。
- 印花稅稅率：英格蘭住宅 SDLT，2025 年 4 月 1 日起的稅率，已於 2026 年 11 月按 GOV.UK 核對。威爾斯（LTT）不適用。
- 私隱聲明是草稿，需 Wilson Conveyancing 審閱。
- 沒有使用圖庫相片。
