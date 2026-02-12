from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="in minutes")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def difficulty(self):
        if self.cooking_time < 10:
            return "Easy"
        elif self.cooking_time < 30:
            return "Medium"
        else:
            return "Hard"

    def __str__(self):
        return self.name
