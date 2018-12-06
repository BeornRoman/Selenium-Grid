import unittest

from selenium import webdriver


class TestGoogleSelGrid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://192.168.1.41:5551/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    def test_main(self):
        self.driver.get("https://google.com")
        print(self.driver.title)
        assert "Google" in self.driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
