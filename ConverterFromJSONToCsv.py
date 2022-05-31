import csv
import json

with open("people_db.json", "r") as file:
    json_file = json.load(file)

sorted_data = []

for record in json_file:
    if all([record["company_name"] is None,
            record["phone"] is not None,
            "software" in str(record["job_title"]).lower()]):
        sorted_data.append(record)

with open("sortedData.csv", "w") as csvFile:
    data_writer = csv.DictWriter(csvFile, fieldnames=sorted_data[0].keys())
    data_writer.writeheader()
    for employee in sorted_data:
        data_writer.writerow(employee)
