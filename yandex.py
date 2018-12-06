import unittest

from selenium import webdriver


class TestYanSelGrid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://192.168.1.52:5550/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    def test_main(self):
        self.driver.get("https://yandex.ru")
        print(self.driver.title)
        assert "Yandex" in self.driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
