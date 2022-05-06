from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

class Image(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    image = models.FileField(upload_to='media')


    
