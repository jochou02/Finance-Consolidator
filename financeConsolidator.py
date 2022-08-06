import csv, gspread, os

MONTH = 'july'
file = 'Statements/Discover-08.csv'

transactions = []

def hFin(file):

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[2]
            amount = float(row[3])
            category = row[4]
            transaction = (date, name, amount, category)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet('Sheet1')

rows = hFin(file)

wks.insert_row([1,2,3], 8)