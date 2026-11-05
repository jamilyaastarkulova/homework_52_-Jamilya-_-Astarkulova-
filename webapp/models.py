from django.db import models


class Todo(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано')
    ]
    status = models.CharField(choices=STATUS_CHOICES, null=False, blank=False, verbose_name='Статус')
    task = models.TextField(max_length=5000, null=False, blank=False, verbose_name="задача")
    deadline = models.DateTimeField(max_length=10, verbose_name="Дата выполнения")

    def __str__(self):
        return f'{self.pk} - {self.task}'
