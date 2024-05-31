import pandas as pd

# Load the dataset
df = pd.read_excel('appended_datasets.xlsx')

# Save to CSV
df.to_csv('appended_datasets.csv', index=False)

# Save to JSON
df.to_json('appended_datasets.json', orient='records')