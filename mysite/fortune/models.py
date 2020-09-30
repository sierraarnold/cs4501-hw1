from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_key = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Fortune(models.Model):
    fortune_text = models.TextField()
    fortune_key = models.IntegerField(default=0)
    def __str__(self):
        return self.fortune_text

