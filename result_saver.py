import logging
from pathlib import Path
import pandas as pd
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_to_csv(df, output_file):
    try:
        df.to_csv(output_file, index=False, encoding='utf-8')
        logging.info(f"Results successfully saved to CSV: '{output_file}'")
    except PermissionError:
        logging.error(f"Permission denied: Unable to write to '{output_file}'. Check if the file is open or if you have write permissions.")
    except Exception as e:
        logging.error(f"Unexpected error saving CSV: {e}")

def save_to_json(df, output_file):
    try:
        df.to_json(output_file, orient='records', force_ascii=False)
        logging.info(f"Results successfully saved to JSON: '{output_file}'")
    except PermissionError:
        logging.error(f"Permission denied: Unable to write to '{output_file}'. Check if the file is open or if you have write permissions.")
    except Exception as e:
        logging.error(f"Unexpected error saving JSON: {e}")

def save_results(results, output_file='results.csv', file_format='csv'):
    if not results or not isinstance(results, list) or not all(isinstance(r, tuple) and len(r) == 3 for r in results):
        logging.warning("Invalid or empty results. Ensure the data is a list of 3-tuple (image, location, text).")
        return

    output_file = f"{Path(output_file).stem}.{file_format}"
    
    output_path = Path(output_file)
    output_dir = output_path.parent
    
    if output_dir and not output_dir.exists():
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {output_dir}")
        except OSError as e:
            logging.error(f"Error creating directory '{output_dir}': {e}")
            return

    try:
        df = pd.DataFrame(results, columns=['Image File', 'Location', 'Extracted Text'])
        if file_format == 'csv':
            save_to_csv(df, output_path)
        elif file_format == 'json':
            save_to_json(df, output_path)
        else:
            logging.error(f"Unsupported file format: '{file_format}'")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    sample_results = [
        ('image1.png', 'Location1', 'Extracted text 1'),
        ('image2.png', 'Location2', 'Extracted text 2')
    ]
    save_results(sample_results, 'output/results.csv', 'csv')
    save_results(sample_results, 'output/results.json', 'json')
