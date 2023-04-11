from selenium import webdriver
import booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import typing
import types
import time
from booking.booking_filtrations import booking_filtrations
from booking.booking_report import BookingReport
from prettytable import PrettyTable
options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)
class Booking(webdriver.Chrome):
    def __init__(self)->None:
        super(Booking,self).__init__()
        self.driver=webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
    def __exit__(self, exc_type: typing.Optional[typing.Type[BaseException]], exc: typing.Optional[BaseException], traceback: typing.Optional[types.TracebackType]):
        self.driver.quit()
        return super().__exit__(exc_type, exc, traceback)
    def land_first_page(self)->None:
        '''Home page '''
        self.driver.get(const.BASE_URL)
        self.driver.implicitly_wait(5)
        self.driver.find_element('css selector','[aria-label="Dismiss sign-in info."]').click()
    
    def change_currency(self,currency:str="USD")->None:
        '''if you want to change the currency (default is USD)'''
        currency_element=self.driver.find_element('css selector','button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        a=self.driver.find_element(By.XPATH,(f"//*[text()='{currency}']"));
        a.click()
        # l=self.driver.find_elements('class name','cf67405157') #alter way to do
        # for i in l:
        #     if(i.text.endswith(f"{currency}")):
        #         i.click()
        #         break
    
    def select_place_to_go(self,place_to_go:str)->None:
        '''enter the place you want to go '''
        place=self.driver.find_element('id',':Ra9:')
        place.send_keys(Keys.CONTROL,'a',Keys.DELETE)
        place.send_keys(place_to_go)
        obj=self.driver.find_element(By.XPATH,(f"//*[text()='{place_to_go}']"));
        obj.click()
    
    def select_date(self,check_in:str,check_out:str)->None:
        '''enter date in format like 21 April 2023'''
        self.driver.find_element('css selector',f'[aria-label="{check_in}"]').click()
        self.driver.find_element('css selector',f'[aria-label="{check_out}"]').click()
                
    def select_adult(self,count:int=2)->None:
        '''enter the number of adults'''
        self.driver.find_element('css selector',f'button[data-testid="occupancy-config"]').click()
        increase_count=self.driver.find_elements(By.CSS_SELECTOR,("button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.d64a4ea64d"))
        if(count>2):
            for i in increase_count:
                for _ in range(count-2):
                    i.click()
                break
        else:
            self.driver.find_element(By.CSS_SELECTOR,("button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.cd7aa7c891")).click()
        self.driver.find_element(By.CSS_SELECTOR,("button.fc63351294.a822bdf511.e2b4ffd73d.f7db01295e.c938084447.a9a04704ee.d285d0ebe9")).click()
    
    def confirm_search(self)->None:
        '''submit button on home page'''
        self.driver.find_element('css selector','button[type="submit"]').click()
        
    def apply_filtrations(self):
        '''apply star filtrations '''
        filtrations=booking_filtrations(driver=self.driver)
        filtrations.apply_star_rating("4 stars","5 stars")
        time.sleep(3)
        filtrations.sort_by_money()
    
    def report_results(self):
        # This function takes the hotel list and generates a report using the Booking Report class.
        # The report is then printed out in a table format.
        hotel_list=self.driver.find_element('id',"search_results_table")
        report=BookingReport(hotel_list)
        table=PrettyTable(field_names=["Hotel Name","Hotel Price","Hotel Score"])
        table.add_rows(report.pull_details())
        print(table)

