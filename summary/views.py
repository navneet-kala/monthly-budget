from django.db.models.aggregates import Count, Max
from summary.models import ExpenseCategories, MonthlySummary
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, F, Count, Max, FloatField
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
# Create your views here.


def index(request):
    # num_products=Count('category__category')
    # , d=(F('category__planned_amount')/F('num_products')-F('amount')
    # expenses = MonthlySummary.objects.values(
    #     'category').annotate(c=Sum('amount')).values('category__category', 'c')
    expenses = MonthlySummary.objects.select_related('category').values('category').annotate(
        c=Sum('amount')).values(
            'category__category', 'c', 'category__planned_amount')
    total_planned = ExpenseCategories.objects.aggregate(
        total=Sum('planned_amount'))
    total_actual = MonthlySummary.objects.aggregate(
        total=Sum('amount'))

    graph = return_graph(total_planned['total'], total_actual['total'])

    context = {'expenses': expenses, 'total_actual': total_actual,
               'total_planned': total_planned, 'graph': graph}

    return render(request, 'summary/index.html', context)


def return_graph(x, y):
    fig, ax = plt.subplots()
    ax.bar(['Planned', 'Actual'], [x, y], color=['red', 'green'])
    ax.set_title('Your total expenses vs total budget')
    # fig = plt.figure()
    # ax = fig.add_axes([0, 0, .25, .25])
    # ax.bar(x, y)
    # plt.plot(x, y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data
