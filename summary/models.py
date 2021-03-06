from django.db import models
from django.forms import ModelForm
import json

# Create your models here.


class ExpenseCategories(models.Model):
    category = models.CharField(max_length=50, unique=True)
    planned_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        #     return self.category, self.planned_amount
        return self.category


class MonthlySummary(models.Model):
    expense_date = models.DateField(null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=0)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        ExpenseCategories, to_field='category', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.category, self.amount


class Expenses(ModelForm):
    class Meta:
        model = MonthlySummary
        fields = ['expense_date', 'amount', 'description',
                  'category']


class Categories(ModelForm):
    class Meta:
        model = ExpenseCategories
        fields = ['category', 'planned_amount']
