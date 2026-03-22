import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Clean HTML Head
head_remove = [
    r'    <!-- SheetJS for \.xlsx export -->\n    <script src="https://cdn\.sheetjs\.com/xlsx-latest/package/dist/xlsx\.full\.min\.js"></script>\n\n',
    r'    <!-- jspreadsheet and Material Icons libraries -->\n    <script src="https://bossanova\.uk/jspreadsheet/v5/jspreadsheet\.js"></script>\n    <script src="https://jsuites\.net/v5/jsuites\.js"></script>\n    <link rel="stylesheet" href="https://bossanova\.uk/jspreadsheet/v5/jspreadsheet\.css" type="text/css" />\n    <link rel="stylesheet" href="https://jsuites\.net/v5/jsuites\.css" type="text/css" />\n',
    r'    <!-- WordCloud2\.js for News Analysis -->\n    <script src="https://cdnjs\.cloudflare\.com/ajax/libs/wordcloud2\.js/1\.2\.2/wordcloud2\.min\.js"></script>\n    \n',
    r'    <!-- NEW: Sentiment\.js for better sentiment analysis -->\n    <script src="https://cdnjs\.cloudflare\.com/ajax/libs/sentiment/2\.1\.0/sentiment\.min\.js"></script>\n',
    r'    <!-- NEW: Compromise \(NLP\) for better keyword extraction -->\n    <script src="https://unpkg\.com/compromise@14\.10\.0/builds/compromise\.min\.js"></script>\n'
]
for p in head_remove:
    content = re.sub(p, '', content)

# 2. Tabs HTML
content = re.sub(r'                    <div class="tab-link" onclick="openTab\(event, \'news-analysis\'\)"><i class="material-icons">analytics</i> News Analysis</div>\n', '', content)
content = re.sub(r'                    <div class="tab-link" onclick="openTab\(event, \'market-cap\'\)"><i class="material-icons">pie_chart</i> Market Cap</div>\n', '', content)
content = re.sub(r'                    <div class="tab-link" onclick="openTab\(event, \'data\'\)"><i class="material-icons">table_view</i> Data</div>\n', '', content)
content = re.sub(r'                    <div class="tab-link" onclick="openTab\(event, \'mci-settings\'\)"><i class="material-icons">settings</i> MCI Config</div>\n', '', content)
content = re.sub(r'                     <div class="chart-sub-tab-link" onclick="openChartSubTab\(event, \'chart-mci\'\)">TSMC vs MCI</div>\n', '', content)

# 3. Tab Contents
content = re.sub(r'            <!-- News Analysis Tab Content -->\n            <div id="news-analysis" class="tab-content">.*?</div>\n        </div>\n    </div>\n\n    <!-- Modals -->', '        </div>\n    </div>\n\n    <!-- Modals -->', content, flags=re.DOTALL)

# 4. Chart MCI
content = re.sub(r'\n                <div id="chart-mci" class="view-content" style="padding-top:20px;">.*?</div>\n            </div>\n\n            <div id="news" class="tab-content">', '\n            </div>\n\n            <div id="news" class="tab-content">', content, flags=re.DOTALL)

# 5. Modals
content = re.sub(r'    <div id="marketCapConfigModal" class="modal">.*?</div>\n\n    <script>', '    <script>', content, flags=re.DOTALL)

# 6. Tickers Config
content = content.replace("'.TWII': 'TWSE', '.SOX': 'SOX', '.SPX': 'S&P 500', '.MCI': 'MCI',", "'.TWII': 'TWSE', '.SOX': 'SOX', '.SPX': 'S&P 500',\n            '^IXIC': 'Nasdaq', '^N225': 'Nikkei 225', '^KS11': 'KOSPI', '000001.SS': 'SSE',")
content = content.replace("'.TWII': 'taiwan.gov.tw', '.SOX': 'nasdaq.com', '.SPX': 'spglobal.com',\n            '.MCI': 'bloomberg.com',", "'.TWII': 'taiwan.gov.tw', '.SOX': 'nasdaq.com', '.SPX': 'spglobal.com',\n            '^IXIC': 'nasdaq.com', '^N225': 'jpx.co.jp', '^KS11': 'krx.co.kr', '000001.SS': 'sse.com.cn',")
content = content.replace("'.TWII': '#000000', '.SOX': '#008080', '.SPX': '#555555',", "'.TWII': '#000000', '.SOX': '#008080', '.SPX': '#555555',\n            '^IXIC': '#0055A2', '^N225': '#C8102E', '^KS11': '#003478', '000001.SS': '#DA291C',")
content = content.replace("'2330.TW': '#8b0000', 'TSM': '#a52a2a', 'TSM.N': '#a52a2a', '.MCI': '#ff9900',", "'2330.TW': '#8b0000', 'TSM': '#a52a2a', 'TSM.N': '#a52a2a',")
content = content.replace("'equity-index': ['.TWII', '.SOX', '.SPX', '.MCI'],", "'equity-index': ['.TWII', '.SOX', '.SPX', '^IXIC', '^N225', '^KS11', '000001.SS'],")


