from Base.base import Base
from Page.UIElements import UIElements


class LoginPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, account, pwd):
        """
        登录方法
        :param account: 账号
        :param pwd: 密码
        :return:
        """
        # 输入用户名
        self.input_text(UIElements.login_account_id, account)
        # 输入密码
        self.input_text(UIElements.login_passwd_id, pwd)
        # 点击登录按钮
        self.click_element(UIElements.login_btn_id)

    def close_login_page(self):
        """关闭登录页方法"""
        self.click_element(UIElements.login_close_page_btn_id)

    def get_login_btn(self):
        """定位登录按钮方法"""
        self.get_element(UIElements.login_btn_id)
