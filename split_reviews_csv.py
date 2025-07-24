# split_reviews_csv.py

import pandas as pd
import math

# Load the original full dataset
df = pd.read_csv('data/kaggle/Reviews.csv')

# Get total number of rows
total_rows = len(df)
rows_per_part = math.ceil(total_rows / 3)

# Split and save into 3 parts
for i in range(3):
    start = i * rows_per_part
    end = min((i + 1) * rows_per_part, total_rows)
    chunk = df[start:end]
    
    output_path = f'data/kaggle/Reviews_part{i+1}.csv'
    chunk.to_csv(output_path, index=False)
    print(f"✅ Saved {output_path} with {len(chunk)} rows")

print("🎉 Done re-splitting into 3 parts!")

