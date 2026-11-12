# Data Processing Lab

## Lab Overview
Student project using Python and Sheets (.csv) to create an data processing program

## Project Structure
data_processing_lab
- ├── README.md             # This file
- ├── Cities.csv            # The dataset
- ├── data_processing.py	  # The analysis code

## Class & Attributes
Located in `data_processing.p`, has `DataLoader` and `Table`

`DataLoader` includes:
- `filename`: The .csv file that uses to load the data

`Table` includes:
- `aggregation_key`: The dictionary key whose values should be aggregated.
- `aggregation_function`: A function such as sum, max, min, etc.

## Methods
From `DataLoader`:
- `load_csv(self, filename)`: Load a CSV file and return its contents as a list of dictionaries using `filename` as the origin.

From `Table`:
- `filter(self, condition)`: Return a new list containing only the dictionaries that satisfy the given `condition` function.
- `aggregate(self, aggregation_function, aggregation_key)`: Aggregate values associated with `aggregation_key` using the provided `aggregation_function`.

## How to test and run your code
Mainly uses data processing program in `data_processing.py`, follow these steps:
1. Define your target 
- if you want a number of data e.g. `latitude`, `longitude`, `temperature`, use .aggregate()
- if you want a list of a filtered countries or cities, use .filter()
2. Write your own aggregate or filter function using lambda expression (recommend because easier to define)
3. Print your target
4. execute and run
```bash
python data_processing.py