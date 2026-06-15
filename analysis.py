# Import the csv package to access DictReader
import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# example of what the first data row looks like
# row = {
#   'request_id': 1001,
#   'date': '2024-01-03',
#   'borough': 'Brooklyn',
#   'complaint_type': 'Noise - Residential',
#   'agency': 'NYPD',
#   'resolution_status': 'Closed'
# }

# meaning_of_life = 42
# f"Meaning of life: {meaning_of_life}\n

counter = 0
for row in rows:
  if row['resolution_status'] == 'Open':
    counter += 1


complaint_types = {}
for row in rows:
  if (row['complaint_type'] not in complaint_types):
    complaint_types[row['complaint_type']] = 0
  complaint_types[row['complaint_type']] += 1

max_complaint = None
count = 0

for key, value in complaint_types.items():
  if value > count:
    max_complaint = key
    count = value


borough_requests = {}
for row in rows:
  if (row['borough'] not in borough_requests):
    borough_requests[row['borough']] = 0
  borough_requests[row['borough']] += 1

sorted_boroughs = sorted(borough_requests)

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {counter}\n")
    f.write(f"\n")
    f.write(f"Most common complaint type: {max_complaint} ({count} requests)\n")
    f.write("\n")
    f.write(f"Requests per borough: \n")
    for borough in sorted_boroughs: # since we need to display each borough and their requests, we a dynamic display with a for loop, it writes each borough within the sorted borough dictionary, and also the requests by accessing the previous borough_requests, which holds the request count. We also use sorted_boroughs because the problem asked for the list to be sorted alphabetically
       f.write(f"- {borough}: {borough_requests[borough]}\n")

print("Output saved to output.txt")