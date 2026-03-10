from playwright.async_api import async_playwright

class BrowserRenderer:

    async def render_url(self, url: str) -> str:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)

            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )

            page = await context.new_page()

            try:
                await page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=15000
                )

                await page.wait_for_timeout(3000)

                html = await page.content()


            except Exception as e:
                raise Exception(f"Render error: {str(e)}")

            finally:
                await browser.close()

            return html

    async def get_accessibility_tree(self, page):

        snapshot = await page.accessibility.snapshot()

        return snapshot