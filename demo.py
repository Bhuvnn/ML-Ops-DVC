import pandas as pd
import numpy as np

# Create a DataFrame with random data
df = pd.DataFrame(np.random.rand(5, 3), columns=['Column1', 'Column2', 'Column3'])
df
print(df)
