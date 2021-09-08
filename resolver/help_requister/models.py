from django.conf import settings
from django.db import models
from django.urls import reverse


class Problem(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        verbose_name='Problem title',
        max_length=30,
    )

    class _ProblemCategories(models.IntegerChoices):
        School = 1
        Car = 2
        Medicine = 3
        Psychology = 4
        Etc = 5

    category = models.IntegerField(
        verbose_name='Problem category',
        choices=_ProblemCategories.choices,
    )

    description = models.TextField(
        verbose_name='Problem full description',
    )

    def get_absolute_url(self):
        return reverse('problem', kwargs={'pk': self.pk})
