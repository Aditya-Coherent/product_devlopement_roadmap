import csv
import json

# Read the CSV file
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

current_category = None
current_element = None

category_names = ['Digital Marketing', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO', 
                  'Performance Marketing', 'Paid PR Submission & Distribution Services (B2C Focus)',
                  'Paid PR Submission & Distribution', 'Brand Positioning & Thought Leadership', 
                  'Content Marketing & Strategy']

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # Skip empty rows
        if not row or all(cell.strip() == '' for cell in row):
            continue
        
        col_team = row[0].strip() if len(row) > 0 else ''
        col_element = row[1].strip() if len(row) > 1 else ''
        col_subelement = row[2].strip() if len(row) > 2 else ''
        col_task = row[3].strip() if len(row) > 3 else ''
        col_monthly_task = row[4].strip() if len(row) > 4 else ''
        col_month = row[5].strip() if len(row) > 5 else ''
        
        # Check if this row is a category header (first column has category name, rest are headers or empty)
        if col_team in category_names:
            current_category = col_team
            current_element = None
            continue
        
        # Skip header rows
        if col_team == 'Team' or (col_element == 'Elements' and col_subelement == 'Sub-elements'):
            continue
        
        # Skip if no task
        if not col_task or col_task == 'Task':
            continue
        
        # Skip rows that look like headers (all starting with ·)
        if col_task.startswith('·') and not col_subelement:
            continue
        
        # Update current element if provided in first data column
        if col_element and not col_element in ['Elements', 'NA', '']:
            current_element = col_element
        
        # Determine months
        month_str = col_month.strip()
        if month_str == 'Jan -  Dec' or month_str == 'Jan - Dec':
            months_to_add = months_list
        elif month_str == 'Jan':
            months_to_add = ['January']
        else:
            months_to_add = ['January']
        
        # Use current category or fallback
        category = current_category if current_category else 'Digital Marketing'
        element = current_element if current_element else 'Other'
        
        # Clean up bullet points from task if needed
        task = col_task.replace('· ', '').strip()
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,
                'subElement': col_subelement,
                'task': task,
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


