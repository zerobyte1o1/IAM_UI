import logging
import time
from random import randint

import allure
from hamcrest import *
from pageObject.material_category_page import MaterialCategoryPage


class TestCreateMaterialCategory:
    def setup_class(self):
        self.mat_cg = MaterialCategoryPage()

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/10", name="创建物料类别")
    def test_create_material_category(self):
        create_name = self.mat_cg.create_material_category_get_name(randint(1, 4))
        get_name = self.mat_cg.get_first_material_category_name()
        assert_that(get_name, equal_to(create_name))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/11", name="编辑物料类别")
    def test_update_material_category(self):
        update_name = self.mat_cg.update_material_category_get_name()
        get_name = self.mat_cg.get_first_material_category_name()
        assert_that(get_name, equal_to(update_name))

    """
    物料类别的删除也包含一些校验逻辑；需要2个cases来验证：
    caseA：创建物料类别、删除。删除成功
    caseB：创建物料类别、创建物料并引用之、删除。删除失败
    """

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/12", name="删除物料类别_正常")
    def test_delete_material_category_a(self):
        self.mat_cg.create_material_category_get_name(randint(1, 4))
        time.sleep(1)
        count_before_delete = self.mat_cg.get_count_of_table()
        self.mat_cg.delete_material_category()
        time.sleep(1)
        count_after_delete = self.mat_cg.get_count_of_table()
        logging.info(f'count_before_delete:{count_before_delete};count_after_delete:{count_after_delete}')
        assert_that(count_before_delete-1, equal_to(count_after_delete))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/13", name="删除物料类别_被引用")
    def test_delete_material_category_b(self):
        category_name = self.mat_cg.create_material_category_get_name(1)
        self.mat_cg.goto_material_manage().create_material_of_specified_category(category=category_name)
        time.sleep(2)
        count_before_delete = self.mat_cg.goto_material_category().get_count_of_table()
        self.mat_cg.delete_material_category()
        count_after_delete = self.mat_cg.get_count_of_table()
        logging.info(f'count_before_delete:{count_before_delete};count_after_delete:{count_after_delete}')
        assert_that(count_before_delete, equal_to(count_after_delete))

    def teardown_class(self):
        self.mat_cg.driver.quit()
