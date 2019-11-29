from django.db import models

# Create your models here.

class question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('publish date')

class choice(models.Model):
    choices_text=models.CharField(max_length=200)
    voit = models.IntegerField(default=0)
    question=models.ForeignKey(question,on_delete=models.CASCADE)





