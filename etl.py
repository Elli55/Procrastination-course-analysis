import csv
import pandas as pd
csvs = []
with open('power_bi/udemy_filtered_1.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for line in reader:
        line[5] = line[5].replace('.', ',')
        
        csvs.append(line)

    with open('power_bi/udemy_filtered_1.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(csvs)