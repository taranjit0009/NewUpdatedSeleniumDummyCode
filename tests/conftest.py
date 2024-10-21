import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#Browser option from command
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == 'firefox':
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice")

    #Passing driver for class's methods
    request.cls.driver = driver

    yield driver   # This will pass the driver instance
    driver.close()


def pytest_html_report_title(report):
    report.title = "Taranjit Is Performing Automation Testing."


