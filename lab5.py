import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://katvin.com/tools/number-characters.html'


class CharacterCounter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def symbol_count(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div/table/tbody/tr[1]/td[2]')))

    def word_count(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div/table/tbody/tr[3]/td[2]')))

    def coma_count(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div/table/tbody/tr[4]/td[2]')))

    def dot_count(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div/table/tbody/tr[5]/td[2]')))

    def space_count(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div/table/tbody/tr[8]/td[2]')))

    def test_1(self):
        self.driver.get(url)
        text_field = self.driver.find_element_by_id('textsymbols')
        text_field.send_keys('...')
        count_button = self.driver.find_element_by_id('run')
        count_button.click()
        self.assertEqual('3', self.symbol_count().text)
        self.assertEqual('1', self.word_count().text)
        self.assertEqual('3', self.dot_count().text)

    def test_2(self):
        self.driver.get(url)
        text_field = self.driver.find_element_by_id('textsymbols')
        text = 'Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен. В то же время стандартная библиотека включает большой объём полезных функций.'
        text_field.send_keys(text)
        count_button = self.driver.find_element_by_id('run')
        count_button.click()
        self.assertEqual('261', self.symbol_count().text)
        self.assertEqual('30', self.word_count().text)
        self.assertEqual('1', self.coma_count().text)
        self.assertEqual('3', self.dot_count().text)
        self.assertEqual('29', self.space_count().text)

    def test_3(self):
        self.driver.get(url)
        text_field = self.driver.find_element_by_id('textsymbols')
        text_field.send_keys('')
        count_button = self.driver.find_element_by_id('run')
        count_button.click()
        alert = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div')
        self.assertEqual('×\nОй! Что-то пошло не так. Вы не ввели никаких символов.', alert.text)

    def test_4(self):
        self.driver.get(url)
        text_field = self.driver.find_element_by_id('textsymbols')
        text_field.send_keys('...')
        count_button = self.driver.find_element_by_id('run')
        count_button.click()
        clear_button = self.driver.find_element_by_id('btnFormClear')
        clear_button.click()
        self.assertEqual('0', self.symbol_count().text)


if __name__ == "__main__":
    unittest.main()
