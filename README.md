<div align="right">
  <strong>English</strong> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ja.md">日本語</a>
</div>

# 📈 Daily Market Update Dashboard

[![Live Demo](https://img.shields.io/badge/Demo-Live_View-success?style=for-the-badge&logo=github)](https://andychu221.github.io/market-summary-dashboard/)

A comprehensive, client-side financial market dashboard designed for equity analysts and investors. It provides real-time performance tracking, interactive charting, AI-driven news sentiment analysis, financial statements, and earnings call summaries—all in a single lightweight Web App.

👉 **[Click Here to View Live Demo](https://andychu221.github.io/market-summary-dashboard/)**

<img width="1231" height="604" alt="MarketUpdate" src="https://github.com/user-attachments/assets/72582f77-f4c0-42c0-9bd3-ce9bdd62b321" />

## 🗄️ Data Sources & Architecture

This project features a **Serverless Frontend Architecture**. Instead of relying on a traditional backend server, the Web App dynamically fetches daily updated JSON data directly from automated GitHub repositories and connects to live APIs.

* **Market & Macro Data:** Sourced from Yahoo Finance and FRED. Includes daily prices, moving averages, market caps, and macroeconomic events.
    * *Source:* `andychu221/yhfinance-fred-data` repository.
* **News & Sentiment:** Aggregated from Reuters, WSJ, FT, UDN, and LTN. The data includes metadata, sentiment scores, and pre-processed AI summaries.
    * *Source:* `andychu221/reuters-news-archive` repository.
* **Earnings Call Transcripts:** Complete transcripts and earnings calendar schedules for covered companies.
    * *Source:* `andychu221/Earnings-Call-Transcripts` repository.
* **Financial Statements:** Comprehensive SEC filings (Income Statement, Balance Sheet, Cash Flow) with quarterly and annual views.
    * *Source:* `yhfinance-fred-data/us_financials` folder.
* **Live AI Integration:** Real-time connection to **Google Gemini API** (`gemini-2.5-flash-lite`). The client-side app sends specific context (prices, news, transcripts) directly to Gemini to generate on-the-fly technical analysis, portfolio summaries, and sentiment reports.

## ✨ Key Features

* 📊 **Performance Tracking:** Monitor custom watchlists categorized by industry segments (e.g., Foundry, Fabless, Equipment). Supports 'Return View' and 'Technical View' (MAs, 1Y Range).
* 🤖 **AI-Powered Analysis:** Integrated with Google Gemini API to automatically summarize market trends and extract key insights from complex earnings transcripts.
* 📈 **Interactive Charting:** Utilizes Chart.js for dynamic 2x2 grids (1W, 1M, YTD, 1Y) and custom period comparisons. X-axes are perfectly aligned to actual trading days.
* 📰 **Smart News Dashboard:** Features a 5-day news volume trend, sentiment analysis, top sources distribution, and keyword statistics.
* 💵 **Interactive Financials:** Drag-and-drop row configuration for financial statements with automatic Growth/Margin ratio calculations.

## 🚀 Getting Started

1.  **Access the App:** Open the [Live Demo](https://andychu221.github.io/market-summary-dashboard/) or run `index.html` locally.
2.  **Enable AI Features:**
    * Click the ⚙️ (Settings) icon in the top right corner.
    * Input your **Google Gemini API Key** (Client-side only, stored locally).
    * Select your preferred output language (English / Traditional Chinese).
