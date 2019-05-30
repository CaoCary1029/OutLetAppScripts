from Base.base import Base
from Page.UIElements import UIElements


class HomePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        """点击个人中心按钮方法"""
        self.click_element(UIElements.home_my_btn_id)
