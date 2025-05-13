import pandas as pd
import os

# Step 1: Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Set your desired directory path
save_path = r'C:\Users\bhuva\OneDrive\Desktop\Programming Practices\ML-Ops\ML-Ops-DVC\data'  # <-- change this to your preferred path

# Step 4: Create the directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Step 5: Define full file path
file_path = os.path.join(save_path, 'data.csv')

# Step 6: Save to CSV
df.to_csv(file_path, index=False)

print(f'DataFrame saved to {file_path}')
