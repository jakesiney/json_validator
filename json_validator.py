import json
import pandas as pd

try:
    with open('test.json', 'r') as f:
        data = json.load(f)
    print("JSON is valid")

    # Flatten the data and convert it to a pandas DataFrame
    df = pd.json_normalize(data, record_path='nestedField')

    # Print the flattened data
    print(df)

except json.JSONDecodeError as err:
    print(f"JSON is invalid. Error: {err}")
