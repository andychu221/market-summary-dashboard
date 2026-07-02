<div align="right">
  <a href="README.md">English</a> | <strong>繁體中文</strong> | <a href="README.ja.md">日本語</a>
</div>

# 📈 每日市場更新儀表板 (Daily Market Update)

這是一個專為股票分析師與投資人打造的全方位前端金融儀表板。提供即時績效追蹤、互動式圖表、AI 驅動的新聞情緒分析，以及財報會議重點摘要，全部整合在一個輕量級的 Web App 中。

![Dashboard Preview](https://via.placeholder.com/800x400.png?text=Dashboard+Preview+Image) *(你可以將此連結替換為你的實際截圖)*

## ✨ 核心功能

*   📊 **市場績效追蹤：** 監控自訂觀察清單，並依產業板塊（如晶圓代工、IC 設計、設備、記憶體等）分類。支援「報酬率視角」與「技術面視角 (包含均線與 1 年區間)」切換。
*   🤖 **AI 智能分析：** 整合 Google Gemini API，自動摘要市場趨勢、進行技術線圖分析，並從冗長的財報會議逐字稿中萃取關鍵洞察。
*   📈 **互動式圖表：** 採用 Chart.js 繪製動態 2x2 矩陣圖（1週、1個月、今年以來、1年）與自訂期間比較，X 軸精準對齊實際交易日。
*   📰 **智能新聞分析儀表板：** 具備過去 5 天的新聞聲量趨勢、整體情緒分析（正向/中立/負向）、新聞來源分佈及熱門關鍵字統計。
*   📅 **財報與總經日曆：** 以週曆形式視覺化呈現即將發布的財報與重要總體經濟事件。

## 🛠️ 技術堆疊

*   **前端技術：** HTML5, CSS3, 原生 JavaScript (Vanilla JS)
*   **開源套件：** [Chart.js](https://www.chartjs.org/) (資料視覺化), [Marked.js](https://marked.js.org/) (Markdown 解析)
*   **AI 模型：** Google Gemini (gemini-2.5-flash-lite)
*   **資料來源：** 透過 GitHub Repositories 動態獲取 JSON 資料 (包含路透社新聞庫、Yahoo Finance/FRED 資料、財報逐字稿)。

## 🚀 快速開始

1.  **複製專案：**
    ```bash
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    ```
2.  **執行應用程式：**
    只需雙擊 `index.html` 即可在任何現代瀏覽器中開啟。無需設定本地伺服器或後端環境。
3.  **啟用 AI 功能：**
    *   點擊右上角的 ⚙️ (設定) 圖示。
    *   輸入你的 **Google Gemini API Key**。
    *   選擇你偏好的 AI 輸出語言（英文 / 繁體中文）。

## 📝 授權條款

本專案採用 MIT 授權條款。
