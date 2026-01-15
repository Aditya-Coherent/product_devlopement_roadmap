import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('='*100)
print('JSON - Brand Positioning & Thought Leadership (January):')
print('='*100)
for entry in data:
    if entry.get('month') == 'January' and entry.get('category') == 'Brand Positioning & Thought Leadership':
        element = str(entry.get('element', 'N/A'))[:40]
        subelement = str(entry.get('subElement', 'N/A'))[:40]
        task = str(entry.get('task', 'N/A'))[:50]
        weekly = str(entry.get('weeklyTask', 'NOT SET'))[:50]
        print(f"Element: {element}")
        print(f"SubElement: {subelement}")
        print(f"Task: {task}")
        print(f"WeeklyTask: {weekly}")
        print('-'*80)

print('\n' + '='*100)
print('JSON - Content Marketing & Strategy (January):')
print('='*100)
for entry in data:
    if entry.get('month') == 'January' and entry.get('category') == 'Content Marketing & Strategy':
        element = str(entry.get('element', 'N/A'))[:40]
        subelement = str(entry.get('subElement', 'N/A'))[:40]
        task = str(entry.get('task', 'N/A'))[:50]
        weekly = str(entry.get('weeklyTask', 'NOT SET'))[:50]
        print(f"Element: {element}")
        print(f"SubElement: {subelement}")
        print(f"Task: {task}")
        print(f"WeeklyTask: {weekly}")
        print('-'*80)

