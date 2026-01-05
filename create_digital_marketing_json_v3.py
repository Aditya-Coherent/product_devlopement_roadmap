import csv
import json

# Read the CSV file
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

current_category = None
current_element = None

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # Skip empty rows or header rows
        if not row or all(cell.strip() == '' for cell in row):
            continue
        
        # Skip header
        if row[0] == 'Team' and row[1] == 'Elements ' or row[1] == 'Elements':
            continue
        
        col_team = row[0].strip() if len(row) > 0 else ''
        col_element = row[1].strip() if len(row) > 1 else ''
        col_subelement = row[2].strip() if len(row) > 2 else ''
        col_task = row[3].strip() if len(row) > 3 else ''
        col_monthly_task = row[4].strip() if len(row) > 4 else ''
        col_month = row[5].strip() if len(row) > 5 else ''
        
        # Check if this is a category header row (e.g., "Digital Marketing", "On-Page SEO")
        if col_team and not col_element and not col_subelement and not col_task:
            if col_team in ['Digital Marketing', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO', 
                           'Performance Marketing', 'Paid PR Submission & Distribution Services (B2C Focus)',
                           'Paid PR Submission & Distribution', 'Brand Positioning & Thought Leadership', 
                           'Content Marketing & Strategy']:
                current_category = col_team
                current_element = None
            continue
        
        # Skip rows that only have element in position 0 (like the header rows in sections)
        if col_team and not col_element and not col_subelement and not col_task and not col_month:
            continue
        
        # Skip rows with "Elements, Sub-elements" headers within sections
        if (col_element == 'Elements' or col_element == 'Sub-elements') and not col_subelement:
            continue
        
        # Skip if no task
        if not col_task:
            continue
        
        # Update current element if it's provided
        if col_element and not col_element.startswith('·'):
            current_element = col_element
        
        # Determine months
        month_str = col_month.strip()
        if month_str == 'Jan -  Dec' or month_str == 'Jan - Dec':
            months_to_add = months_list
        elif month_str == 'Jan':
            months_to_add = ['January']
        else:
            months_to_add = ['January']  # Default
        
        # Use current category or fallback to team
        category = current_category if current_category else col_team
        element = current_element if current_element else 'Other'
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,
                'subElement': col_subelement,
                'task': col_task,
                'monthlyTask': col_monthly_task,
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

print("\nSample entries from January:")
jan_entries = [e for e in data if e['month'] == 'January']
for entry in jan_entries[:5]:
    print(f"  Category: {entry['category']}")
    print(f"  Element: {entry['element']}")
    print(f"  Sub-element: {entry['subElement']}")
    print(f"  Task: {entry['task']}")
    print(f"  Monthly Task: {entry['monthlyTask']}\n")



