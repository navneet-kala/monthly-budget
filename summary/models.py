from django.db import models
import json

# Create your models here.


class ExpenseCategories(models.Model):
    category = models.CharField(max_length=50, unique=True)
    planned_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return self.category, self.planned_amount


class MonthlySummary(models.Model):
    expense_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        ExpenseCategories, to_field='category', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.category, self.amount
