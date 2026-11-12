# Data Processing Lab

## Lab Overview
A student project that uses Python and CSV files to build a small data processing program.

## Project Structure
```
data_processing_lab
├── README.md             # This file
├── Cities.csv            # The cities dataset
├── Countries.csv         # The countries dataset
└── data_processing.py    # The analysis code
```

## Classes and Attributes
All classes are in `data_processing.py`: `DataLoader`, `DB` and `Table`.

`DataLoader` has:
- `base_path`: The folder where the CSV files are loaded from.

`DB` has:
- `tables`: A list of `Table` objects.

`Table` has:
- `name`: The name of the table, e.g. `cities`.
- `table`: A list of dictionaries (one dictionary per row).

## Methods
`DataLoader`:
- `load_csv(self, filename)`: Load a CSV file and return its rows as a list of dictionaries.

`DB`:
- `insert(self, table)`: Add a `Table` to the DB.
- `search(self, table_name)`: Find a `Table` by its name. Returns `None` if not found.

`Table`:
- `filter(self, condition)`: Return a new `Table` with only the rows where `condition(row)` is True.
- `aggregate(self, aggregation_function, aggregation_key)`: Collect the values of `aggregation_key` and give them to `aggregation_function` (like sum, max, min).
- `join(self, other, key)`: Combine two tables. Rows are matched when `key` has the same value in both.

## How to Run
1. Decide what you want:
   - A single number (average, min, max, count): use `.aggregate()`
   - A list of rows: use `.filter()`
   - Data from both files: use `.join()` first
2. Write the condition or function as a lambda.
3. Print the result.
4. Run:
```bash
python data_processing.py
```