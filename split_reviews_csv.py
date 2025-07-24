# split_reviews_csv.py

import pandas as pd

# Load the full CSV file
csv_path = 'data/kaggle/Reviews.csv'
df = pd.read_csv(csv_path)

sample_size = 1000
bytes_per_row = df.head(sample_size).to_csv(index=False).encode('utf-8')
avg_bytes_per_row = len(bytes_per_row) / sample_size

target_chunk_size_mb = 40
target_chunk_size_bytes = target_chunk_size_mb * 1024 * 1024
rows_per_chunk = int(target_chunk_size_bytes / avg_bytes_per_row)

# Calculate number of parts
num_parts = (len(df) + rows_per_chunk - 1) // rows_per_chunk

print(f"Splitting into {num_parts} parts of ~{rows_per_chunk} rows each...")

# Split and save each part
for i in range(num_parts):
    start = i * rows_per_chunk
    end = min((i + 1) * rows_per_chunk, len(df))
    chunk = df[start:end]
    
    output_path = f'data/kaggle/Reviews_part{i+1}.csv'
    chunk.to_csv(output_path, index=False)
    print(f"Saved {output_path} with {len(chunk)} rows")

print("🎉 Done splitting!")
