'''
Created on 05/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.abhibus.com/")
    time.sleep(2)
    driver.find_element_by_class_name("abhi-modal-close").click()
    driver.find_element_by_xpath(".//*[@id='source']").send_keys("Bidar")
    driver.find_element_by_xpath(".//*[@id='destination']").send_keys("Bangalore")
    driver.find_element_by_xpath(".//*[@id='datepicker1']").click()
    driver.find_element_by_xpath("//a[text()='24']").click()
    driver.find_element_by_xpath(".//*[@id='datepicker2']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[text()='26']").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='roundTrip']/a").click()
