import os
import csv
import datetime

new_record = []
reformatted_list = []
dob = None
first_name = ""
last_name = ""
ssn = ""


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Set path for file for read file
csvpath = os.path.join("employee_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header and sum month in dataset
    for row in csvreader:
        # set Emp Id
        new_record.append(row[0])

        # set first and last name
        split_name = row[1].split(" ")
        first_name = split_name[0]
        last_name = split_name[1]
        new_record.append(first_name)
        new_record.append(last_name)

        # set date of birth
        dob = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y')
        new_record.append(dob)

        # set reformatted SSN
        split_ssn = row[3].split("-")
        ssn = "***-**-" + split_ssn[len(split_ssn)-1]
        new_record.append(ssn)

        # set abbreviated state
        state_abberv = us_state_abbrev[row[4]]
        new_record.append(state_abberv)

        # add reformatted current row to final list
        reformatted_list.append(new_record)

        split_name = []
        first_name = ""
        last_name = ""
        dob = None
        split_ssn = []
        ssn = ""
        new_record = []

# Open the file using "write" mode. Specify the variable to hold the contents

# Specify the file to write to
output_path = os.path.join("employee_data_results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Write the second row
    for formatted_record in reformatted_list:
        csvwriter.writerow(formatted_record)
