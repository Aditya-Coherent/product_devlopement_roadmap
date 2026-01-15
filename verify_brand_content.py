import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('='*100)
print('VERIFICATION - Brand Positioning & Thought Leadership')
print('='*100)

print('\n--- JANUARY ---')
for entry in data:
    if entry.get('month') == 'January' and entry.get('category') == 'Brand Positioning & Thought Leadership':
        task = str(entry.get('task', 'N/A'))[:50]
        weekly = entry.get('weeklyTask', 'NOT SET')
        if weekly != 'NOT SET':
            print(f"✓ {task}")
            print(f"  Weekly: {str(weekly)[:70]}...")
        else:
            print(f"✗ {task} - NO WEEKLY TASK")

print('\n--- FEBRUARY ---')
for entry in data:
    if entry.get('month') == 'February' and entry.get('category') == 'Brand Positioning & Thought Leadership':
        task = str(entry.get('task', 'N/A'))[:50]
        weekly = entry.get('weeklyTask', 'NOT SET')
        if weekly != 'NOT SET':
            print(f"✓ {task}")
            print(f"  Weekly: {str(weekly)[:70]}...")
        else:
            print(f"✗ {task} - NO WEEKLY TASK")

print('\n' + '='*100)
print('VERIFICATION - Content Marketing & Strategy')
print('='*100)

print('\n--- JANUARY ---')
for entry in data:
    if entry.get('month') == 'January' and entry.get('category') == 'Content Marketing & Strategy':
        task = str(entry.get('task', 'N/A'))[:50]
        weekly = entry.get('weeklyTask', 'NOT SET')
        if weekly != 'NOT SET':
            print(f"✓ {task}")
            print(f"  Weekly: {str(weekly)[:70]}...")
        else:
            print(f"✗ {task} - NO WEEKLY TASK")

print('\n--- FEBRUARY ---')
for entry in data:
    if entry.get('month') == 'February' and entry.get('category') == 'Content Marketing & Strategy':
        task = str(entry.get('task', 'N/A'))[:50]
        weekly = entry.get('weeklyTask', 'NOT SET')
        if weekly != 'NOT SET':
            print(f"✓ {task}")
            print(f"  Weekly: {str(weekly)[:70]}...")
        else:
            print(f"✗ {task} - NO WEEKLY TASK")

# Count statistics
jan_brand_with = sum(1 for e in data if e.get('month') == 'January' and e.get('category') == 'Brand Positioning & Thought Leadership' and 'weeklyTask' in e)
jan_brand_total = sum(1 for e in data if e.get('month') == 'January' and e.get('category') == 'Brand Positioning & Thought Leadership')
feb_brand_with = sum(1 for e in data if e.get('month') == 'February' and e.get('category') == 'Brand Positioning & Thought Leadership' and 'weeklyTask' in e)
feb_brand_total = sum(1 for e in data if e.get('month') == 'February' and e.get('category') == 'Brand Positioning & Thought Leadership')

jan_content_with = sum(1 for e in data if e.get('month') == 'January' and e.get('category') == 'Content Marketing & Strategy' and 'weeklyTask' in e)
jan_content_total = sum(1 for e in data if e.get('month') == 'January' and e.get('category') == 'Content Marketing & Strategy')
feb_content_with = sum(1 for e in data if e.get('month') == 'February' and e.get('category') == 'Content Marketing & Strategy' and 'weeklyTask' in e)
feb_content_total = sum(1 for e in data if e.get('month') == 'February' and e.get('category') == 'Content Marketing & Strategy')

print('\n' + '='*100)
print('STATISTICS')
print('='*100)
print(f"January Brand Positioning: {jan_brand_with}/{jan_brand_total} with weekly tasks")
print(f"February Brand Positioning: {feb_brand_with}/{feb_brand_total} with weekly tasks")
print(f"January Content Marketing: {jan_content_with}/{jan_content_total} with weekly tasks")
print(f"February Content Marketing: {feb_content_with}/{feb_content_total} with weekly tasks")

