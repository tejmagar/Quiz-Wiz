from django.db import models
from django.contrib.auth import get_user_model

from dj_admin_plus import navigation
from dj_admin_plus.navigation import Navigation


# Create your models here.


categories = (
    ('easy', 'EASY'),
    ('medium', 'MEDIUM'),
    ('heard', 'HARD')
)


class Question(models.Model):
    category = models.CharField(max_length=100, choices=categories)
    question = models.TextField()
    answers = models.TextField()
    correct_option = models.IntegerField()

    def __str__(self):
        return f'{self.pk}  {self.answers}'


navigation.register([
    Navigation(
        _id='blog',
        title='Questions',
        icon_class='fa-edit',
        model=Question,
    ),

    Navigation(_id='users', title='Users',
               icon_class='fa-user', model=get_user_model()),
], True)
