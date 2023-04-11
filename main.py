from booking.booking import Booking
import os
import time
with Booking() as bot:
    bot.land_first_page()
    bot.change_currency("USD")
    place_to_go= input("Enter the place of stay ")
    bot.select_place_to_go(place_to_go)
    date_in=input("Enter check in date in 21 April 2023 format ")
    date_out=input("Enter check in date in 21 April 2023 format ")
    bot.select_date(check_in=date_in,check_out=date_out)
    count=int(input("Enter number of adults "))
    bot.select_adult(count)
    bot.confirm_search()
    bot.apply_filtrations()
    bot.driver.refresh()
    bot.report_results()
    time.sleep(5)    