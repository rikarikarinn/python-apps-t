from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

# リセットアクション
def reset_votes(modeladmin, request, queryset):
    for question in queryset:
        question.choice_set.update(votes=0)
    modeladmin.message_user(request, "選択肢の投票数をリセットしました。")
reset_votes.short_description = "選択肢の投票数をリセット"

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'is_active')  # is_active を表示
    list_filter = ('is_active', 'pub_date')  # フィルタ追加
    search_fields = ('question_text',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    search_fields = ('choice_text',)
