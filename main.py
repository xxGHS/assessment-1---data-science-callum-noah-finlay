import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import seaborn as sns

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cars.csv')

# Show the first 5 rows of the DataFrame
print(df.head())

# Extract unique values from the "Brand" column
unique_brands = np.unique(df['Brand'])

# Display the unique brands
print(unique_brands)

print("\n listing all the models of Toyota \n")

# Specify the desired brand
brand = "Toyota"

# Use boolean indexing to extract rows where the value in the "Brand" column is equal to the desired brand
brand_df = df.loc[df["Brand"] == brand]

# Extract the values from the "Model" column for the rows in brand_df
models = brand_df["Model"].values

# Display the models
print(models)

# Get unique brands
unique_brands = np.unique(df['Brand'])

# Take user input for brand
print("Available brands: ", unique_brands)
brand = input("Enter brand: ")

# Extract the rows where the value in the "Brand" column is equal to the desired brand
brand_df = df.loc[df["Brand"] == brand]

# Get unique models for the chosen brand
unique_models = np.unique(brand_df['Model'])

# Take user input for model
print("Available models for brand ", brand, ": ", unique_models)
model = input("Enter model: ")

# Extract the rows where the value in the "Model" column is equal to the desired model
model_df = brand_df.loc[brand_df["Model"] == model]

# Take user input for price range
price_min = float(input("Enter minimum price: "))
price_max = float(input("Enter maximum price: "))

# Extract the rows where the value in the "Price" column is between the price range
price_range_df = model_df.loc[(model_df["Price"] >= price_min) & (model_df["Price"] <= price_max)]

# Display the search result
print(price_range_df)


columns = df.columns

print("The number of samples in dataset: {}".format(df.shape[0]))
for column in columns:
    print(column, " unique size: {}".format(df[column].unique().size))
    
    if df[column].unique().size == df.shape[0]:
        print(column, ": Unnecessary Column. Delete from the dataset.")
        df = df.drop(labels=column, axis=1)

# using matplotlib

# Get the top 20 companies
company_top20 = (df.groupby('Brand').size().reset_index(name='counts').sort_values(by='counts', ascending=False).head(20))
#
plt.figure(figsize=(18, 5))
sns.barplot(x=company_top20.Brand, y=company_top20.counts) #, palette='Set2')
plt.xlabel('Company Name')
plt.ylabel('Number of cars')
plt.xticks(rotation=45)
plt.show()