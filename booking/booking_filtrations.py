#interact with website to apply filtrations
from selenium.webdriver.remote.webdriver import WebDriver

class booking_filtrations:
    '''Applies filtrations to searched results'''
    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver
    
    def apply_star_rating(self,*stars:str)->None:
        filtration_box=self.driver.find_element('id','filter_group_class_:R14q:')
        star_child_elements=filtration_box.find_elements('css selector','*')
        for star in stars:
            for star_child_element in star_child_elements:
                if(str(star_child_element.get_attribute('innerHTML'))).strip()==star:
                    star_child_element.click()
                    
    def sort_by_money(self)->None:
        self.driver.find_element('css selector','button[data-testid="sorters-dropdown-trigger"]').click()
        self.driver.find_element('css selector','button[data-id="price"]').click()