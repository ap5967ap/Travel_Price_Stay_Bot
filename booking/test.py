# from constants import BASE_URL as xx
# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
# driver.implicitly_wait(3)
# driver.maximize_window()
# driver.get(xx)
# def __exit__(self, exc_type, exc, traceback):
#         if self.teardown:
#             self.quit()
#         # self.close()
#         # os.system("killall chrome")
#         # return super().__exit__(exc_type, exc, traceback)
from selenium import webdriver
driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
# maximize with maximize_window()
driver.maximize_window()
driver.get("https://www.justdial.com/Bangalore/Bakeries")
# identify elements of same classname
l=driver.find_elements("store-name")
# iterate through list and get text
for i in l:
   print("Store names:"+ i.text)
driver.close()