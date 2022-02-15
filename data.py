import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


file_data.pop(0)
total_number = 0
total_ofnumber = len(file_data)


for numbers in file_data:
    total_number += float(numbers[1])

mean = total_number / total_ofnumber
print("The mean is -> "+str(mean))