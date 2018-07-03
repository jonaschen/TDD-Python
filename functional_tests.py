#!/usr/bin/python3

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith wants to add items in the todo list
		self.browser.get('http://localhost:8000')

		# Title of the web app shows "TO-DO"
		assert 'To-Do lists' in self.browser.title

		# She is invited to add one item

		# She enters an item - app development study plan

		# After 'enter' key pressed, this item is added into a to-do list

		# She can enter another item
		# She enters 'OOP Concepts Study'

		# Now she has two items on the list

		# The app gives her an unique URL

		# She can goto the URL to check her to-do list


if __name__ == '__main__':
	unittest.main(warnings='ignore')








