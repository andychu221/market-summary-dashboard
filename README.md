<div align="right">
  <strong>English</strong> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ja.md">日本語</a>
</div>

# 📈 Daily Market Update Dashboard

A comprehensive, client-side financial market dashboard designed for equity analysts and investors. It provides real-time performance tracking, interactive charting, AI-driven news sentiment analysis, and earnings call summaries—all in a single lightweight Web App.

<img width="1231" height="604" alt="MarketUpdate" src="https://github.com/user-attachments/assets/72582f77-f4c0-42c0-9bd3-ce9bdd62b321" />

## ✨ Key Features

*   📊 **Performance Tracking:** Monitor custom watchlists categorized by industry segments (e.g., Foundry, Fabless, Equipment, Memory). Supports toggling between Return View and Technical View (MAs, 1Y Range).
*   🤖 **AI-Powered Analysis:** Integrated with Google Gemini API to automatically summarize market trends, analyze technical charts, and extract key insights from complex earnings call transcripts.
*   📈 **Interactive Charting:** Utilizes Chart.js for dynamic 2x2 grids (1W, 1M, YTD, 1Y) and custom period comparisons. X-axes are perfectly aligned to actual trading days.
*   📰 **Smart News Dashboard:** Features a 5-day news volume trend, overall sentiment analysis (Positive/Neutral/Negative), top sources distribution, and keyword statistics.
*   📅 **Earnings & Macro Calendar:** Visualizes upcoming earnings reports and macroeconomic events with a weekly calendar view.

## 🛠️ Tech Stack

*   **Frontend:** HTML5, CSS3, Vanilla JavaScript
*   **Libraries:** [Chart.js](https://www.chartjs.org/) (Data Visualization), [Marked.js](https://marked.js.org/) (Markdown Parsing)
*   **AI Model:** Google Gemini (gemini-2.5-flash-lite)
*   **Data Sources:** Fetches JSON data dynamically from GitHub repositories (Reuters News Archive, Yahoo Finance/FRED data, Earnings Transcripts).

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    ```
2.  **Run the App:**
    Simply double-click `index.html` to open it in any modern web browser. No local server or backend setup is required.
3.  **Enable AI Features:**
    *   Click the ⚙️ (Settings) icon in the top right corner.
    *   Input your **Google Gemini API Key**.
    *   Select your preferred output language (English / Traditional Chinese).

## 📝 License

This project is licensed under the MIT License.
