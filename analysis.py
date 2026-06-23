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

# Part 2
sorted_complaints = sorted(complaint_types.items(), key=lambda x: x[1], reverse=True)
#items() gives (key, value) pair
#key=lambda x: x[1] tells sorted() to sort by count
#reverse=True flips to highest-first sorting

open_by_borough = {}
for row in rows:
   if row['resolution_status'] == 'Open':
      open_by_borough[row['borough']] = open_by_borough.get(row['borough'], 0) + 1
#.get(borough, 0) is essentially if a key exits, increment

max_open_borough = max(open_by_borough, key=open_by_borough.get)
max_open_count = open_by_borough[max_open_borough]
#max() on dictionaries iterate over keys by default, key=open_by_borough.get makes it compare values rather than alphabetically

closed_by_boroughs = {}
for row in rows:
   if row['resolution_status'] == 'Closed':
      closed_by_boroughs[row['borough']] = closed_by_boroughs.get(row['borough'], 0) + 1

closure_rate = {}
for borough in borough_requests:
   closed = closed_by_boroughs.get(borough, 0)
   total = borough_requests[borough]
   closure_rate[borough] = round((closed / total) * 100, 1)
#round(x, 1) rounds to one decimal place

sorted_by_count = sorted(borough_requests.items(), key=lambda x: (-x[1], x[0]))
top3 = sorted_by_count[:3]
#(-x[1], x[0])
# 

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {counter}\n")
    f.write("\n")
    f.write(f"Most common complaint type: {max_complaint} ({count} requests)\n")
    f.write("\n")
    f.write("Requests per borough:\n")
    for borough in sorted_boroughs:
        f.write(f"- {borough}: {borough_requests[borough]}\n")
    f.write("\n")
    f.write("Requests by complaint type:\n")
    for complaint, cnt in sorted_complaints:
        f.write(f"- {complaint}: {cnt}\n")
    f.write("\n")
    f.write(f"Borough with most open requests: {max_open_borough} ({max_open_count} open)\n")
    f.write("\n")
    f.write("Closure rate by borough:\n")
    for borough in sorted_boroughs:
        f.write(f"- {borough}: {closure_rate[borough]}%\n")
    f.write("\n")
    f.write("Top 3 boroughs by total requests:\n")
    for i, (borough, cnt) in enumerate(top3, 1):
        f.write(f"{i}. {borough} ({cnt} requests)\n")

print("Output saved to output.txt")