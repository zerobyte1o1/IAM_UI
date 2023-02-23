import allure
from hamcrest import assert_that, equal_to

from pageObject.management_center.person_page import PersonPage
from pageObject.management_center.account_page import AccountPage


class TestAccountManage:
    def setup_class(self):
        self.person_page = PersonPage()
        self.person_page.add_person()
        self.person_page.create_account()
        self.account_page = AccountPage()

    def setup(self):
        self.account_page.get_base_url()


    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/144", name="配置角色")
    def test_configure_roles(self):
        assert_info = self.account_page.configure_roles()
        assert_that(assert_info, equal_to("配置成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/145", name="配置账号功能权限")
    def test_account_function_permission(self):
        assert_info=self.account_page.account_function_permission()
        assert_that(assert_info,equal_to("配置成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/157", name="配置账号数据权限")
    def test_account_data_permission(self):
        assert_info=self.account_page.account_data_permission()
        assert_that(assert_info,equal_to("配置成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/158", name="预览功能权限")
    def test_account_review_function_permission(self):
        assert_info=self.account_page.account_review_function_permission()
        assert_that("功能清单" in assert_info)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/159", name="预览数据权限")
    def test_account_review_data_permission(self):
        assert_info=self.account_page.account_review_data_permission()
        assert_that("数据权限" in assert_info)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/160", name="删除单个权限")
    def test_delete_accoungt_function_permission(self):
        assert_info=self.account_page.delete_account_function_permission()
        assert_that(assert_info,equal_to("删除成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/161", name="批量删除功能权限")
    def test_batch_delete_account_function_permission(self):
        assert_info=self.account_page.batch_delete_account_function_permission()
        assert_that(assert_info,equal_to("删除成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/150", name="账号详情-配置角色")
    def test_account_detail_role(self):
        assert_info=self.account_page.account_detail_role()
        assert_that(assert_info,equal_to("配置成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/152", name="批量配置角色")
    def batch_assign_role(self):
        assert_info = self.account_page.batch_assign_role()
        assert_that(assert_info, equal_to("分配成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/153", name="批量移除角色")
    def batch_remove_role(self):
        assert_info = self.account_page.batch_remove_role()
        assert_that(assert_info, equal_to("移除成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/162", name="账号详情-允许登录")
    def test_account_detail_able_login(self):
        assert_info=self.account_page.account_detail_able_login()
        assert_that(assert_info,equal_to("允许登录成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/163", name="账号详情-禁止登陆")
    def test_account_detail_disable_login(self):
        assert_info=self.account_page.account_detail_disable_login()
        assert_that(assert_info,equal_to("禁止登录成功"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/154", name="删除账号")
    def test_account_detail_delete(self):
        assert_info=self.account_page.account_detail_delete()
        assert_that(assert_info,equal_to("删除成功"))