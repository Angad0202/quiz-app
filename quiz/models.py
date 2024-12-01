from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question_text
