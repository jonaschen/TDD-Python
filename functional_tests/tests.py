#!/usr/bin/python3

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

import time

MAX_WAIT = 5

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# FIXME: this function can be used for a specific table only
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
			time.sleep(0.1)


	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith wants to add items in the todo list
		self.browser.get(self.live_server_url)

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

		self.wait_for_row_in_list_table(('1: ' + item1))

		# She can enter another item
		# She enters 'OOP Concepts Study'
		inputbox = self.browser.find_element_by_id('id_new_item')
		item2 = 'OOP Concepts Study'
		inputbox.send_keys(item2)
		inputbox.send_keys(Keys.ENTER)

		# Now she has two items on the list
		self.wait_for_row_in_list_table(('1: ' + item1))
		self.wait_for_row_in_list_table(('2: ' + item2))

		# The app gives her an unique URL
		self.fail('Finish the test!')

		# She can goto the URL to check her to-do list

