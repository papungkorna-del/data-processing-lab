import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    # YOUR CODE HERE
    return [d for d in dict_list if condition(d)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    # YOUR CODE HERE
    newdict = []
    for key in dict_list:
        newdict.append((key[aggregation_key]))

    return aggregation_function(newdict)

    
# Print first 5 cities only
print("FIRST 5 CITIES:")
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', lambda t: sum(float(x) for x in t)/len(t), cities))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', lambda t: sum(float(x) for x in t)/len(t), cities))
print()

# Print all cities in Germany
print("GERMANY CITIES:")
german_cities = filter_items(lambda g: g['country'] == 'Germany', cities)
for city in german_cities:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("SPAIN CITIES WITH TEMPERATURE ABOVE 12°C:")
spain_cities = filter_items(lambda s: s['country'] == 'Spain' and float(s['temperature']) > 12, cities)
for city in spain_cities:
    print(city)
print()

# Count the number of unique countries
print("Unique Countries Count:")
print(len({city['country'] for city in cities}))
print()

# Print the average temperature for all the cities in Germany
german_avg_temp = []
for city in german_cities:
    german_avg_temp.append(float(city['temperature']))

print("German Cities Average Temp:")
print(aggregate('temperature', lambda t: sum(float(x) for x in t)/len(t), german_cities))
print()

# Print the max temperature for all the cities in Italy
italy_cities = filter_items(lambda i: i['country'] == 'Italy', cities)

print("Max Italy City Temp:")
print(aggregate('temperature', lambda t: max(float(x) for x in t), italy_cities))
print()

if __name__ == "__main__":
    import doctest
    doctest.testmod()