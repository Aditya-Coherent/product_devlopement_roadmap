import csv
import json

# Read the CSV file
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

current_category = None

category_names = {
    'Digital Marketing', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO', 
    'Performance Marketing', 'Paid PR Submission & Distribution Services (B2C Focus)',
    'Paid PR Submission & Distribution', 'Brand Positioning & Thought Leadership', 
    'Content Marketing & Strategy'
}

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # Skip completely empty rows
        if not row or all(cell.strip() == '' for cell in row):
            continue
        
        col_team = row[0].strip() if len(row) > 0 else ''
        col_elements = row[1].strip() if len(row) > 1 else ''  # Main element
        col_subelements = row[2].strip() if len(row) > 2 else ''  # Sub-element
        col_task = row[3].strip() if len(row) > 3 else ''  # Task description
        col_monthly_task = row[4].strip() if len(row) > 4 else ''  # Monthly task
        col_month = row[5].strip() if len(row) > 5 else ''  # Month
        
        # Check if col_team is a category name (even with spaces)
        if col_team in category_names or col_team == ' Technical SEO':
            current_category = col_team.strip()
            continue
        
        # Skip header rows
        if (col_team == 'Team') or (col_elements == 'Elements' and col_subelements == 'Sub-elements'):
            continue
        
        # Skip if no task or task is the header "Task"
        if not col_task or col_task == 'Task':
            continue
        
        # Determine months
        month_str = col_month.strip()
        if month_str == 'Jan -  Dec' or month_str == 'Jan - Dec':
            months_to_add = months_list
        elif month_str == 'Jan':
            months_to_add = ['January']
        else:
            months_to_add = ['January']
        
        # Fallback values
        category = current_category if current_category else 'Digital Marketing'
        element = col_elements if col_elements else 'Other'
        subelement = col_subelements if col_subelements else 'Other'
        
        # Clean task (remove leading bullet points)
        task = col_task
        if task.startswith('·'):
            task = task.replace('·', '').strip()
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,           # A. Page Metadata, B. HTML Structure, etc.
                'subElement': subelement,     # i. Page Title Optimization, etc.
                'task': task,                 # Create and Optimize title tags, etc.
                'monthlyTask': col_monthly_task,
                'team': 'digital-marketing'
            }
            data.append(entry)

# Write to JSON file
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully created digital-marketing-data.json with {len(data)} entries")
print("\nTotal by category:")
categories = {}
for entry in data:
    cat = entry['category']
    if cat not in categories:
        categories[cat] = 0
    categories[cat] += 1

for cat in sorted(categories.keys()):
    print(f"  {cat}: {categories[cat]}")

print("\nSample from January (showing correct 3-level structure):")
jan_entries = [e for e in data if e['month'] == 'January']
for entry in jan_entries[:8]:
    print(f"  Category: {entry['category']}")
    print(f"  Element: {entry['element']}")
    print(f"  SubElement: {entry['subElement']}")
    print(f"  Task: {entry['task']}")
    print(f"  Monthly Task: {entry['monthlyTask']}\n")
