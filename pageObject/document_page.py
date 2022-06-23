from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.env import Environment


class DocumentPage(BasePage):
    env = Environment()
    _base_url = env.url(module="document")

    def go_to_document_tab(self, pro_name: str, doc_type_name: str):
        project_xpath = self.driver.find_element(
            By.XPATH, f'//p[contains(text(), "{pro_name}")]'
        )
        project_xpath.click()
        doc_type_tab_xpath = self.driver.find_element(
            By.XPATH, f'//button[span="{doc_type_name}"]'
        )
        doc_type_tab_xpath.click()
