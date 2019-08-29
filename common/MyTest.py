import unittest
from common.Driver import Driver

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):                 #当前测试类中所有test开头的用例前执行一次
        print('执行初始化类方法')
        d = Driver()
        cls.driver = d.startUp()

    def setUp(self):                     #当前测试类中每一个test开头的用例前执行一次
        print('执行初始化方法')
        self.driver.launch_app()

    def tearDown(self):
        print('执行清理方法')
        self.driver.close_app()

    @classmethod
    def tearDownClass(cls):
        print('执行清理类方法')
        cls.driver.quit()


#
if __name__ == '__main__':
    unittest.main()