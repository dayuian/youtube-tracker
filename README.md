
# 📈 YouTube 訂閱即時追蹤器（Streamlit + YouTube API）

使用 Streamlit 打造的即時 YouTube 訂閱人數追蹤器，支援頻道 @handle 自動辨識、滾動動畫呈現訂閱變化，以及完整頻道資訊顯示。支援部署至本地端或 Streamlit Cloud。

> 📌 專案定位：**教育、分析、展示用途**  
> 💡 適用對象：數據分析師、自媒體經營者、開發者、教育用途展示

---

## 🚀 功能特色

- 🎯 支援輸入頻道名稱 / `@handle` 自動解析 channel ID
- 📊 即時訂閱人數更新（可自訂更新頻率）
- 🔢 使用 Odometer.js 顯示滾動動畫數字
- 🖼️ 頻道封面、名稱、影片數、觀看數、地區、自訂網址完整顯示
- 🛡️ 內建 API 錯誤處理（配額用盡、自訂錯誤提示）
- ✅ 模組化結構，方便維護與擴充

---

## 🖼️ 預覽畫面

> 📺 即時訂閱數滾動動畫（Odometer 效果）  
> 🧾 完整頻道資訊卡片顯示  
> ⏱️ 更新頻率可調整


---

## 📦 專案結構

```
youtube_tracker_streamlit/
├── main.py                # 主應用程式（Streamlit）
├── youtube_api.py         # YouTube API 資料處理邏輯
├── sidebar.py             # 側欄輸入模組
├── visual.py              # Odometer 動畫元件
├── requirements.txt       # 套件清單
├── Dockerfile             # （選用）部署用 Dockerfile
└── README.md
```

---

## 📋 使用方式（本地執行）

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

### 2. 啟動應用

```bash
streamlit run main.py
```

### 3. 開啟瀏覽器後，請於側欄輸入：

- ✅ 你的 **YouTube Data API Key**
- ✅ 任意 YouTube 頻道名稱 或 `@handle`
- ✅ 更新頻率（例如每 10 秒）

---

## 🔐 如何取得 YouTube API Key？

1. 前往：[Google Cloud Console](https://console.cloud.google.com/)
2. 建立專案 → 啟用 `YouTube Data API v3`
3. 建立 API 金鑰，並複製至此應用程式使用
4. 注意每日免費配額為 **10,000 單位**

> `channels().list()`：查詢訂閱數只耗費 **1 單位**  
> `search().list()`：查詢頻道名稱（用 @handle）需 **100 單位**

---

## ☁️ 如何部署至 Streamlit Cloud（免後端）

1. Push 此專案至 GitHub
2. 登入 [Streamlit Cloud](https://streamlit.io/cloud)
3. 建立新 App，指向 `main.py`
4. 於「Secrets」中新增你的 `API_KEY`（或直接側欄輸入）

---

## ⚠️ 注意事項

- 本工具使用共用 API Key 時，請避免大量頻繁請求（如每 1 秒）
- 建議每次查詢間隔至少 **10 秒以上**
- 若出現錯誤訊息（如「quotaExceeded」），表示配額已滿，請等待隔日或更換金鑰

---

## 📄 授權條款

本專案以 MIT 授權釋出  
請自由使用、修改、商業化，但請保留原始作者資訊。

---

## 🙌 開發者 [余彦志](https://github.com/dayuian)  
若你喜歡這個專案，歡迎 🌟 Star！
