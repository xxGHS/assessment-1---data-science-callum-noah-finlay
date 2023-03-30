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

# Remove rows with missing values
df.dropna()

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

# run the app
if __name__ == '__main__':
    app.run()