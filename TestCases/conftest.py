# import pytest
# from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# from selenium import webdriver

# options = Options()
# options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
# options.add_argument("--allow-insecure-localhost")   # Allow localhost with bad cert
# options.add_argument("--disable-web-security")       # Disable same-origin policy (only for testing)



import pytest
from colorama.ansi import clear_screen
from selenium import webdriver

from Utilities.Read_Properties import ReadConfig


@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    # serv_obj = Service()
    # driver = webdriver.Chrome(Service=serv_obj)
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


######################pytest HTML report########################

# #it is a hook for adding environment info to HTML report
# def pytest_configure(config):
#     config.metadata['project name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'MOHITH'
#
#
#
# #It is a hook for delete/modify Environment info to HTML report
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)