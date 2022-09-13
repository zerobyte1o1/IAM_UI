from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.env import Environment


class PersonPage(BasePage):
    env = Environment()
    _base_url = env.url(module="person")

    def add_person(self):
        fack_name = self.mock.mock_data("name")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/button[2]').click()
        self.driver.find_element(By.XPATH, '//input[@name="jobNumber"]').send_keys(self.faker.ssn())
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(fack_name)
        self.driver.find_element(By.XPATH, '//div[@name="organizations"]').click()
        self.driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]//input').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        finally_name = self.wait_for_element.after_display('class_name', 'MuiAlert-message').text
        return finally_name

    def update_person(self):
        self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[10]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/div[1]/li').click()
        self.clear_and_enter('//input[@name="jobNumber"]', self.faker.ssn())
        self.clear_and_enter('//input[@name="name"]', self.mock.mock_data("name"))
        self.clear_and_enter('//input[@name="phoneNumber"]', self.faker.phone_number())
        self.clear_and_enter('//input[@name="email"]', self.faker.email())
        self.clear_and_enter('//input[@name="remark"]', self.faker.text(max_nb_chars=50))
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        finally_name = self.wait_for_element.after_display('class_name', 'MuiAlert-message').text
        return finally_name


if __name__ == '__main__':
    a = PersonPage()
    res = a.add_person()
    print(res)
