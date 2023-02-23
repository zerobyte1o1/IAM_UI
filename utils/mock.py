import string
import random
import time


class Mock:
    def mock_data(self, data_name: str):
        ran_str = '_' + ''.join(random.sample(string.ascii_letters + string.digits, 6))
        res = data_name + ran_str
        return res

    # Format = YYYYMMDD
    def current_date(self):
        return time.strftime('%Y%m%d', time.localtime(time.time()))

    def attachment_path(self, attachment_name: str):
        path = '/Library/Python/pro/uiProject/utils/attachment/' + attachment_name
        return path


if __name__ == "__main__":
    mock = Mock()
    # print(mock.mock_data("test"))
    print(mock.attachment_path("s"))
