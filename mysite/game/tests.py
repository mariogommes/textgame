from django.test import TestCase
from .models import Page, Choice

# Create your tests here.

class PageMethodTests(TestCase):
	def test_page_has_content_with_no_content_page(self):
		page = Page(content="")
		page.save()
		page.choice_set.create(text_choice="Some choice")
		self.assertIs(page.pageHasContent(), False)

	def test_page_has_content_with_content(self):
		page = Page(content="Some content")
		page.save()
		page.choice_set.create(text_choice="Some choice")
		self.assertIs(page.pageHasContent(), True)

	def test_page_has_choice_with_no_choice(self):
		page = Page(content="Some content")
		self.assertIs(page.pageHasChoice(), False)

	def test_page_has_choice_with_choice(self):
		page = Page(content="Some content")
		page.save()
		page.choice_set.create(text_choice="Some choice")
		self.assertIs(page.pageHasChoice(), True)

	def test_one_choice_page_right_text(self):
		page1 = Page(content="A page")
		page1.save()
		#forma mais simples de criar choice com obj page1, abaixo deixei mais complicado só pra ver a diferença
		page1.choice_set.create(text_choice="Próxima página")
		allChoices = page1.choice_set.all()
		self.assertEqual(allChoices[0].__str__(), "Próxima página") #ver como acessar o text_choice da page

	def test_one_choice_page_wrong_text(self):
		page1 = Page(content="A page")
		page1.save()
		choice = Choice(page=page1, text_choice="Another text")
		choice.save()
		allChoices = page1.choice_set.all()
		self.assertNotEqual(allChoices[0].__str__(), "Próxima página")

class ChoiceMethodTests(TestCase):
	def test_choice_has_page_without_page(self):
		choice = Choice(text_choice="A choice")
		self.assertIs(choice.choiceHasPage(), False)

	def test_choice_has_page_with_page(self):
		page = Page(content="Some content")
		page.save()
		page.choice_set.create(text_choice="A choice")
		allChoices = page.choice_set.all()
		self.assertIs(allChoices[0].choiceHasPage(), True)




