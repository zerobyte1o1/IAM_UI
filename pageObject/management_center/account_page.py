import time

from selenium.webdriver.common.by import By
from pageObject.base_page import BasePage
from utils.env import Environment


class AccountPage(BasePage):
    env = Environment()
    _base_url = env.url(module="account")

    def configure_roles(self):
        """
        配置角色
        """
        self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]//button').click()
        self.driver.find_element(By.XPATH, '//div/div/div//div[2]/div[2]/ul/li[1]').click()
        self.driver.find_element(By.XPATH, '//button[@title="Open"]').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]/div/ul/li[2]/div/p').click()
        self.driver.find_element(By.XPATH, '//button[@title="Close"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def account_function_permission(self):
        """
        配置账号功能权限
        """
        self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]//button').click()
        self.driver.find_element(By.XPATH, '//div/div/div//div[2]/div[2]/ul/li[3]').click()
        self.driver.find_element(By.XPATH, '//button[text()="添加规则"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="管理中心"]').click()
        self.driver.find_element(By.XPATH, '//ul/li[1]//input[@type="checkbox"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def delete_account_function_permission(self):
        """
        删除单个功能权限
        """
        self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]//button').click()
        self.driver.find_element(By.XPATH, '//div/div/div//div[2]/div[2]/ul/li[3]').click()
        self.driver.find_element(By.XPATH, '//ul/li[4]/div/div[2]//button').click()
        self.driver.find_element(By.XPATH, '//button[text()="删除"]').click()
        assert_info = self.get_last_alert()
        return assert_info

    def batch_delete_account_function_permission(self):
        """
        批量删除功能权限
        """
        self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]//button').click()
        self.driver.find_element(By.XPATH, '//div/div/div//div[2]/div[2]/ul/li[3]').click()
        self.driver.find_element(By.XPATH, '//ul//li[1]//input').click()
        self.driver.find_element(By.XPATH, '//button[text()="批量删除"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="删除"]').click()
        assert_info = self.get_last_alert()
        return assert_info

    def account_data_permission(self):
        """
        配置数据权限
        """
        self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]//button').click()
        self.driver.find_element(By.XPATH, '//div/div/div//div[2]/div[2]/ul/li[3]').click()
        self.driver.find_element(By.XPATH, '//button[text()="数据权限"]').click()
        self.driver.find_element(By.XPATH, '//div[2]/div/button[text()="配置"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def account_review_permission(self):
        """
        权限预览
        """
        self.driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]//button').click()
        self.driver.find_element(By.XPATH, '//div[2]/div[2]/ul/li[2]').click()
        assert_info = self.driver.find_element(By.XPATH, '//div[2]/div[1]/div/div[1]/h6').text
        return assert_info

    def account_review_function_permission(self):
        """
        预览功能权限
        """
        self.account_review_permission()
        self.driver.find_element(By.XPATH, '//button[text()="功能权限"]').click()
        assert_info = self.driver.find_element(By.XPATH, '//hr/../div/h6').text
        return assert_info

    def account_review_data_permission(self):
        """
        预览数据权限
        """
        self.account_review_permission()
        self.driver.find_element(By.XPATH, '//button[text()="数据权限"]').click()
        assert_info = self.driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[1]/h6').text
        return assert_info

    def account_detail(self):
        """
        进入账号详情页
        """
        self.driver.find_element(By.XPATH, '//tr[1]/td[2]/a').click()
        assert_info = self.driver.find_element(By.XPATH, '//div/div/div/div/button/../h6').text
        return assert_info

    def account_detail_role(self):
        """
        账号详情-配置角色
        """
        self.account_detail()
        self.driver.find_element(By.XPATH, '//button[text()="配置角色"]').click()
        self.driver.find_element(By.XPATH, '//button[@title="Open"]').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]/div/ul/li[2]/div/p').click()
        self.driver.find_element(By.XPATH, '//button[@title="Close"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="确定"]').click()
        assert_info = self.get_alert()
        return assert_info

    def account_detail_reset_password(self):
        """
        账号详情-重置密码
        """
        self.account_detail()
        self.driver.find_element(By.XPATH, '//button[text()="重置密码"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="重置"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="复制"]').click()
        assert_info = self.get_alert()
        return assert_info

    def account_detail_disable_login(self):
        """
        账号详情-禁止登陆
        """
        self.account_detail()
        self.driver.find_element(By.XPATH, '//button[text()="禁止登录"]').click()
        self.driver.find_element(By.XPATH, '//div/h2/../div/button[text()="禁止登录"]').click()
        assert_info = self.get_alert()
        return assert_info

    def account_detail_able_login(self):
        """
        账号详情-允许登陆
        """
        self.account_detail()
        self.driver.find_element(By.XPATH, '//button[text()="允许登录"]').click()
        self.driver.find_element(By.XPATH, '//div/h2/../div/button[text()="允许登录"]').click()
        assert_info = self.get_alert()
        return assert_info

    def account_detail_delete(self):
        """
        账号详情-删除账号
        """
        self.account_detail()
        self.driver.find_element(By.XPATH, '//button[text()="删除账号"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="删除"]').click()
        assert_info = self.get_alert()
        return assert_info

    def batch_assign_role(self):
        """
        批量分配角色
        """
        self.driver.find_element(By.XPATH, '//tr[1]/td[1]/span/input').click()
        self.driver.find_element(By.XPATH, '//button[text()="分配角色"]').click()
        self.driver.find_element(By.XPATH, '//button[@title="Open"]').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]/div/div/div/li[1]/div/p').click()
        self.driver.find_element(By.XPATH, '//button[@title="Close"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="分配"]').click()
        self.driver.find_element(By.XPATH, '//div[text()="确定将已选人员分配角色吗？"]/../..//button[text()="分配"]').click()
        assert_info = self.get_alert()
        return assert_info

    def batch_remove_role(self):
        """
        批量移除角色
        """
        self.driver.find_element(By.XPATH, '//tr[1]/td[1]/span/input').click()
        self.driver.find_element(By.XPATH, '//button[text()="移除角色"]').click()
        self.driver.find_element(By.XPATH, '//button[@title="Open"]').click()
        self.driver.find_element(By.XPATH, '//div[@role="presentation"]/div/div/div/li[1]/div/p').click()
        self.driver.find_element(By.XPATH, '//button[@title="Close"]').click()
        self.driver.find_element(By.XPATH, '//button[text()="移除"]').click()
        self.driver.find_element(By.XPATH, '//div[text()="确定将已选人员移除角色吗？"]/../..//button[text()="移除"]').click()
        assert_info = self.get_alert()
        return assert_info


if __name__ == '__main__':
    a = AccountPage()
    res = a.batch_remove_role()
    print(res)
