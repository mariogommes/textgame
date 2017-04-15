from django.db import models

# Create your models here.

class Page(models.Model):
	content = models.TextField()

	def pageHasContent(self):
		return self.content.strip() != ""

	def pageHasChoice(self):
		return self.choice_set.count() > 0

	def __str__(self):
		return self.content

class Choice(models.Model):
	page = models.ForeignKey(Page, on_delete=models.CASCADE)
	text_choice = models.CharField(max_length=200)

	def choiceHasPage(self):
		if hasattr(self, 'page'):
			return True

		return False

	def __str__(self):
		return self.text_choice