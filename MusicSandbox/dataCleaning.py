import pandas as pd

#these are pandas methods that will help us clean the data.
# we will use the apply method to apply a function to each column in the DataFrame.
# You should be familiar with lambda functions from the previous lesson.

# Read in the dataset as a DataFrame
df = pd.read_csv('music.csv')

# Print the cleaned DataFrame
print(df)

# Remove any leading or trailing spaces from all columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Remove quotes from all columns
df = df.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)

# Convert "Release Date" column to a standard date format (YYYY-MM-DD)
df['Release Date'] = pd.to_datetime(df['Release Date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# Print the cleaned DataFrame
print(df)
