import csv
import json

# Read the CSV file using proper CSV reader
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

current_category = None
current_element = None

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, fieldnames=['Team', 'Elements', 'SubElements', 'Task', 'MonthlyTask', 'Month'])
    
    for row in reader:
        # Skip empty rows
        if not row or all(v == '' or v is None for v in row.values()):
            continue
        
        team = row['Team'].strip() if row['Team'] else ''
        elements = row['Elements'].strip() if row['Elements'] else ''
        subelements = row['SubElements'].strip() if row['SubElements'] else ''
        task = row['Task'].strip() if row['Task'] else ''
        monthly_task = row['MonthlyTask'].strip() if row['MonthlyTask'] else ''
        month_str = row['Month'].strip() if row['Month'] else ''
        
        # Skip header row
        if team == 'Team':
            continue
        
        # Check if this is a category header (main section)
        if team in ['Digital Marketing', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO',
                   'Performance Marketing', 'Paid PR Submission & Distribution Services (B2C Focus)',
                   'Brand Positioning & Thought Leadership', 'Content Marketing & Strategy']:
            current_category = team
            current_element = None
            continue
        
        # Skip lines with just "Elements" header
        if elements == 'Elements' and subelements == 'Sub-elements':
            continue
        
        # Skip if no task
        if not task or task == 'Task':
            continue
        
        # Update current element if provided
        if elements and elements not in ['Elements', 'NA', '']:
            current_element = elements
        
        # Use current element if this row doesn't have one
        element = current_element if current_element else 'Other'
        subelement = subelements if subelements else 'Other'
        
        # Determine months
        if month_str in ['Jan -  Dec', 'Jan - Dec']:
            months_to_add = months_list
        elif month_str == 'Jan':
            months_to_add = ['January']
        else:
            months_to_add = ['January']
        
        category = current_category if current_category else 'Digital Marketing'
        
        # Clean up task - remove leading bullet points
        task_clean = task
        if task_clean.startswith('·'):
            task_clean = task_clean.replace('·', '', 1).strip()
        
        # Clean up monthly_task - remove leading bullet points
        monthly_task_clean = monthly_task
        if monthly_task_clean.startswith('·'):
            monthly_task_clean = monthly_task_clean.replace('·', '', 1).strip()
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,
                'subElement': subelement,
                'task': task_clean,
                'monthlyTask': monthly_task_clean,
                'team': 'digital-marketing'
            }
            data.append(entry)

# Write to JSON file
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully created digital-marketing-data.json with {len(data)} entries")
print("\nBreakdown by category:")
categories = {}
for entry in data:
    cat = entry['category']
    if cat not in categories:
        categories[cat] = 0
    categories[cat] += 1

for cat in sorted(categories.keys()):
    print(f"  {cat}: {categories[cat]}")

# Check for missing categories
expected_categories = ['On-Page SEO', 'Off-Page SEO', 'Technical SEO', 'Performance Marketing',
                       'Paid PR Submission & Distribution Services (B2C Focus)',
                       'Brand Positioning & Thought Leadership', 'Content Marketing & Strategy']
missing = [c for c in expected_categories if c not in categories]
if missing:
    print(f"\nMissing categories: {missing}")
else:
    print("\nAll 7 categories present!")

print("\nSample entries showing hierarchy:")
print("\n1. On-Page SEO sample:")
on_page_jan = [e for e in data if e['category'] == 'On-Page SEO' and e['month'] == 'January'][:2]
for entry in on_page_jan:
    print(f"   Element: {entry['element']}, SubElement: {entry['subElement']}, Task: {entry['task']}")

print("\n2. Off-Page SEO sample:")
off_page_jan = [e for e in data if e['category'] == 'Off-Page SEO' and e['month'] == 'January'][:2]
for entry in off_page_jan:
    print(f"   Element: {entry['element']}, SubElement: {entry['subElement']}, Task: {entry['task']}")

print("\n3. Technical SEO sample:")
tech_seo_jan = [e for e in data if e['category'] == 'Technical SEO' and e['month'] == 'January'][:2]
for entry in tech_seo_jan:
    print(f"   Element: {entry['element']}, SubElement: {entry['subElement']}, Task: {entry['task']}, Monthly: {entry['monthlyTask']}")
