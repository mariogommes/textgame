from django.db import models

# Create your models here.

class Page(models.Model):
	page_id = models.CharField(max_length=20, primary_key=True, null=False)
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
	next_page = models.CharField(max_length=20, default="")
	active_talent = models.CharField(max_length=20, default="")
	karma = models.IntegerField(default=0)
	consequence = models.CharField(max_length=20, default="")


	def choiceHasPage(self):
		if hasattr(self, 'page'):
			return True

		return False

	def __str__(self):
		return self.text_choice