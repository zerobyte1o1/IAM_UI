import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.base_page import BasePage
from utils.env import Environment
from utils.mock import Mock


class MaterialCategoryPage(BasePage):
    env = Environment()
    _base_url = env.url(module="category")

    # 选物料属性，创建物料类别
    def create_material_category_get_name(self, pick_num_category_form:int):
        mock = Mock()
        category_name = mock.mock_data('category_name')
        self.driver.find_element(By.XPATH, '//button[span="新增物料类别"]').click()
        self.driver.find_element(By.XPATH, '//div[label="*物料类别"]/ancestor::div//input[@name="property"]').click()
        self.driver.find_element(By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//li[{pick_num_category_form}]')\
            .click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(category_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[span="确定"]'))
        )
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(2)
        return category_name

    # filter="物料属性"，list搜索，获取返回物料类别列表
    def get_materials_category_search(self, pick_num_category_filter: int):
        self.driver.find_element(By.XPATH, '//input[@placeholder="物料属性"]').click()
        self.driver.find_element(By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//li[{pick_num_category_filter}]')\
            .click()
        self.driver.find_element(By.XPATH, '//button[span="查询"]').click()
        time.sleep(2)
        return [i.text for i in self.driver.find_elements(By.XPATH, '//tr/td[2]')]

    def get_first_material_category_name(self):
        first_material_category_name = self.driver.find_element(By.XPATH, '//tr[1]/td[2]').text
        return first_material_category_name

    # 更新第一个物料类别的名称
    def update_material_category_get_name(self):
        mock = Mock()
        category = mock.mock_data("category")
        self.driver.find_element(By.XPATH, '//tr[1]/td[3]//button[@title="编辑"]').click()
        ele = self.driver.find_element(By.XPATH, '//input[@name="name"]')
        self.new_clear(ele)
        ele.send_keys(category)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[span="确定"]'))
        )
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(2)
        return category

    def delete_material_category(self):
        self.driver.find_element(By.XPATH, '//tr[1]/td[3]//button[@title="删除"]').click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(3)
