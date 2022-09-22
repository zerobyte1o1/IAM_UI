import time

from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.driver_factory import DriverFactory
from utils.env import Environment
from utils.wait_for_element import WaitForElement
from utils.mock import Mock


class BasePage:
    _base_url = None
    mock = Mock()
    faker = Faker(locale=['zh-cn'])
    wait_for_element = WaitForElement()

    # 当子类没有构造函数的时候，在实例化的过程中，会自动父类的构造函数
    # 所以，每个PO 在实例化过程中，都会执行构造函数的逻辑
    # 问题： 如何避免driver 的重复实例化

    def __init__(self, **kwargs):
        """
        告诉父类的构造函数，如果传参了，不需要进行重复的实例化操作
        如果没有传参， 那么就是第一次的实例化操作，需要进行实例化
        :param base_driver:
        """
        # 判断是否用新的账号进行操作
        if kwargs:
            # 有新的账号时，若有driver，则关闭driver
            if DriverFactory.driver:
                DriverFactory.driver.quit()
            # 使用新的账号登录进入平台
            self.driver = DriverFactory.get_driver(**kwargs)
        # 不存在新账号时，DriverFactory.driver为真，则已有开启窗口无需重新实例化
        elif DriverFactory.driver:
            # 存在driver时则沿用driver
            self.driver = DriverFactory.driver
        # 如果不存在driver，则重新开启窗口并登录管理员账号
        else:
            self.driver = DriverFactory.get_driver()
        # 防止登录接口未返回直接请求页面导致停留在登录页面，加入显示等待
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/header/div/div[4]/div[1]/div[2]/input'))
        )
        self.driver.get(self._base_url)

    def get_count_of_table(self):
        count = self.driver.find_element(By.XPATH, '//span[contains(text(),"共")]').text[2: -2]
        return int(count)

    # 查询返回第一行数据第n个column的value;理论上n要填写的是int型，但考虑到可能会有"最后一个元素"这种特殊需求，所以不限制数据类型
    def get_list_n_column_value(self, n):
        get_column_ele = self.driver.find_element(By.XPATH, f'//tr[1]/td[{n}]')
        get_column_value = get_column_ele.text
        return get_column_value

    # 获取alert信息
    def get_alert(self):
        ele = self.wait_for_element.after_display('xpath', '//div[contains(@class,"MuiAlert-message")]')
        alert = ele.text
        return alert

    # 获取最后的alert信息
    def get_last_alert(self):
        ele = self.wait_for_element.after_display('xpath', '//div[2]/div/div/div/div/div[contains(@class,"MuiAlert-message")]')
        alert = ele.text
        return alert

    # 监听当前页面dialog数量
    def detect_num_of_dialog(self, expect: int):
        eles = self.driver.find_elements(By.XPATH, '//div[@role="dialog"]')
        if len(eles) == expect:
            return True
        else:
            return False

    @staticmethod
    def new_clear(element):
        """清空输入框内容，部分使用clear没有用，使用这种方法可以"""
        element.clear()
        element.send_keys(Keys.ARROW_DOWN)
        while element.get_attribute("value"):
            element.send_keys(Keys.BACKSPACE)

    def get_login(self):
        self.driver.get("http://www.test3.teletraan.io")

    def get_base_url(self):
        self.driver.get(self._base_url)

    def clear_and_enter(self, xpath, content):
        """
        清空并输入
        """
        self.driver.find_element(By.XPATH, xpath).clear()
        self.driver.find_element(By.XPATH, xpath).send_keys(content)

    def click_button(self, value):
        """点击button"""
        self.driver.find_element(By.XPATH, '//button[text()="' + value + '"]').click()


if __name__ == '__main__':
    BasePage()
