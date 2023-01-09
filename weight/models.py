from django.db import models
from django.core.validators import MaxValueValidator
from account.models import Account
import uuid

# Create your models here.
class Weight(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    weight = models.DecimalField('Weight (kg)', max_digits=5, decimal_places=2, null=True, blank=True, validators=[MaxValueValidator(150)])
    calorie_intake = models.PositiveIntegerField('Calorie Intake', default=0, null=True, blank=True, validators=[MaxValueValidator(5000)])
    date = models.DateField()

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return (self.user.first_name + '-' + str(self.date))


