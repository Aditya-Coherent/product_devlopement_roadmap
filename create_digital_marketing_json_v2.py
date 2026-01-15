import csv
import json

# Read the CSV file
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Month mapping for "Jan - Dec" format
month_expansion = {
    'Jan -  Dec': months_list,
    'Jan': ['January'],
    'Jan -  Dec': months_list,
}

current_category = None

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Skip header
    
    for row in reader:
        # Skip empty rows
        if not row or all(cell.strip() == '' for cell in row):
            continue
        
        team = row[0].strip() if len(row) > 0 and row[0] else None
        elements = row[1].strip() if len(row) > 1 and row[1] else None
        sub_elements = row[2].strip() if len(row) > 2 and row[2] else None
        task = row[3].strip() if len(row) > 3 and row[3] else None
        monthly_task = row[4].strip() if len(row) > 4 and row[4] else None
        month_str = row[5].strip() if len(row) > 5 and row[5] else None
        
        # Skip rows with no task
        if not task:
            continue
        
        # Update category if provided
        if elements and not team:
            current_category = elements
            continue
        
        # Determine months to add
        if month_str in month_expansion:
            months_to_add = month_expansion[month_str]
        elif month_str == 'Jan':
            months_to_add = ['January']
        else:
            months_to_add = ['January']  # Default to January
        
        category = current_category if current_category else 'Digital Marketing'
        element = elements if elements else 'Other'
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,
                'subElement': sub_elements if sub_elements else '',
                'task': task,
                'monthlyTask': monthly_task,
                'team': 'digital-marketing'
            }
            data.append(entry)

# Write to JSON file
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully created digital-marketing-data.json with {len(data)} entries")
print("\nEntries by category:")
categories = {}
for entry in data:
    cat = entry['category']
    if cat not in categories:
        categories[cat] = 0
    categories[cat] += 1

for cat in sorted(categories.keys()):
    print(f"  {cat}: {categories[cat]}")

print("\nEntries by month (January):")
jan_entries = [e for e in data if e['month'] == 'January']
for entry in jan_entries[:10]:
    print(f"  - {entry['category']} > {entry['element']} > {entry['subElement']}: {entry['task']}")
print(f"  ... and {len(jan_entries) - 10} more")





