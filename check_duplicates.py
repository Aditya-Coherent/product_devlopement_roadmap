import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('FEBRUARY - Brand Positioning entries:')
print('='*80)
seen_tasks = set()
duplicates = []

for i, entry in enumerate(data):
    if entry.get('month') == 'February' and entry.get('category') == 'Brand Positioning & Thought Leadership':
        task = entry.get('task', 'N/A')
        element = entry.get('element', '')
        
        key = (element, task)
        if key in seen_tasks:
            duplicates.append(i)
            print(f'DUPLICATE [{i}]: {element[:30]} | {task[:40]}')
        else:
            seen_tasks.add(key)
            print(f'UNIQUE [{i}]: {element[:30]} | {task[:40]}')

print(f'\nTotal duplicates found: {len(duplicates)}')
print(f'Duplicate indices: {duplicates}')

