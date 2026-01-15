import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('='*70)
print('JANUARY - On-Page SEO Weekly Tasks:')
print('='*70)
count = 0
for entry in data:
    if entry.get('month') == 'January' and entry.get('category') == 'On-Page SEO' and 'weeklyTask' in entry:
        count += 1
        print(f"\n[{count}] {entry['subElement']}")
        print(f"Task: {entry['task'][:60]}...")
        print(f"Weekly: {entry['weeklyTask'][:100]}...")
        if count >= 3:
            break

print("\n" + "="*70)
print("FEBRUARY - On-Page SEO Weekly Tasks:")
print("="*70)
count = 0
for entry in data:
    if entry.get('month') == 'February' and entry.get('category') == 'On-Page SEO' and 'weeklyTask' in entry:
        count += 1
        print(f"\n[{count}] {entry['subElement']}")
        print(f"Task: {entry['task'][:60]}...")
        print(f"Weekly: {entry['weeklyTask'][:100]}...")
        if count >= 3:
            break

print("\n" + "="*70)
print("COMPARISON - Week 4 January vs Week 1 February:")
print("="*70)

# Find the same task in both months
for entry_jan in data:
    if entry_jan.get('month') == 'January' and entry_jan.get('subElement') == 'i. Page Title Optimization':
        jan_weekly = entry_jan.get('weeklyTask', 'NA')
        print(f"\nJanuary - Page Title Optimization:")
        print(f"  {jan_weekly[:100]}")
        
        for entry_feb in data:
            if entry_feb.get('month') == 'February' and entry_feb.get('subElement') == 'i. Page Title Optimization':
                feb_weekly = entry_feb.get('weeklyTask', 'NA')
                print(f"\nFebruary - Page Title Optimization:")
                print(f"  {feb_weekly[:150]}")
        break

