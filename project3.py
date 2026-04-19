import pandas as pd

# Create a messy dataset to simulate a real client file
data = {
    "Name": ["alice", "BOB", "charlie", "DAVE", "eve", "alice", "bob"],
    "Age": [25, 30, None, 22, 28, 25, 30],
    "Salary": [50000, 60000, 55000, None, 62000, 50000, 60000],
    "Email": ["alice@gmail.com", "bob@gmail.com", "charlie@gmail.com", "dave@gmail.com", "eve@gmail.com", "alice@gmail.com", "bob@gmail.com"]
}

df = pd.DataFrame(data)

print("BEFORE CLEANING:")
print(df)

# Clean the data
df = df.drop_duplicates()
df = df.dropna()
df["Name"] = df["Name"].str.title()
df["Salary"] = df["Salary"].astype(int)

print("\nAFTER CLEANING:")
print(df)

df.to_excel("cleaned_data.xlsx", index=False)
print("\nDone! Saved to cleaned_data.xlsx")