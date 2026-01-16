import json
import re
import os

# Words to remove (case-insensitive)
WORDS_TO_REMOVE = [
    'bionutra',
    'ayurvedic',
    'ayurveda',
    'wellness',
    'skinnminimalism',
    'nutraceutical'
]

def remove_words_from_text(text):
    """Remove specified words from text while preserving surrounding content."""
    if not text or not isinstance(text, str):
        return text

    result = text
    for word in WORDS_TO_REMOVE:
        # Pattern matches the word with optional surrounding spaces
        # Handles cases like "word ", " word", " word ", "word,", etc.
        pattern = re.compile(
            r'\b' + re.escape(word) + r'\b',
            re.IGNORECASE
        )
        result = pattern.sub('', result)

    # Clean up multiple spaces and trim
    result = re.sub(r'\s+', ' ', result)
    result = re.sub(r'\s*,\s*,', ',', result)  # Fix double commas
    result = re.sub(r'^\s*,\s*', '', result)   # Remove leading comma
    result = re.sub(r'\s*,\s*$', '', result)   # Remove trailing comma
    result = result.strip()

    return result

def process_json_object(obj):
    """Recursively process JSON object and remove words from all string values."""
    if isinstance(obj, dict):
        return {key: process_json_object(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [process_json_object(item) for item in obj]
    elif isinstance(obj, str):
        return remove_words_from_text(obj)
    else:
        return obj

def process_json_file(filepath):
    """Process a single JSON file and remove specified words."""
    print(f"\nProcessing: {filepath}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  ERROR: Invalid JSON in {filepath}: {e}")
        return False
    except Exception as e:
        print(f"  ERROR: Could not read {filepath}: {e}")
        return False

    # Count occurrences before removal
    original_str = json.dumps(data, ensure_ascii=False)
    total_found = 0
    for word in WORDS_TO_REMOVE:
        count = len(re.findall(r'\b' + re.escape(word) + r'\b', original_str, re.IGNORECASE))
        if count > 0:
            print(f"  Found '{word}': {count} occurrences")
            total_found += count

    if total_found == 0:
        print(f"  No target words found in this file.")
        return True

    # Process the data
    processed_data = process_json_object(data)

    # Write back to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=2, ensure_ascii=False)
        print(f"  SUCCESS: Removed {total_found} word occurrences")
        return True
    except Exception as e:
        print(f"  ERROR: Could not write to {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("REMOVING BRAND WORDS FROM JSON FILES")
    print("=" * 60)
    print(f"\nWords to remove: {', '.join(WORDS_TO_REMOVE)}")

    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Find all JSON files in public folder
    public_dir = os.path.join(script_dir, 'public')
    json_files = []
    if os.path.exists(public_dir):
        for filename in os.listdir(public_dir):
            if filename.endswith('.json'):
                json_files.append(os.path.join('public', filename))

    success_count = 0
    fail_count = 0

    for json_file in json_files:
        filepath = os.path.join(script_dir, json_file)
        if os.path.exists(filepath):
            if process_json_file(filepath):
                success_count += 1
            else:
                fail_count += 1
        else:
            print(f"\nSkipping (not found): {json_file}")

    print("\n" + "=" * 60)
    print(f"COMPLETED: {success_count} files processed, {fail_count} failures")
    print("=" * 60)

if __name__ == '__main__':
    main()
