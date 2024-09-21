import pytesseract
import re

def extract_text(image_path):
    return pytesseract.image_to_string(image_path)

# Use regex for entity extraction
def extract_entity_values(text):
    patterns = {
        'weight': r'(\d+(\.\d+)?\s*(gram|grams|kg|kilogram|kilograms|g))',
        'volume': r'(\d+(\.\d+)?\s*(ml|litres?|liter|milliliter|l))',
        'voltage': r'(\d+(\.\d+)?\s*(volts?|v))',
        'wattage': r'(\d+(\.\d+)?\s*(watt|watts?|w))',
        'dimensions': r'(\d+(\.\d+)?\s*(cm|centimetres?|centimeters?|inch|inches?))'
    }

    entity_values = {}
    for entity, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            entity_values[entity] = matches[0][0]
    return entity_values
