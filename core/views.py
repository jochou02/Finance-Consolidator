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

    total_expenditure = px.line(
        x=[t.date for t in displayed_transactions],
        y=[t.amount for t in displayed_transactions],
        title='Total Expenditure',
        labels={'x': 'Date', 'y': 'Amount'}
    )

    total_expenditure.update_layout(title={
        'font_size': 22,
        'xanchor': 'center',
        'x': 0.5
    })

    total_expenditure = total_expenditure.to_html()



    # List of all transactions

    all_transactions = Transaction.objects.all()

    # Render HTML page #

    context = {
        'total_expenditure': total_expenditure, 'form': DateForm(),
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
