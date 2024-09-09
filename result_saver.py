import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_results(results, output_file='results.csv'):
    if not results:
        logging.info("No results to save.")
        return

    output_file = output_file if output_file.lower().endswith('.csv') else f"{output_file}.csv"
    
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
        df.to_csv(output_path, index=False, encoding='utf-8')
        logging.info(f"Results successfully saved to '{output_file}'")
    except PermissionError:
        logging.error(f"Permission denied: Unable to write to '{output_file}'. Check if the file is open or if you have write permissions.")
    except Exception as e:
        logging.error(f"Unexpected error saving results: {e}")

if __name__ == "__main__":
    sample_results = [
        ('image1.png', 'Location1', 'Extracted text 1'),
        ('image2.png', 'Location2', 'Extracted text 2')
    ]
    save_results(sample_results, 'output/results.csv')
