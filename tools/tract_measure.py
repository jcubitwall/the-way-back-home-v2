"""Measures where the words start on each tract story panel, for tools/tract_art.py (writes tools/tract_fit.json).

The blur is baked into the pictures, so it must be fitted to the text: each panel stays sharp until just above its
own words. Measures every language that has tract text and keeps the tallest text block per panel, so the blur
fits every language. Needs a local server on the repo root and Playwright's Chromium:
    python3 -m http.server 8765 &   then   python3 tools/tract_measure.py
"""
import asyncio, glob, json
from playwright.async_api import async_playwright

async def main():
    langs = json.load(open('content/languages.json'))['langs']
    codes = [c for c in langs if 'tract' in json.load(open(f'content/i18n/{c}.json'))]
    exe = (glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') or [None])[0]
    fit = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=exe) if exe else await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1700, 'height': 1200})
        for code in codes:
            await pg.goto(f'http://localhost:8765/tract.html?lang={code}'); await pg.wait_for_timeout(1500)
            got = await pg.evaluate("""() => Object.fromEntries([...document.querySelectorAll('.fr[data-p]')].map(f => {
                const t = f.querySelector('.txt'); return [f.dataset.p, t.offsetTop / f.offsetHeight]; }))""")
            for k, v in got.items():
                fit[k] = min(fit.get(k, 1), round(v, 4))
            print(code, got)
        await b.close()
    json.dump(fit, open('tools/tract_fit.json', 'w'), indent=1, sort_keys=True)
    print('tools/tract_fit.json', fit)

asyncio.run(main())
