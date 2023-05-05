from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Topic, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if [form.cleaned_data['is_main'] for form in self.forms if form.cleaned_data].count(True) == 1:
            return super().clean()
        else:
            raise ValidationError('(!) Должен быть один главный раздел')


class ArticleInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline, ]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    ordering = ['name']