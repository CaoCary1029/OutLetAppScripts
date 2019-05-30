from appium import webdriver


def get_phone_driver(package, activity):
    """
    声明手机驱动对象方法
    :param package: App包名
    :param activity: App启动名
    :return: 手机驱动对象
    """
    desired_caps = dict()

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.242.101:5555'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['noReset'] = True
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
