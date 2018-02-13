from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('الربط مع قصيدة', {'fields': ['poem']}),
        ('معلومات الوقت والتاريخ', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently','poem')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)