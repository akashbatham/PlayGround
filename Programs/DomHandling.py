from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options=options)
url = "https://practice.expandtesting.com/shadowdom"
d.implicitly_wait(5)

d.get(url)
tot = d.find_element(By.ID,'my-btn').text
print(tot)
shd = d.find_element(By.CSS_SELECTOR,'[id="shadow-host"]').shadow_root
tex = shd.find_element(By.ID,'my-btn').text
print(tex)