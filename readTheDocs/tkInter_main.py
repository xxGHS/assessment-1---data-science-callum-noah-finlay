import tkinter as tk
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('cars.csv')
# Remove duplicates from the "Model" column and keep the first occurrence of each unique value
df = df.drop_duplicates(subset="Model", keep="first")

# Create the main window
root = tk.Tk()
root.title("Car Search")
root.geometry("500x300")

# Create the label for the brand dropdown
brand_label = tk.Label(root, text="Brand:")
brand_label.pack()

# Create the dropdown for the brands
brand_var = tk.StringVar()
brand_dropdown = tk.OptionMenu(root, brand_var, *pd.unique(df['Brand']))
brand_dropdown.pack()

# Create the label for the model dropdown
model_label = tk.Label(root, text="Model:")
model_label.pack()

# Create the dropdown for the models
model_var = tk.StringVar()
model_dropdown = tk.OptionMenu(root, model_var, '')
model_dropdown.pack()

# Function to update the models dropdown when the brand is selected
def update_models(*args):
    brand = brand_var.get()
    models = df.loc[df["Brand"] == brand]["Model"].values
    model_var.set(models[0])
    model_dropdown['menu'].delete(0, 'end')
    for model in models:
        model_dropdown['menu'].add_command(label=model, command=lambda value=model: model_var.set(value))

brand_var.trace('w', update_models)

# Create the label for the price range entry
price_label = tk.Label(root, text="Price range:")
price_label.pack()

# Create the entry for the price range
price_var = tk.StringVar()
price_entry = tk.Entry(root, textvariable=price_var)
price_entry.pack()

# Create the search button
search_button = tk.Button(root, text="Search", command=lambda: search(df, brand_var.get(), model_var.get(), price_var.get()))
search_button.pack()

# Function to search for cars
def search(df, brand, model, price_range):
    price_min, price_max = map(float, price_range.split(','))
    result_df = df.loc[(df["Brand"] == brand) & (df["Model"] == model) & (df["Price"] >= price_min) & (df["Price"] <= price_max)]
    print(result_df)

# Start the main event loop
root.mainloop()
