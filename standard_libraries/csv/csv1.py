import csv
import math

#-------------------------------------------------------
# Writing
#-------------------------------------------------------
with open("csv/data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    for i in range(1000):
        writer.writerow([1000 + i, 2 * i, round(abs(100 * math.sin(i)), 2)])
#-------------------------------------------------------
# Reading
#-------------------------------------------------------
with open("csv/data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
