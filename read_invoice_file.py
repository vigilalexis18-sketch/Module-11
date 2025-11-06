import csv

cust_no_input = input("Enter a customer no: ")
total = 0.0

with open("invoices.csv", mode="r") as file:
    reader = csv.Dictreader(file)
    for row in reader:
        if row["cust_no"] == cust_no_input:
            total += float(row["inv_total"])
print(f"Customer Number: {cust_no_input}, Total Invoice Amount ${total:.2f}")