from django.test import TestCase
from .models import Page, Choice

# Create your tests here.

class PageMethodTests(TestCase):
	def test_page_has_content_with_no_content_page(self):
		page = Page(content="", Choice("A choice"))
		self.assertIs(pageHasContent(page), False)

	def test_page_has_content_with_content(self):
		page = Page(content="Some content", Choice("A choice"))
		self.assertIs(pageHasContent(page), True)

class ChoiceMethodTests(TestCase):
	def test_choice_has_page_without_page(self):
		choice = Choice("A choice") #Não tenho certeza se pode criar uma choice sem determinar page, se não, teste é inutil
		self.assertIs(choiceHasPage(choice), False)



