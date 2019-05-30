from selenium.webdriver.common.by import By

from Base.getDriver import get_phone_driver
from Page.pages import Pages

driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")

pages_obj = Pages(driver)

# 首页点击-我
pages_obj.home_page().click_my_btn()

# 去登陆
pages_obj.index_page().click_exits_account_btn()

# 登录页操作
pages_obj.login_page().login("13348011029", "123ab")

error_msg = (By.XPATH, '//*[contains(@text,"错误")]')
msg = pages_obj.login_page().get_element(error_msg, timeout=5, poll_frequency=0.5).text
print(msg)
# 我的页面操作
# print(pages_obj.my_page().get_my_shop_cart_text())
# pages_obj.my_page().click_my_setting_btn()

# 退出
# pages_obj.setting_page().logout()
driver.quit()
