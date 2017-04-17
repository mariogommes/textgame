from django.contrib import admin
from .models import Page, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PageAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name ', {'fields': ['name']}),
		(None, {'fields': ['content']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Page, PageAdmin)
admin.site.register(Choice)
