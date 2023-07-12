import pandas as pd
import csv

original_data = pd.read_csv('OriginalBakery.csv', header=0)

transactions = []

# Data Extraction & Cleaning
currTransactionNo = 1
temp_items = []
for index, row in original_data.iterrows():
    # Different Transaction
    if (currTransactionNo < row['TransactionNo']):
        transactions.append(temp_items[:])
        currTransactionNo = currTransactionNo + 1
        temp_items.clear()
        temp_items.append(row['Items'].strip())
    # Same Transaction
    else:
        temp_items.append(row['Items'].strip())
    
    # For last row
    if(index == len(original_data) - 1):
        transactions.append(temp_items[:])

# Data Transformation
with open(f'ModifiedBakery.csv', 'w', newline='') as f:
    w = csv.writer(f)
    for items in transactions:
        w.writerow(items)
    