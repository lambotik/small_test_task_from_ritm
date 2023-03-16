from selenium.webdriver.common.by import By


class LiveCodePageLocators:
    ELEMENTS = (By.XPATH, "//div[@class='card mt-4 top-card'][.='Elements']")
    CHECKBOX = (By.XPATH, "//span[@class='text'][.='Check Box']")
    TOGGLE = (By.XPATH, "//button[@title='Toggle']")
    DOWNLOAD_TOGGLE = (By.CSS_SELECTOR, "li:nth-child(3) span button svg")
    WORD_FILE = (By.XPATH, "//span[@class='rct-title'][.='Word File.doc']")
    MESSAGE = (By.XPATH, "//div[@id='result']")
    MESSAGE_RESULT = (By.XPATH, "//span[@class='text-success']")
