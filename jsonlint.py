import json


def lint_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print("Valid JSON")
    except ValueError as e:
        print("Invalid JSON")
        print("Error:", str(e))


# Use the function
lint_json('ticket_template.json')
