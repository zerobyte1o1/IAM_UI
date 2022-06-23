import logging

import allure
from hamcrest import *
from pageObject.flow_page import FlowPage


class TestFlow:
    def setup_class(self):
        self.flow = FlowPage()

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/1", name="流程创建、及其表单交互")
    def test_create_flow_and_form_interaction(self):
        expect = self.flow.create_flow()
        real = self.flow.get_flow_and_tasks()
        logging.info(f'\nexpect_flow_and_tasks:{expect};\nreal_flow_and_tasks:{real}')
        assert_that(real, equal_to(expect))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/2", name="更新流程")
    def test_update_flow_task(self):
        expect = self.flow.update_flow()
        real = self.flow.get_list_n_column_value(2)
        assert_that(real, equal_to(expect))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/3", name="删除流程")
    def test_delete_flow(self):
        before_delete = self.flow.get_flow_and_tasks()
        self.flow.delete_flow()
        after_delete = self.flow.get_flow_and_tasks()
        assert_that(before_delete, not_(equal_to(after_delete)))

    def teardown_class(self):
        self.flow.driver.quit()
