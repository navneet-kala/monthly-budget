from django.db.models.aggregates import Count, Max
from summary.models import Categories, ExpenseCategories, Expenses, MonthlySummary
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum, F, Count, Max, FloatField
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
from django.db import connection
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def index(request):

    sql = f"""SELECT a.category, a.planned_amount,sum(b.amount) FROM summary_ExpenseCategories as a
    left join summary_MonthlySummary as b on b.category_id =a.category group by a.category"""
    cursor = connection.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    total_planned = ExpenseCategories.objects.aggregate(
        total=Sum('planned_amount'))
    total_actual = MonthlySummary.objects.aggregate(
        total=Sum('amount'))

    graph = return_graph(total_planned['total'], total_actual['total'])

    context = {'total_actual': total_actual,
               'total_planned': total_planned, 'graph': graph, 'row': row}

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


def expenses(request):
    if request.method == 'POST':
        form = Expenses(request.POST)
        if form.is_valid():
            form.save()
            form = Expenses()
            messages.add_message(request, messages.INFO, 'Expense Added')
            # return HttpResponseRedirect(reverse('index'))
    else:
        form = Expenses()
    context = {'allrows': MonthlySummary.objects.order_by(
        "-pk"), 'form': form}
    return render(request, 'summary/expenses.html', context)


def categories(request):
    if request.method == 'POST':
        form = Categories(request.POST)
        if form.is_valid():
            form.save()
            form = Categories()
            messages.add_message(request, messages.INFO, 'Category Added')
            # return HttpResponseRedirect(reverse('index'))
    else:
        form = Categories()
    context = {'allrows': ExpenseCategories.objects.order_by(
        "-pk"), 'form': form}
    return render(request, 'summary/categories.html', context)
