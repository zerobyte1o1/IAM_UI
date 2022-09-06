from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utils.env import Environment


class DriverFactory:
    # 静态属性
    driver = None

    @classmethod
    def get_driver(cls,**kwargs):
        env = Environment()
        DriverFactory.driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))
        DriverFactory.driver.maximize_window()
        DriverFactory.driver.implicitly_wait(10)
        DriverFactory.driver.get(env.login_url())
        # 如果传入账号
        if kwargs:
            DriverFactory.driver.find_element(By.XPATH, "//input[@name='tenantCode']").send_keys(kwargs["code"])
            DriverFactory.driver.find_element(By.XPATH, "//input[@name='account']").send_keys(kwargs["account"])
            DriverFactory.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(kwargs["password"])
        else:

            DriverFactory.driver.find_element(By.XPATH, "//input[@name='tenantCode']").send_keys(env.code())
            DriverFactory.driver.find_element(By.XPATH, "//input[@name='account']").send_keys(env.account())
            DriverFactory.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(env.password())
        DriverFactory.driver.find_element(By.XPATH, "//form//button[@id]").click()
        return DriverFactory.driver
