import json

# Read the JSON file
with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the entries to remove from February
entries_to_remove = [
    # On-Page SEO
    {
        "month": "February",
        "element": "Preparation for Upcoming Rituva Summer Kit",
        "subElement": "On-Page SEO Strategy Preparation for Rituva Summer Kit"
    },
    # Off-Page SEO
    {
        "month": "February",
        "element": "Off-Page SEO for Upcoming Rituva Kit",
        "subElement": "Rituva Summer Kit Preparation"
    },
    # Performance Marketing (3 entries)
    {
        "month": "February",
        "element": "Performance Marketing Strategy for Upcoming Rituva Kit",
        "subElement": "Preparation for Rituva Summer Kit Launch",
        "task": "1. Develop Performance Marketing Strategy"
    },
    {
        "month": "February",
        "element": "Performance Marketing Strategy for Upcoming Rituva Kit",
        "subElement": "Preparation for Rituva Summer Kit Launch",
        "task": "2. Search Engine Marketing & Social Media Campaigns"
    },
    {
        "month": "February",
        "element": "Performance Marketing Strategy for Upcoming Rituva Kit",
        "subElement": "Preparation for Rituva Summer Kit Launch",
        "task": "3. Creative Content Planning"
    },
    # Paid PR
    {
        "month": "February",
        "element": "Preparation for Upcoming Season Rituva Kit",
        "subElement": "Rituva Summer Kit PR Strategy",
        "category": "Paid PR Submission & Distribution Services (B2C Focus)"
    },
    # Content Marketing & Strategy
    {
        "month": "February",
        "element": "Rituva Kit Preparation",
        "subElement": "Content Marketing & Strategy for Upcoming Rituva Summer Kit"
    }
]

# Count removals
removed_count = 0
original_count = len(data)

# Filter out matching entries
new_data = []
for entry in data:
    should_remove = False
    
    for remove_spec in entries_to_remove:
        # Check if entry matches the removal spec
        match = True
        for key, value in remove_spec.items():
            if entry.get(key) != value:
                match = False
                break
        
        if match:
            should_remove = True
            print(f"✓ REMOVING: [{entry.get('month')}] {entry.get('category')} - {entry.get('element')}")
            print(f"  SubElement: {entry.get('subElement')}")
            print(f"  Task: {entry.get('task')[:80] if entry.get('task') else 'N/A'}")
            print()
            removed_count += 1
            break
    
    if not should_remove:
        new_data.append(entry)

# Write the updated JSON back
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)

print("\n" + "="*70)
print("✅ REMOVAL COMPLETED")
print("="*70)
print(f"✓ Total entries removed: {removed_count}")
print(f"✓ Original total entries: {original_count}")
print(f"✓ New total entries: {len(new_data)}")
print("="*70)
print("✅ File updated successfully!")



