'''
Created on 05/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver=webdriver.Firefox()
    driver.get("http://www.makemytrip.com/car-rental/ola_cabs-online-booking.php")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='locCity']/p/span[2]/span[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='ui-active-menuitem']").click()
    driver.find_element_by_xpath(".//*[@id='carsLandingForm']/div[3]/div[4]/table/tbody/tr/td[2]/div/p/span[1]/span/a").click()
    driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[2]/td[6]/a").click()
    driver.find_element_by_xpath(".//*[@id='customerEmail']").send_keys("Rachappahalinge@gmail.com")
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='localbooking']").click()