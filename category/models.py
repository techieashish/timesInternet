from django.db import models


class Category(models.Model):
    featured = (("Y", "Yes"), ("N", "No"))

    name = models.CharField(max_length=200)
    parent = models.CharField(max_length=100)
    is_featured = models.CharField(max_length=1, choices=featured)
    image = models.ImageField()
    is_active = models.BooleanField(initial=True)
    description = models.TextField()

    class Meta:
        db_table = "category"

    def __str__(self):return self.name
