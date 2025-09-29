### expense tracker (cli)

a simple command-line expense tracker built with python.  
it stores expenses in a csv file and lets you add, list, summarize, and delete them.

notes
-data is saved in expenses.csv
-ids are automatically rearranged after deletion to stay sequential (1, 2, 3, …)
-built with: argparse, csv, datetime, tabulate

### usage

run the script with a mode and optional arguments:

```bash
python expense-tracker.py <mode> [options]

modes

add : add a new expense
list : list all expenses
summary : show total expenses (all or for a specific month)
delete : delete an expense by id

options

-d, --description : description of the expense
-a, --amount : cost of the expense
-m, --month : specify month (1–12) for summary
-i, --id : id of the expense (for delete)

examples

add an expense:
python expense-tracker.py add -d "lunch" -a 500

list all expenses:
python expense-tracker.py list

get summary for all expenses:
python expense-tracker.py summary

get summary for a specific month:
python expense-tracker.py summary -m 9

delete an expense by id:
python expense-tracker.py delete -i 2