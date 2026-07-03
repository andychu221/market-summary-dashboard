<div align="right">
  <a href="README.md">English</a> | <strong>繁體中文</strong> | <a href="README.ja.md">日本語</a>
</div>

# 📈 每日市場更新儀表板 (Daily Market Update)

[![Live Demo](https://img.shields.io/badge/Demo-Live_View-success?style=for-the-badge&logo=github)](https://andychu221.github.io/market-summary-dashboard/)

這是一個專為股票分析師與投資人打造的全方位前端金融儀表板。提供即時績效追蹤、互動式圖表、AI 驅動的新聞情緒分析、財務報表，以及財報會議重點摘要，全部整合在一個輕量級的 Web App 中。

👉 **[點此進入 Live Demo 網站](https://andychu221.github.io/market-summary-dashboard/)**

<img width="1231" height="604" alt="MarketUpdate" src="https://github.com/user-attachments/assets/8ae35689-f0d1-4106-8b01-7daabdc4732b" />

## 🗄️ 資料來源與架構

本專案採用 **無伺服器前端架構 (Serverless Frontend)**。網頁不依賴傳統後端伺服器，而是透過 JavaScript 直接呼叫公開的 API，並動態載入由爬蟲每日自動更新至 GitHub 儲存庫的靜態 JSON 資料庫。

* **市場與總經數據：** 來自 Yahoo Finance 與 FRED。包含每日收盤價、均線、總市值、還原權息績效與重要總體經濟日曆。
    * *來源位置：* `andychu221/yhfinance-fred-data` 儲存庫。
* **新聞與情緒分析：** 彙整自路透社、華爾街日報 (WSJ)、金融時報 (FT)、聯合報與自由時報。資料內含情緒分數標籤與預處理好的 AI 摘要。
    * *來源位置：* `andychu221/reuters-news-archive` 儲存庫。
* **財報會議逐字稿：** 提供重點公司的法說會/財報會議日程表與完整中英文逐字稿。
    * *來源位置：* `andychu221/Earnings-Call-Transcripts` 儲存庫。
* **財務報表資料：** 美股三大報表 (損益表、資產負債表、現金流量表) 的歷年季報與年報數據。
    * *來源位置：* `yhfinance-fred-data/us_financials` 資料夾。
* **即時 AI 串接：** 系統前端直接串接 **Google Gemini API** (`gemini-2.5-flash-lite`)。能根據使用者選擇的新聞、圖表區間或財報內容，即時生成技術面分析、板塊表現摘要與重點整理。

## ✨ 核心功能

* 📊 **市場績效追蹤：** 監控自訂觀察清單，依產業板塊分類。支援「報酬率視角」與「技術面視角 (包含均線與 1 年區間)」切換。
* 🤖 **AI 智能分析：** 一鍵呼叫 Gemini API，從冗長的新聞與法說會逐字稿中萃取關鍵洞察。
* 📈 **互動式圖表：** 採用 Chart.js 繪製動態 2x2 矩陣圖與自訂期間比較，X 軸過濾假日，精準對齊實際交易日。
* 📰 **智能新聞分析：** 具備過去 5 天的新聞聲量趨勢、整體情緒統計、新聞來源分佈及熱門關鍵字條形圖。
* 💵 **互動式財報表：** 支援拖曳自訂報表行數 (Row Config)，並具備自動化年增率 (Growth) 與利潤率 (Margin) 計算功能。

## 🚀 快速開始

1.  **開啟應用：** 直接點擊 [Live Demo](https://andychu221.github.io/market-summary-dashboard/) 或在本地端雙擊 `index.html` 即可運行。
2.  **啟用 AI 功能：**
    * 點擊右上角的 ⚙️ (設定) 圖示。
    * 輸入你的 **Google Gemini API Key** (僅存儲於本地瀏覽器，確保安全)。
    * 選擇你偏好的 AI 輸出語言（英文 / 繁體中文）。
