import csv
import json

# Read the CSV file
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Month mapping
month_mapping = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar (Q1)': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun (Q2)': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep (Q3)': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec (Q4)': 'December'
}

current_category = 'Research'

with open('public/market research.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        element = row['Element'].strip() if row['Element'] else ''
        task = row['Task (what is delivered that month)'].strip() if row['Task (what is delivered that month)'] else ''
        month_str = row['Month'].strip() if row['Month'] else ''
        
        # Skip rows with empty element or task
        if not element or not task:
            continue
        
        # Get the month
        if month_str in month_mapping:
            month = month_mapping[month_str]
        else:
            month = 'January'
        
        entry = {
            'month': month,
            'category': current_category,
            'element': element,
            'task': task,
            'monthlyTask': '',
            'monthlyQuantifiable': '',
            'team': 'market-research'
        }
        data.append(entry)

# Write to JSON file
with open('public/market-research-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully created market-research-data.json with {len(data)} entries")
print("\nEntries by month:")
for month in months_list:
    count = sum(1 for entry in data if entry['month'] == month)
    if count > 0:
        print(f"  {month}: {count}")





