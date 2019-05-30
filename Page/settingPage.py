from Base.base import Base
from Page.UIElements import UIElements


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def logout(self, is_logout=True):
        """
        退出登录方法
        :param is_logout: 确认退出--True，取消退出--False
        :return:
        """
        # 滑动到屏幕底部
        self.scroll_screen()
        self.click_element(UIElements.setting_logout_btn_id)

        self.click_element(UIElements.setting_acc_quit_btn_id)\
            if is_logout else self.click_element(UIElements.setting_dis_quit_btn_id)
