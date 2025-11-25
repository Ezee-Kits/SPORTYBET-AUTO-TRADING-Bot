

import os
import asyncio
from pyppeteer import launch


user_dir = os.path.join(os.getcwd(), "SportyBet_Dir")
os.makedirs(user_dir, exist_ok=True)


async def main(): 
    browser = await launch({
        'headless': False,
        'userDataDir': user_dir,
        'args': [
            '--no-sandbox',
            '--disable-infobars',
            '--disable-blink-features=AutomationControlled',
            '--no-first-run',
            '--no-default-browser-check',
        ]
    })
    page = await browser.newPage()
    await page.goto('https://github.com/Ezee-Kits/SOCIAL-EARNING-TASK-BOT',timeout = 0,waitUntil='networkidle2')
    input('\n PRESS ENTER AFTER YOUR ARE DONE SETTING UP YOUR ACCOUNT ::::: \n')

    await browser.close()

asyncio.run(main())