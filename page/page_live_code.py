import time

import allure

from page.base_page import BasePage
from locators.live_code_page_locators import LiveCodePageLocators


class LiveCodePage(BasePage):
    locators = LiveCodePageLocators()

    def checked_checkbox(self):
        with allure.step('Click Elements'):
            self.element_is_visible(self.locators.ELEMENTS).click()
        with allure.step('Click Checkbox'):
            self.element_is_visible(self.locators.CHECKBOX).click()
        with allure.step('Click Toggle'):
            self.element_is_visible(self.locators.TOGGLE).click()
        with allure.step('Click Download Toggle'):
            self.element_is_visible(self.locators.DOWNLOAD_TOGGLE).click()
        with allure.step('Click select word file'):
            self.element_is_visible(self.locators.WORD_FILE).click()
            message = self.element_is_visible(self.locators.MESSAGE).text
            return message
