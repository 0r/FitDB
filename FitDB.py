import fitparse
import os
import re
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

    # Call upload with output directory from convert as input
    upload(fitdata['output'], fitdata["server"]["host"], fitdata["server"]["username"], fitdata["server"]["password"], fitdata["server"]["database"])

# Converts all .fit files in directory to .json file in ouput
def convert(directory, output):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".fit", ".FIT")):
                print("File processing: " + directory + "/" + file)
                os.system("python " + os.path.join(os.path.dirname(__file__), "fitdump.py ") + directory + "/" + file + " -o " + output + "/" + file + ".json" + " -t json")

# Uploads JSON data to MySQL database
def upload(directory, host, user, password, db):
    print(directory)
    print(host)
    print(user)
    print(password)
    print(db)

if __name__ == "__main__":
    main()
