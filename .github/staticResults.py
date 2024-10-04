import csv
import glob
import os

def process_csv(file_path, output_file):
    count = 0
    with open(file_path, mode='r') as csv_file, open(output_file, mode='w') as txt_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Misconfigurations']:
                txt_file.write(f"Resource: {row['Resource']}\n")
                txt_file.write(f"Path: {row['Path']}\n")
                txt_file.write(f"Misconfigurations: {row['Misconfigurations']}\n")
                txt_file.write(f"Severity: {row['Severity']}\n")
                txt_file.write(f"Policy title: {row['Policy title']}\n")
                txt_file.write(f"Guideline: {row['Guideline']}\n")
                txt_file.write("-" * 40 + "\n")
                count += 1

def main():
    output_file = 'missconfigurations.txt'
    with open(output_file, mode='w') as txt_file:
        for file_path in glob.glob('*iac*.csv'):
            process_csv(file_path, output_file)

if __name__ == "__main__":
    main()
