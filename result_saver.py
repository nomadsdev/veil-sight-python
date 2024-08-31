import csv
import os

def save_results(results, output_file='results.csv'):
    if not results:
        print("No results to save.")
        return
    
    if not output_file.endswith('.csv'):
        output_file += '.csv'
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Image File', 'Location', 'Extracted Text'])
            
            for result in results:
                if len(result) != 3:
                    print(f"Skipping invalid result entry: {result}")
                    continue
                writer.writerow(result)
        
        print(f"Results successfully saved to {output_file}")
    
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}. Check if the file is open or if you have write permissions.")
    except FileNotFoundError:
        print(f"File not found: The path {output_file} does not exist.")
    except Exception as e:
        print(f"Unexpected error saving results: {e}")
