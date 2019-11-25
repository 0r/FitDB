import fitparse
import "fitdump.py"
import json

def main():
    # Get absolute path of JSON file
    script_dir = os.path.dirname(__file__)
    rel_path = "FitDB.json"
    abs_json_path = os.path.join(script_dir, rel_path)

    # Get JSON data
    with open(abs_json_path, 'r') as f:
        fitdata = json.load(f)

    # Call convert for each directory
    for directory in fitdata['directories']:
        convert(directory, fitdata['output'])

def convert(directory, output):
    os.system("fitdump")

if __name__ == "__main__":
    main()
