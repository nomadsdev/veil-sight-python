import csv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_results(results, output_file='results.csv'):
    if not results:
        logging.info("No results to save.")
        return

    if not output_file.lower().endswith('.csv'):
        output_file += '.csv'

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            logging.info(f"Created directory: {output_dir}")
        except OSError as e:
            logging.error(f"Error creating directory '{output_dir}': {e}")
            return

    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Image File', 'Location', 'Extracted Text'])

            for result in results:
                if len(result) != 3:
                    logging.warning(f"Skipping invalid result entry: {result}")
                    continue
                if not all(isinstance(item, str) for item in result):
                    logging.warning(f"Skipping invalid result entry with non-string values: {result}")
                    continue
                writer.writerow(result)

        logging.info(f"Results successfully saved to '{output_file}'")

    except PermissionError:
        logging.error(f"Permission denied: Unable to write to '{output_file}'. Check if the file is open or if you have write permissions.")
    except FileNotFoundError:
        logging.error(f"File not found: The path '{output_file}' does not exist.")
    except Exception as e:
        logging.error(f"Unexpected error saving results: {e}")

if __name__ == "__main__":
    sample_results = [
        ('image1.png', 'Location1', 'Extracted text 1'),
        ('image2.png', 'Location2', 'Extracted text 2')
    ]
    save_results(sample_results, 'output/results.csv')
