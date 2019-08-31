# coding:utf-8
from common.MyTest import MyTest

import time,unittest
from po.HomePage import HomePage
from common.Public import Operation


class HomeTest(MyTest):


    # def test_one(self):

        # 清除搜索输入框
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
        # driver.find_element_by_id("com.ss.android.article.news:id/a9z").clear()
        # print("clear")
        # time.sleep(3)
        # driver.find_element_by_id("com.ss.android.article.news:id/m0").clear()
        # print("clear2")
        # time.sleep(3)
        # # 输入想要搜索的内容
        # driver.find_element_by_id("com.ss.android.article.news:id/m0").send_keys("ABCDE")
        # print("send_keys")
    # #
    # def test_two(self):
    #     driver = Driver.startUp(self.driver)
    #     # 清除搜索输入框
    #     driver.find_element_by_id("com.ss.android.article.news:id/a9z").clear()
    #     print("clear3")
    #     time.sleep(3)
    #     driver.find_element_by_id("com.ss.android.article.news:id/m0").clear()
    #     print("clear4")
    #     time.sleep(3)
    #     # 输入想要搜索的内容
    #     driver.find_element_by_id("com.ss.android.article.news:id/m0").send_keys("ttt")
    #     print("send_keys2")


    def test_click(self):
        print('run hometest')
        h = HomePage(self.driver)
        print('点击搜索')
        # h.clickSearch()
        # self.assertEqual(1,1)

    # def test_fore(self):
    #     p = Operation(self.driver)
    #     p.swipeLeft()


if __name__ == '__main__':
    unittest.main()

# class HomeTest(unittest.TestCase):
#      # def setUpClass(cls):
#      #     print('AAAAAA')
#      #     driver = Driver()
#      #     cls.driver = driver.startUp()
#
#
#     def setUp(self):
#         print('BBBBBB')
#         driver = Driver()
#         self.driver = driver.startUp()
#         #如果放在这里，每执行一条案例就要执行一次，浪费时间
#         #driver = Driver()
#         #self.driver = driver.startup()
#
#     def test1(self):
#         #driver = Driver()
#         #self.driver = driver.startup()
#
#         print("QQQQQ")
#
#         self.driver.find_element_by_xpath(
#             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout[1]/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView").click()
#         print("click")
#         self.driver.find_element_by_id("com.ss.android.article.news:id/adu").click()
#         print("click2")
#         self.driver.find_element_by_id("com.ss.android.article.news:id/h3").send_keys("12345678901")
#         print("send_keys")
#
#     def test2(self):
#         #清除搜索输入框
#         #driver = Driver()
#         #driver.startup()
#         print("pppppp")
#
#         # self.driver.find_element_by_id("com.ss.android.article.news:id/a9z").clear()
#         # print("clear")
#         # self.driver.find_element_by_id("com.ss.android.article.news:id/m0").clear()
#         # print("clear2")
#         # #输入想要搜索的内容
#         # self.driver.find_element_by_id("com.ss.android.article.news:id/m0").send_keys("ABCDE")
#         # print("send_keys")
#         # #点击搜索按钮
#         # self.driver.find_element_by_id("com.ss.android.article.news:id/ok").click()
#         # print("click")
#
#
#     def tearDown(self):
#         print("CCCCCC")
#
#
#     # def tearDownClass(cls):
#     #     print("DDDDDDD")
#     #     cls.driver.quit()
#
#
#
# if __name__ == '__main__':
#     unittest.main()