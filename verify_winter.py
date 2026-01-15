import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

january_winter_count = 0
february_winter_count = 0

january_entries = []
february_entries = []

for entry in data:
    if entry.get('month') == 'January':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry and 'winter' in entry[key].lower():
                january_winter_count += 1
                january_entries.append(f'{key}: {entry[key][:80]}')
    elif entry.get('month') == 'February':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry and 'winter' in entry[key].lower():
                february_winter_count += 1
                february_entries.append(f'{key}: {entry[key][:80]}')

print("="*70)
print("JANUARY - Winter Occurrences Still Found:")
print("="*70)
for entry in january_entries:
    print(f'✗ {entry}')

print("\n" + "="*70)
print("FEBRUARY - Winter Occurrences Still Found:")
print("="*70)
for entry in february_entries:
    print(f'✗ {entry}')

print("\n" + "="*70)
print(f"Total winter occurrences in January: {january_winter_count}")
print(f"Total winter occurrences in February: {february_winter_count}")
print("="*70)



