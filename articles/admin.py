from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        scopes = set()
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get("is_main") is True:
                main_count += 1
            scope = form.cleaned_data.get("scope")
            if scope is not None:
                if scope not in scopes:
                    scopes.add(form.cleaned_data.get("scope"))
                else:
                    raise ValidationError(f'Дупликат темы - {form.cleaned_data.get("scope")}')

            # print(form.cleaned_data)
            # pass
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if main_count > 1:
            raise ValidationError('Главная тема может быть только одна')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope.article.through
    fields = ("scope", "is_main")
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass