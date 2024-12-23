from locale import windows_locale
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach",True)
d = webdriver.Chrome(options=options)
# url = "https://testautomationpractice.blogspot.com/"
# url = "https://www.globalsqa.com/demo-site/frames-and-windows/"
# url = "https://ui.vision/demo/webtest/frames/"
url = "https://rahulshettyacademy.com/AutomationPractice/"

# Year = ""
# Month = ""

class CalendarWorker:

    def __init__(self,driver:webdriver.Chrome,url):
        self.d = driver
        self.url = url
        self.d.get(url)
        self.d.maximize_window()

    # def calenderOne(self):
    #     self.d.find_element(By.ID,"datepicker").click()
    #
    #     while Year!="2026":
    #         next = self.d.find_element(By.XPATH, '//span[text()="Next"]')
    #         next.click()
    #         Year = self.d.find_element(By.CSS_SELECTOR, '.ui-datepicker-year').text
    #
    #     while Month!="July":
    #         next = self.d.find_element(By.XPATH,'//span[text()="Next"]')
    #         next.click()
    #         Month = self.d.find_element(By.CSS_SELECTOR, '.ui-datepicker-month').text
    #     print("Calendar One: ",Year, Month)

    # def calendarSelect(self):
    #     self.d.find_element(By.XPATH,'//input[@id="txtDate"]').click()
    #     self.d.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]').click()
    #     sleep(5)
    #     self.monthlist = self.d.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]')
    #     ml = Select(self.monthlist)
    #     ml.select_by_visible_text("Jul")
    #     sleep(3)
    #     # ml.select_by_value("5")
    #     # ml.select_by_index("")

    # def actionClass(self):
    #     self.action = ActionChains(d)
    #     self.action.move_to_element(d.find_element(By.ID,"alertBtn")).perform()

    # def parChild(self):
    #     self.d.find_element(By.XPATH,'//button[text()="New Tab"]').click()
    #     self.window = self.d.window_handles
    #     self.wit = self.d.switch_to.window(self.window[1])
    #     curl = self.d.current_url
    #     print(curl)

    # def frames(self):
    #     self.d.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
    #     sleep(3)
    #     self.d.find_element(By.ID,'iFrame').click()
    #     self.d.switch_to.frame("globalSqa")
    #     self.d.find_element(By.XPATH,'//div/a[@title="Facebook"]').click()

    # def frames(self):
    #     # self.d.get("https://ui.vision/demo/webtest/frames/")
    #     sleep(3)
    #     #Main iframe switch is happening here
    #     self.ele = d.find_element(By.XPATH,'//frameset[1]/frameset[1]/frame[@src="frame_3.html"]')
    #     self.d.switch_to.frame(self.ele)
    #     self.d.find_element(By.NAME,'mytext3').send_keys("Akash")
    #     #You can directly add the Location of the element while switching to frame instead of creating the object first
    #     self.d.switch_to.frame(self.d.find_element(By.XPATH,'//iframe[@src="https://docs.google.com/forms/d/1yfUq-GO9BEssafd6TvHhf0D6QLDVG3q5InwNE2FFFFQ/viewform?embedded=true"]'))
    #     try:
    #         #Creation of Relative XPATH since the element only had Class which was shared with other elements as well
    #         element_list = self.d.find_element(By.XPATH,'//body//div[1]//div[1]//form[1]//div[2]//div[1]//div[2]//div[1]//div[1]//div[1]//div[@class="oyXaNc"]//div[1]//div[1]//span//div[1]//label//div[1]//div[1]//div[1]//div[3]//div[@class="AB7Lab Id5V1"]')
    #         element_list.click()
    #     except Exception as e:
    #         print(e)
    #     try:
    #         self.d.find_element(By.XPATH,'//span[text()="Next"]').click()
    #         print("Next button Successful")
    #     except Exception as e:
    #         print(e)
    #     #This statement will help in switching to original frame from iFrame that is your original webpage
    #     self.d.switch_to.default_content()
    #     #If you try to switch from 1 frame to another directly without switching to ORIGINAL FRAME you will get an error
    #     #Here we are swtiching from 1 frame to another
    #     self.d.switch_to.frame(self.d.find_element(By.XPATH,'//frameset[1]/frameset[1]/frame[@src="frame_4.html"]'))
    #     self.d.find_element(By.NAME,"mytext4").send_keys("Akash")

    def tableTest(self):
        # self.name = self.d.find_elements(By.XPATH,'//div[@class="right-align"]//table[@id="product"]/tbody/tr/td[1]')
        # for i in self.name:
        #     print(i.text)
        # self.position = self.d.find_elements(By.XPATH,'//div[@class="right-align"]//table[@id="product"]/tbody/tr/td[2]')
        # for i in self.position:
        #     print(i.text)
        self.city = self.d.find_elements(By.XPATH, '//div[@class="right-align"]//table[@id="product"]/tbody/tr/td[3]')
        for i in self.city:
            cit = i.text
            self.your = self.city.index(i)
            t = self.your+1
            if cit == "Chennai":
                pwc = self.d.find_element(By.XPATH,'//div[@class="right-align"]//table[@id="product"]/tbody/tr['+str(t)+']/td[1]')
                print(pwc.text)
        # self.amount = self.d.find_elements(By.XPATH, '//div[@class="right-align"]//table[@id="product"]/tbody/tr/td[4]')
        # for i in self.amount:
            # print(i.text)

obj = CalendarWorker(d,url)
# obj.calenderOne()
# obj.calendarSelect()
# obj.actionClass()
# obj.parChild()
# obj.frames()
obj.tableTest()