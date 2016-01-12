from django.contrib import admin

from .models import Question,Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
	"""docstring for ChoiceInline"""
	model=Choice
	extra=3
	
		

class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	#fields=['pub_date','question_text']
	fieldsets=[
	(None,{'fields':['question_text']}),
	('Data information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	inlines=[ChoiceInline]
	list_display=('question_text','pub_date',)
	list_filter=['pub_date']
	search_fields=['question_text']

admin.site.register(Question,QuestionAdmin)	
#sadmin.site.register(Choice)		
