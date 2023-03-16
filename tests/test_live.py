from page.page_live_code import LiveCodePage
import allure

@allure.suite('Live Code')
class TestLiveCode:
    @allure.feature('Test Live Code')
    class TestLiveCodePage:
        @allure.step('Test result selected checkbox')
        def test_result_selected_checkbox(self, driver):
            test_page = LiveCodePage(driver, 'https://demoqa.com/')
            test_page.open()
            result = test_page.checked_checkbox()
            assert result == 'You have selected :\nwordFile', 'Result incorrect'
