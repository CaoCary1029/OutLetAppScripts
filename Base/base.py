import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, poll_frequency=1.0):
        """
        定位单个元素方法
        :param loc:
        :param timeout:
        :param poll_frequency:
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, poll_frequency=1.0):
        """
        定位一组元素方法
        :param loc:
        :param timeout:
        :param poll_frequency:
        :return: 元素定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, poll_frequency=1.0):
        """
        点击元素对象方法
        :param loc:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).click()

    def input_text(self, loc, text, timeout=30, poll_frequency=1.0):
        """
        输入元素对象方法
        :param loc:
        :param text:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        element = self.get_element(loc, timeout, poll_frequency)
        element.clear()
        element.send_keys(text)

    def page_scroll_to_bottom(self):
        """滑到页面底部方法"""
        width = self.driver.get_window_size().get('width')
        height = self.driver.get_window_size().get('height')
        self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, duration=2000)

    def scroll_screen(self, direction=1):
        """
        滑动屏幕方法
        :param direction: 上-1,下-2，左-3，右-4
        :return:
        """
        screen_size = self.driver.get_window_size()
        width = screen_size.get('width')
        height = screen_size.get('height')
        time.sleep(2)
        if isinstance(direction, int):
            if direction == 1:
                self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
            elif direction == 2:
                self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
            elif direction == 3:
                self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
            elif direction == 4:
                self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)
            else:
                return "direction value is wrong"
        else:
            return "direction value is wrong"

    def screen_page(self, shot_name="截图"):
        """截图操作"""
        img_path = "./images" + os.sep + "{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(img_path)
        with open(img_path, "rb") as f:
            allure.attach(shot_name, f.read(), allure.attach_type.PNG)

    def get_toast(self, toast):
        """

        :param toast: 关键字
        :return: toast全部信息
        """
        tip_ele = (By.ID, "//*[contains(@text,{})]".format(toast))
        tip_msg = self.get_element(tip_ele).text
        return tip_msg
