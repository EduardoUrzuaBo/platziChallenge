import pytest
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver

from subtests import test_create_an_dynamic_account
from subtests import test_login
from subtests import test_logout
from subtests import test_search_item
from subtests import test_verify_contact_information
from subtests import test_verify_details_page

"""
This pytest test was automatically generated by TestProject
    Project: Test Projects
    Package: TestProject.Generated.Tests.TestProjects
    Test: Integration Test
    Generated by: Eduardo Andres Urzuas (eduardoandresu.u@gmail.com)
    Generated on 09/02/2021, 03:56:35
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="AewvQ8RB-GRZPLR5FvGgYnVwr6MYc5st_nBmov_CWxg1",
                              project_name="Platzi test",
                              job_name="Integration Test")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://magento-demo.lexiconn.com/"
    Password = ""  # This was a SECRET parameter and therefore its value is empty
    TestEmail = "testemail@test.com"
    SearchItem = "Books"
    BookName = "A TALE OF TWO CITIES"
    DynamicEmail = ""
    RandomEmail = ""
    RandomCity = ""
    LoginEmail = ""

    driver.get(ApplicationURL)
    driver.report().test()
    driver.report().disable_reports(False)

    # 1. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    step_output = test_create_an_dynamic_account.test_main(driver)
    RandomEmail = step_output

    # 2. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    test_verify_contact_information.test_main(driver)

    # 3. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    test_logout.test_main(driver)

    # 4. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    test_login.test_main(driver)

    # 5. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    test_verify_contact_information.test_main(driver)

    # 6. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    test_search_item.test_main(driver)

    # 7. This test was auto generated from steps of the 'CreateAccount' test
    # This step was auto generated from several steps
    test_verify_details_page.test_main(driver)
