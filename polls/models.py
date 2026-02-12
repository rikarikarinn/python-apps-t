from django.db import models

# 質問モデル
class Question(models.Model):
    question_text = models.CharField("質問内容", max_length=200)
    pub_date = models.DateTimeField("公開日")
    is_active = models.BooleanField("表示するか", default=True)  # ←追加

    def __str__(self):
        return self.question_text

# 選択肢モデル
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("選択肢", max_length=200)
    votes = models.IntegerField("投票数", default=0)

    def __str__(self):
        return self.choice_text
