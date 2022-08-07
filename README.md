This Django application consolidates billing and banking statements from different financial institutions (currently supporting Wells Fargo, Chase, Discover, Amex) into a joint database to enable customizable viewing (e.g., total expenditure vs consolidated categorical expenditure) of visual trends and stats. 

I have included real statements (with redacted information) in the Statements folder. The program works by reading all CSV files in this directory and inputting each individual transaction into the database. 

To load the transactions, use the command 'python manage.py load_transactions'.