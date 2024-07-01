from django.contrib import admin


from .models import (
    Activity,
    TargetIndicator,
)


# @admin.register(Test)
# class TestAdmin(admin.ModelAdmin):
#     list_display = ('id', 'author', 'name')


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('test', 'text', 'sequence')
#     ordering = ('test', 'sequence')


# @admin.register(TestResult)
# class TestResultAdmin(admin.ModelAdmin):
#     list_display = ('test', 'points', 'summary')
#     ordering = ('test', 'points')


# @admin.register(UserResult)
# class UserResultAdmin(admin.ModelAdmin):
#     pass


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(TargetIndicator)
class TargetIndicatorAdmin(admin.ModelAdmin):
    pass



