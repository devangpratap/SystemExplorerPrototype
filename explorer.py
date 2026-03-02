import asyncio
from playwright.async_api import async_playwright

async def build_inventory(url):
    print(f"--- Scanning System: {url} ---")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)

        # 1. Look for Mandatory Pages (Home, Contact, Accessibility)
        # We check the text of all links on the page
        links = await page.query_selector_all("a")
        inventory = {"mandatory_pages": [], "forms": 0}

        for link in links:
            text = await link.inner_text()
            href = await link.get_attribute("href")
            
            # Simple check for the pages the project description asks for
            if any(word in text.lower() for word in ["contact", "accessibility", "feedback"]):
                inventory["mandatory_pages"].append({"type": text, "url": href})

        # 2. Identify Forms and Dynamic Components
        forms = await page.query_selector_all("form")
        inventory["forms"] = len(forms)

        # 3. Export a structured summary (The 'Outcome' in your screenshot)
        print(f"\n[Result] Found {len(inventory['mandatory_pages'])} mandatory pages.")
        print(f"[Result] Found {inventory['forms']} interactive forms.")
        
        await browser.close()
        return inventory

if __name__ == "__main__":
    asyncio.run(build_inventory("https://example.com"))
    