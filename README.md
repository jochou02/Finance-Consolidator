This Django application consolidates billing and banking statements from different financial institutions (currently supporting Wells Fargo Checking, Discover, Amex) into a joint database to enable customizable viewing (e.g., total expenditure vs consolidated categorical expenditure) of visual trends and stats. 

# Usage:

* Statements to populate the database with must be in the `/Statements` directory
* Wells Fargo statements must include `Wells` in the name of the file for input parsing
* Discover statements must include `Discover` in the name of the file for input parsing
* Amex statements must include `Amex` in the name of the file for input parsing
* Load transactions into the database with `python manage.py load_transactions`


# Notes:

* I have included real statements (with redacted information) in the Statements folder. 
* The program works by reading all CSV files in this directory and inputting each individual transaction into the database.
