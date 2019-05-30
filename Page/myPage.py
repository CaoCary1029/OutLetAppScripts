from Base.base import Base
from Page.UIElements import UIElements


class MyPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_my_shop_cart_text(self):
        """
        获取优惠券文本内容
        :return: 优惠券文本内容
        """
        return self.get_element(UIElements.person_shop_cart_id).text

    def click_my_setting_btn(self):
        """点击设置按钮方法"""
        self.click_element(UIElements.person_setting_btn_id)
