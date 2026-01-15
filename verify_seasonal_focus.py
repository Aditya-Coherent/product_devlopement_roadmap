import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for entry in data:
    if entry.get('month') in ['January', 'February']:
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry and 'seasonal focus only' in entry[key]:
                count += 1
                print(f'✓ [{entry["month"]}] {key}: {entry[key][:80]}')

print(f'\n{"="*70}')
print(f'✅ Total "seasonal focus only" found in January/February: {count}')
print(f'{"="*70}')



