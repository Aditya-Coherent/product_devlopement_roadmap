import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('='*80)
print('REMOVING DUPLICATES FROM FEBRUARY')
print('='*80)

# Find and track duplicates
seen = {}  # (month, category, element, task) -> first index
duplicates_to_remove = []

for i, entry in enumerate(data):
    month = entry.get('month')
    category = entry.get('category')
    element = entry.get('element', '')
    task = entry.get('task', '')
    
    key = (month, category, element, task)
    
    if key in seen:
        duplicates_to_remove.append(i)
        print(f'DUPLICATE at index {i}: {month} | {category[:30]} | {task[:30]}')
    else:
        seen[key] = i

print(f'\nTotal duplicates to remove: {len(duplicates_to_remove)}')

# Remove duplicates (from end to start to preserve indices)
duplicates_to_remove.sort(reverse=True)
for idx in duplicates_to_remove:
    del data[idx]
    print(f'Removed index {idx}')

# Save
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'\n✅ Removed {len(duplicates_to_remove)} duplicate entries')
print(f'New total entries: {len(data)}')

