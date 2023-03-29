import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import seaborn as sns
import flask as fl
from flask import Flask, render_template, url_for, request
from jinja2 import Template
import json
# create a flask app
app = fl.Flask(__name__)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cars.csv')
dfmodels = pd.read_csv('cars (Models).csv')

# Remove duplicates from the "Model" column and keep the first occurrence of each unique value
df = df.drop_duplicates(subset="Model", keep="first")
dfmodels = dfmodels.drop_duplicates(subset="Model", keep="first")

brand = "Toyota"
models = df.loc[df["Brand"] == brand]["Model"].values

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

html = df.to_html('converted_file.html')

# turn the car brands into a html file and save it as brands.html
brands = df['Brand'].unique()

# create a route for the app

@app.route('/', methods=["GET", "POST"])
def home(name=None):
    pagevariable = 0
    data = pd.read_csv('cars.csv')
    options = [{'label': i, 'value': i} for i in df['Brand'].unique()]
    modelreturn = '0'
    brandreturn = '0'
    if request.method == "POST":
        if 'brandentry' in request.form:
            modelreturn = request.form.get("brandentry")
            data = data[data['Brand'] == modelreturn]
            options = [{'label': i, 'value': i} for i in data['Model'].unique()]
            return render_template("modelselect.html", tables=[data.to_html()], titles=data.columns.values, modelreturn=modelreturn, options = options)
        elif 'modelentry' in request.form:
            pricereturn = request.form.get("modelentry")
            data = data[data['Model'] == pricereturn]
            options = [{'label': i, 'value': i} for i in data['Price'].unique()]
            currentbrand = data['Brand'].unique()
            currentmodel = data['Model'].unique()
            lowest = data['Price'].min()
            highest = data['Price'].max()
            median = data['Price'].median()
            mode = data['Price'].mode()
            mean = data['Price'].mean()
            return render_template("priceselect.html", tables=[data.to_html()], titles=data.columns.values, pricereturn=pricereturn, options = options, lowest=lowest, highest=highest, median=median, mode=mode, mean=mean, currentbrand=currentbrand, currentmodel=currentmodel)
        elif 'priceentry' in request.form:
            finalresult = request.form.get("priceentry")
            brandcheck = request.form.get("Brand:")
            brandcheck = brandcheck.replace("[", "")
            brandcheck = brandcheck.replace("]", "")
            brandcheck = brandcheck.replace("'", "")
            modelcheck = request.form.get("Model:")
            modelcheck = modelcheck.replace("[", "")
            modelcheck = modelcheck.replace("]", "")
            modelcheck = modelcheck.replace("'", "")
            data = data[data.Brand == brandcheck]
            data = data[data.Model == modelcheck]
            data = data[data['Price'] <= int(finalresult)]
            return render_template("finale.html", tables=[data.to_html()], titles=data.columns.values, finalresult=finalresult)
    return fl.render_template('home.html', tables=[data.to_html()], titles=data.columns.values, options = options)

@app.route('/modelselect')
def modela():
    data = pd.read_csv('cars.csv')
    options = [{'label': i, 'value': i} for i in dfmodels['Model'].unique()]
    return fl.render_template('modelselect.html', tables=[data.to_html()], titles=data.columns.values, options = options)

@app.route('/priceselect')
def pricea():
    data = pd.read_csv('cars.csv')
    options = [{'label': i, 'value': i} for i in df['Price'].unique()]
    return fl.render_template('priceselect.html', tables=[data.to_html()], titles=data.columns.values, options = options)

@app.route('/gearboxselect')
def gearboxa():
    data = pd.read_csv('cars.csv')
    options = [{'label': i, 'value': i} for i in df['Gearbox'].unique()]
    return fl.render_template('gearboxselect.html', tables=[data.to_html()], titles=data.columns.values, options = options)

# run the app
if __name__ == '__main__':
    app.run()

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

# write html to let the user select the brand
html = df.to_html('converted_file.html')   
brands = df['Brand'].unique()
brands = pd.DataFrame(brands)
brands.to_html('brands.html')

(df.loc[df['Brands'] == 'input'])