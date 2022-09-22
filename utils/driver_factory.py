
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utils.env import Environment


class DriverFactory:
    # 静态属性
    driver = None

    @classmethod
    def get_driver(cls, **kwargs):
        env = Environment()
        cls.driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get(env.login_url())
        # 如果传入账号
        if kwargs:
            cls.driver.execute_script('window.localStorage.clear();')
            cls.driver.find_element(By.XPATH, "//input[@name='tenantCode']").send_keys(kwargs["code"])
            cls.driver.find_element(By.XPATH, "//input[@name='account']").send_keys(kwargs["account"])
            cls.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(kwargs["password"])
        else:
            cls.driver.find_element(By.XPATH, "//input[@name='tenantCode']").send_keys(env.code())
            cls.driver.find_element(By.XPATH, "//input[@name='account']").send_keys(env.account())
            cls.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(env.password())
        cls.driver.find_element(By.XPATH, "//form//button[@id]").click()
        return cls.driver
