import os
import sys
import pytest

sys.path.append(os.getcwd())

from Base.getDriver import get_phone_driver
from Base.getfiledata import GetFileData
from Page.pages import Pages
from selenium.common.exceptions import TimeoutException


def get_login_data():
    login_data = GetFileData.get_yaml_data("logindata.yml")
    suc_list = list()
    fail_list = list()

    for i in login_data:
        if login_data.get(i).get('toast'):
            temp_data = login_data.get(i)
            fail_list.append((i, temp_data.get("account"), temp_data.get("passwd"), temp_data.get("toast"),
                              temp_data.get("expect_data")))
        else:
            temp_data = login_data.get(i)
            suc_list.append((i, temp_data.get("account"), temp_data.get("passwd"), temp_data.get("expect_data")))
    return {"suc_data": suc_list, "fail_data": fail_list}


class TestLogin:
    def setup_class(self):
        self.driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page = Pages(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def goto_login_page(self):
        # 首页点击-我
        self.page.home_page().click_my_btn()
        # 引导页点击-去登录
        self.page.index_page().click_exits_account_btn()

    @pytest.mark.parametrize("case_num, account, pwd, expect_data", get_login_data().get("suc_data"))
    def test_login_success(self, case_num, account, pwd, expect_data):
        """

        :param case_num: 测试用例编号
        :param account: 账号
        :param pwd: 密码
        :param expect_data: 预期
        :return:
        """

        # 登录页-登录
        self.page.login_page().login(account, pwd)
        try:
            my_cart_text = self.page.my_page().get_my_shop_cart_text()
            # print(my_cart_text)
            try:
                assert expect_data == my_cart_text
            except AssertionError:
                self.page.my_page().screen_page(case_num)
                assert False
            finally:
                self.page.my_page().click_my_setting_btn()
                self.page.setting_page().logout()

        except TimeoutException:
            self.page.login_page().screen_page(case_num)
            # 关闭登录页面
            self.page.login_page().close_login_page()
            assert False

    @pytest.mark.parametrize("case_num, account, pwd, toast, expect_data", get_login_data().get("fail_data"))
    def test_login_fail(self, case_num, account, pwd, toast, expect_data):
        """

        :param case_num:测试用例编号
        :param account:账号
        :param pwd:密码
        :param toast:提示信息关键字
        :param expect_data:预期结果
        :return:
        """

        # 登录页-登录
        self.page.login_page().login(account, pwd)
        try:
            """登录页"""
            tip_msg = self.page.login_page().get_toast(toast)
            print("tip_msg=", tip_msg, "expect_data", expect_data)
            # try:
            #     assert expect_data == tip_msg
            # except AssertionError:
            #     self.page.setting_page().screen_page(case_num)
            #     assert False
            # finally:
            #     try:
            #         """在登录页"""
            #         self.page.login_page().get_login_btn()
            #         # 关闭登录页
            #         self.page.login_page().close_login_page()
            #     except TimeoutException:
            #         """个人中心页"""
            #         # 退出操作
            #         self.page.my_page().click_my_setting_btn()
            #         self.page.setting_page().logout()
            try:
                self.page.login_page().get_login_btn()
                assert tip_msg == expect_data
                self.page.login_page().close_login_page()
            except AssertionError:
                print("有toast断言错误截图---1-")
                self.page.login_page().screen_page(case_num)
                self.page.login_page().close_login_page()
                assert False
            except TimeoutException:
                """在个人中心页"""
                print("有toast进入个人中心截图---2--")
                self.page.login_page().screen_page(case_num)
                self.page.my_page().click_my_setting_btn()
                self.page.setting_page().logout()
                assert False
        except TimeoutException:
            print("没有toast截图---3-")
            self.page.setting_page().screen_page(case_num)
            try:
                """登录页"""
                self.page.login_page().get_login_btn()
                # 关闭登录页
                self.page.login_page().close_login_page()
            except TimeoutException:
                """个人中心页"""
                # 退出操作
                self.page.my_page().click_my_setting_btn()
                self.page.setting_page().logout()
            assert False
