import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.base_page import BasePage
from utils.env import Environment
from utils.mock import Mock


class GroupSettingPage(BasePage):
    env = Environment()
    _base_url = env.url(module="projectGroup")


    def add_group(self):
        mock = Mock()
        group_name = mock.mock_data(data_name="group")
        self.driver.find_element(By.XPATH, '//*[name()="svg"][@title="新增小组"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(group_name)
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        try:
            ele = self.driver.find_element(By.XPATH, '//div[h6="小组列表"]/following-sibling::div[2]/div[1]')
            text = ele.text
            WebDriverWait(self.driver, 10).until(lambda x: ele.text != text)
        except:
            time.sleep(3)
        return group_name

    # 就是加第一个人员
    def add_member(self):
        self.driver.find_element(By.XPATH, '//button[span="配置组员"]').click()
        self.driver.find_element(
            By.XPATH, '//div[h4="配置组员"]/ancestor::div//tbody/tr[1]//button'
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[h4="配置组员"]//button'))
        )
        res = self.driver.find_element(
            By.XPATH, '//div[h4="配置组员"]/ancestor::div//tbody/tr[1]//td[1]'
        ).text
        self.driver.find_element(By.XPATH, '//div[h4="配置组员"]//button').click()
        time.sleep(1)
        return res

    # 这个表格最新的记录新增在底部，所以不用base_page的通用method
    def get_new_member(self):
        ele = self.driver.find_element(By.XPATH, '//tr[last()]/td[1]')
        return ele.text

    def get_new_group(self):
        ele = self.driver.find_element(By.XPATH, '//div[h6="小组列表"]/following-sibling::div[2]/div[1]')
        text = ele.text
        return text

    def get_all_groups(self) -> list:
        eles = '//div[h6="小组列表"]/following-sibling::div[2]/div'
        groups = [i.text for i in self.driver.find_elements(By.XPATH, eles)]
        return groups

    def delete_member(self):
        self.driver.find_element(By.XPATH, '//tbody/tr[1]//button').click()

    def delete_group(self):
        ele = self.driver.find_element(By.XPATH, '//div[h6="小组列表"]/following-sibling::div[2]/div[1]')
        text = ele.text
        ActionChains(self.driver).move_to_element(ele).perform()
        ele.find_element_by_xpath(
            f".//*[name()='svg'][@title='删除']"
        ).click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        try:
            res = self.get_alert()
            return res
        except:
            WebDriverWait(self.driver, 10).until(lambda x: ele.text != text)

    def update_group(self):
        mock = Mock()
        update_group_name = mock.mock_data(data_name="group")
        ele = self.driver.find_element(By.XPATH, '//div[h6="小组列表"]/following-sibling::div[2]/div[1]')
        text = ele.text
        ActionChains(self.driver).move_to_element(ele).perform()
        ele.find_element_by_xpath(
            f"./following-sibling::div//*[name()='svg'][@title='编辑']"
        ).click()
        target = self.driver.find_element(By.XPATH, '/input[@name="name"]')
        self.new_clear(target)
        target.send_keys(update_group_name)
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        WebDriverWait(self.driver, 10).until(lambda x: ele.text != text)
        return update_group_name
