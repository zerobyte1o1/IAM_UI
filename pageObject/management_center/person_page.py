from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.env import Environment


class PersonPage(BasePage):
    env = Environment()
    _base_url = env.url(module="person")

    def add_person(self):
        """
        添加人员
        """
        fack_name = self.mock.mock_data("name")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/button[2]').click()
        self.driver.find_element(By.XPATH, '//input[@name="jobNumber"]').send_keys(self.faker.ssn())
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(fack_name)
        self.driver.find_element(By.XPATH, '//div[@name="organizations"]').click()
        self.driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]//input').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def update_person(self):
        """
        更新人员

        """
        self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[10]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/div[1]/li').click()
        self.clear_and_enter('//input[@name="jobNumber"]', self.faker.ssn())
        self.clear_and_enter('//input[@name="name"]', self.mock.mock_data("name"))
        self.clear_and_enter('//input[@name="phoneNumber"]', self.faker.phone_number())
        self.clear_and_enter('//input[@name="email"]', self.mock.mock_data("name")+self.faker.email())
        self.clear_and_enter('//input[@name="remark"]', self.faker.text(max_nb_chars=50))
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def create_account(self):
        """
        创建账号
        """
        self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[10]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/div[4]/li').click()
        self.driver.find_element(By.NAME, 'account').send_keys(self.mock.mock_data("account"))
        self.driver.find_element(By.XPATH, '//button[text()="随机生成"]').click()
        self.driver.find_element(By.NAME, 'roles').click()
        self.driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]').click()
        self.driver.find_element(By.NAME, 'roles').click()
        self.driver.find_element(By.XPATH, '//label/span/input').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def resign_person(self):
        """
        办理离职
        """
        self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[10]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/div[3]/li').click()
        self.driver.find_element(By.XPATH, '//button[text()="办理离职"]').click()
        assert_info = self.get_alert()
        return assert_info

    def rehire_person(self):
        """
        办理入职
        """
        self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[10]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/div[2]/li').click()
        self.driver.find_element(By.XPATH, '//button[text()="办理入职"]').click()
        assert_info = self.get_alert()
        return assert_info

    def delete_person(self):
        """
        删除
        """
        self.driver.find_element(By.XPATH, '//table/tbody/tr[1]/td[10]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/div[5]/li').click()
        self.driver.find_element(By.XPATH, '//button[text()="删除"]').click()
        assert_info = self.get_alert()
        return assert_info

    def transfer_person(self):
        self.driver.find_element(By.XPATH, '//button[text()="转移人员"]').click()
        self.driver.find_element(By.XPATH, '//div[@name="originOrganization"]//button').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]//li[1]/div/div/span').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]//table//tbody/tr[1]/td[1]').click()
        self.driver.find_element(By.XPATH, '//div[@name="targetOrganization"]//button').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]//li[2]/div/div/span').click()
        self.driver.find_element(By.XPATH, '//button[text()="转移"]').click()
        self.driver.find_element(By.XPATH, '//div[text()="确定将已选人员转移组织吗？"]/../..//button[text()="转移"]').click()
        assert_info = self.get_alert()
        return assert_info


if __name__ == '__main__':
    a = PersonPage()
    res = a.create_account()
    a.driver.close()
    print(res)
