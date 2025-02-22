from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
from key import api_key

import time

web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://www.google.com/recaptcha/api2/demo"
web.get(link)

captcha_key = web.find_element(By.ID, "recaptcha-demo").get_attribute("data-sitekey")

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(api_key)
solver.set_website_url(link)
solver.set_website_key(captcha_key)

answer = solver.solve_and_return_solution()

if answer != 0:
    print(answer)
    web.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{answer}'")
    web.find_element(By.ID, "recaptcha-demo-submit").click()
else:
    print(solver.err_string)
    time.sleep(10)
    exit(0)
