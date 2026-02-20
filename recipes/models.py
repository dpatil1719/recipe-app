from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    cooking_time = models.IntegerField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return self.name

    def difficulty(self):
        if self.cooking_time < 10:
            return "Easy"
        elif self.cooking_time < 30:
            return "Medium"
        else:
            return "Hard"
