import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    #获取cookie
    def test_get_cookie(self):
        time.sleep(20)
        #扫码登录成功后 获取cookie
        cookies = self.driver.get_cookies()
        #cookie保存到json文件
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)
        print(f"{cookies}")

    #用cookie登录
    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 植入cookie
            self.driver.add_cookie(cookie)
        # time.sleep(50)

        while True:
            #刷新页面
            self.driver.refresh()
            res = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            #首页可点击，则跳出循环
            if res is not None:
                break

    # def teardown(self):
    #     self.driver.quit()
