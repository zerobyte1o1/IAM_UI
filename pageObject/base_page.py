import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.env import Environment
from utils.driver_factory import DriverFactory


class BasePage:
    _base_url = None

    # 当子类没有构造函数的时候，在实例化的过程中，会自动父类的构造函数
    # 所以，每个PO 在实例化过程中，都会执行构造函数的逻辑
    # 问题： 如何避免driver 的重复实例化

    def __init__(self):
        """
        告诉父类的构造函数，如果传参了，不需要进行重复的实例化操作
        如果没有传参， 那么就是第一次的实例化操作，需要进行实例化
        :param base_driver:
        """
        # DriverFactory.driver为真，则已有开启窗口无需重新实例化
        if DriverFactory.driver:
            # 存在driver时则沿用driver
            self.driver = DriverFactory.driver
            self.driver.get(self._base_url)
        # 如果不存在driver，则重新开启窗口并登录
        else:
            self.driver = DriverFactory.get_driver()

    def goto_bom(self):
        self.driver.find_element(By.XPATH, "//ul/div[2]").click()
        from pageObject.bom_page import BOMPage
        return BOMPage(self.driver)

    def goto_material_manage(self):
        self.driver.find_element(By.XPATH, "//ul/div[5]//div[@role='button'][1]").click()
        from pageObject.material_manage_page import MaterialManagePage
        time.sleep(1)
        return MaterialManagePage(self.driver)

    def goto_material_category(self):
        self.driver.find_element(By.XPATH, "//ul/div[5]//div[@role='button'][2]").click()
        from pageObject.material_category_page import MaterialCategoryPage
        time.sleep(1)
        return MaterialCategoryPage(self.driver)

    def goto_group_setting(self):
        self.driver.find_element(By.XPATH, "//ul/div[5]//div[@role='button'][3]").click()
        from pageObject.group_setting_page import GroupSettingPage
        time.sleep(1)
        return GroupSettingPage(self.driver)

    def goto_flow(self):
        self.driver.find_element(By.XPATH, "//ul/div[5]//div[@role='button'][5]").click()
        from pageObject.flow_page import FlowPage
        time.sleep(1)
        return FlowPage(self.driver)

    def goto_project(self):
        self.driver.find_element(By.XPATH, "//ul/div[1]").click()
        from pageObject.project_page import ProjectPage
        time.sleep(1)
        return ProjectPage(self.driver)

    def goto_file(self):
        self.driver.find_element(By.XPATH, "//ul/div[3]").click()
        from pageObject.document_page import DocumentPage
        return DocumentPage(self.driver)

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
        time.sleep(1)
        ele = self.driver.find_element(By.XPATH, '//div[@class="MuiAlert-message"]')
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


if __name__ == '__main__':
    BasePage()
