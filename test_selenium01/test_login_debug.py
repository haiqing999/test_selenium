from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestLogin:
    def test_login_deb(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        #driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
