from sre_parse import CATEGORIES
from django.db import models

# Create your models here.

class Transaction(models.Model):

    TRANSACTION_CATEGORIES = [
        ('General Merchanise', 'General Merchanise'),
        ('General Services', 'General Services'),
        ('Transportation/Travel', 'Transportation/Travel'),
        ('Food/Dining', 'Food/Dining'),
        ('Entertainment', 'Entertainment'),
        ('Credits', 'Credits'),
        ('Other', 'Other'),
    ]

    date = models.DateField()
    merchant = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100, choices=TRANSACTION_CATEGORIES, default='Other')

    class Meta:
        ordering = ('date',)

