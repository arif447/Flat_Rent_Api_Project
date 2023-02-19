from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Flat(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='flat_category')
    house_name = models.CharField(max_length=200,)
    house_number = models.IntegerField()
    area = models.CharField(max_length=200,)
    flat_size = models.IntegerField()
    flat_rent = models.IntegerField()
    bad = models.IntegerField()
    bath = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.house_name

    class Meta:
        ordering = ['-created_at']

