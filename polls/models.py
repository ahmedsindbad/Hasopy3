import datetime

from django.db import models
from django.utils import timezone
from Search import models as Smodels


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="نص السؤال")
    pub_date = models.DateTimeField('تاريخ النشر')
    poem = models.ForeignKey(Smodels.Poem, null=True, on_delete=models.CASCADE, verbose_name="عنوان القصيدة")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'نشر مؤخرا ؟'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="نص الخيار")
    votes = models.IntegerField(default=0, verbose_name="عدد التصويتات")

    def __str__(self):
        return self.choice_text

