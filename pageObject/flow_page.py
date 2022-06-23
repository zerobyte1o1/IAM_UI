import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from pageObject.base_page import BasePage
from utils.env import Environment
from utils.mock import Mock


class FlowPage(BasePage):
    env = Environment()
    _base_url = env.url(module="flow")

    """
    这里我让它做的事情如下：
    1、打开表单
    2、填写流程名称
    3、依次创建任务b,d,a
    4、在b后面创建c、e
    5、删除e
    6、a拖拽到b前面
    return [流程名称,任务自上而下排名]。届时断言的时候，直接验证是不是[flow_name,a,b,c,d]
    """

    # 先来写2个基本方法
    # 表单新增任务
    def _add_task(self, add_num: int):
        for task_num in range(1, add_num + 1):
            self.driver.find_element(
                By.XPATH, f'//label[contains(text(),"任务{task_num}名称")]/'
                          f'parent::div/parent::div/following-sibling::div//button[2]'
            ).click()

    # 填写任务名称。args形式：(ord("a"), 0), (ord("b"), 1)...含义是在第0、1个任务名称填写下标为a、b的mock数据
    def _input_task_name(self, *args):
        mock = Mock()
        tmp_list = []
        for (task_name_suffix, n) in args:
            task_name = mock.mock_data("task_name_" + chr(task_name_suffix))
            ele = self.driver.find_element(By.XPATH, f'//input[@name="taskConfiguration.{n}.name"]')
            self.new_clear(ele)
            ele.send_keys(task_name)
            tmp_list.append(task_name)
        return tmp_list

    def create_flow(self) -> list:
        mock = Mock()
        flow_name = mock.mock_data("flow_name")
        expect = [flow_name]
        # step 1
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//button[span="新增流程"]'))
        )
        self.driver.find_element(By.XPATH, '//button[span="新增流程"]').click()
        # step 2
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(flow_name)
        # step 3
        self._add_task(add_num=2)
        first_add = self._input_task_name((ord("b"), 0), (ord("d"), 1), (ord("a"), 2))
        expect.extend(first_add)
        # step 4
        self._add_task(2)
        second_add = self._input_task_name((ord("c"), 1), (ord("e"), 2))
        expect[2:len(expect) - 2] = second_add
        self.driver.find_element(
            By.XPATH, '//label[contains(text(),"任务3名称")]/parent::div/parent::div/following-sibling::div//button[1]'
        ).click()
        expect.pop(3)
        # step 5
        source = self.driver.find_element(By.XPATH, '//p[contains(text(),"设定任务")]/following-sibling::div[4]/div')
        target = self.driver.find_element(By.XPATH, '//p[contains(text(),"设定任务")]/following-sibling::div[1]/div')
        # 这个方法由JS实现，网上有热心网友封装，这里直接拿来用
        drag_and_drop(self.driver, source, target)
        expect.insert(1, expect[4])
        expect.pop(5)
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        try:
            ele = self.driver.find_element(By.XPATH, '//p[1]')
            text = ele.text
            WebDriverWait(self.driver, 10).until(lambda x: ele.text != text)
        except:
            time.sleep(3)
        return expect

    def get_flow_and_tasks(self) -> list:
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//button[span="新增流程"]'))
        )
        real = [self.driver.find_element(By.XPATH, '//p[1]').text]
        tasks = [i.text for i in self.driver.find_elements(By.XPATH, '//tr/td[2]')]
        real.extend(tasks)
        return real

    # 修改第一个task名称并返回
    def update_flow(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//button[span="修改流程"]'))
        )
        self.driver.find_element(By.XPATH, '//button[span="修改流程"]').click()
        update_task_name = self._input_task_name((ord("a"), 0))[0]
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(3)
        return update_task_name

    def delete_flow(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//button[span="新增流程"]'))
        )
        ele = self.driver.find_element(By.XPATH, '//p[1]')
        text = ele.text
        ActionChains(self.driver).move_to_element(ele).perform()
        ele.find_element_by_xpath(
            "./following-sibling::div//*[name()='svg'][@title='删除']"
        ).click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        WebDriverWait(self.driver, 10).until(lambda x: ele.text != text)
