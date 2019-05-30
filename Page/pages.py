from Page.homePage import HomePage
from Page.indexPage import IndexPage
from Page.loginPage import LoginPage
from Page.myPage import MyPage
from Page.settingPage import SettingPage


class Pages:
    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        """实例化首页页面对象"""
        return HomePage(self.driver)

    def index_page(self):
        """实例化引导页页面对象"""
        return IndexPage(self.driver)

    def login_page(self):
        """实例化登录页页面对象"""
        return LoginPage(self.driver)

    def my_page(self):
        """实例化个人中心页页面对象"""
        return MyPage(self.driver)

    def setting_page(self):
        """实例化设置页页面对象"""
        return SettingPage(self.driver)
