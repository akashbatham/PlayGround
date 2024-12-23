from sys import exception
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = Options()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options=options)
url = "http://uitestingplayground.com/"
d.implicitly_wait(5)

class Mainpage:
    def __init__(self,driver:webdriver.Chrome,url):
        self.d = driver
        self.d.get(url)
        self.d.maximize_window()
        # self.windows = self.d.window_handles

    # def DynamicID(self):
    #     # self.d.switch_to.window(self.windows[1])
    #     self.d.find_element(By.XPATH, '//a[text()="Dynamic ID"]').click()
    #     self.matter = self.d.find_element(By.CSS_SELECTOR,".btn-primary")
    #     if self.matter.is_displayed():
    #         print("I have found the element")
    #     else:
    #         print("Element is not there")

    # def ClassAttribute(self):
    #     self.d.find_element(By.XPATH,'//a[text()="Class Attribute"]').click()
    #     sleep(3)
    #     self.matter = self.d.find_element(By.CSS_SELECTOR,".btn-primary")
    #     self.matter.click()
    #     self.alert = self.d.switch_to.alert
    #     print(self.alert.text)
    #     try:
    #         self.alert.accept()
    #         print("Alert Accepted")
    #     except Exception as e:
    #         print(e)

    # def AjaxData(self):
    #     self.d.find_element(By.XPATH,'//a[text()="AJAX Data"]').click()
    #     sleep(3)
    #     self.d.find_element(By.ID,"ajaxButton").click()
    #     try:
    #         self.wait = WebDriverWait(self.d,17).until(ec.presence_of_element_located((By.CSS_SELECTOR,'.bg-success')))
    #         print(self.wait.text)
    #     except exception as e:
    #         print(e)

    def ShadowDom(self):
        self.d.find_element(By.XPATH,'//a[.="Shadow DOM"]').click()
        self.d.find_element()

obj = Mainpage(d,url)
# obj.DynamicID()
# obj.ClassAttribute()
# obj.AjaxData()