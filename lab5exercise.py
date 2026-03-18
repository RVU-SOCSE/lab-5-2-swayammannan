import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "City": ["Bengaluru", "Delhi", "Mumbai", "Chennai", "Kolkata"]
}

df = pd.DataFrame(data)

print(df.shape)
print(df.ndim)
print(len(df))
print(df.head(3))
print(df.tail(2))
print(df.index)
print(df.columns)
