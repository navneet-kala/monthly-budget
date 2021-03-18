from django.contrib import admin

# Register your models here.
from .models import MonthlySummary, ExpenseCategories

admin.site.register(MonthlySummary)
admin.site.register(ExpenseCategories)
