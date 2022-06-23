from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.base_page import BasePage
from utils.env import Environment


class BOMPage(BasePage):
    env = Environment()
    _base_url = env.url(module="bom")

    def get_num_of_released_bom(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//tr[1]/th[1]'))
        )
        self.driver.find_element(By.XPATH, '//label[span="仅查看定版BOM"]//input').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//tr[1]/th[1]'))
        )
        res = self.get_count_of_table()
        return res
