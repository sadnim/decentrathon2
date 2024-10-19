from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    user_telegram_id = models.CharField(max_length=255, unique=True)
    photo_url = models.URLField()

    def __str__(self):
        return self.username


class Teacher(User):
    # Можем добавить дополнительные поля для Teacher, если потребуется
    pass


class Student(User):
    # Можем добавить дополнительные поля для Student, если потребуется
    pass


class Course(models.Model):
    FUNDAMENTAL = 'Fundamental'
    ADVANCED = 'Advanced'
    COMPLEXITY_CHOICES = [
        (FUNDAMENTAL, 'Fundamental'),
        (ADVANCED, 'Advanced'),
    ]

    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    complexity = models.CharField(max_length=12, choices=COMPLEXITY_CHOICES)
    theory_practice_ratio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
