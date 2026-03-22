const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('file:///app/index.html');
  await page.waitForTimeout(5000);
  // test changing tab to chart
  await page.click('button:has-text("Chart")');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: '/home/jules/verification/verification_chart.png' });
  // test changing tab to news
  await page.click('button:has-text("News")');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: '/home/jules/verification/verification_news.png' });
  await browser.close();
})();
