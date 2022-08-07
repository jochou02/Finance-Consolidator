import csv, os
from itertools import islice
from datetime import date
from lib2to3.pytree import Base
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Transaction

class Command(BaseCommand):
    help = 'Load transactions'


    def getDate(self, row):
        date_split = row[0].split('/') 
        year, day, month = int(date_split[2]), int(date_split[1]), int(date_split[0])
        dt = date(year, month, day)
        return dt

    def getCategoryAmex(self, row):
        raw = row[10]
        if 'Restaurant' in raw or 'Groceries' in raw:
            return 'Food/Dining'
        elif 'Merchandise' in raw:
            return 'General Merchanise'
        elif 'Services' in raw:
            return 'General Services'
        elif 'Transportation' in raw:
            return 'Transportation/Travel'
        else:
            return 'Other'
    
    def getCategoryDiscover(self, row):
        raw = row[4]
        if 'Entertainment'in raw:
            return 'Entertainment'
        elif 'Merchandise' in raw:
            return 'General Merchanise'
        elif 'Services' in raw:
            return 'General Services'
        else:
            return 'Other'
        

    def handle(self, *args, **kwargs):

        statement_directory = settings.BASE_DIR / 'Statements'
        for filename in os.listdir(statement_directory):

            current_CSV = f'{statement_directory}/{filename}'
            with open(current_CSV, 'r') as f:
            
                # Default reader that skips CSV heading
                reader = csv.reader(islice(f, 1, None)) 
                
                if 'Wells' in filename:
                    # Wells Fargo CSV has no heading, needs special reader
                    reader = csv.reader(f)
                    for row in reader:
                        dt = self.getDate(row)
                        merchant = row[4]
                        # Banking amounts need to be inverted to match credit spending
                        amount = -1 * float(row[1])
                        # Wells Fargo does not categorize transactions
                        Transaction.objects.get_or_create(
                            date=dt,
                            merchant=merchant,
                            amount=amount
                        )
 
                elif 'Amex' in filename:
                    for row in reader:
                        dt = self.getDate(row)
                        merchant = row[4]
                        amount = row[2]
                        category = self.getCategoryAmex(row)
                        Transaction.objects.get_or_create(
                            date=dt,
                            merchant=merchant,
                            amount=amount,
                            category=category
                        )
                        
                elif 'Discover' in filename:
                    for row in reader:
                        dt = self.getDate(row)
                        merchant = row[2]
                        amount = row[3]
                        Transaction.objects.get_or_create(
                            date=dt,
                            merchant=merchant,
                            amount=amount,
                            category=category
                        )
                        
    

                        