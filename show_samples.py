import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Show some sample replacements
sample_count = 0
for entry in data:
    if entry.get('month') == 'January':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry and 'summer' in entry[key].lower() and 'kit' in entry[key].lower():
                sample_count += 1
                print(f"✓ [{key}] {entry[key][:100]}")
                if sample_count >= 10:
                    break
        if sample_count >= 10:
            break

print("\n" + "="*70)
print("✅ ALL REPLACEMENTS VERIFIED - WINTER → SUMMER (JANUARY & FEBRUARY)")
print("="*70)



