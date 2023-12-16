# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Tests(LiveServerTestCase):
    """Testing the Home page works on multiple browsers"""

    def test_chrome_home_page_title(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(self.live_server_url)

        assert "Home" in driver.title

    def test_firefox_home_page_title(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

        driver.get(self.live_server_url)

        assert "Home" in driver.title

    def test_edge_home_page_title(self):
        options = webdriver.EdgeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)

        driver.get(self.live_server_url)

        assert "Home" in driver.title
