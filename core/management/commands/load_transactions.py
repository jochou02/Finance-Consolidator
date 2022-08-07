import csv
from datetime import date
from lib2to3.pytree import Base
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Transaction

class Command(BaseCommand):
    help = 'Load transactions'

    def handle(self, *args, **kwargs):
        statement_directory = settings.BASE_DIR / 'Statements'
        print('test')