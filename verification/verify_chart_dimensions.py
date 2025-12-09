
import os
from playwright.sync_api import sync_playwright

def verify_chart7_generation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load index.html from local file
        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Wait for data to load
        try:
            page.wait_for_selector('#loading-overlay', state='hidden', timeout=10000)
            print("Data loaded (overlay hidden).")
        except Exception as e:
            print("Loading overlay did not disappear within timeout. Proceeding anyway (might rely on cached/mocked data if any).")

        # Inject script to monkey-patch getImageFromChart
        # We handle the case where chartInstance.canvas might be null, although it shouldn't be if charts are rendered.

        page.evaluate("""
            window.getImageFromChartArgs = [];
            const originalGetImageFromChart = window.getImageFromChart;
            window.getImageFromChart = function(chartInstance, width, height) {
                // Log the arguments
                let chartId = "unknown";
                if (chartInstance && chartInstance.canvas) {
                    chartId = chartInstance.canvas.id;
                }

                window.getImageFromChartArgs.push({
                    id: chartId,
                    width: width,
                    height: height
                });
                return originalGetImageFromChart(chartInstance, width, height);
            };
        """)

        # Now trigger generateReport
        print("Triggering generateReport...")
        page.evaluate("generateReport()")

        # Wait for report modal to show up
        try:
            page.wait_for_selector('#reportModal.show', timeout=10000)
            print("Report modal appeared.")
        except:
             print("Report modal did not appear.")

        # Check captured arguments
        args = page.evaluate("window.getImageFromChartArgs")

        found_chart7 = False
        all_passed = True

        print("\nChecking getImageFromChart calls:")
        for arg in args:
            chart_id = arg['id']
            width = arg['width']
            height = arg['height']

            if 'Chart-7' in chart_id:
                found_chart7 = True
                print(f"Chart-7 call: ID={chart_id}, Width={width}, Height={height}")
                if width != 800 or height != 600:
                    print("FAIL: Expected 800x600 for Chart-7")
                    all_passed = False
                else:
                    print("PASS: Correct dimensions for Chart-7")
            else:
                # Other charts should remain 1200x500
                 if width == 1200 and height == 500:
                     pass # OK
                 # else: print(f"Info: Other chart {chart_id} size {width}x{height}")

        if not found_chart7:
            print("FAIL: No Chart-7 calls detected.")
            all_passed = False

        # Take a screenshot of the report modal content
        if found_chart7:
             page.screenshot(path='verification/report_modal.png')
             print("Screenshot saved to verification/report_modal.png")

        browser.close()

if __name__ == "__main__":
    verify_chart7_generation()
