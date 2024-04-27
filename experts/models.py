from django.db import models


class WorkCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkSubcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    work_category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    work_subcategory = models.ForeignKey(WorkSubcategory, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def __str__(self):
        return self.name
