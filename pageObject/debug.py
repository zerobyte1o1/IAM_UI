# -*-coding:utf-8 -*-

"""
# File       : debug
# Time       ：2021/12/15 4:49 下午
# Author     ：10
"""
import time
from random import randint

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.webdriver.common.by import By


from utils.mock import Mock


def get_driver(port=8888):
    """拿到打开的浏览器，debug模式，调试用"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:%s" % port)
    c = webdriver.Chrome(port=19888, options=options)
    return c


def Clear(element):
    """清空输入框内容，部分使用clear没有用，使用这种方法可以"""
    element.clear()
    element.send_keys(Keys.ARROW_DOWN)
    while element.get_attribute("value"):
        element.send_keys(Keys.BACKSPACE)

def input_task_name(*args):
    driver = get_driver()
    mock = Mock()
    tmp_list = []
    for (task_name_suffix, n) in args:
        task_name = mock.mock_data("task_name_" + chr(task_name_suffix))
        ele = driver.find_element(By.XPATH, f'//input[@name="taskConfiguration.{n}.name"]')
        Clear(ele)
        ele.send_keys(task_name)
        tmp_list.append(task_name)
    return tmp_list

def test():
    driver = get_driver()
    path1 = driver.find_element(By.XPATH, '//p[contains(text(),"设定任务")]/following-sibling::div[1]/div')
    path2 = driver.find_element(By.XPATH, '//p[contains(text(),"设定任务")]/following-sibling::div[2]/div')
    drag_and_drop(driver, path1, path2)


def test_1():
    driver = get_driver()
    driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="category"]').click()
    driver.find_element(By.XPATH, f'//span[contains(text(),"新品定制")]').click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[span="确定"]')))
    driver.find_element(By.XPATH, '//button[span="确定"]').click()
    time.sleep(5)
    ele = driver.find_element(By.XPATH, '//tr[1]/td[1]')
    res = ele.text
    WebDriverWait(driver, 10).until(lambda x: ele.text != res)
    print(res)


def test_2():
    driver = get_driver()
    WebDriverWait(driver, 10).until(
        lambda x: len(driver.find_elements(By.XPATH, '//div[label="立项文档"]//img')) > 1
    )


def test_3():
    driver = get_driver()
    eles = '//div[h6="小组列表"]/following-sibling::div[2]/div'
    res = [i.text for i in driver.find_elements(By.XPATH, eles)]
    print(res)


def test_4():
    driver = get_driver()
    mock = Mock()
    for i in range(2):
        proportion = randint(1, 10)
        research_unit = mock.mock_data("research_unit")
        driver.find_element(By.XPATH, f'//tbody/tr[{i + 1}]//td[9]//input').send_keys(proportion)
        driver.find_element(By.XPATH, f'//tbody/tr[{i + 1}]//td[10]//input').send_keys(research_unit)
        i += 1


