from django.shortcuts import render, redirect
from .models import *
import plotly.express as px
from .forms import *

# Create your views here.

def chart(request):

    # Chart 1: Total Expenditure #

    displayed_transactions = Transaction.objects.all()

    start = request.GET.get('start')
    end = request.GET.get('end')

    if start:
        displayed_transactions = displayed_transactions.filter(date__gte=start)
    if end: 
        displayed_transactions = displayed_transactions.filter(date__lte=end)

    # Spending Over Time #
    line_graph = px.line(
        x=[t.date for t in displayed_transactions],
        y=[t.amount for t in displayed_transactions],
        labels={'x': 'Date', 'y': 'Amount'}
    )
    line_graph = line_graph.to_html()

    # Cumulative Spending #
    cumulative = px.ecdf(
        x=[t.date for t in displayed_transactions],
        y=[t.amount for t in displayed_transactions],
    )
    cumulative = cumulative.to_html()

    # Pie graph 1 #
    pie_graph_category = px.pie(
        values=[t.amount for t in displayed_transactions],
        names=[t.category for t in displayed_transactions],
    )
    pie_graph_category = pie_graph_category.to_html()
    
    # Pie graph 2 #
    pie_graph_banks = px.pie(
        values=[t.amount for t in displayed_transactions],
        names=[t.issuer for t in displayed_transactions],
    )
    pie_graph_banks = pie_graph_banks.to_html()

    # List of all transactions
    all_transactions = Transaction.objects.all()

    # Render HTML page #
    context = {
        'form': DateForm(),
        'line_graph': line_graph,
        'cumulative': cumulative,
        'pie_graph_category': pie_graph_category,
        'pie_graph_banks': pie_graph_banks,
        'all_transactions': all_transactions,
    }

    return render(request, 'core/chart.html', context)


def updateTransaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    form = TransactionForm(instance=transaction)

    if request.method == 'POST': 
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'core/transaction_form.html', context)
