from django.db import models
from config.models import BasedModel


from django.db import models

class Certificate(BasedModel):
    card_no = models.CharField(max_length=10, unique=True)
    certificate_no = models.CharField(max_length=10, unique=True)
    operator_name = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    operator_trade = models.CharField(max_length=100)
    iqama_number = models.CharField(max_length=15, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    profile = models.ImageField(upload_to='operator_profiles/', blank=True, null=True)
    undercard = models.CharField(max_length=150)
    

    def __str__(self):
        return f"{self.operator_name} - {self.card_no}"
