import pandas as pd

def sanity_check(output_file_path, test_file_path):
    test_data = pd.read_csv(test_file_path)
    output_data = pd.read_csv(output_file_path)
    
    if len(test_data) != len(output_data):
        raise ValueError(f"Number of rows in the output file ({len(output_data)}) does not match the test file ({len(test_data)})")
    
    print(f"Sanity check passed for file: {output_file_path}")

# Example Usage
sanity_check('output/predictions.csv', 'dataset/test.csv')
