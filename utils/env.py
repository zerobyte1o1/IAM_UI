import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(BASE_DIR, "env.ini")
cf = configparser.ConfigParser()
cf.read(configPath, encoding='UTF-8')

pick = cf.get("pick", "env")

environment = cf.get(pick, "env")
code = cf.get(pick, "code")
account = cf.get(pick, "account")
password = cf.get(pick, "password")


class Environment:
    def login_url(self):
        return "https://" + environment + ".XXX.io/login"

    def url(self, module: str):
        return "https://" + environment + ".XXX.io/subapp/admin/" + module

    def account(self):
        return account

    def password(self):
        return password

    def code(self):
        return code


if __name__ == "__main__":
    env = Environment()
    # print(env.url(module="flow"))
    print(environment)
    # print(account, password)
