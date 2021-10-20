from typing import Dict
import csv
import datetime

def parse_price_data() -> Dict:

    with open("/Users/othurm/Desktop/RiskData/api/data.csv") as price_data_file:
        price_data = []
        date_data = []
        reader = csv.reader(price_data_file, delimiter=',', quotechar='|')
        for row in reader:
            try:
                date = row[0]
                price = float(row[1])
                price_data.append(price)
                date_data.append(date)
            except ValueError:
                continue
    return {
        'prices': price_data,
        'dates': date_data,
    }

