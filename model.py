import pandas as pd
from src.utils import download_images
from src.preprocessing import preprocess_image
from src.extraction import extract_text, extract_entity_values

def generate_predictions(test_file_path, output_file_path):
    test_data = pd.read_csv(test_file_path)
    predictions = []

    for index, row in test_data.iterrows():
        image_url = row['image_link']
        image_path = f'images/{index}.jpg'
        
        # Step 1: Download and preprocess image
        download_images(image_url, image_path)
        preprocessed_image = preprocess_image(image_path)
        
        # Step 2: Extract text and entities
        text = extract_text(preprocessed_image)
        entities = extract_entity_values(text)
        
        # Step 3: Choose relevant entity based on entity_name
        entity_name = row['entity_name']
        prediction = entities.get(entity_name, "")
        
        predictions.append({'index': row['index'], 'prediction': prediction})

    # Step 4: Save predictions to output file
    pd.DataFrame(predictions).to_csv(output_file_path, index=False)

# Example Usage
generate_predictions('dataset/test.csv', 'output/predictions.csv')
