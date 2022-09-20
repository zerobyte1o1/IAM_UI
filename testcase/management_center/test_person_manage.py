import allure
from hamcrest import *

from pageObject.management_center.person_page import PersonPage


class TestPersonManage:
    def setup(self):
        self.person_page = PersonPage()
        self.person_page.get_base_url()
        self.person_page.add_person()
        # 防止创建成功的alert影响结果
        self.person_page.get_base_url()

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/137", name="新增人员")
    def test_add_person(self):
        assert_info = self.person_page.add_person()
        assert_that(assert_info, equal_to("新增成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/138", name="编辑人员")
    def test_update_person(self):
        assert_info = self.person_page.update_person()
        assert_that(assert_info, equal_to("编辑成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/139", name="创建账号")
    def test_create_account(self):
        assert_info = self.person_page.create_account()
        assert_that(assert_info, equal_to("创建成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/140", name="办理离职")
    def test_resign_person(self):
        assert_info = self.person_page.resign_person()
        assert_that(assert_info, equal_to("办理离职成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/141", name="办理离职")
    def test_rehire_person(self):
        self.person_page.resign_person()
        self.person_page.get_base_url()
        assert_info = self.person_page.rehire_person()
        assert_that(assert_info, equal_to("办理入职成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/142", name="删除人员")
    def test_delete_person(self):
        self.person_page.resign_person()
        self.person_page.get_base_url()
        assert_info = self.person_page.delete_person()
        assert_that(assert_info, equal_to("删除成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/143", name="转移人员")
    def test_transfer_person(self):
        assert_info = self.person_page.transfer_person()
        assert_that(assert_info, equal_to("转移成功"))
