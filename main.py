from src.gmaps import Gmaps
import sys

import pandas as pd


# Check if an argument is provided
if len(sys.argv) > 1:
    try:
        i = int(sys.argv[1])  # Convert the first argument to an integer
    except ValueError:
        print("Please provide a valid integer for 'i'.")
        sys.exit(1)
else:
    print("No starting index provided. Using default value of 1000.")
    i = 1100


# Load the CSV file into a pandas DataFrame
df = pd.read_csv('pincodes.csv')

# Construct the full address by concatenating the relevant columns
df['Full_Address'] = df['officename'] + ', ' + \
                     df['officeType'] + ', ' + \
                     df['Taluk'] + ', ' + \
                     df['Districtname'] + ', ' + \
                     df['statename'] + ' - ' + \
                     df['pincode'].astype(str)

m_list = df['Full_Address'].tolist()

# Prefix to add
prefix = "Masjids in "

# Add the prefix to all items in the list
queries  = [prefix + str(address) for address in m_list][i:i+100]





fields = [
    Gmaps.Fields.NAME, 
    Gmaps.Fields.MAIN_CATEGORY,
    Gmaps.Fields.ADDRESS,
    Gmaps.Fields.DETAILED_ADDRESS,
    Gmaps.Fields.IMAGES,
    Gmaps.Fields.LINK,
    Gmaps.Fields.COORDINATES
]

results = Gmaps.places(queries, fields=fields)



