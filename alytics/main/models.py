from django.db import models
from django.contrib.auth.models import User


class UserFunction(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь")
    func = models.CharField(max_length=200, null=False, blank=False, verbose_name="Формула", help_text="Формула вида: t*t + 2/t")
    graph = models.ImageField(upload_to="graphs", verbose_name="График")
    interval = models.DurationField(verbose_name="Глубина периода моделирования в днях")
    dt = models.DurationField(verbose_name="шаг в часах")
