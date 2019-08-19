#引入appium包

from appium import webdriver
import time

class Driver():
    def startup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "21e5ec9d",
            "platformVersion": "5.1.1",
            #"app"安装包在手机安装后就不用再执行了
            #"app": "D:\\apkk\\jinritoutiao5.9.5_anfensi.com.apk",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.SplashActivity",
            "noReset": "True"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

        return self.driver

Driver().startup()














