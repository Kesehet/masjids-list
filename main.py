from src.gmaps import Gmaps
import sys

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

queries = Gmaps.Cities.India("masjid")[i:i+100]
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

# Process results here or add further code


