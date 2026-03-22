const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Expose an error handler
  page.on('pageerror', error => {
    console.log(`Page error: ${error.message}`);
    console.log(`Stack trace: ${error.stack}`);
  });

  await page.goto('file:///app/index.html');
  await page.waitForTimeout(5000);
  await page.screenshot({ path: '/home/jules/verification/verification_final.png' });
  await browser.close();
})();
