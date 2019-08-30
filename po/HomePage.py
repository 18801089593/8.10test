from appium import  webdriver
import time
from selenium.webdriver.common.by import By
from common.Driver import Driver
from common.MyTest import MyTest


class HomePage(Driver):



    def __init__(self,driver):
        #用来接收xxTest的driver实例
        self.driver = driver


    #封装页面元素属性
    search_page = (By.ID, 'com.ks.kaishustory:id/icon_tosearch')        # 搜索页

    #封装页面元素的操作方法
    def clickSearch(self):
        time.sleep(5)
        self.driver.find_element(*self.search_page).click()
        print('点击完成')
        time.sleep(10)
        return self.driver



#调试

# #
# if __name__ == '__main__':
#     h = HomePage()
#     h.clickSearch()