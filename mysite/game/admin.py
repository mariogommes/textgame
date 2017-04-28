from django.contrib import admin
from .models import Page, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PageAdmin(admin.ModelAdmin):
	fieldsets = [
		('page_id ', {'fields': ['page_id']}),
		(None, {'fields': ['content']}),
	]
	inlines = [ChoiceInline]
	list_display = ('page_id',) 

admin.site.register(Page, PageAdmin)
admin.site.register(Choice)
