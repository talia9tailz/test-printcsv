import csv

# open spreadsheet
with open('data.csv', newline='') as data:
    reader = csv.reader(data)
    # iterate over rows
    for row in reader:
        # format row
        printer = ''
        for cell in row:
            while len(cell)<10:
                cell = ' ' + cell
            printer = printer + cell
        x=float(cell)/5
        a='|'
        b=''
        c=0
        while c<x:
            b=b+a
            c+=1
        printer = printer + '\t' + b
        # print row
        print(printer)
