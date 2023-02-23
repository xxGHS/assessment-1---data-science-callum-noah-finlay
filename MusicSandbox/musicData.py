import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('music.csv')

# Filter the songs by length greater than or equal to 200 seconds
df_filtered = df[df['Duration (in seconds)'] >= 200]

# Display the filtered data
print(df_filtered)