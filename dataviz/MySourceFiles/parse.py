import csv
import pprint

MY_FILE = '..\\data\\sample_sfpd_incident_all.csv'

def parse(raw_file, delimiter):
    '''Parse a raw CSV file to a JSON-line object.'''

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build a data structure to return parsed_data
    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = next(csv_data)

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    opened_file.close()

    return parsed_data

def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE, ',')

    # Let's see what the data looks like!
    #pprint.pprint(new_data)

    # Create a new file with the data and save it to '.\\'
    new_file = open('.\\testFile.txt', 'w')
    new_file.write(pprint.pformat(new_data))
    new_file.close()

if __name__ == '__main__':
    main()
