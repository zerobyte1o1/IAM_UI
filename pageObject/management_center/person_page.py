from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.base_page import BasePage
from utils.env import Environment


class PersonPage(BasePage):
    env = Environment()
    _base_url = env.url(module="person")

    def add_person(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/button[2]').click()
        self.driver.find_element(By.XPATH, '//input[@name="jobNumber"]').send_keys(self.faker.ssn())
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(self.mock.mock_data("name"))
        self.driver.find_element(By.XPATH, '//div[@name="organizations"]').click()
        self.driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]//input').click()
        self.driver.find_element(By.XPATH,'//button[text()="确定"]').click()

if __name__ == '__main__':
    a = PersonPage()
    a.add_person()
