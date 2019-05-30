from Base.base import Base
from Page.UIElements import UIElements


class IndexPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_account_btn(self):
        """点击已注册，去登陆按钮方法"""
        self.click_element(UIElements.sign_exits_account_btn_id)
