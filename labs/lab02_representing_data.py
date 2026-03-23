import csv
import requests

FILENAME = "labs/data.csv"

print("CSV as lists:")
with open(FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)

print("\nAverage age:")
with open(FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0

    for line in reader:
        if linecount == 0:
            pass
        else:
            total += int(line[1])
        linecount += 1

    print(total / (linecount - 1))

print("\nCSV as dictionaries:")
with open(FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",")
    total = 0
    count = 0

    for line in reader:
        print(line)
        total += int(line["age"])
        count += 1

    print("average is", total / count)

print("\nJSON from internet:")
url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)

print("\nFirst holiday in Northern Ireland:")
print(data["northern-ireland"]["events"][0])