from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import DriverFactory


class WaitForElement():

    def __init__(self):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }

    def after_display(self, locationType, locatorExpression):
        """
        显示等待元素出现

        """
        try:
            # 直接使用DriverFactory.driver可在调用该方法时直接获取最新的driver信息。
            element = WebDriverWait(DriverFactory.driver, 30).until(
                EC.element_to_be_clickable((
                    self.locationTypeDict[locationType],
                    locatorExpression)
                ))
            return element
        except Exception as e:
            raise e
