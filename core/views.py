from django.shortcuts import render
from .models import *
import plotly.express as px

# Create your views here.

def chart(request):

    transactions = Transaction.objects.all()

    fig = px.line(
        x=[t.date for t in transactions],
        y=[t.amount for t in transactions]
    )

    chart = fig.to_html()

    context = {'chart': chart}

    return render(request, 'core/chart.html', context)
