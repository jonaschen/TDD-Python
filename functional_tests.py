#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		#self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith wants to add items in the todo list
		self.browser.get('http://localhost:8000')

		# Title of the web app shows "TO-DO"
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to add one item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She enters an item - app development study plan
		item1 = 'Making App Development Study Plan'
		inputbox.send_keys(item1)

		# After 'enter' key pressed, this item is added into a to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == ('1: ' + item1) for row in rows)
		)

		# She can enter another item
		# She enters 'OOP Concepts Study'
		self.fail('Finish the test!')

		# Now she has two items on the list

		# The app gives her an unique URL

		# She can goto the URL to check her to-do list


if __name__ == '__main__':
	unittest.main(warnings='ignore')








