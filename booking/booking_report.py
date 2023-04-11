from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BookingReport:
    '''BookingReport makes the report of hotel name, prices and rating out of 10'''
    def __init__(self, boxes_section_element: WebElement) -> None:
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            'class name', "da89aeb942")

    def pull_details(self) -> list:
        collections = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                'class name', 'a23c043802').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(
                'css selector',
                'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip()
            try:
                hotel_score = deal_box.find_element(
                    'css selector',
                    '[data-testid="review-score"]').find_element(
                        'css selector',
                        ".b5cd09854e.d10a6220b4").get_attribute(
                            'innerHTML').strip()
            except:
                hotel_score = "No Data"
            collections.append([hotel_name, hotel_price, hotel_score])
        return collections


