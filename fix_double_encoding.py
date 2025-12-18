import json

# Read the file
with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the problematic Unicode sequences
# \u00e2\u20ac\u201c is the UTF-8 encoded version of en-dash that got double-encoded
content = content.replace('\\u00e2\\u20ac\\u201c', '-')  # This is the encoded en-dash
content = content.replace('\\u00e2\\u20ac\\u201d', '-')  # Encoded em-dash variant

# Also handle if they're already decoded
content = content.replace('\u00e2\u20ac\u201c', '-')
content = content.replace('\u00e2\u20ac\u201d', '-')

# Parse and validate JSON
data = json.loads(content)

# Write back with ensure_ascii=False to preserve proper UTF-8
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('✅ Fixed double-encoded character issue!')

# Verify the fix
with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    test_content = f.read()
    if '50-100' in test_content:
        print('✅ Verified: Dashes are now correct!')
    else:
        print('⚠️ Still has issues, checking content...')

