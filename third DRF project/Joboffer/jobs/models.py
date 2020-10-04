from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=60)
    company_email = models.CharField(max_length=60)
    company_tel = models.CharField(max_length=15, default="")
    def __str__(self):
        return f'{self.company_email}'

class jobOffer(models.Model):

    company = models.ForeignKey(Company,
                               on_delete=models.CASCADE,
                               related_name="offers")
    job_title = models.CharField(max_length=155)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.job_title} {self.salary}'

