import time
from random import randint

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.base_page import BasePage
from utils.env import Environment
from utils.mock import Mock


class ProjectPage(BasePage):
    env = Environment()
    _base_url = env.url(module="project")

    def _go_to_detail_tab(self, pro_name: str, tab_name: str):
        detail_enter_xpath = f'//td[text()="{pro_name}"]/ancestor::tr//button[@title="查看详情"]'
        self.driver.find_element(By.XPATH, detail_enter_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//button[span="{tab_name}"]'))
        )
        self.driver.find_element(By.XPATH, f'//button[span="{tab_name}"]').click()

    # 就是options里面的中文string，比如 project_category="新品定制"
    def create_project_get_name(self, project_category: str):
        mock = Mock()
        plan_date = mock.current_date()
        create_project_attachment = mock.attachment_path(attachment_name="create_project.jpeg")
        project_name = mock.mock_data("project_name")
        project_code = mock.mock_data("project_code")
        self.driver.find_element(By.XPATH, '//button[span="项目立项"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(project_name)
        self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(project_code)
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="projectGroup"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="category"]').click()
        self.driver.find_element(By.XPATH, f'//span[contains(text(),"{project_category}")]').click()
        self.driver.find_element(
            By.XPATH, '//label[contains(text(),"计划开始日期")]/parent::div//input'
                                 ).send_keys(plan_date)
        ele = self.driver.find_element(By.XPATH, '//label[contains(text(),"立项文档")]/parent::div//input')
        ele.send_keys(create_project_attachment)
        WebDriverWait(self.driver, 10).until(
            lambda x: len(self.driver.find_elements(By.XPATH, '//div[label="立项文档"]//img')) > 1
        )
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        try:
            ele = self.driver.find_element(By.XPATH, '//tr[1]/td[1]')
            text = ele.text
            WebDriverWait(self.driver, 10).until(lambda x: ele.text != text)
        except:
            time.sleep(3)
        return project_name

    # 创建项目表单，执行小组下拉选项获取
    def create_project_form_get_group_options(self):
        self.driver.find_element(By.XPATH, '//button[span="项目立项"]').click()
        self.driver.find_element(By.XPATH, '//div[label="*项目名称"]/ancestor::div//input[@name="projectGroup"]').click()
        options = [i.text for i in self.driver.find_elements(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li')]
        self.driver.find_element(By.XPATH, '//button[span="取消"]').click()
        return options

    def add_product_to_project(self, pro_name: str, pro_category: str):
        mock = Mock()
        material_name = mock.mock_data("name")  # 名称
        material_code = mock.mock_data("code")  # 编号
        material_version = mock.mock_data("version")  # 版本
        material_unit = mock.mock_data("unit")  # 计量单位
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发产品")
        if pro_category == "新品定制" or "内部研发":
            self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(material_name)
            self.driver.find_element(By.XPATH, '//input[@name="code"]').send_keys(material_code)
            self.driver.find_element(By.XPATH, '//input[@name="versions"]').send_keys(material_version)
            self.driver.find_element(By.XPATH, '//input[@name="unit"]').send_keys(material_unit)
        elif pro_category == "工艺优化":
            self.driver.find_element(By.XPATH, '//input[@name="product"]').click()
            self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
            self.driver.find_element(By.XPATH, '//input[@name="versions"]').send_keys(material_version)
        self.driver.find_element(By.XPATH, '//button[span="保存"]').click()
        time.sleep(1)
        return ProjectPage(self.driver)

    # 前置条件：project_category = 工艺优化
    def get_product_options(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发产品")
        self.driver.find_element(By.XPATH, '//input[@name="product"]').click()
        options = [i.text for i in self.driver.find_elements(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li')]
        return options

    # 填写新增任务表单时的操作元素对象
    def _fill_task_form(self, label_name: str):
        ele = self.driver.find_element(
            By.XPATH,
            f'//div[p="2.设定任务"]/div/child::div[1]//label[contains(text(),"{label_name}")]/following-sibling::div//input'
        )
        return ele

    def add_task_to_project(self, pro_name: str, flow_name: str):
        mock = Mock()
        task_date = mock.current_date()
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//button[span="新增任务"]').click()
        self.driver.find_element(By.XPATH, '//label[contains(text(), "流程")]/following-sibling::div//input').click()
        self.driver.find_element(
            By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//span[contains(text(), "{flow_name}")]'
        ).click()
        # 禁用除第一个任务外的其他任务
        cards = self.driver.find_elements(By.XPATH, '//div[p="2.设定任务"]/div/child::div')
        switches = self.driver.find_elements(By.XPATH, '//label[span="启用"]')
        for i in range(1, len(cards)):
            switches[i].click()
        self._fill_task_form(label_name="负责人员").click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self._fill_task_form(label_name="参与人员").click()
        self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        self._fill_task_form(label_name="预计开始日期").send_keys(task_date)
        self._fill_task_form(label_name="预计结束日期").send_keys(task_date)
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        return ProjectPage(self.driver)

    def get_first_task_of_project(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        task = self.get_list_n_column_value(n=1)
        return task

    """
    获取研发任务可操作按钮数量（业务逻辑：
    1.未启动项目-任务，仅能编辑
    2.进行中项目-任务，可以编辑、查看详情，详情内可以进一步维护BOM
    ）
    """
    def get_len_acts_of_tasks(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        acts = self.driver.find_elements(By.XPATH, '//tr[1]/td[last()]//button')
        return len(acts)

    def create_bom(self, pro_name: str, create_time: int):
        mock = Mock()
        bom_versions = []
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        for i in range(create_time):
            bom_version = mock.mock_data(data_name="bom_version")
            self.driver.find_element(By.XPATH, '//div[h4="BOM版本号"]//button').click()
            self.driver.find_element(By.XPATH, '//input[@name="versions"]').send_keys(bom_version)
            self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
            bom_versions.append(bom_version)
            i += 1
            time.sleep(2)
        return bom_versions

    def get_first_bom_of_project(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        res = self.driver.find_element(By.XPATH, '//div[h4="BOM版本号"]/following-sibling::div/div[1]//p').text
        return res

    def get_all_boms(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        boms = [i.text for i in self.driver.find_elements(
            By.XPATH, '//div[h4="BOM版本号"]/following-sibling::div/div/p'
        )]
        return boms[::-1]

    def update_bom(self, pro_name: str):
        mock = Mock()
        bom_version = mock.mock_data(data_name="bom_version")
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        ele = self.driver.find_element(
            By.XPATH, '//div[h4[contains(text(),"BOM版本号")]]/following-sibling::div/div[1]'
        )
        ActionChains(self.driver).move_to_element(ele).perform()
        ele.find_element(By.XPATH, './/*[name()="svg"][@title="修改"]').click()
        input_ele = self.driver.find_element(By.XPATH, '//input[@name="versions"]')
        self.new_clear(input_ele)
        input_ele.send_keys(bom_version)
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        WebDriverWait(self.driver, 10).until(
            lambda x: self.detect_num_of_dialog(expect=0) == True
        )
        return bom_version

    def delete_bom(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        ele = self.driver.find_element(
            By.XPATH, '//div[h4[contains(text(),"BOM版本号")]]/following-sibling::div/div[1]'
        )
        ActionChains(self.driver).move_to_element(ele).perform()
        ele.find_element(By.XPATH, './/*[name()="svg"][@title="删除"]').click()
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        return ProjectPage(self.driver)

    def edit_material_of_bom(self, pro_name: str, add_times: int, delete_times: int):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        for i in range(add_times):
            self.driver.find_element(
                By.XPATH, '//button[span="添加物料"]'
            ).click()
            self.driver.find_element(By.XPATH, '//input[@name="material"]').click()
            self.driver.find_element(By.XPATH, f'//div[@class="MuiAutocomplete-popper"]//li[{i+1}]').click()
            ele = self.driver.find_element(By.XPATH, '//button[span="确定"]')
            self.driver.execute_script("arguments[0].click();", ele)
            WebDriverWait(self.driver, 10).until(
                lambda x: self.detect_num_of_dialog(expect=0) == True
            )
            i += 1
        for i in range(delete_times):
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="删除"]').click()
            ele = self.driver.find_element(By.XPATH, '//button[span="确定"]')
            self.driver.execute_script("arguments[0].click();", ele)
            i += 1
        return ProjectPage(self.driver)

    def fill_bom(self, pro_name: str, num_of_material: int):
        mock = Mock()
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        for i in range(num_of_material):
            proportion = randint(1, 10)
            research_unit = mock.mock_data("research_unit")
            self.driver.find_element(By.XPATH, f'//tbody/tr[{i+1}]//td[9]//input').send_keys(proportion)
            self.driver.find_element(By.XPATH, f'//tbody/tr[{i+1}]//td[10]//input').send_keys(research_unit)
            i += 1
        self.driver.find_element(By.XPATH, '//button[span="保存配方"]').click()
        return ProjectPage(self.driver)

    def task_attachment(self, pro_name: str):
        mock = Mock()
        task_attachment = mock.attachment_path(attachment_name="task.jpeg")
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发任务")
        self.driver.find_element(By.XPATH, '//tr[1]/td[last()]//button[@title="查看详情"]').click()
        ele = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        ele.send_keys(task_attachment)
        WebDriverWait(self.driver, 10).until(
            lambda x: len(self.driver.find_elements(
                By.XPATH, '//input[@type="file"]/parent::label/preceding-sibling::div//img'
            )) > 0
        )
        self.driver.find_element(By.XPATH, '//button[span="保存附件"]').click()
        return ProjectPage(self.driver)

    def status_pending_to_inprocess(self, pro_name: str):
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发产品")
        self.driver.find_element(By.XPATH, '//button[span="启动项目"]').click()
        return ProjectPage(self.driver)

    def status_inprocess_to_ended(self, pro_name: str, is_bom_released: bool):
        mock = Mock()
        description = mock.mock_data(data_name="description")
        end_project_attachment = mock.attachment_path("end.jpg")
        self._go_to_detail_tab(pro_name=pro_name, tab_name="研发产品")
        self.driver.find_element(By.XPATH, '//button[span="完结项目"]').click()
        self.driver.find_element(By.XPATH, '//input[@name="description"]').send_keys(description)
        ele = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        ele.send_keys(end_project_attachment)
        WebDriverWait(self.driver, 10).until(
            lambda x: len(self.driver.find_elements(
                By.XPATH, '//input[@type="file"]/parent::label/preceding-sibling::div//img'
            )) > 0
        )
        # 结项。填完结项说明、添加完文档后，依据是否有定版BOM，验证后面的页面交互
        if is_bom_released is True:
            self.driver.find_element(By.XPATH, '//input[@name="bom"]').click()
            self.driver.find_element(By.XPATH, '//div[@class="MuiAutocomplete-popper"]//li[1]').click()
        else:
            pass
        self.driver.find_element(By.XPATH, '//button[span="确定"]').click()
        return ProjectPage(self.driver)


if __name__ == "__main__":
    ck = ProjectPage()
    ck.task_attachment(pro_name="project_name_70SIK8")
    # ck.edit_material_of_bom(pro_name="project_name_70SIK8", add_times=2, delete_times=0)
    # ck.add_task_to_project(pro_name="project_name_BmZgac", flow_name="flow_name_5b7cqm")