# 7. JavaScript Clean up
js_removals = [
    r'        let marketCapGroups = \{.*?\};\n        \n        let mcColumnMinWidth = \'50px\';\n\n        let mciMembers = \[.*?\];\n        let defaultWeights = \{.*?\};\n        \n        let mciWeightHistory = \[\]; \n        let historicalMciData = null; \n\n',
    r'\n        let pivotedPriceData = new Map\(\);\n        let pivotedVolumeData = new Map\(\);\n        let pivotedTriData = new Map\(\); \n        let pivotedDataHeaders = \[\];\n        let isDataPivoted = false;\n        let jspreadsheetInstance = null;\n        \n        let mcZoomLevel = 1\.0;\n',
    r'                \'https://raw\.githubusercontent\.com/andychu221/yhfinance-fred-data/main/market_data/custom_index\.json\',\n',
    r'                historicalMciData = results\[3\];\n                fxData = results\[4\] \|\| \{\}; \n\n                results\.slice\(0,3\)\.forEach\(\(json, idx\) => \{', '                fxData = results[3] || {}; \n\n                results.slice(0,3).forEach((json, idx) => {',
    r'                status\.innerText = "Initializing MCI Weights\.\.\.";\n                \n                if \(historicalMciData && historicalMciData\.weights\) \{\n                    parseImportedMciWeights\(historicalMciData\.weights\);\n                \} else \{\n                    initMciWeightHistory\(\);\n                \}\n                \n                // Requirement 1: Auto-extend MCI based on latestDataDate\n                checkMciAutoExtension\(\);\n\n                renderMciTable\(\);      \n\n                status\.innerText = "Calculating Custom Index \(MCI\)\.\.\.";\n                calculateMCI\(\);\n\n',
    r'                document\.getElementById\(\'mc-as-of-date\'\)\.value = formatDateYYYYMMDD\(latestDataDate\);\n                ',
    r'\n                document\.getElementById\(\'mci-comp-start\'\)\.value = \'2020-01-01\';\n                document\.getElementById\(\'mci-comp-end\'\)\.value = formatDateYYYYMMDD\(latestDataDate\);\n',
    r'                renderMarketCapTab\(\);\n                \n                status\.innerText = "Processing Raw Data\.\.\.";\n                pivotDataForDownload\(\);\n',
    r'            if \(tabName === \'data\' && isDataPivoted && !jspreadsheetInstance\) renderDataTab\(\);\n            if \(tabName === \'market-cap\'\) renderMarketCapTab\(\);\n            // MOD: Trigger resize/redraw for News Analysis when tab becomes visible\n            if \(tabName === \'news-analysis\'\) \{\n                setTimeout\(\(\) => updateNewsDashboard\(\), 100\);\n            \}\n'
]
for i in range(len(js_removals)):
    if type(js_removals[i]) is tuple or type(js_removals[i]) is list:
        content = re.sub(js_removals[i][0], js_removals[i][1], content, flags=re.DOTALL)
    else:
        content = re.sub(js_removals[i], '', content, flags=re.DOTALL)


# Delete Functions completely
content = re.sub(r'        function getBlendedMarketCap\(date\) \{.*?        \}\n        \n        function calculateMarketCap\(ticker, price, date\) \{.*?        \}\n        \n        function calculateMarketCapNumeric\(ticker, price, date\) \{.*?        \}\n', '', content, flags=re.DOTALL)
content = re.sub(r'        function initMciWeightHistory\(\) \{.*?        \}\n\n        function parseImportedMciWeights\(weightsObj\) \{.*?        \}\n\n        // Requirement 1: Optimized Logic\n        function checkMciAutoExtension\(\) \{.*?        \}\n\n        function renderMciTable\(\) \{.*?        \}\n\n        function updateMciHeader\(input, colIdx\) \{.*?        \}\n\n        function updateMciWeight\(input\) \{.*?        \}\n\n        function addMciTicker\(\) \{.*?        \}\n\n        function saveMciConfig\(\) \{.*?        \}\n\n        function calculateMCI\(\) \{.*?        \}\n\n', '\n', content, flags=re.DOTALL)
content = re.sub(r'        function renderMciComparison\(\) \{.*?        \}\n', '', content, flags=re.DOTALL)
content = re.sub(r'        function zoomMarketCap\(delta\) \{.*?        \}\n        \n        function openMarketCapConfig\(\) \{.*?        \}\n\n        function renderMarketCapConfigUI\(\) \{.*?        \}\n\n        function moveMcTicker\(groupId, index, dir\) \{.*?        \}\n\n        function removeMcTicker\(groupId, index\) \{.*?        \}\n\n        function addMcTicker\(groupId\) \{.*?        \}\n        \n        function updateMcTickerName\(ticker, newName\) \{.*?        \}\n\n        function saveMarketCapConfig\(\) \{.*?        \}\n\n        function renderMarketCapTab\(\) \{.*?        \}\n        \n        function getFirstTradingDay\(year\) \{.*?        \}\n   \n        function generateMarketCapDates\(anchorDate\) \{.*?        \}\n        \n        function getHistoricalMarketCap\(ticker, targetDate\) \{.*?        \}\n\n        // Requirement 3: Filter TRI for MCI and non-stocks\n        function pivotDataForDownload\(\) \{.*?        \}\n        \n        function renderDataTab\(\) \{.*?        \}\n', '', content, flags=re.DOTALL)
content = re.sub(r'        // --- NEWS DASHBOARD FUNCTIONALITY START ---.*', '', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content + "    </script>\n</body>\n</html>\n")
