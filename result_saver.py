import csv

def save_results(results, output_file='results.csv'):
    try:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Image File', 'Location', 'Extracted Text'])
            for result in results:
                writer.writerow(result)
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results: {e}")