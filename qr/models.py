from django.db import models
from config.models import BasedModel


class Certificate(BasedModel):
    id_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    s_office = models.CharField(max_length=255)
    ts_no = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    id_iqama_no = models.CharField(max_length=50)
    issue_date = models.DateField()
    valid_until = models.DateField()
    details = models.TextField()
    photo = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name
